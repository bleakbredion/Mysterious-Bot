from datetime import datetime
from pathlib import Path

from database.menu import add_menu
from database.database import get_db

MEALS = {
    "Завтрак:": "breakfast",
    "Обед:": "lunch",
    "Полдник:": "afternoon",
    "Ужин:": "dinner",
}


def parse_menu_file(path: str | Path) -> dict:
    path = Path(path)

    lines = [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    menu = {
        "date": None,
        "duty_class": None,
        "breakfast": "",
        "lunch": "",
        "afternoon": "",
        "dinner": "",
    }

    current_section = None

    for line in lines:

        # дата
        if menu["date"] is None:
            menu["date"] = datetime.strptime(
                line,
                "%d.%m.%y"
            ).date()

            continue

        # дежурный класс
        if line.startswith("Дежурный класс:"):
            menu["duty_class"] = (
                line.split(":", 1)[1]
                .strip()
            )

            continue

        # раздел еды
        if line in MEALS:
            current_section = MEALS[line]
            continue

        # блюда
        if line.startswith("-") and current_section:
            menu[current_section] += (
                line[1:].strip() + "\n"
            )


    for meal in MEALS.values():
        menu[meal] = menu[meal].strip()


    return menu


async def import_menu(path: str | Path) -> None:
    menu = parse_menu_file(path)

    await add_menu(
        menu_date=menu["date"],
        duty_class=menu["duty_class"],
        breakfast=menu["breakfast"],
        lunch=menu["lunch"],
        afternoon=menu["afternoon"],
        dinner=menu["dinner"],
    )
    # async with get_db() as db:
    #     async with db.execute("SELECT date FROM menus") as cursor:
    #         print(await cursor.fetchall())


