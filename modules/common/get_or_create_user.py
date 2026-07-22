from database.database import get_db
from modules.common.time import get_time


async def get_or_create_user(vk_id: int, first_name: str, last_name: str) -> None:
    async with await get_db() as db:
        await db.execute(
            """
            INSERT OR IGNORE INTO users (
                vk_id,
                first_name,
                last_name,
                created_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                vk_id,
                first_name,
                last_name,
                get_time().isoformat(),
            ),
        )

        await db.commit()
