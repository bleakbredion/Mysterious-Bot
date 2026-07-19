from database.database import get_db


async def init_db():
    db = await get_db()

    await db.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vk_id INTEGER UNIQUE NOT NULL,
            fullname TEXT,
            role TEXT
        )
    """)

    await db.execute("""
        CREATE TABLE IF NOT EXISTS menu(
            date TEXT PRIMARY KEY,
            breakfast TEXT,
            lunch TEXT,
            afternoon TEXT,
            dinner TEXT,
            updated_at TEXT
        )
    """)

    await db.execute("""
        CREATE TABLE IF NOT EXISTS weather_cache(
            id INTEGER PRIMARY KEY,
            temperature REAL,
            description TEXT,
            wind REAL,
            updated_at TEXT
        )
    """)

    await db.execute("""
        CREATE TABLE IF NOT EXISTS invites(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_vk INTEGER,
            komsenok_vk INTEGER,
            status TEXT,
            created_at TEXT,
            approved_by INTEGER
        )
    """)

    await db.commit()
    await db.close()
