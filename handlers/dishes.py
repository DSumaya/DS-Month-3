from aiogram import Router, types
from aiogram.filters import Command

from bot_config import database
from pprint import pprint


restaurant_router = Router()


@restaurant_router.message(Command("dishes"))
async def show_all_dishes(message: types.Message):
    food_list = database.get_all_dishes()
    pprint(food_list)
    for food in food_list:
        txt = f"Название: {food['name']}\nЦена: {food['price']}\nОписание: {food['description']}\nКатегория:{food['categories']}"
        await message.answer(txt)