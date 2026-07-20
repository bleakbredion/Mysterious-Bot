import aiosqlite
from datetime import date

from logger import logger

from database.database import get_db
from modules.common.time import get_time


async def add_menu(
    menu_date: date,
    breakfast: str,
    lunch: str,
    afternoon: str,
    dinner: str,
) -> None:
    try:
        async with get_db() as db:
            await db.execute(
                """
                INSERT INTO menu (
                    date,
                    breakfast,
                    lunch,
                    afternoon,
                    dinner,
                    updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    menu_date.isoformat(),
                    breakfast,
                    lunch,
                    afternoon,
                    dinner,
                    get_time().isoformat(),
                ),
            )
            await db.commit()

        logger.info(f"Added menu for {menu_date}")

    except aiosqlite.IntegrityError:
        logger.warning(f"Menu for {menu_date} is already exist")

    except Exception:
        logger.exception(f"Error while addind menu for a date {menu_date}")
        raise

async def get_menu(menu_date: date) -> dict | None:
    try:
        async with get_db() as db:
            cursor = await db.execute(
                """
                SELECT
                    date,
                    breakfast,
                    lunch,
                    afternoon,
                    dinner,
                    updated_at
                FROM menu
                WHERE date = ?
                """,
                (menu_date.isoformat(),),
            )

            row = await cursor.fetchone()

        if row is None:
            logger.warning(f"Menu for {menu_date} is not finded")
            return None

        return {
            "date": row[0],
            "breakfast": row[1],
            "lunch": row[2],
            "afternoon": row[3],
            "dinner": row[4],
            "updated_at": row[5],
        }

    except Exception:
        logger.exception(f"Error while receiving menu for a date {menu_date}")
        raise


async def update_menu(
    menu_date: date,
    breakfast: str,
    lunch: str,
    afternoon: str,
    dinner: str,
) -> None:
    try:
        async with get_db() as db:
            await db.execute(
                """
                INSERT INTO menu (
                    date,
                    breakfast,
                    lunch,
                    afternoon,
                    dinner,
                    updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(date)
                DO UPDATE SET
                    breakfast = excluded.breakfast,
                    lunch = excluded.lunch,
                    afternoon = excluded.afternoon,
                    dinner = excluded.dinner,
                    updated_at = excluded.updated_at
                """,
                (
                    menu_date.isoformat(),
                    breakfast,
                    lunch,
                    afternoon,
                    dinner,
                    get_time().isoformat(),
                ),
            )

            await db.commit()

        logger.info(f"Menu for a {menu_date} update")

    except Exception:
        logger.exception(f"Error update menu for a date {menu_date}")
        raise


async def delete_menu(menu_date: date) -> bool:
    try:
        async with get_db() as db:
            cursor = await db.execute(
                """
                DELETE FROM menu
                WHERE date = ?
                """,
                (menu_date.isoformat(),),
            )

            await db.commit()

        if cursor.rowcount == 0:
            logger.warning(f"Menu for {menu_date} is not finded")
            return False

        logger.info(f"Menu for a date {menu_date} is deleted")
        return True

    except Exception:
        logger.exception(f"Error while deleting menu for a date {menu_date}")
        raise


async def get_available_dates() -> list[str]:
    try:
        async with get_db() as db:
            cursor = await db.execute(
                """
                SELECT date
                FROM menu
                ORDER BY date
                """
            )

            rows = await cursor.fetchall()

        return [row[0] for row in rows]

    except Exception:
        logger.exception("Error while receiving menu dates list")
        raise
