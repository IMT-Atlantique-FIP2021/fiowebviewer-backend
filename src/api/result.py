from typing import List, Union

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import UploadFile, File, APIRouter, Response, status
from pydantic.error_wrappers import ValidationError

from src.api.tags import link_a_result_to_a_tag
from src.database.mongo import insertInMongo, getAllElements, getElementById, ElementNotFound, resultTable
from src.models.resultsListModel import ShortenResult
from src.models.resultModel import FioResult

router = APIRouter(prefix="/result", tags=["Results"])


@router.post("/post", status_code=status.HTTP_201_CREATED,
             response_model=str,
             responses={status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": str}})
async def send_fio_result(response: Response,
                          file: UploadFile = File(...),
                          hostname: str = "Unknown"):
    """
    Post a FIO json output file to the system and save it into the database.
    Return the id of the new element.

    :param response: Response
    :param hostname: server/computer hostname
    :param file: FIO json output file
    :return: str
    """
    try:
        json_string = await file.read()
        contents = FioResult.parse_raw(json_string)
        contents.hostname = hostname
        contents.tags = []
        result_id = insertInMongo(contents, resultTable)
        if hostname != "Unknown":  # FIXME maybe do not do this
            await link_a_result_to_a_tag(hostname, result_id, response)
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
        result_list.append(current_result.shortened())
    return result_list


@router.get("/byId/{result_id}", response_model=FioResult,
            responses={status.HTTP_404_NOT_FOUND: {"model": str},
                       status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": None}},
            status_code=status.HTTP_200_OK)
async def get_a_result(result_id: str, response: Response) -> Union[FioResult, str, None]:
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
            return result
    except ElementNotFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
    except InvalidId:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return None  # FIXME f"The id {result_id} is not a valid id."
        # I don't now why but it try to check the return with pydantic, spoiler: it doesn't work
    raise Exception("Unknown error")
