from .labeler import labeler
from .keyboard import start_keyboard
from modules.common.get_user_info import get_first_name, get_id, get_last_name
from modules.common.create_or_update_user import create_or_update_user


@labeler.message(text="/start")
async def start(message):
    create_or_update_user(get_id, get_first_name, get_last_name)
    await message.answer(
        "Привет! Что ты хочешь узнать?",
        keyboard=start_keyboard
    )

@labeler.message(payload={"cmd": "start"})
async def menu(message):
    create_or_update_user(get_id, get_first_name, get_last_name)
    await message.answer(
        "Что хочешь узнать?",
        keyboard=start_keyboard
    )