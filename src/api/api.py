from fastapi import UploadFile, File, APIRouter
from src.tools import importers
from src.database.mongo import insertInMongo, getAllResults

router = APIRouter()


@router.get("/")
async def rootGet():
    return {"message": "Hello World"}


@router.post("/")
async def sendFioResult(file: UploadFile = File(...)):
    """
    WIP - Post a FIO json output file to the system and save it to the database
    :param file: FIO json output file
    :return: boolean
    """
    # TODO handle error
    # TODO verify the file integrity (type is json, fio fields are presents)
    contents = await file.read()
    contents = importers.removePointInJsonKeys(contents)
    insertInMongo(importers.jsonfileToDic(contents))
    return True


@router.get("/resultList")
async def getResultList():
    results_list = []
    for r in getAllResults():
        current_result = {
            "id": r["id"],
            "hostname": "TODO",  # TODO add hostname
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
