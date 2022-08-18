from configparser import ConfigParser
from dataclasses import dataclass

@dataclass
class App:
    version: str
    is_prod: bool
    path_log: str | None = None

@dataclass
class Bot:
    token: str
    chat_id: int
    channel_id: int
    
@dataclass
class Redis:
    password: str

@dataclass
class DataBase:
    user: str
    db_name: str
    password: str
    db_url: str
    host: str = "localhost"
    port: int = 5432
    
@dataclass
class Conf:
    bot: Bot
    db: DataBase
    redis: Redis
    app: App

def load_config(path: str) -> Conf:
    config = ConfigParser()
    config.read(path)
    
    return Conf(Bot(**config["TG"]), DataBase(**config["DB"]),
                Redis(**config["REDIS"]),
                App(config["APP"].get("version"), config["APP"].getboolean("is_prod")))