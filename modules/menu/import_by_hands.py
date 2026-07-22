import asyncio

from modules.menu.hand_importer import import_menu


async def main():
    await import_menu(
        "modules/menu/data/2.txt"
    )

asyncio.run(main())