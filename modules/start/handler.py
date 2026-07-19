from .labeler import labeler
from .keyboard import start_keyboard

@labeler.message(text="/start")
async def start(message):
    await message.answer(
        "Привет! Что ты хочешь узнать?",
        keyboard=start_keyboard
    )

@labeler.message(payload={"cmd": "start"})
async def menu(message):
    await message.answer(
        "Что хочешь узнать?",
        keyboard=start_keyboard
    )