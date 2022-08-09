from cgitb import text
from aiogram import types

from dispatcher import dp
from model import *

@dp.callback_query_handler(text="callback")
async def first_callback_handler(callback_query: types.CallbackQuery):
    pass