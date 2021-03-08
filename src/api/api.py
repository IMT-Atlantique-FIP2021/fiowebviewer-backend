from fastapi import UploadFile, File, APIRouter
from src.tools import importers
from src.database.mongo import insertInMongo, getAllResults, getResultById

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


@router.get("/resultList")
async def getResultList():
    results_list = []
    for r in getAllResults():
        current_result = {
            "id": r["id"],
            "hostname": r["hostname"],
            "time": r["time"],
            "timestamp": r["timestamp"],
            "jobs": []
        }
        for job in r["jobs"]:
            current_result["jobs"].append({
                "jobname": job["jobname"],
                "error": job["error"],
                "option": {
                    "name": job["job options"]["name"],
                    "size": job["job options"]["size"],
                    "rw": job["job options"]["rw"],
                }
            })
        results_list.append(current_result)
    return results_list


@router.get("/result/{result_id}")
async def getResultList(result_id: str):
    return getResultById(result_id)
