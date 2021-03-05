from fastapi import UploadFile, File, APIRouter
from src.tools import importers
from src.database.mongo import insertInMongo

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
