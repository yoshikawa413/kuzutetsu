import json
from pymongo import MongoClient


def lambda_handler(event, context):
    client = MongoClient(
        "",
        username="",
        password="",
    )
    db = client["test3"]
    collection = db["test3"]
    result = collection.insert_one({"id": 10, "name": "aaa"})
    [print(_) for _ in collection.find()]
    [print(_) for _ in client.list_database_names()]
    collection.delete_many({})

    client.close()

    # TODO implement
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
