from aiogram import Router, types
from aiogram.filters import Command

my_info_router = Router()

@my_info_router.message(Command("myinfo"))
async def my_info_handler(message: types.Message):
   id_person =message.from_user.id
   name = message.from_user.first_name
   username = message.from_user.username
   await message.answer(f"Ваш id: {id_person}. Имя: {name}. Имя пользователя: {username} ")
