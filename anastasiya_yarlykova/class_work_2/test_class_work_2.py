import requests
import pytest
import pytest_check

# response = requests.get('https://api.github.com')
# assert response.status_code == 200, f'Статус код не равен 200: статус код  равен {response.status_code}'
#
# response = response.json()
#
# assert response ['emails_url'] == "https://api.github.com/user/emails"



# params = {'page': 2, 'limit': 10}
# response = requests.get('https://httpbin.org/get', params=params)
# print(response.url) # URL с параметрами: https://httpbin.org/get?page=2&limit=10
#
# assert response.url == 'https://httpbin.org/get?page=2&limit=10'


# response = requests.post('https://httpbin.org/post', data={'key': 'value'})

# print(response)
# print(response.text)
# response = response.json()
#
# assert response ['url'] == "https://httpbin.org/post"

# token = 'Bearer YOUR_TOKEN'
# user_agent = 'MyApp/1.0'
#
# headers = {
#     'User-Agent': f'{user_agent}',
#     'Authorization': f'{token}'
# }
#
# response = requests.get('https://httpbin.org/headers', headers=headers)
# print(response.text)
#
# assert response.json()['headers']['Authorization'] == token
# assert response.json()['headers']['User-Agent'] == user_agent

# try:
#     response = requests.get('https://httpbin.org/status/201')
#     response.raise_for_status()  # Проверка на ошибки 4xx/5xx
# except requests.exceptions.HTTPError as err:
#     print(f"Ошибка: {err}")
# except requests.exceptions.HTTPError as err:
#     print(f"Ошибка: {err}")


def test_21_vek():
    url = 'https://httpbin.org/headers/'

    respons = requests.get(url)
    print(respons.status_code)
    check.equal(respons.status_code, 200, f'Статус код не равен {respons.status_code}')
