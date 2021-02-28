from fastapi import APIRouter

from json import loads

from time import sleep

from typing import List
from .models import Result

router = APIRouter()

@router.get("/results", response_model=List[Result])
async def get_results():
    # sleep(2)
    with open("./static/resultList.json", 'r') as exampleResultList:
        resultList = loads(exampleResultList.read())
        resultList[3]["tags"].append("testtest")
        return resultList

@router.put("/results")
async def add_result():
    pass

@router.get("/random")
async def get_random():
    # TODO: Implement Faker
    return {}