import asyncio
import logging

from bot_config import dispatcher, bot, database
from handlers import individual_router
from handlers.group_management import group_router

async def on_startup():
    database.crate_tables()

async def main():
    dispatcher.include_router(individual_router)
    dispatcher.include_router(group_router)

    dispatcher.startup.register(on_startup)


    await dispatcher.start_polling(bot)  # запуск бота


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())