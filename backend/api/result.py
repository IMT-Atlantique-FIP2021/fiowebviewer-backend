from typing import List, Optional

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import UploadFile, File, APIRouter, Response, status
from pydantic.error_wrappers import ValidationError

from backend.api.tags import link_tag_to_result
from backend.database.mongo import insertInMongo, getAllElements, getElementById, ElementNotFound, resultTable, \
    removeElement, tagsTable
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
        resolved_tag_list.append(getElementById(ObjectId(tag), tagsTable).name)
    result.tags = resolved_tag_list
    return result


@router.post("/post", status_code=status.HTTP_201_CREATED,
             response_model=str,
             responses={status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": str}})
async def send_fio_result(response: Response,
                          name: str,
                          file: UploadFile = File(...),
                          hostname: str = "Unknown",
                          tags: List[str] = None) -> str:
    """
    Post a FIO json output file to the system and save it into the database.
    Return the id of the new element.

    :param name: str
    :param response: Response
    :param tags: List[str] = None
    :param hostname: str = "Unknown"
    :param file: FIO json output file
    :return: str
    """
    if tags is None:
        tags = []
    try:
        json_string = await file.read()
        contents = FioResult.parse_raw(json_string)
        contents.name = name
        contents.tags = tags
        result_id = insertInMongo(contents, resultTable)
        if hostname != "Unknown":
            await link_tag_to_result(tag_name=hostname,
                                     result_id=result_id,
                                     response=response)
        return result_id
    except ValidationError:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return f"{file.filename} is not an valid json fio result"


@router.get("/list", response_model=List[ShortenResult])
async def get_results_list(limit: int = 0) -> List[ShortenResult]:
    """
    Get a list of all results

    :param limit: int
    :return: List[ShortenResult]
    """
    result_list = []
    for current_result in getAllElements(limit, resultTable):
        result_list.append(__resolve_tag(current_result).shortened())
    return result_list


@router.get("/byId/{result_id}", response_model=FioResult,
            responses={status.HTTP_404_NOT_FOUND: {"model": None},
                       status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": None}})
async def get_a_result(result_id: str, response: Response) -> Optional[FioResult]:
    """
    Fetch the FioResult matching the result_id if it is founded

    :param result_id: str
    :param response: Response
    :return: Union[FioResult, None]
    """
    try:
        result_object_id = ObjectId(result_id)
        result = getElementById(result_object_id, resultTable)
        if type(result) is FioResult:
            return __resolve_tag(result)
    except ElementNotFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
    except InvalidId:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return None
    raise Exception("Unknown error")


@router.delete("/byId/{result_id}", response_model=None,
               responses={
                   status.HTTP_422_UNPROCESSABLE_ENTITY: {"models": None},
                   status.HTTP_404_NOT_FOUND: {"models": None}
               })
async def delete_fio_result(result_id: str, response: Response) -> None:
    try:
        result_id = ObjectId(result_id)
        removeElement(result_id, resultTable)
        return None
    except InvalidId:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return None
    except ElementNotFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
