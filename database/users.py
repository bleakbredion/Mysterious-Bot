import aiosqlite
from logger import logger

from database.database import get_db
from modules.common.time import get_time
from database.constants import Role


async def add_user(
    vk_id: int,
    fullname: str,
    role: Role,
) -> None:
    try:
        async with get_db() as db:
            registered_at = get_time().isoformat()

            await db.execute(
                """
                INSERT INTO users (
                    vk_id,
                    fullname,
                    role,
                    registered_at
                )
                VALUES (?, ?, ?, ?)
                """,
                (
                    vk_id,
                    fullname,
                    role.value,
                    registered_at,
                ),
            )

            await db.commit()

    except aiosqlite.Error:
        logger.exception(
            "Database error while adding user vk_id=%s",
            vk_id,
        )
        raise

    except Exception:
        logger.exception(
            "Unexpected error while adding user vk_id=%s",
            vk_id,
        )
        raise


async def get_user(
    vk_id: int,
):
    try:
        async with get_db() as db:
            cursor = await db.execute(
                """
                SELECT *
                FROM users
                WHERE vk_id = ?
                """,
                (vk_id,),
            )

            return await cursor.fetchone()

    except aiosqlite.Error:
        logger.exception(
            "Database error while getting user vk_id=%s",
            vk_id,
        )
        raise


async def user_exists(
    vk_id: int,
) -> bool:
    try:
        return await get_user(vk_id) is not None

    except Exception:
        logger.exception(
            "Error checking user existence vk_id=%s",
            vk_id,
        )
        raise


async def update_user(
    vk_id: int,
    fullname: str,
    role: Role,
) -> None:
    try:
        async with get_db() as db:
            await db.execute(
                """
                UPDATE users
                SET
                    fullname = ?,
                    role = ?
                WHERE vk_id = ?
                """,
                (
                    fullname,
                    role.value,
                    vk_id,
                ),
            )

            await db.commit()

    except aiosqlite.Error:
        logger.exception(
            "Database error while updating user vk_id=%s",
            vk_id,
        )
        raise


async def update_role(
    vk_id: int,
    role: Role,
) -> None:
    try:
        async with get_db() as db:
            await db.execute(
                """
                UPDATE users
                SET role = ?
                WHERE vk_id = ?
                """,
                (
                    role.value,
                    vk_id,
                ),
            )

            await db.commit()

    except aiosqlite.Error:
        logger.exception(
            "Database error while updating role vk_id=%s",
            vk_id,
        )
        raise


async def update_fullname(
    vk_id: int,
    fullname: str,
) -> None:
    try:
        async with get_db() as db:
            await db.execute(
                """
                UPDATE users
                SET fullname = ?
                WHERE vk_id = ?
                """,
                (
                    fullname,
                    vk_id,
                ),
            )

            await db.commit()

    except aiosqlite.Error:
        logger.exception(
            "Database error while updating fullname vk_id=%s",
            vk_id,
        )
        raise


async def delete_user(
    vk_id: int,
) -> None:
    try:
        async with get_db() as db:
            await db.execute(
                """
                DELETE FROM users
                WHERE vk_id = ?
                """,
                (vk_id,),
            )

            await db.commit()

    except aiosqlite.Error:
        logger.exception(
            "Database error while deleting user vk_id=%s",
            vk_id,
        )
        raise


async def get_users_by_role(
    role: Role,
):
    try:
        async with get_db() as db:
            cursor = await db.execute(
                """
                SELECT *
                FROM users
                WHERE role = ?
                ORDER BY fullname
                """,
                (role.value,),
            )

            return await cursor.fetchall()

    except aiosqlite.Error:
        logger.exception(
            "Database error while getting users by role=%s",
            role.value,
        )
        raise


async def get_all_users():
    try:
        async with get_db() as db:
            cursor = await db.execute(
                """
                SELECT *
                FROM users
                ORDER BY fullname
                """
            )

            return await cursor.fetchall()

    except aiosqlite.Error:
        logger.exception(
            "Database error while getting all users",
        )
        raise


async def create_or_update_user(
    vk_id: int,
    fullname: str,
    role: Role,
) -> None:
    try:
        async with get_db() as db:
            if await get_user(vk_id) is None:
                await db.execute(
                    """
                    INSERT INTO users (
                        vk_id,
                        fullname,
                        role,
                        registered_at
                    )
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        vk_id,
                        fullname,
                        role.value,
                        get_time().isoformat(),
                    ),
                )
            else:
                await db.execute(
                    """
                    UPDATE users
                    SET
                        fullname = ?,
                        role = ?
                    WHERE vk_id = ?
                    """,
                    (
                        fullname,
                        role.value,
                        vk_id,
                    ),
                )

            await db.commit()

    except aiosqlite.Error:
        logger.exception(
            "Database error while creating/updating user vk_id=%s",
            vk_id,
        )
        raise

    except Exception:
        logger.exception(
            "Unexpected error while creating/updating user vk_id=%s",
            vk_id,
        )
        raise