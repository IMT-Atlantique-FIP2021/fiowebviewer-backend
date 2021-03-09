from os import getenv
from json import load, JSONDecodeError
from typing import List, Union
from pymongo.collection import Collection

from models.resultModel import FioResult


from bson.objectid import ObjectId
from pymongo import MongoClient

from models.config import mongo_settings


def connectToMongo() -> Collection:
    """
    Connect to a mongo database with parameters provided by the user

    :return: Collection
    """
    client = MongoClient(**mongo_settings.getConnectConfig())
    db = client[mongo_settings.db]
    collection = db["results"]

    return collection


def insertInMongo(my_fio_result) -> str:
    """
    Insert a FioResult object in the mongo

    :param my_fio_result: FioResult
    """
    collection = connectToMongo()
    new_result = collection.insert_one(my_fio_result.dict())
    return str(new_result.inserted_id)


def getAllResults() -> List[FioResult]:
    """
    Get all results from database

    :return: List[FioResult]
    """
    collection = connectToMongo()
    all_results = []
    for e in collection.find():
        # Convert the objectId "_id" to a string "id"
        e["id"] = str(e["_id"])
        e.pop("_id")
        all_results.append(FioResult.parse_obj(e))
    return all_results


def getResultById(result_id) -> Union[FioResult, None]:
    """
    Get a result from database. Return None if nothing is found.

    :param result_id: ObjectId
    :return: Union[FioResult, None]
    """
    collection = connectToMongo()
    result = collection.find_one({"_id": result_id})
    if result is None:
        return None
    else:
        # Convert the objectId "_id" to a string "id"
        result["id"] = str(result["_id"])
        result.pop("_id")
        return FioResult.parse_obj(result)
