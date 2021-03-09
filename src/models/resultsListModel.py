from typing import List
from pydantic import BaseModel, Field


class ShortenJobOption(BaseModel):
    name: str
    size: str
    rw: str


class ShortenJob(BaseModel):
    jobname: str
    error: int
    option: ShortenJobOption


class ShortenResult(BaseModel):
    result_id: str = Field(alias="id")
    hostname: str
    time: str
    timestamp: int
    jobs: List[ShortenJob]
