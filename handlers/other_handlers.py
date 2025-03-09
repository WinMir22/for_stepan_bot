import html
import logging
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from lexicon.lexicon_ru import lexicon

router = Router()
logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def start_command(message: Message):
    name, id = message.from_user.full_name, message.from_user.id
    formatting_name = "<b>" + html.escape(name) + "</b>"
    logging.info(f"Пользователь {name}({id}) запустил бота")
    await message.answer(lexicon["start"].format(formatting_name))
