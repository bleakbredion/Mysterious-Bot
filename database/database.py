import aiosqlite

from config import DB_PATH


def get_db() -> aiosqlite.Connection:
    return aiosqlite.connect(DB_PATH)