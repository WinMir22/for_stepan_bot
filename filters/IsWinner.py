from aiogram.types import TelegramObject
from aiogram.filters import BaseFilter

from config.config import load_config


class IsWinner(BaseFilter):
    async def __call__(self, obj: TelegramObject) -> bool:
        config = load_config()
        return obj.from_user.id in config.tg_bot.winner_id
