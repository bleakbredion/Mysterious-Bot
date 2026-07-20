import asyncio

from database.menu import add_menu, get_menu, get_available_dates, delete_menu, update_menu
from database.constants import Role

from datetime import date

async def main():
    await delete_menu(date(2026,8,1))
    menu = await get_available_dates()
    print(menu)

if __name__ == "__main__":
    asyncio.run(main())
