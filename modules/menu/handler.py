from config import Bot, MAX_DATE
#from vkbottle.dispatch.rules.base import PayloadRule
import re
from .keyboard import menu_keyboard, get_menu_keyboard
from .labeler import labeler
from modules.common.get_user_info import get_first_name, get_last_name, get_user_fullname
from database.users import add_user
from database.menu import get_menu
from datetime import date
from vkbottle.bot import Message
from logger import logger



@labeler.message()
async def menu_router(message: Message):
    payload = message.get_payload_json()

    if not payload:
        return

    match payload.get("cmd"):
        case "menu_date":
            await add_user(
                message.from_id,
                await get_user_fullname(message)
            )
            logger.info(
                "Add or do nothing with user %s",
                message.from_id
            )

            await message.answer(
                "Доступные даты:",
                keyboard=await get_menu_keyboard()
            )
            logger.info(
                "User %s opened menu dates",
                message.from_id
            )

        case "menu":
            await add_user(
                message.from_id,
                await get_user_fullname(message)
            )

            logger.info(
                "Add or do nothing with user %s",
                message.from_id
            )

            f = open(
                f"/home/Rostislav/Mysterius Letka VKBot/modules/menu/data/{MAX_DATE}.txt"
            ).read()

            await message.answer(
                f,
                keyboard=menu_keyboard
            )
            logger.info(
                "User %s opened current menu",
                message.from_id
            )

        case "menu_on_date":
            await add_user(
                message.from_id,
                await get_user_fullname(message)
            )
            logger.info(
                "Add or do nothing with user %s",
                message.from_id
            )

            menu_date = date.fromisoformat(payload["date"])
            menu = await get_menu(menu_date)

            logger.info(
                "User %s looking for %s date menu",
                message.from_id,
                menu_date.isoformat()
            )

            if menu is None:
                await message.answer("Меню не найдено")
                logger.warning(
                    "Menu for %s not found",
                    menu_date.isoformat()
                )
            else:
                await message.answer(
                    f"🍽 Меню на {menu_date.strftime('%d.%m')}\n\n"
                    f"🧑‍🍳 Дежурный класс: {menu["duty_class"]}.\n\n"
                    f"🥣 Завтрак: {menu["breakfast"]}\n"
                    f"🍲 Обед: {menu["lunch"]}\n"
                    f"☕ Полдник: {menu["afternoon"]}\n"
                    f"🍽 Ужин: {menu["dinner"]}",
                    keyboard=menu_keyboard
                )
                logger.info(
                    "Menu for %s sent to user %s",
                    menu_date.isoformat(),
                    message.from_id,
                )