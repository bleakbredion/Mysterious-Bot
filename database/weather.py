import aiosqlite
from logger import logger

from database.database import get_db
from modules.common.time import get_time


async def save_weather(weather: str) -> None:
    try:
        async with get_db() as db:
            updated_at = get_time().isoformat()

            await db.execute(
                """
                INSERT OR REPLACE INTO weather(id, weather, updated_at)
                VALUES (1, ?, ?)
                """,
                (weather, updated_at),
            )
            await db.commit()

    except aiosqlite.Error as e:
        logger.exception(f"Failed to save weather: {e}")


async def get_weather() -> tuple[str, str] | None:
    try:
        async with get_db() as db:
            cursor = await db.execute(
                """
                SELECT weather, updated_at
                FROM weather
                WHERE id = 1
                """
            )
            return await cursor.fetchone()

    except aiosqlite.Error as e:
        logger.exception(f"Failed to get weather: {e}")
        return None


async def clear_weather() -> None:
    try:
        async with get_db() as db:
            await db.execute(
                """
                DELETE FROM weather
                WHERE id = 1
                """
            )
            await db.commit()

    except aiosqlite.Error as e:
        logger.exception(f"Failed to clear weather: {e}")


async def weather_exists() -> bool:
    try:
        async with get_db() as db:
            cursor = await db.execute(
                """
                SELECT 1
                FROM weather
                WHERE id = 1
                """
            )
            return await cursor.fetchone() is not None

    except aiosqlite.Error as e:
        logger.exception(f"Failed to check weather existence: {e}")
        return False
