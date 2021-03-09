from fastapi import (
    APIRouter,
)

from models.config import (
    mongo_settings,
)

router = APIRouter(prefix="/test", tags=["Tests"])


@router.get("/db/connexion")
async def get_db_connexion():
    return mongo_settings.getConnectConfig()


@router.get("/db")
async def get_db():
    return mongo_settings.db
