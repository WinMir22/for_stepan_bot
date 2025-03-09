from aiogram import types
from aiogram.filters import BaseFilter


class IsWinner(BaseFilter):
    def __init__(self, winner_id: int) -> None:
        self.winner_id = winner_id

    async def __call__(self, message: types.Message) -> bool:
        return message.from_user.id in self.winner_id
