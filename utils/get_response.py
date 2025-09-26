import requests
import json

from utils.get_token import get_token_from_env_variable


TOKEN = get_token_from_env_variable()


def get_response_from_api_to_json():
    link = f'https://api.openweathermap.org/data/2.5/weather?q=Volzhsk&appid={TOKEN}&lang=ru'
    response = requests.get(link)
    data = response.json()

    with open('data.json', 'w', encoding='utf-8') as file:  
        json.dump(data, file, ensure_ascii=False, indent=4) 