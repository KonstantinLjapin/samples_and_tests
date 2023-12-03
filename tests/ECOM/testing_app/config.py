from dataclasses import dataclass

from environs import Env


@dataclass
class MongoKey:
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_INITDB_DATABASE: str
    MONGO_INITDB_HOST: str


@dataclass
class Config:
    mongo_key: MongoKey


def load_config(path: str = None):
    env = Env()
    env.read_env(path)
    return Config(
        mongo_key=MongoKey(MONGO_INITDB_DATABASE=env.str("MONGO_INITDB_ROOT_USERNAME"),
                           MONGO_INITDB_ROOT_PASSWORD=env.str("MONGO_INITDB_ROOT_PASSWORD"),
                           MONGO_INITDB_ROOT_USERNAME=env.str("MONGO_INITDB_ROOT_USERNAME"),
                           MONGO_INITDB_HOST=env.str("MONGO_INITDB_HOST"),)
        ,
    )
