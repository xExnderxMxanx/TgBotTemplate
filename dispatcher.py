import asyncio

from aiogram import Bot, Dispatcher
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from loguru import logger

from filters import IsCustomFilter

# Configure logger
logger.add("./Bot.log", level="DEBUG",
            format="<b><g>{time:%Y-%m-%d %r}</g>:<level>{level}</level>:<lw>{name}</lw>:<level>{message}</level></b>",
            colorize=True)

# init Bot and Db session
bot = Bot(token=config('BOT_TOKEN'), parse_mode="MarkDown")
dp = Dispatcher(bot)

DB_url = config("URL_DB")
engine = create_engine(DB_url)
model = declarative_base()
DB_session = sessionmaker(bind=engine)
db_s = DB_session()

# activate filters
dp.filters_factory.bind(IsCustomFilter)