from fastapi import UploadFile, File, APIRouter
from fiowebviewer.backend.tools import importers
from fiowebviewer.backend.database.mongo import insertInMongo

router = APIRouter()


@router.get("/")
async def rootGet():
    return {"message": "Hello World"}


@router.post("/")
async def sendFioResult(file: UploadFile = File(...)):
    contents = await file.read()
    contents = importers.removePointInJsonKeys(contents)
    insertInMongo(importers.jsonfileToDic(contents))
    return True
