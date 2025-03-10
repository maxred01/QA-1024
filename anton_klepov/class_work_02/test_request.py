import requests
import pytest
import pytest_check as check



# response = requests.get('https://api.github.com')
#
# assert response.status_code == 200, f'статус код равен {response.status_code}'
#
# response = response.json()
#
# assert response['starred_url'] == "https://api.github.com/user/starred{/owner}{/repo}"
# print(response.status_code)  # Код статуса (200 = OK)
# print(response.json())       # Ответ в формате JSON

# params = {'page': 2, 'limit': 10}
# response = requests.get('https://httpbin.org/get', params=params)
# print(response.url)  # URL с параметрами: https://httpbin.org/get?page=2&limit=10
#
# assert response.status_code == 200
# print(response.status_code)
#
# assert response.url == 'https://httpbin.org/get?page=2&limit=10'

# response = requests.post('https://httpbin.org/post', data={'key': 'value'})
# # print(response.json())
# print(response.text)
# response = response.json()
#
# assert response['url'] == "https://httpbin.org/post"
# user_agent = 'MyApp/1.0'
# headers = {
#     'User-Agent': f'{user_agent}',
#     'Authorization': 'Bearer YOUR_TOKEN'
# }
#
# response = requests.get('https://httpbin.org/headers', headers=headers)
# print(response.json()['headers'])
# print(response.text)
#
# assert response.json()['headers']['User-Agent'] == user_agent
#
#
# try:
#     response = requests.get('https://httpbin.org/status/200')
#     response.raise_for_status()  # Проверка на ошибки 4xx/5xx
# except requests.exceptions.HTTPError as err:
#     print(f"Ошибка: {err}")
# except requests.exceptions.RequestException as err:
#     print(f"Request Failed: {err}")

def test_21_vek():
    url = 'https://www.whitehouse.gov/'

    respons = requests.get(url)
    print(respons.status_code)
    check.equal(respons.status_code, 200, f'Статус код равен {respons.status_code}')
