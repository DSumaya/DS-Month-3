from aiogram import Router, types
from aiogram.filters import Command

menu_router = Router()

item = (f'Пицца Маргарита: 350 сом\n Пицца Пепперони: 360 сом\n Пицца с грибами: 380 сом\n'
        f'Пицца с морепродуктами: 400 сом\n Пицца Сырная: 300 сом')

@menu_router.message(Command("menu"))
async def menu_handler(message: types.Message):
    menu = f"Наше меню: \n '{item}"
    await message.answer(menu)



