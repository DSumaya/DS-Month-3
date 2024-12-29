from aiogram import Router, F, types
from aiogram.filters import Command


start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    print(message.chat.type)
    name = message.from_user.first_name
    #await message.answer(f"Добро пожаловать {name}. Для просмотра меню  /menu")

    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data="review")
            ]
        ]
    )
    await message.answer(f"Привет, {name}", reply_markup=kb)




