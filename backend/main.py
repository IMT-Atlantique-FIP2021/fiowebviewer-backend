import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.result import router as result_router
from api.tags import router as tags_router


__version__ = "0.6"


app = FastAPI(
    debug=True,
    version=__version__,
    title="FLEX Backend API",
    description="Related <a href='https://github.com/IMT-Atlantique-FIP2021'>Github page</a>",
)

app.include_router(result_router, prefix="/api")
app.include_router(tags_router, prefix="/api")

# app.mount("/", StaticFiles(directory="./build", html=True), name="static")
