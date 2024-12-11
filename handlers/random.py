import random
from aiogram import Router, types
from aiogram.filters import Command

random_router = Router()

names = ['Sumaya', 'Ayana', 'Mika', 'Manya', 'Alex', 'levi', 'Sakura']
@random_router.message(Command("random"))
async def random_name_handler(message: types.Message):
    name_random = random.choice(names)
    await message.answer(f" {name_random}")