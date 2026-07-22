import asyncio

from database.menu import add_menu, get_menu, get_available_dates, delete_menu
from database.constants import Role
from database.database import get_db
from datetime import date

async def main():
    menu = await get_menu(date(2026, 8, 2))
    print(menu)

if __name__ == "__main__":
    asyncio.run(main())
