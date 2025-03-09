import logging
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()
logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def start_command(message: Message):
    name, id = message.from_user.full_name, message.from_user.id
    logging.info(f"Пользователь {name}({id}) запустил бота")
    await message.answer(
        "Привет! Ты можешь ознакомиться с командами, написав /help"
        )
