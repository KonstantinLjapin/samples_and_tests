from pymongo import MongoClient
from config import load_config, Config


def get_db(config: Config = load_config()):
    CONNECTION_STRING: str = (f"mongodb://{config.mongo_key.MONGO_INITDB_ROOT_USERNAME}:"
                              f"{config.mongo_key.MONGO_INITDB_ROOT_PASSWORD}@"
                              f"{config.mongo_key.MONGO_INITDB_HOST}:27017/")
    client = MongoClient(CONNECTION_STRING)
    return client


fake_db = {"data": [{
    "name": "First",
    "field_name_1": "boba@iu.ru",
    "field_name_2": "79663678900"},
    {
        "name": "Last",
        "field_name_1": "shlepa@zoo.gb",
        "field_name_2": "79656788823"}]}


def up_load(data: dict):
    client = get_db()
    dbname = client['task_dict']
    collection_name = dbname["users_form"]
    try:
        for _ in collection_name.find():
            print("del garbage")
            collection_name.delete_one(data)
    except TypeError as err:
        print("error")
        collection_name.insert_one(data)
        print("face_db_upload")
        for item in collection_name.find():
            print(item.get("data"))
    finally:
        print("face_db_upload")
        collection_name.insert_one(data)
        for item in collection_name.find():
            print(item.get("data"))
    client.close()


up_load(fake_db)
