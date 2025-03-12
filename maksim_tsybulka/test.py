import requests
import pytest_check as check


#
# response = requests.get('https://api.github.com')
#
# assert response.status_code == 403


# params = {'page': 2, 'limit': 10}
# response = requests.get('https://httpbin.org/get', params=params)
#
# assert response.url == 'https://httpbin.org/get?page=2&limit=10'

# response = requests.post('https://httpbin.org/post', data={'key': 'value'})
# print(response.text)
# response = response.json()
#
# assert response['headers']['Host'] == "httpbin.org"


# token = 'Bearer YOUR_TOKEN'
# user_agent = 'MyApp/1.0'
#
# headers = {
#     'User-Agent': 'MyApp/1.0',
#     'Authorization': f'{token}'
# }
#
# response = requests.get('https://httpbin.org/headers', headers=headers)
# print(response.text)
#
# assert response.json()['headers']['Authorization'] == token

#
# try:
#     # 1. Отправляем GET-запрос на URL, который всегда возвращает статус 404
#     response = requests.get('https://httpbin.org/status/404')
#
#     # 2. Проверяем статус ответа. Если статус в диапазоне 4xx или 5xx,
#     #    метод выбросит исключение HTTPError
#     response.raise_for_status()
#
# except requests.exceptions.HTTPError as err:
#     # 3. Этот блок выполнится ТОЛЬКО при ошибках HTTP (4xx и 5xx)
#     print(f"HTTP Error: {err}")
#
# except requests.exceptions.RequestException as err:
#     # 4. Этот блок ловит ВСЕ остальные ошибки библиотеки requests
#     print(f"Request Failed: {err}")
#

def test_21vek():
    url = 'https://www.21vek.by/'
    respons = requests.get(url)
    check.equal(respons.status_code, 200, f'Статус код равен {respons.status_code}')
