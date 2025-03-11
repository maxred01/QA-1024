import requests
import os

#Задание
#Отправьте GET-запрос на https://httpbin.org/json.
#Извлеките значение поля slideshow.title из ответа.
#Выведите результат в формате:
#Title: [НАЙДЕННЫЙ_ЗАГОЛОВОК]

response = requests.get('https://httpbin.org/json')
response = response.json()
print(f'Title: {response["slideshow"]["title"]}')

#Цель: Работа с POST-запросами и обработка ошибок.
#
#Задание
#Отправьте POST-запрос на https://httpbin.org/post с данными:
#data = {'username': 'test_user', 'password': 'qwerty'}
#Реализуйте обработку ошибок:
#При статусе ≠ 200 выведите: Ошибка: [КОД_СТАТУСА]
#При проблемах соединения: Сервер недоступен
#При успехе выведите содержимое ключа form из ответа.
#Требования
#Используйте try/except с HTTPError и RequestException
#Обязательно вызовите raise_for_status()

username_test = 'test_user'
password_test = 'qwerty'
data = \
    {
        'username': username_test,
        'password': password_test
    }
try:
    response = requests.post('https://httpbin.org/post',
                             data={'username': username_test, 'password': password_test})
    response.raise_for_status()
    print(f'{response.status_code}')
except requests.exceptions.HTTPError as error_code:
    print(f"Ошибка 400-500: {error_code}")
except requests.exceptions.RequestException as error_code:
    print(f"Ошибка нечто другое: {error_code}")

#Задание
#Создайте сессию через requests.Session()
#Через сессию выполните:
#GET-запрос к https://httpbin.org/cookies/set/test_cookie/12345
#GET-запрос к https://httpbin.org/cookies
#Извлеките значение куки test_cookie
#Загрузите текстовый файл через POST на https://httpbin.org/post
#Выведите:
#Cookie: [ЗНАЧЕНИЕ_КУКИ]
#File size: [РАЗМЕР_ФАЙЛА_В_БАЙТАХ]

response3 = requests.get('https://httpbin.org/cookies/set/test_cookie/12345')
response4 = requests.get('https://httpbin.org/cookies')

with open('test_file.txt') as f:
    files = {'file': f}
    response5 = requests.post('https://httpbin.org/post', files=files)

print(f'{response3.json()["cookies"]["test_cookie"]}')
print(f'{os.path.getsize('test_file.txt')}')