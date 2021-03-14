from json import load, JSONDecodeError
from typing import List, Union

import switch as switch
from bson import ObjectId
from pymongo import MongoClient
from pymongo.database import Database

from src.models.resultModel import FioResult
from src.models.tagModel import Tag


class ElementNotFound(Exception):
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


def getAllElements(limit: int, table_name: str) -> Union[List[FioResult], List[Tag], List[object]]:
    """
    Get all elements from a table of the database.
    Return a list of FioResult, a list of Tag or a list of object depending of the table name.

    :param limit: int
    :param table_name: str
    :return: Union[List[FioResult], List[Tag], List[object]]
    """
    db = __connectToMongo()
    collection = db[table_name]
    elements_table = []
    for element in collection.find().limit(limit):
        # Convert the objectId "_id" to a string "id"
        element["id"] = str(element["_id"])
        element.pop("_id")
        if table_name == resultTable:
            elements_table.append(FioResult.parse_obj(element))
        if table_name == tagsTable:
            elements_table.append(Tag.parse_obj(element))
        else:
            elements_table.append(element)
    return elements_table


def getElementById(object_id: ObjectId, table_name: str) -> Union[FioResult, Tag, object]:
    """
    Get a result from database.

    :param object_id: ObjectId
    :param table_name: str
    :return: FioResult
    """
    db = __connectToMongo()
    collection = db[table_name]
    result = collection.find_one({"_id": object_id})
    if result is None:
        raise ElementNotFound
    # Convert the objectId "_id" to a string "id"
    result["id"] = str(result["_id"])
    result.pop("_id")
    if table_name == resultTable:
        return FioResult.parse_obj(result)
    if table_name == tagsTable:
        return Tag.parse_obj(result)
    else:
        return result


def getResultsByTagsId(tag_id_list: List[ObjectId], limit: int) -> List[FioResult]:  # TODO
    """
    Return results matching the given tag.

    :param tag_id_list: List[ObjectId]
    :param limit: int
    :return: List[FioResult]
    """
    pass
