from json import load, JSONDecodeError
from typing import List, Union

from bson import ObjectId
from pymongo import MongoClient
from pymongo.database import Database

from src.models.resultModel import FioResult
from src.models.tagModel import Tag


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


def insertInMongo(my_object: Union[Tag, FioResult], table_name: str) -> str:
    """
    Insert a object in the mongo. Return the id of the new object.

    :param table_name: str
    :param my_object: Union[Tag, FioResult]
    :return: str
    """
    db = __connectToMongo()
    collection = db[table_name]
    new_object = collection.insert_one(my_object.dict())
    return str(new_object.inserted_id)


def getAllResults(limit: int) -> List[FioResult]:
    """
    Get all results from database

    :return: List[FioResult]
    """
    db = __connectToMongo()
    collection = db[resultTable]
    all_results = []
    for e in collection.find().limit(limit):
        # Convert the objectId "_id" to a string "id"
        e["id"] = str(e["_id"])
        e.pop("_id")
        all_results.append(FioResult.parse_obj(e))
    return all_results


def getResultById(result_id: ObjectId) -> FioResult:
    """
    Get a result from database.

    :param result_id: ObjectId
    :return: FioResult
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


# FIXME maybe merge those function with getAllResults() and getResultById()
def getAllTags(limit: int) -> List[Tag]:
    """
    Get all tags from database.

    :param limit: int
    :return: List[Tag]
    """
    db = __connectToMongo()
    collection = db[tagsTable]
    returned_tags = []
    for e in collection.find().limit(limit):
        # Convert the objectId "_id" to a string "id"
        e["id"] = str(e["_id"])
        e.pop("_id")
        returned_tags.append(Tag.parse_obj(e))
    return returned_tags


def getTagById(tag_id: ObjectId) -> Tag:
    """
    Get a tag from database.

    :param tag_id: ObjectId
    :return: Tag
    """
    db = __connectToMongo()
    collection = db[tagsTable]
    tag = collection.find_one({"_id": tag_id})
    if tag is None:
        raise ResultNotFound
    else:
        # Convert the objectId "_id" to a string "id"
        tag["id"] = str(tag["_id"])
        tag.pop("_id")
        return Tag.parse_obj(tag)


def getResultsByTagsId(tag_id_list: List[ObjectId], limit: int) -> List[FioResult]:  # TODO
    """
    Return results matching the given tag.

    :param tag_id_list: List[ObjectId]
    :param limit: int
    :return: List[FioResult]
    """
    pass
