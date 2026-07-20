from vkbottle.bot import Message
from .labeler import labeler
from modules.common.keyboard import back_to_main_menu_keyboard

# @labeler.message(payload={"cmd": "menu"})
# async def menu_demo(message: Message):
#     await message.answer(
#         "🍽 Меню на сегодня:\n\n"
#         "Завтрак:\nКаша, бутерброд, чай\n\n"
#         "Обед:\nСуп, второе, компот\n\n"
#         "Полдник:\nПеченье, сок\n\n"
#         "Ужин:\nМакароны с котлетой"
#     )


@labeler.message(payload={"cmd": "night"})
async def night_demo(message: Message):
    await message.answer(
        "🌙 Кто ночной сегодня?\n\n"
        "Андей Бобылев\n",
        keyboard=back_to_main_menu_keyboard
    )


@labeler.message(payload={"cmd": "shedule"})
async def schedule_demo(message: Message):
    await message.answer(
        "📅 Расписание летки:\n\n"
        "07:00 — Подъём\n"
        "07:30 — Завтрак\n"
        "8:30 — Пары\n"
        "14:10 — Обед\n"
        "18:00 — Мероприятия\n"
        "23:00 — Отбой",
        keyboard=back_to_main_menu_keyboard
    )


@labeler.message(payload={"cmd": "common_info"})
async def info_demo(message: Message):
    await message.answer(
        "🏕 Общая информация про летку:\n\n"
        "Название: Летняя школа\n"
        "Корпус: главный корпус\n"
        "Воспитатели:\n"
        "Иван Иванович\n"
        "Мария Сергеевна\n\n"
        "Правила и важная информация будут здесь.",
        keyboard=back_to_main_menu_keyboard
    )


# @labeler.message(payload={"cmd": "weather"})
# async def weather_demo(message: Message):
#     await message.answer(
#         "🌤 Погода возле НГУ:\n\n"
#         "Температура: +22°C\n"
#         "Ощущается как +21°C\n"
#         "Ветер: 3 м/с\n"
#         "Осадки: нет"
#     )


@labeler.message(payload={"cmd": "invite_komsenok"})
async def invite_demo(message: Message):
    await message.answer(
        "🤝 Приглашение комсенка в блок\n\n"
        "Для начала давайте познакомимся! Напишите свое ФИО, класс, блок куда хотите пргосить комсенка\n"
        "Выберите комсенка, которого хотите пригласить.\n\n"
        "После отправки заявки воспитатель должен её подтвердить.\n\n\n\n"
        "И тд и тп, функция пока не реализована",
        keyboard=back_to_main_menu_keyboard
    )