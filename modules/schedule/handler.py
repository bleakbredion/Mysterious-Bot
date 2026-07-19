from config import Bot
from modules.common.keyboard import back_to_main_menu_keyboard
from .labeler import labeler

@labeler.message(payload={"cmd": "shedule"})
async def shedule(message):
    await message.answer(
        "Рассписание летки",
        keyboard=back_to_main_menu_keyboard
    )