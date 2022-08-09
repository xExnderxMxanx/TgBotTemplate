from aiogram import types

from dispatcher import dp
from model import *

@dp.message_handler()
async def first_handler(message: types.Message):
    return await message.answer(message.text)