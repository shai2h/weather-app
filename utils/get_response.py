import requests
import json

from utils.get_token import get_token_from_env_variable


TOKEN = get_token_from_env_variable()


def get_response_from_api():
    link = f'https://api.openweathermap.org/data/2.5/weather?lat=55.8664&lon=48.3594&appid={TOKEN}'
    response = requests.get(link)
    data = response.json()

    with open('data.json', 'w', encoding='utf-8') as file:  
        json.dump(data, file, ensure_ascii=False, indent=4) 