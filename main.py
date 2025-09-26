from utils.get_response import get_response_from_api_to_json
import json
from datetime import datetime, timedelta, timezone

# write to json file >> data.json
# get_response_from_api_to_json()

moscow_tz = timezone(timedelta(hours=3))

def start():
    with open('data.json', 'r') as file:
        data = json.load(file)

    context = {
        'date_time_now': datetime.now(moscow_tz).strftime("%d.%m.%Y %H:%M"),
        'city': data['name'],
        'description': data['weather'][0]['description'],
    }

    print(
        f"Город: {context['city']}\n"
        f"Дата/Время: {context['date_time_now']}\n"
        f"Погода: {context['description']}"
    )

# пример №1 tg
"""
Пример для возврата в телеграмм канале:
📍 Город: Volzhsk
📅 Дата: 26.02.2025
🕖 Время: 08:45

🌡 Температура: -3°C (ощущается как -8°C)
💨 Ветер: 5 м/с, северо-западный
💧 Влажность: 82%
☁️ Облачность: 60%
🌬 Давление: 745 мм рт. ст.
🌦 Погода: Переменная облачность, небольшой снег
"""

# # пример №2 sms
"""
Пример для SMS
Volzhsk, 26.02.2025 08:45
Темп: -3°C (ощ -8°C)
Ветер: 5 м/с СЗ
Влажн: 82%
Давл: 745 мм рт. ст.
Облачн: 60%
"""

