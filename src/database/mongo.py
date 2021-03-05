from pymongo import MongoClient

from src.tools.importers import jsonfileToDic

databaseConfigFile = "./database.json"

database = jsonfileToDic(databaseConfigFile)


def connectToMongo():
    # establishing connection
    connect = MongoClient(database["host"], database["port"], username=database["username"],
                          password=database["password"])

    db = connect[database["name"]]
    collection = db[database["name"]]

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
