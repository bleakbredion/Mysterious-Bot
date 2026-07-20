import asyncio

from database.users import add_user, get_user, update_user
from database.constants import Role

async def main():
    await update_user(723227228, "Мирошников Глеб", Role.KOMSENOK)
    user = await get_user(723227228)
    print(user)


if __name__ == "__main__":
    asyncio.run(main())
