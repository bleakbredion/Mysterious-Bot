from vkbottle import Keyboard, Text
from database.menu import get_available_dates


async def get_menu_keyboard():
    keyboard = Keyboard(inline=True)

    dates = await get_available_dates()

    for index, menu_date in enumerate(dates, start=1):
        keyboard.add(
            Text(
                menu_date,
                payload={
                    "cmd": "menu",
                    "date": menu_date
                }
            )
        )

        if index % 4 == 0:
            keyboard.row()

    return keyboard.get_json()


menu_keyboard = (
    Keyboard(inline=True)
    .add(Text("На главную", payload={'cmd': 'start'}))
    .row()
    .add(Text("Назад", payload={'cmd': 'menu_date'}))
    .get_json()
)