from config import Bot, MAX_DATE
#from vkbottle.dispatch.rules.base import PayloadRule
import re
from .keyboard import menu_keyboard
from .keyboard import menu_date_keyboard
from .labeler import labeler
from modules.common.get_user_info import get_first_name, get_id, get_last_name
from modules.common.create_or_update_user import create_or_update_user


# @bot.on.message(PayloadRule({"cmd": re.compile(r"menu_date_\d+")}))
# @labeler.message(text=re.compile(r'^menu_date_([1-9]|1[0-9]|2[0-5])$'))
# async def menu_date(message):
#     date = int(message.payload.get("cmd").split('_')[-1])
#     f = open(f'/home/Rostislav/Mysterius Letka VKBot/menu/menu_{date}.txt').read()

#     await message.answer(
#         f,
#         keyboard=menu_keyboard
#     )


@labeler.message(payload={'cmd': "menu_date"})
async def menu_date(message):
    create_or_update_user(get_id, get_first_name, get_last_name)
    await message.answer(
        "Доступные даты:",
        keyboard=menu_date_keyboard
    )


@labeler.message(payload={'cmd': "menu"})
async def menu(message):
    create_or_update_user(get_id, get_first_name, get_last_name)
    f = open(f'/home/Rostislav/Mysterius Letka VKBot/modules/menu/data/{MAX_DATE}.txt').read()
    await message.answer(
        f,
        keyboard=menu_keyboard
    )