from datetime import datetime
from zoneinfo import ZoneInfo


def get_time(timezone: str = "Asia/Novosibirsk") -> datatime:
    return datetime.now(ZoneInfo(timezone))
