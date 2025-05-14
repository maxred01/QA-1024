import requests

#Цель: Отработка GET-запросов и парсинга JSON.
#
# Задание
# Отправьте GET-запрос на https://httpbin.org/json.
# Извлеките значение поля slideshow.title из ответа.
# Выведите результат в формате:
# Title: [НАЙДЕННЫЙ_ЗАГОЛОВОК]

url = 'https://httpbin.org/json'
response = requests.get(url)

response.status_code == 200

print(f"Title: {response.json()['slideshow']['title']}")


import requests
import os

with requests.Session() as session:
    # Сохраняет куки и заголовки между запросами
    session.get('https://httpbin.org/cookies/set/session/12345')
    response = session.get('https://httpbin.org/cookies')
    print(f'Cookie: {response.json()['cookies']}')

with open('file.txt', 'rb') as f:
    files = {'file': f}
    response = requests.post('https://httpbin.org/post', files=files)
    file_size = os.path.getsize('file.txt')
    print(f'Размер файла {"file.txt"}: {file_size} Bytes')