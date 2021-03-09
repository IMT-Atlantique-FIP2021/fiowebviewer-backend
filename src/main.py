import uvicorn
from fastapi import FastAPI
from api.api import router as apiRouter


__version__ = '0.2'


app = FastAPI(
    debug=True,
    version=__version__,
    title="FLEX Backend API",
    description="Related <a href='https://github.com/IMT-Atlantique-FIP2021'>Github page</a>",
    )

app.include_router(apiRouter, prefix="/api")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
