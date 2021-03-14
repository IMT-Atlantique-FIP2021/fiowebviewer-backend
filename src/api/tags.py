from typing import List

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, status, Response

from src.database.mongo import getElementById, ElementNotFound, tagsTable, get_tag_by_name, insertInMongo, \
    updateElement, resultTable, removeElement
from src.models.resultModel import FioResult
from src.models.resultsListModel import ShortenResult
from src.models.tagModel import Tag

router = APIRouter(prefix="/tags", tags=["Tags"])


def __get_results_by_tag_id(tag_id: ObjectId, limit: int) -> List[FioResult]:
    pass


@router.post("/link/{result_id}",
             status_code=status.HTTP_200_OK,  # When the tag already exist
             response_model=str,
             responses={
                 status.HTTP_201_CREATED: {"model": str},
                 # When the tag is crated
                 status.HTTP_404_NOT_FOUND: {"model": str},
                 # When the result_id is not found
                 status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": str},
                 # When the result_id or the tag_name is misspelled
                 status.HTTP_400_BAD_REQUEST: {"model": str}
                 # When the tag_name is missing or when the tag is already linked to the result
             })
async def link_a_tag_to_a_result(result_id: str, tag_name: str, response: Response) -> str:
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
        result = getElementById(result_id, resultTable)
        try:
            tag_id = get_tag_by_name(tag_name).tag_id
        except ElementNotFound:  # Create the tag if it not exist
            new_tag = Tag.parse_obj({"name": tag_name})
            tag_id = insertInMongo(new_tag, tagsTable)
            response.status_code = status.HTTP_201_CREATED
        if tag_id not in result.tags:
            result.tags.append(tag_id)
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return f"The result {result_id} has already the tag {tag_name}."
        updateElement(result_id, result, resultTable)
        return ""
    except ElementNotFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return f"Result {result_id} not found."
    except InvalidId:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return f"{result_id} is not a valid id."


@router.delete("/link/{result_id}",
               status_code=status.HTTP_200_OK,
               responses={
                   status.HTTP_404_NOT_FOUND: {"model": str},  # When the result_id or the tag_name is not found
                   status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": str},
                   # When the result_id or the tag_name is misspelled
                   status.HTTP_400_BAD_REQUEST: {"model": str}  # When the tag_name is missing
               })
async def remove_a_tag_from_a_result(result_id: str, tag_name: str, response: Response) -> str:
    """
    Unlink a tag form a result. Remove the tag if it isn't used anymore.

    :param result_id: str
    :param tag_name: str
    :param response: Response
    :return: str
    """
    try:
        result_id = ObjectId(result_id)
        result = getElementById(result_id, resultTable)
        tag_id = get_tag_by_name(tag_name).tag_id
        if tag_id in result.tags:
            result.tags.remove(tag_id)
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
            return f"The result {result_id} was not linked to the tag {tag_name}."
        updateElement(result_id, result, resultTable)
        if len(__get_results_by_tag_id(ObjectId(tag_id), 5)) == 0:
            removeElement(ObjectId(tag_id), tagsTable)
    except ElementNotFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return f"Result {result_id} not found."
    except InvalidId:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return f"{result_id} is not a valid id."


@router.get("/list")
async def get_tag_list(limit: int = 0) -> List[Tag]:
    """
    Return the list of tags.

    :param limit: int
    :return: List[Tag]
    """
    pass


@router.get("/search/byTagName",
            response_model=List[ShortenResult])
async def get_results_by_tags_name(tag_list: List[str], response: Response, limit: int = 0) -> List[FioResult]:
    """
    Get the corresponding results list to a list of tags name.

    :param tag_list: List[str]
    :param response: Response
    :param limit: int
    :return: List[FioResult]
    """
    pass


@router.get("/search/byTagId",
            response_model=List[ShortenResult])
async def get_results_by_tags_id(tag_list: List[str], response: Response, limit: int = 0) -> List[FioResult]:
    """
    Get the corresponding results list to a list of tags id.

    :param tag_list: List[str]
    :param response: Response
    :param limit: int
    :return: List[FioResult]
    """
    pass
