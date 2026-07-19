from config import Bot
from .service import get_temp, get_cloud_cover, get_humidity, get_temp_feel, get_wind, get_last_update
from .labeler import labeler

@labeler.message(payload={"cmd": "weather"})
async def weather(message):

    last_update = get_last_update()
    if last_update:
        update_time = last_update.strftime("%H:%M:%S")  # или "%H:%M"
        update_text = f"🔄 Обновлено: {update_time}"
    else:
        update_text = "🔄 Данные еще не обновлены"

    await message.answer(
        f"🌡 Температура: {get_temp()}°C (ощущается как {get_temp_feel()}°C)\n💨 Ветер: {get_wind()} м/с\n💧 Влажность: {get_humidity()}%\n{update_text}",
        keyboard=keyboard()
    )