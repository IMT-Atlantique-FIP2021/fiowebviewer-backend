from fastapi import UploadFile, File, APIRouter
from src.tools import importers
from src.database.mongo import insertInMongo, getAllResults, getResultById
from src.models.resultListModels import ResultsList, ShortenResult, ShortenJob, ShortenJobOption


router = APIRouter()


@router.get("/")
async def rootGet():
    return {"message": "Hello World"}


@router.post("/")
async def sendFioResult(file: UploadFile = File(...), hostname: str = "Unknown"):
    """
    WIP - Post a FIO json output file to the system and save it to the database
    :param hostname: server/computer hostname
    :param file: FIO json output file
    :return: boolean
    """
    # TODO handle error
    # TODO verify the file integrity (type is json, fio fields are presents)
    contents = await file.read()
    contents = importers.removePointInJsonKeys(contents)
    contents = importers.jsonfileToDic(contents)
    contents["hostname"] = hostname
    insertInMongo(contents)
    return True


@router.get("/resultList", response_model=ResultsList)
async def getResultList() -> ResultsList:
    """
    Get a list of all fio results
    :return: ResultsList
    """
    results_list = ResultsList(results=[])
    for current_result in getAllResults():
        # This loop append current result as a ShortenResult to the result_list
        jobs = []
        for current_job in current_result["jobs"]:
            jobs.append(
                ShortenJob(
                    jobname=current_job["jobname"],
                    error=current_job["error"],
                    option=ShortenJobOption(
                        name=current_job["job options"]["name"],
                        size=current_job["job options"]["size"],
                        rw=current_job["job options"]["rw"]
                    )
                )
            )
        results_list.results.append(
            ShortenResult(
                id=current_result["id"],
                hostname=current_result["hostname"],
                time=current_result["time"],
                timestamp=current_result["timestamp"],
                jobs=jobs  # List of ShortenJob
            )
        )
    return results_list


@router.get("/result/{result_id}")
async def getResultList(result_id: str):
    return getResultById(result_id)

