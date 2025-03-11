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
