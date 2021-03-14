from typing import List

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, status, Response

from src.database.mongo import getResultById, ResultNotFound
from src.models.resultModel import FioResult
from src.models.resultsListModel import ShortenResult
from src.models.tagModel import Tag

router = APIRouter(prefix="/tags", tags=["Tags"])


# TODO specify all responses models
@router.post("/link/{tag_name}",
             status_code=status.HTTP_200_OK,  # When the tag already exist
             response_model=None,
             responses={
                 status.HTTP_201_CREATED: {"model": None},  # When the tag is crated
                 status.HTTP_404_NOT_FOUND: {"model": None},  # When the result_id is not found
                 status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": None},
                 # When the result_id or the tag_name is misspelled
                 status.HTTP_400_BAD_REQUEST: {"model": None}  # When the result_id is missing
             })
async def link_a_result_to_a_tag(tag_name: str, result_id: str, response: Response):
    """
    Link a result to a tag. Create the tag if it isn't exist.

    :param tag_name: str
    :param result_id: str
    :param response: Response
    :return: None
    """
    try:
        result_id = ObjectId(result_id)
        result = getResultById(result_id)
    except ResultNotFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
    except InvalidId:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return None
    pass


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
