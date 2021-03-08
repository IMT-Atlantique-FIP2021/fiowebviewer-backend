from fastapi import UploadFile, File, APIRouter
from tools import importers
from database.mongo import insertInMongo, getAllResults, getResultById

router = APIRouter(prefix="/result", tags=["Results"])


@router.post("/")
async def upload_result(file: UploadFile = File(...)):
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
    return True # FIXME: Return 200 response


@router.get("/all")
async def get_all_result():
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


@router.get("/{result_id}")
async def get_result(result_id):
    return getResultById(result_id)
