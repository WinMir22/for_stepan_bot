from aiogram import types
from aiogram.filters import BaseFilter


class IsDima(BaseFilter):
    def __init__(self, dima_id: int) -> None:
        self.dima_id = dima_id

    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id in self.dima_id
