from .labeler import labeler
from .keyboard import start_keyboard
from modules.common.get_user_info import get_first_name, get_last_name, get_user_fullname
from database.users import add_user


@labeler.message(text="/start")
async def start(message):
    await add_user(message.from_id, await get_user_fullname(message))
    await message.answer(
        "Привет! Что ты хочешь узнать?",
        keyboard=start_keyboard
    )

@labeler.message(payload={"cmd": "start"})
async def menu(message):
    await add_user(message.from_id, await get_user_fullname(message))
    await message.answer(
        "Что хочешь узнать?",
        keyboard=start_keyboard
    )