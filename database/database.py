import aiosqlite

from config import DB_PATH


async def get_db() -> aiosqlite.Connection:
    db = await aiosqlite.connect(DB_PATH)

    # Получать строки как словари:
    # row["fullname"], а не row[0]
    db.row_factory = aiosqlite.Row

    return db