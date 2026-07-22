from config import Bot
from modules.common.keyboard import back_to_main_menu_keyboard
from .labeler import labeler
from modules.common.get_user_info import get_first_name, get_last_name, get_user_fullname
from database.users import add_user
from common.get_or_create_user import get_or_create_user


@labeler.message(payload={"cmd": "add_user_name"})
async def add_user_name(message):
    await add_user(message.from_id, await get_user_fullname(message))
    await message.answer(
        
    )