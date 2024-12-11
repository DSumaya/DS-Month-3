import asyncio
import logging

from bot_config import bot, dispatcher
from handlers.start import start_router
from handlers.my_info import my_info_router
from handlers.random import random_router
from handlers.pizza_empire_menu import menu_router
from handlers.other_message import echo_router



async def main():
    dispatcher.include_router(start_router)
    dispatcher.include_router(my_info_router)
    dispatcher.include_router(random_router)
    dispatcher.include_router(menu_router)
    dispatcher.include_router(echo_router)




    await dispatcher.start_polling(bot)  # запуск бота


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())