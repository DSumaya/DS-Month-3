from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from bot_config import database
from pprint import pprint


restaurant_management_router = Router()
# restaurant_management_router.message.filter(F.from_user.id == 278850960)


class Restaurant(StatesGroup):
    name = State()
    price = State()
    cover = State()
    description = State()
    categories = State()


@restaurant_management_router.message(Command("food"))
async def add_dishes (message: types.Message, state:FSMContext):
    await message.answer('Введите название:')
    await state.set_state(Restaurant.name)


@restaurant_management_router.message(Restaurant.name)
async def add_name (message: types.Message, state:FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите цену:')
    await state.set_state(Restaurant.price)


@restaurant_management_router.message(Restaurant.price)
async def process_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Загрузите фото:")
    await state.set_state(Restaurant.cover)


@restaurant_management_router.message(Restaurant.cover, F.photo)
async def add_price (message: types.Message, state:FSMContext):
    cover_list = message.photo
    pprint(cover_list)
    biggest_image = cover_list[-1]
    biggest_image_id = biggest_image.file_id
    await state.update_data(cover=biggest_image_id)
    await message.answer('Напишите описание:')
    await state.set_state(Restaurant.description)


@restaurant_management_router.message(Restaurant.description)
async def change_description(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Завтраки"),
                types.KeyboardButton(text="Горячие блюда"),
                types.KeyboardButton(text="Супы")
            ],
            [
                types.KeyboardButton(text="Салаты"),
                types.KeyboardButton(text="Напитки"),
                types.KeyboardButton(text="Десерты")
            ],
        ],
        resize_keyboard=True
    )
    await state.update_data(description=message.text)
    await message.answer('Выберите категорию:',  reply_markup=kb)
    await state.set_state(Restaurant.categories)


@restaurant_management_router.message(Restaurant.categories)
async def add_categories(message: types.Message, state: FSMContext):
    await state.update_data(categories=message.text)
    data = await state.get_data()
    print(data)
    database.save_dishes(data)
    await message.answer("Блюдо добавлено! Для просмотра добавленных блюд нажмите /dishes")
    await state.clear()