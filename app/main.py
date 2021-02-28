from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

from routers import results

app = FastAPI(
    debug=True,
    version="0.1",
    title="FLEX Backend API",
    description="Related <a href='https://github.com/IMT-Atlantique-FIP2021'>Github page</a>",
    )

app.include_router(results.router)

# origins = [
#     "http://localhost",
#     "http://localhost:8000",
#     "http://localhost:3000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
