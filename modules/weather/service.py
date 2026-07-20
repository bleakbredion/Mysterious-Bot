import requests
import sys
import os
import time
import threading
from datetime import datetime
import json

secret_dir = os.path.abspath("/home/Rostislav/Mysterius Letka VKBot")
if secret_dir not in sys.path:
    sys.path.append(secret_dir)

from secret import WTHR_API_KEY
from config import lat, lon

class WeatherCache:
    def __init__(self, update_interval=600):  # 600 секунд = 10 минут
        self.update_interval = update_interval
        self.cached_data = None
        self.last_update = None
        self.lock = threading.Lock()
        
        # Запускаем фоновый поток для обновления
        self.running = True
        self.thread = threading.Thread(target=self._auto_update, daemon=True)
        self.thread.start()
        
        # Первое обновление
        self._update_weather()
    
    def _update_weather(self):
        """Получение и сохранение данных о погоде"""
        try:
            city_name = "Novosibirsk"  # или ""Akademgorodok"
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={WTHR_API_KEY}&units=metric&lang=ru"
            # url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WTHR_API_KEY}&units=metric&lang=ru"
            response = requests.get(url, timeout=10)
            
            if response.status_code == 200:
                with self.lock:
                    self.cached_data = response.json()
                    self.last_update = datetime.now()
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Погода обновлена")
                return True
            else:
                print(f"Ошибка получения погоды: {response.status_code}")
                return False
        except Exception as e:
            print(f"Ошибка при обновлении погоды: {e}")
            return False
    
    def _auto_update(self):
        """Фоновый поток для автоматического обновления"""
        while self.running:
            time.sleep(self.update_interval)
            self._update_weather()
    
    def get_weather_data(self):
        """Получение текущих данных из кэша"""
        with self.lock:
            if self.cached_data is None:
                # Если данных нет, пытаемся получить сейчас
                self._update_weather()
            return self.cached_data
    
    def get_last_update_time(self):
        """Время последнего обновления"""
        with self.lock:
            return self.last_update
    
    def stop(self):
        """Остановка фонового потока"""
        self.running = False
        if self.thread.is_alive():
            self.thread.join(timeout=1)


# Создаем глобальный экземпляр кэша
weather_cache = WeatherCache()


# Функции для получения данных из кэша
def get_weather():
    """Получение полных данных о погоде из кэша"""
    try:
        return weather_cache.get_weather_data()
    except:
        return None


def get_last_update():
    """Время последнего обновления"""
    try:
        return weather_cache.get_last_update_time()
    except:
        return None


def get_temp():
    try:
        data = get_weather()
        return data['main']['temp'] if data else "Error"
    except (KeyError, TypeError):
        return None


def get_temp_feel():
    try:
        data = get_weather()
        return data['main']['feels_like'] if data else "Error"
    except (KeyError, TypeError):
        return None


def get_cloud_cover():
    try:
        data = get_weather()
        return data['weather'][0]['description'] if data else "Error"
    except (KeyError, TypeError, IndexError):
        return None


def get_wind():
    try:
        data = get_weather()
        return data['wind']['speed'] if data else "Error"
    except (KeyError, TypeError):
        return None


def get_humidity():
    try:
        data = get_weather()
        return data['main']['humidity'] if data else "Error"
    except (KeyError, TypeError):
        return None


# Дополнительные полезные функции
def get_weather_summary():
    """Краткая сводка погоды"""
    data = get_weather()
    if not data:
        return "Не удалось получить данные о погоде"
    
    try:
        temp = data['main']['temp']
        feels = data['main']['feels_like']
        desc = data['weather'][0]['description']
        wind = data['wind']['speed']
        humidity = data['main']['humidity']
        
        last_update = get_last_update()
        update_time = last_update.strftime("%H:%M") if last_update else "неизвестно"
        
        return (f"🌡 Температура: {temp}°C (ощущается как {feels}°C)\n"
                f"☁️ {desc.capitalize()}\n"
                f"💨 Ветер: {wind} м/с\n"
                f"💧 Влажность: {humidity}%\n"
                f"🔄 Обновлено: {update_time}")
    except (KeyError, TypeError):
        return "Ошибка при формировании сводки"


# Пример использования
if __name__ == "__main__":
    # Демонстрация работы
    import time
    
    print("Получение погоды из кэша...")
    for i in range(3):
        print(f"\nЗапрос {i+1}:")
        print(f"Температура: {get_temp()}°C")
        print(f"Ветер: {get_wind()} м/с")
        print(f"Обновлено: {get_last_update()}")
        time.sleep(3)
    
    # Остановка фонового потока при завершении
    weather_cache.stop()




# import json

# await save_weather(json.dumps(weather, ensure_ascii=False))

# weather, updated_at = await get_weather()
# weather = json.loads(weather)

# print(weather["temperature"])
# print(weather["condition"])