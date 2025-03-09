import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from config.config import Config, get_url, load_config
from handlers import other_handlers
from middlewares import DBSessionMiddleware


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )
    config: Config = load_config()

    engine = create_async_engine(get_url())
    sessionmaker = async_sessionmaker(engine)
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    # dp.include_router(user_handlers.router)
    # dp.include_router(admin_handlers.router)
    dp.include_router(other_handlers.router)
    dp.update.outer_middleware(DBSessionMiddleware(sessionmaker))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
