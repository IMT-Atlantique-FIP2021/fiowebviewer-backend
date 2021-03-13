from json import load, JSONDecodeError
from typing import List, Union
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.collection import Collection
from pymongo.database import Database

from src.models.resultModel import FioResult


class ResultNotFound(Exception):
    pass


databaseConfigFile = "./database.json"
try:
    databaseConfig = load(open(databaseConfigFile))
except JSONDecodeError:
    raise Exception(f"Database configuration file {databaseConfigFile} is not a JSON file")
resultTable = "results"
tagsTable = "tags"


def __connectToMongo() -> Database:
    """
    Connect to a mongo database with parameters provided by the user

    :return: Database
    """
    connect = MongoClient(databaseConfig["host"], databaseConfig["port"], username=databaseConfig["username"],
                          password=databaseConfig["password"])
    db = connect[databaseConfig["name"]]
    return db


def insertInMongo(my_fio_result) -> str:
    """
    Insert a FioResult object in the mongo. Return the id of the new object.

    :param my_fio_result: FioResult
    :return: str
    """
    db = __connectToMongo()
    collection = db[resultTable]
    new_result = collection.insert_one(my_fio_result.dict())
    return str(new_result.inserted_id)


def getAllResults() -> List[FioResult]:
    """
    Get all results from database

    :return: List[FioResult]
    """
    db = __connectToMongo()
    collection = db[resultTable]
    all_results = []
    for e in collection.find():
        # Convert the objectId "_id" to a string "id"
        e["id"] = str(e["_id"])
        e.pop("_id")
        all_results.append(FioResult.parse_obj(e))
    return all_results


def getResultById(result_id) -> FioResult:
    """
    Get a result from database. Return None if nothing is found.

    :param result_id: ObjectId
    :return: Union[FioResult, None]
    """
    db = __connectToMongo()
    collection = db[resultTable]
    result = collection.find_one({"_id": result_id})
    if result is None:
        raise ResultNotFound
    else:
        # Convert the objectId "_id" to a string "id"
        result["id"] = str(result["_id"])
        result.pop("_id")
        return FioResult.parse_obj(result)
