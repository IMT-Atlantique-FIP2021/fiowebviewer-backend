from pymongo import MongoClient

from src.tools.importers import jsonfileToDic

databaseConfigFile = "./database.json"

database = jsonfileToDic(databaseConfigFile)


def insertInMongo(my_dic):
    """
    Insert a dict object in the mongo

    :param my_dic: dic
    """

    # establishing connection
    connect = MongoClient(database["host"], database["port"], username=database["username"],
                          password=database["password"])

    db = connect[database["name"]]
    collection = db[database["name"]]

    collection.insert_one(my_dic)
