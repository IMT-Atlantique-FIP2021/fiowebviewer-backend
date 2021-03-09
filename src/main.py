import uvicorn
from fastapi import (
    FastAPI,
)

from api.results import router as resultAPI
from api.test import router as testAPI

__version__ = "0.1"


app = FastAPI(
    version=__version__,
    title="FLEX Backend API",
    description="Related <a href='https://github.com/IMT-Atlantique-FIP2021'>Github page</a>",
)

app.include_router(resultAPI, prefix="/api")
app.include_router(testAPI, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True, debug=True)
