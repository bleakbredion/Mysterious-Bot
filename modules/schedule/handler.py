from config import Bot
from modules.common.keyboard import back_to_main_menu_keyboard
from .labeler import labeler
from modules.common.get_user_info import get_first_name, get_id, get_last_name
from modules.common.create_or_update_user import create_or_update_user


@labeler.message(payload={"cmd": "shedule"})
async def shedule(message):
    create_or_update_user(get_id, get_first_name, get_last_name)
    await message.answer(
        "Рассписание летки",
        keyboard=back_to_main_menu_keyboard
    )