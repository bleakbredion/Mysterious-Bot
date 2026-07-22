import asyncio

from database.users import add_user, get_user, update_user, get_all_users
from database.constants import Role

async def main():
    # await update_user(407135481, "Зяблов Ростик", Role.ADMIN)
    users = await get_all_users()
    print(users)


if __name__ == "__main__":
    asyncio.run(main())
