import asyncio

from aiogram import Bot, Dispatcher
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from loguru import logger

from config import load_config
from filters import IsCustomFilter

conf = load_config("config.ini")

# Configure logger
logger.add("./Bot.log", level="DEBUG",
            format="<b><g>{time:%Y-%m-%d %r}</g>:<level>{level}</level>:<lw>{name}</lw>:<level>{message}</level></b>",
            colorize=True)

# init Bot and Db session
bot = Bot(token=conf.bot.token, parse_mode="MarkdownV2")
dp = Dispatcher(bot)

DB_url = conf.db.db_url
engine = create_engine(DB_url)
model = declarative_base()
DB_session = sessionmaker(bind=engine)
db_s = DB_session()

# activate filters
dp.filters_factory.bind(IsCustomFilter)