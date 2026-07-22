from config import Bot, MAX_DATE
#from vkbottle.dispatch.rules.base import PayloadRule
import re
from .keyboard import menu_keyboard, get_menu_keyboard
from .labeler import labeler
from modules.common.get_user_info import get_first_name, get_last_name, get_user_fullname
from database.users import add_user

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
    await add_user(
        message.from_id,
        await get_user_fullname(message)
    )

    await message.answer(
        "Доступные даты:",
        keyboard=await get_menu_keyboard()
    )


@labeler.message(payload={'cmd': "menu"})
async def menu(message):
    await add_user(message.from_id, await get_user_fullname(message))
    f = open(f'/home/Rostislav/Mysterius Letka VKBot/modules/menu/data/{MAX_DATE}.txt').read()
    await message.answer(
        f,
        keyboard=menu_keyboard
    )