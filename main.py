import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config.config import Config, load_config


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )
    config: Config = load_config()
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    # dp.include_router(user_handlers.router)
    # dp.include_router(admin_handlers.router)
    # dp.update.outer_middleware(DBMiddleware())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
