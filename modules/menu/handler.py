from config import bot, MAX_DATE
from vkbottle.dispatch.rules.base import PayloadRule
import re
from keyboards.menu import menu_keyboard
from keyboards.menu_date import menu_date_keyboard


# @bot.on.message(PayloadRule({"cmd": re.compile(r"menu_date_\d+")}))
@bot.on.message(text=re.compile(r'^menu_date_([1-9]|1[0-9]|2[0-5])$'))
async def menu_date(message):
    date = int(message.payload.get("cmd").split('_')[-1])
    f = open(f'/home/Rostislav/Mysterius Letka VKBot/menu/menu_{date}.txt').read()

    await message.answer(
        f,
        keyboard=menu_keyboard
    )


@bot.on.message(payload={'cmd': "menu_date"})
async def menu_date(message):
    await message.answer(
        "Доступные даты:",
        keyboard=menu_date_keyboard
    )


@bot.on.message(payload={'cmd': "menu"})
async def menu(message):
    f = open(f'/home/Rostislav/Mysterius Letka VKBot/menu/menu_{MAX_DATE}.txt').read()
    await message.answer(
        f,
        keyboard=menu_keyboard
    )