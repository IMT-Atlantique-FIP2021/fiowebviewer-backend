from typing import List
from pydantic import BaseModel, Field


class ShortenJob(BaseModel):
    jobname: str
    error: int


class ShortenResult(BaseModel):
    result_id: str = Field(alias="id")
    hostname: str
    tags: List[str]
    time: str
    timestamp: int
    jobs: List[ShortenJob]
