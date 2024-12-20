from aiogram import Router, F, types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from bot_config import  database


dialog_router = Router()


class RestourantReview(StatesGroup):
    name = State()
    phone_or_instagram = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


@dialog_router.callback_query(F.data == "review")
async def review(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer("Как вас зовут?")
    await state.set_state(RestourantReview.name)


@dialog_router.message(RestourantReview.name)
async def get_number_instagram (message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Ваш номер телефона или инстаграм?")
    await state.set_state(RestourantReview.phone_or_instagram)


@dialog_router.message(RestourantReview.phone_or_instagram)
async def get_food_rating(message: types.Message, state: FSMContext):
        await state.update_data(phone_or_instagram=message.text)
        await message.answer("Как оцениваете качество еды?")
        await state.set_state(RestourantReview.food_rating)


@dialog_router.message(RestourantReview.food_rating)
async def get_cleanliness_rating(message: types.Message, state: FSMContext):
        kb = types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(text="Плохо"),
                    types.KeyboardButton(text="Удовлетворительно")
                ],
                [
                    types.KeyboardButton(text="Хорошо"),
                    types.KeyboardButton(text="Отлично")
                ],
            ],
            resize_keyboard=True
        )
        if message.text in ("Плохо", "Удовлетворительно", "Хорошо", "Отлично"):

           await state.update_data(food_rating=message.text)
           await state.set_state(RestourantReview.cleanliness_rating)
           await message.answer("Как оцениваете чистоту заведения?", reply_markup=kb)



@dialog_router.message(RestourantReview.cleanliness_rating)
async def cleanliness_rating(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Плохо"),
                types.KeyboardButton(text="Удовлетворительно")
            ],
            [
                types.KeyboardButton(text="Хорошо"),
                types.KeyboardButton(text="Отлично")
            ],
        ],
        resize_keyboard=True
    )
    if message.text in ("Плохо", "Удовлетворительно", "Хорошо", "Отлично"):
        rating = message.text
        if rating == "Плохо":
            rating_num = 2
        elif rating == "Удовлетворительно":
            rating_num = 3
        elif rating == "Хорошо":
            rating_num = 4
        elif rating == "Отлично":
            rating_num = 5
        else:
            return
    await state.update_data(rating=rating_num)
    await state.update_data(cleanliness_rating=message.text)
    await message.answer("Дополнительные комментарии/жалоба?", reply_markup=kb)
    await state.set_state(RestourantReview.extra_comments)


@dialog_router.message(RestourantReview.extra_comments)
async def start_opros(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    await message.answer("Спасибо за пройденый опрос!")
    data = await state.get_data()
    print(data)
    database.save_survey(data)

    await state.clear()








