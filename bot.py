import asyncio
import atexit

from vkbottle.bot import Bot
from secret import api
bot=Bot(api)

from database.database import init_db

from modules.weather import service as weather_service


from modules.start import labeler as start_labeler
from modules.menu import labeler as menu_labeler
from modules.weather import labeler as weather_labeler
from modules.schedule import labeler as schedule_labeler
from modules.invite import labeler as invite_labeler
from modules.info import labeler as info_labeler
from modules.common import labeler_exit as common_exit_labeler


bot.labeler.load(start_labeler)
bot.labeler.load(menu_labeler)
bot.labeler.load(weather_labeler)
bot.labeler.load(schedule_labeler)
bot.labeler.load(invite_labeler)
bot.labeler.load(info_labeler)
bot.labeler.load(common_exit_labeler)


atexit.register(weather_service.weather_cache.stop)


async def startup():
    await init_db()


bot.run()
