from typing import List, Optional

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import UploadFile, File, APIRouter, Response, status
from pydantic.error_wrappers import ValidationError

from backend.api.tags import link_tag_to_result
from backend.database.mongo import (
    insert_in_mongo,
    get_all_elements,
    get_element_by_id,
    ElementNotFound,
    RESULTS_TABLE,
    remove_element,
    TAGS_TABLE,
)
from backend.models.resultsListModel import ShortenResult
from backend.models.resultModel import FioResult

router = APIRouter(prefix="/result", tags=["Results"])


def __resolve_tag(result: FioResult) -> FioResult:
    """
    Replace tags id by tags name in a FioResult

    :param result: FioResult
    :return: FioResult
    """
    resolved_tag_list = []
    for tag in result.tags:
        resolved_tag_list.append(get_element_by_id(ObjectId(tag), TAGS_TABLE).name)
    result.tags = resolved_tag_list
    return result


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=str,
    responses={status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": str}},
)
async def send_fio_result(
    response: Response, name: str, file: UploadFile = File(...), tags: List[str] = None
) -> Optional[str]:
    """
    Post a FIO json output file to the system and save it into the database.
    Return the id of the new element.

    :param name: str
    :param response: Response
    :param tags: List[str] = None
    :param file: FIO json output file
    :return: str
    """
    if tags is None:
        tags = []
    try:
        json_string = await file.read()
        contents = FioResult.parse_raw(json_string)
        contents.name = name
        contents.tags = []
        result_id = insert_in_mongo(contents, RESULTS_TABLE)
        for tag in tags:
            await link_tag_to_result(
                tag_name=tag, result_id=result_id, response=response
            )
        if response.status_code not in [status.HTTP_200_OK, status.HTTP_201_CREATED]:
            response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            return None
        response.status_code = status.HTTP_201_CREATED
        return result_id
    except ValidationError:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return f"{file.filename} is not an valid json fio result"


@router.get("/", response_model=List[ShortenResult])
async def get_results_list(limit: int = 0) -> List[ShortenResult]:
    """
    Get a list of all results

    :param limit: int
    :return: List[ShortenResult]
    """
    result_list = []
    for current_result in get_all_elements(limit, RESULTS_TABLE):
        result_list.append(__resolve_tag(current_result).shortened())
    return result_list


@router.get(
    "/{result_id}",
    response_model=FioResult,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": None},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": None},
    },
)
async def get_a_result(result_id: str, response: Response) -> Optional[FioResult]:
    """
    Fetch the FioResult matching the result_id if it is founded

    :param result_id: str
    :param response: Response
    :return: Union[FioResult, None]
    """
    try:
        result_object_id = ObjectId(result_id)
        result = get_element_by_id(result_object_id, RESULTS_TABLE)
        if type(result) is FioResult:
            return __resolve_tag(result)
    except ElementNotFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
    except InvalidId:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return None
    raise Exception("Unknown error")


@router.delete(
    "/{result_id}",
    response_model=None,
    responses={
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"models": None},
        status.HTTP_404_NOT_FOUND: {"models": None},
    },
)
async def delete_fio_result(result_id: str, response: Response) -> None:
    try:
        result_id = ObjectId(result_id)
        remove_element(result_id, RESULTS_TABLE)
        return None
    except InvalidId:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return None
    except ElementNotFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
