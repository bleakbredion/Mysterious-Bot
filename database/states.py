import aiosqlite
from logger import logger

from database.database import get_db
from modules.common.time import get_time


async def set_state(vk_id: int, state: str | None):
    ...


async def get_state(vk_id: int) -> str | None:
    ...


async def clear_state(vk_id: int):
    ...
