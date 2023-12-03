from pymongo import MongoClient
from config import load_config, Config


def get_db(config: Config = load_config()):
    CONNECTION_STRING: str = (f"mongodb://{config.mongo_key.MONGO_INITDB_ROOT_USERNAME}:"
                              f"{config.mongo_key.MONGO_INITDB_ROOT_PASSWORD}@"
                              f"{config.mongo_key.MONGO_INITDB_HOST}:27017/")
    client = MongoClient(CONNECTION_STRING)
    return client


if __name__ == '__main__':
    pass
