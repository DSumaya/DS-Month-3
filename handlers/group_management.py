from aiogram import Router, F, types
from aiogram.filters import Command

group_router = Router()
group_router.message.filter(F.chat.type != "individual")


WORDS = ("лет", "год")

@group_router.message(Command('ban', prefix='!'))
async def ban_user(message:types.Message):
    if not message.reply_to_message:
        await message.reply("Команда !ban должна быть ответом на сообщение!")
        return
    if any(word in message.text.lower() for word in WORDS):
        user = message.from_user.id
        await message.bot.ban_chat_member(
        chat_id=message.chat.id,
        user_id=user)
    await message.answer(f"Пользователь {message.from_user.full_name} был заблокирован за использование запрещенных слов.")



@group_router.message()
async def check_words_handler(message: types.Message):
     await message.answer(f'Привет, {message.from_user.first_name}')



