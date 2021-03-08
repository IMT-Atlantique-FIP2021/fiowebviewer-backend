from pymongo import MongoClient
from bson.objectid import ObjectId
from tools.importers import jsonfileToDic

databaseConfigFile = "./database.json"

dbConfig = jsonfileToDic(databaseConfigFile)


def connectToMongo():
    # establishing connection
    # connect = MongoClient(
    #     host=database["host"], 
    #     port=database["port"], 
    #     username=database["username"],
    #     password=database["password"]
    # )
    # db = connect[database["name"]]
    # collection = db[database["name"]]

    client = MongoClient(**dbConfig["connect"])
    db = client[dbConfig["db"]]
    collection = db[dbConfig["collection"]]

    return collection


def insertInMongo(my_dic):
    """
    Insert a dict object in the mongo

    :param my_dic: dic
    """
    collection = connectToMongo()
    # TODO add a data verification
    collection.insert_one(my_dic)


def getAllResults():
    """
    Get all result from database
    :return: list of all result
    """
    collection = connectToMongo()
    all_results = []
    for e in collection.find():
        # Convert the objectId "_id" to a string "id"
        e["id"] = str(e["_id"])
        e.pop("_id")
        all_results.append(e)
    return all_results


def getResultById(result_id):
    """
    Get a result from database
    :return: a result
    """
    collection = connectToMongo()
    result = collection.find_one({"_id": ObjectId(result_id)})
    if result is None:
        return {}
    else:
        # Convert the objectId "_id" to a string "id"
        result["id"] = str(result["_id"])
        result.pop("_id")
        return result
