from config import bot
from keyboards.start import start_keyboard


@bot.on.message(payload={"cmd": "shedule"})
async def shedule(message):
    await message.answer(
        "Рассписание летки"
    )