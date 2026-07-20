import aiosqlite
from logger import logger

from database.database import get_db
from modules.common.time import get_time


async def create_invite(
    student_vk: int,
    fullname: str,
    block: str,
) -> int:
    try:
        async with get_db() as db:
            created_at = get_time().isoformat()

            cursor = await db.execute(
                """
                INSERT INTO invites(
                    student_vk,
                    fullname,
                    block,
                    status,
                    created_at
                )
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    student_vk,
                    fullname,
                    block,
                    "pending",
                    created_at,
                ),
            )

            await db.commit()
            return cursor.lastrowid

    except aiosqlite.Error:
        logger.exception("Error while creating invite")
        raise


async def approve_invite(
    invite_id: int,
    komsenok_vk: int,
    approved_by: int,
) -> None:
    try:
        async with get_db() as db:
            await db.execute(
                """
                UPDATE invites
                SET
                    status = ?,
                    komsenok_vk = ?,
                    approved_by = ?
                WHERE id = ?
                """,
                (
                    "approved",
                    komsenok_vk,
                    approved_by,
                    invite_id,
                ),
            )

            await db.commit()

    except aiosqlite.Error:
        logger.exception("Error while approving invite")
        raise


async def reject_invite(
    invite_id: int,
    approved_by: int,
) -> None:
    try:
        async with get_db() as db:
            await db.execute(
                """
                UPDATE invites
                SET
                    status = ?,
                    approved_by = ?
                WHERE id = ?
                """,
                (
                    "rejected",
                    approved_by,
                    invite_id,
                ),
            )

            await db.commit()

    except aiosqlite.Error:
        logger.exception("Error while rejecting invite")
        raise


async def get_invite(
    invite_id: int,
) -> aiosqlite.Row | None:
    try:
        async with get_db() as db:
            cursor = await db.execute(
                """
                SELECT *
                FROM invites
                WHERE id = ?
                """,
                (invite_id,),
            )

            return await cursor.fetchone()

    except aiosqlite.Error:
        logger.exception("Error while getting invite")
        raise


async def get_active_invites(
    student_vk: int,
) -> list[aiosqlite.Row]:
    try:
        async with get_db() as db:
            cursor = await db.execute(
                """
                SELECT *
                FROM invites
                WHERE student_vk = ?
                AND status = ?
                """,
                (
                    student_vk,
                    "pending",
                ),
            )

            return await cursor.fetchall()

    except aiosqlite.Error:
        logger.exception("Error while getting active invites")
        raise
