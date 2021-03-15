from json import load, JSONDecodeError
from typing import List, Union

from bson import ObjectId
from pymongo import MongoClient
from pymongo.database import Database

from models.resultModel import FioResult
from models.resultsListModel import ShortenResult
from models.tagModel import Tag
from models.config import mongo_settings


class ElementNotFound(Exception):
    pass


resultTable = "results"
tagsTable = "tags"


def __connectToMongo() -> Database:
    """
    Connect to a mongo database with parameters provided by the user

    :return: Database
    """
    client = MongoClient(**mongo_settings.getConnectConfig())
    return client[mongo_settings.db]


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


def updateElement(
    element_id: ObjectId, updated_element: Union[Tag, FioResult], table_name: str
):
    """
    Update one element in the database.

    :param element_id: ObjectId
    :param updated_element: Union[Tag, FioResult]
    :param table_name: str
    """
    db = __connectToMongo()
    collection = db[table_name]
    if table_name == resultTable:
        collection.replace_one(
            {"_id": element_id}, FioResult.parse_obj(updated_element).dict()
        )
    elif table_name == tagsTable:
        collection.replace_one({"_id": element_id}, Tag.parse_obj(updated_element))


def removeElement(element_id: ObjectId, table_name: str) -> None:
    """
    Remove one element from the database. Return true if deleted.

    :param element_id: ObjectId
    :param table_name: str
    :return: bool
    """
    db = __connectToMongo()
    collection = db[table_name]
    if collection.delete_one({"_id": element_id}).deleted_count == 1:
        return None
    else:
        raise ElementNotFound


def getAllElements(
    limit: int, table_name: str
) -> Union[List[FioResult], List[Tag], List[object]]:
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
        elif table_name == tagsTable:
            elements_table.append(Tag.parse_obj(element))
        else:
            elements_table.append(element)
    return elements_table


def getElementById(
    object_id: ObjectId, table_name: str
) -> Union[FioResult, Tag, object]:
    """
    Get a element from the database with its ID.

    :param object_id: ObjectId
    :param table_name: str
    :return: Union[FioResult, Tag, object]
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
    elif table_name == tagsTable:
        return Tag.parse_obj(result)
    else:
        return result


def get_tag_by_name(tag_name: str) -> Tag:
    db = __connectToMongo()
    collection = db[tagsTable]
    tag = collection.find_one({"name": tag_name})
    if tag is None:
        raise ElementNotFound
    # Convert the objectId "_id" to a string "id"
    tag["id"] = str(tag["_id"])
    tag.pop("_id")
    return Tag.parse_obj(tag)


def get_shorten_results_by_tags_id(
    tag_id_list: List[ObjectId], limit: int
) -> List[ShortenResult]:
    """
    Return results matching given tags.

    :param tag_id_list: List[ObjectId]
    :param limit: int
    :return: List[FioResult]
    """
    results_list = []
    for result in getAllElements(limit, resultTable):
        for tag_id in tag_id_list:
            if str(tag_id) not in result.tags:
                break
            results_list.append(result.shortened())
    return results_list
