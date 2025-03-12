import requests

response = requests.get('https://httpbin.org/json')
data = response.json()
title = data.get('slideshow', {}).get('title', 'Заголовок не найден')
print(f'Title: {title}')


import requests

url = 'https://httpbin.org/post'
data = {'username': 'test_user', 'password': 'qwerty'}

try:
    response = requests.post(url, data=data)
    response.raise_for_status()  # Проверка статуса ответа
    print(f"Form: {response.json().get('form')}")
except requests.exceptions.HTTPError as err:
    print(f"Ошибка: {response.status_code}")
except requests.exceptions.RequestException:
    print("Сервер недоступен")

