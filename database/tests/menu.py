import asyncio

from database.menu import add_menu, get_menu, get_available_dates, delete_menu
from database.constants import Role
from database.database import get_db
from datetime import date

async def main():
    await delete_menu(date(2026, 6, 2))
    

if __name__ == "__main__":
    asyncio.run(main())
