import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values


token = dotenv_values('.env')['BOT_TOKEN']
bot = Bot(token = token) #отправляет
dispatcher = Dispatcher() #принимает


@dispatcher.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}")

@dispatcher.message(Command("myinfo"))
async def my_info_handler(message: types.Message):
   id_person =message.from_user.id
   name = message.from_user.first_name
   username = message.from_user.username
   await message.answer(f"Ваш id: {id_person}. Имя: {name}. Имя пользователя: {username} ")

names = ['Sumaya', 'Ayana', 'Mika', 'Manya', 'Alex', 'levi', 'Sakura']
@dispatcher.message(Command("random"))
async def random_name_handler(message: types.Message):
    name_random = random.choice (names)
    await message.answer(f" {name_random}")


@dispatcher.message()
async def echo_handler(message: types.Message):
    txt = message.text
    await message.answer(txt)

async def main():
    await dispatcher.start_polling(bot)  # запуск бота



if __name__ == '__main__':
    asyncio.run(main())