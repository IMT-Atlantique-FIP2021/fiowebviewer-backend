from typing import List, Optional, Union

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, status, Response

from database.mongo import (
    get_element_by_id,
    ElementNotFound,
    TAGS_TABLE,
    get_tag_by_name,
    insert_in_mongo,
    update_element,
    RESULTS_TABLE,
    remove_element,
    get_all_elements,
    get_shorten_results_by_tags_id,
)
from models.resultsListModel import ShortenResult
from models.tagModel import Tag

router = APIRouter(prefix="/tags", tags=["Tags"])


@router.post(
    "/link/{result_id}",
    status_code=status.HTTP_200_OK,  # When the tag already exist
    response_model=None,
    responses={
        status.HTTP_201_CREATED: {"model": str},
        # When the tag is crated
        status.HTTP_404_NOT_FOUND: {"model": str},
        # When the result_id is not found
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": str},
        # When the result_id or the tag_name is misspelled
        status.HTTP_400_BAD_REQUEST: {"model": str}
        # When the tag_name is missing or when the tag is already linked to the result
    },
)
async def link_tag_to_result(
    result_id: str, tag_name: str, response: Response
) -> Optional[str]:
    """
    Link a result to a tag. Create the tag if it isn't exist.

    :param tag_name: str
    :param result_id: str
    :param response: Response
    :return: str
    """
    if tag_name is None:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return "Tag name is missing"
    try:
        result_id = ObjectId(result_id)
        result = get_element_by_id(result_id, RESULTS_TABLE)
        try:
            tag_id = get_tag_by_name(tag_name).tag_id
        except ElementNotFound:  # Create the tag if it not exist
            new_tag = Tag.parse_obj({"name": tag_name})
            tag_id = insert_in_mongo(new_tag, TAGS_TABLE)
            response.status_code = status.HTTP_201_CREATED
        if tag_id not in result.tags:
            result.tags.append(tag_id)
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return f"The result {result_id} has already the tag {tag_name}."
        update_element(result_id, result, RESULTS_TABLE)
        return None
    except ElementNotFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return f"Result {result_id} not found."
    except InvalidId:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return f"{result_id} is not a valid id."


@router.delete(
    "/link/{result_id}",
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": str
        },  # When the result_id or the tag_name is not found
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": str},
        # When the result_id or the tag_name is misspelled
        status.HTTP_400_BAD_REQUEST: {"model": str},  # When the tag_name is missing
    },
)
async def remove_tag_from_result(
    result_id: str, tag_name: str, response: Response
) -> str:
    """
    Unlink a tag form a result. Remove the tag if it isn't used anymore.

    :param result_id: str
    :param tag_name: str
    :param response: Response
    :return: str
    """
    try:
        result_id = ObjectId(result_id)
        result = get_element_by_id(result_id, RESULTS_TABLE)
        tag_id = get_tag_by_name(tag_name).tag_id
        if tag_id in result.tags:
            result.tags.remove(tag_id)
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return f"The result {result_id} was not linked to the tag {tag_name}."
        update_element(result_id, result, RESULTS_TABLE)
        if len(get_shorten_results_by_tags_id([ObjectId(tag_id)], 1)) == 0:
            remove_element(ObjectId(tag_id), TAGS_TABLE)
    except ElementNotFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return f"Result {result_id} not found."
    except InvalidId:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return f"{result_id} is not a valid id."


@router.get(
    "/list",
    response_model=List[str],
    responses={status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": None}},
)
async def get_tag_list(response: Response, limit: int = 0) -> Optional[List[str]]:
    """
    Return the list of tags names.

    :param response: Response
    :param limit: int
    :return: List[str]
    """
    if type(limit) != int:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return None
    tag_list = []
    for tag in get_all_elements(limit, TAGS_TABLE):
        tag_list.append(tag.name)
    return tag_list


@router.get(
    "/search/byTag/{tag_name}",
    response_model=List[ShortenResult],
    responses={status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": str}},
)
async def get_results_by_tag_name(
    tag_name: str, response: Response, limit: int = 0
) -> Union[List[ShortenResult], str]:
    """
    Get the corresponding results list to a tag.

    :param tag_name: str
    :param response: Response
    :param limit: int
    :return: Union[List[FioResult], str]
    """
    try:
        if type(limit) != int:
            response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
            return "Limit must be an int."
        tag_id = ObjectId(get_tag_by_name(tag_name).tag_id)
        return get_shorten_results_by_tags_id([tag_id], limit)
    except ElementNotFound:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return ""


@router.post(
    "/search/byTagList",
    response_model=List[ShortenResult],
    responses={status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": str}},
)
async def get_results_by_tags_names(
    tags_name_list: List[str], response: Response, limit: int = 0
) -> Union[List[ShortenResult], str]:
    """
    Get the corresponding results list to a list of tags.

    :param tags_name_list: List[str]
    :param response: Response
    :param limit: int
    :return: Union[List[FioResult], str]
    """
    if type(limit) != int:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return "Limit must be an int."
    tags_object_id_list = []
    for tag in tags_name_list:
        tag_id = ObjectId(get_tag_by_name(tag).tag_id)
        tags_object_id_list.append(tag_id)
    return get_shorten_results_by_tags_id(tags_object_id_list, limit)
