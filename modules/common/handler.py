from config import Bot
from .labeler import labeler_exit
from .keyboard import back_to_main_menu_keyboard
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


@labeler_exit.message()
async def exit_answer(message):
    create_or_update_user(get_id, get_first_name, get_last_name)
    await message.answer(
        "Эта функция сейчас недоступна",
        keyboard=back_to_main_menu_keyboard
    )