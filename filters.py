from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

class IsCustomFilter(BoundFilter):
    key = "is_custom_filter"

    def __init__(self, is_custom_filter: bool) -> None:
        self.is_custom_filter = is_custom_filter

    async def check(self, message: types.Message) -> bool:
        return message.from_user.id == self.is_custom_filter