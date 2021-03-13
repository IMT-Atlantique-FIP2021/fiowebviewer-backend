from typing import List, Union

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import UploadFile, File, APIRouter, Response, status
from src.database.mongo import insertInMongo, getAllResults, getResultById, ResultNotFound
from src.models.resultsListModel import ShortenResult
from src.models.resultModel import FioResult

router = APIRouter(prefix="/result", tags=["Results", "results", "Result", "result"])


@router.post("/post", status_code=status.HTTP_201_CREATED)
async def send_fio_result(file: UploadFile = File(...), hostname: str = "Unknown"):
    """
    Post a FIO json output file to the system and save it into the database

    :param hostname: server/computer hostname
    :param file: FIO json output file
    :return: boolean
    """
    # TODO handle error
    json_string = await file.read()
    contents = FioResult.parse_raw(json_string)
    contents.hostname = hostname
    return insertInMongo(contents)


@router.get("/list", response_model=List[ShortenResult])
async def get_results_list() -> List[ShortenResult]:
    """
    Get a list of all results

    :return: List[ShortenResult]
    """
    # TODO limit the number of results
    result_list = []
    for current_result in getAllResults():
        result_list.append(current_result.shortened())
    return result_list


@router.get("/byId/{result_id}", response_model=FioResult,
            responses={status.HTTP_404_NOT_FOUND: {"model": None},
                       status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": None}},
            status_code=status.HTTP_200_OK)
async def get_a_result(result_id: str, response: Response) -> Union[FioResult, None]:
    """
    Fetch the FioResult matching the result_id if it is founded

    :param result_id: str
    :param response: Response
    :return: Union[FioResult, None]
    """
    try:
        result_id = ObjectId(result_id)
        result = getResultById(result_id)
        if type(result) is FioResult:
            return result
    except ResultNotFound:
        response.status_code = status.HTTP_404_NOT_FOUND
        return None
    except InvalidId:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return None
    raise Exception("Unknown error")
