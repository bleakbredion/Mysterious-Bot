from database.database import get_db


async def init_db():
    async with get_db() as db:

        await db.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vk_id INTEGER UNIQUE NOT NULL,
                fullname TEXT,
                role TEXT,
                registered_at TEXT NOT NULL
            )
        """)
        # await db.execute("""DROP TABLE menus""")

        await db.execute("""
            CREATE TABLE IF NOT EXISTS menus(
                id INTEGER PRIMARY KEY,
                date DATE UNIQUE NOT NULL,
                breakfast TEXT NOT NULL,
                lunch TEXT NOT NULL,
                afternoon TEXT NOT NULL,
                dinner TEXT NOT NULL,
                duty_class TEXT,
                updated_at TEXT NOT NULL
            )
        """)

        await db.execute("""
            CREATE TABLE IF NOT EXISTS weather(
            id INTEGER PRIMARY KEY CHECK(id = 1),
            weather TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
        """)

        # await db.execute("""DROP TABLE invites""")

        await db.execute("""
            CREATE TABLE IF NOT EXISTS invites(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_vk INTEGER,
                fullname TEXT,
                block TEXT,
                komsenok_vk INTEGER,
                status TEXT,
                created_at TEXT,
                approved_by INTEGER
            )
        """)

        await db.commit()
