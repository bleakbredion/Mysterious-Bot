from vkbottle.bot import Bot
from secret import OWNER_ID

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "database" / "bot.db"

MAX_DATE = 2

lat=54.8483; lon=83.1064