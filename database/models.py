import aiosqlite
from config import DB_PATH

async def add_user(vk_id, first_name, last_name):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT OR IGNORE INTO users(vk_id, first_name, last_name)
            VALUES (?, ?, ?)
        """, (vk_id, first_name, last_name))
        await db.commit()



async def get_user(vk_id):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute(
            "SELECT * FROM users WHERE vk_id = ?",
            (vk_id,)
        )
        return await cursor.fetchone()


async def set_role(vk_id, role):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "UPDATE users SET role = ? WHERE vk_id = ?",
            (role, vk_id)
        )
        await db.commit()