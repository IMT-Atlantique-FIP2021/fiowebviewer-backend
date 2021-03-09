from fastapi import APIRouter
from models.config import mongo_settings
from database.mongo import connectToMongo


router = APIRouter(prefix="/test", tags=["Tests"])


@router.get("/db")
async def get_db():
    return mongo_settings.db


@router.get("/db/connect")
async def get_db_connected():
    return {"numberOfDocs": connectToMongo().count()}


@router.get("/db/debug_info")
async def get_db_connexion():
    return mongo_settings.getConnectConfig()
