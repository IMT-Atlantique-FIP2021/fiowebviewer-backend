from typing import List
from pydantic import BaseModel


class ShortenJobOption(BaseModel):
    name: str
    size: str
    rw: str


class ShortenJob(BaseModel):
    jobname: str
    error: int
    option: ShortenJobOption


class ShortenResult(BaseModel):
    id: str
    hostname: str
    time: str
    timestamp: int
    jobs: List[ShortenJob]


class ResultsList(BaseModel):
    results: List[ShortenResult]
