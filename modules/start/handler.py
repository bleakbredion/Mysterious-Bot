from config import bot
from keyboards.start import start_keyboard
from vkbottle.bot import BotLabeler


common_labeler = BotLabeler()


@common_labeler.message(text=["/start"])
async def start(message):
    await message.answer(
        "Привет! Что ты хочешь узнать?",
        keyboard=start_keyboard
    )


@common_labeler.message(payload={'cmd': "start"})
async def menu(message):
    await message.answer(
        "Что хочешь узнать?",
        keyboard=start_keyboard
    )
