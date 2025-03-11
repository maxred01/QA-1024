import requests
import pytest
import pytest_check as check
# response = requests.get('https://api.github.com')
#
# assert response.status_code == 201, f'Status code {response.status_code}'
#
# response = response.json()
#
# #assert response["current_user_url"] == 'https://api.github.com/user'
# assert response["followers_url"] == "https://api.github.com/user/followers"
#
# params = {'page': 2, 'limit': 10}
# response = requests.get('https://httpbin.org/get', params=params)
#
# assert response.status_code == 200, f'Status code: {response.status_code}'
# assert response.url == 'https://httpbin.org/get?page=2&limit=10', f'Response url: {response.url}'

response = requests.post('https://httpbin.org/post', data={'key': 'value'})

#assert response.status_code == 200
print(response.json())
print(response.text)
#
# response = response.json()
#
# #assert response["headers"]["Host"] == "httpbin.or", f'No, please repeat: {response["headers"]["Host"]}'
# assert response['url'] == 'https://httpbin.org/pos', f'{response["url"]}'

# user_agent = 'MyApp/1.0'
# user_agent1 = 'MyApp/1.1'
#
# headers = {
#     'User-Agent': f'{user_agent}',
#     'Authorization': 'Bearer YOUR_TOKEN'
# }
# #
# response = requests.get('https://httpbin.org/headers', headers=headers)
#
# response = response.json()
# print(response)
#
# assert response['headers']['User-Agent'] == user_agent, f"error, {response['headers']['User-Agent']}"
# assert response['headers']['User-Agent'] == user_agent1, f"error, {response['headers']['User-Agent']}"

# try:
#     response = requests.get('https://httpbin.org/status/302')
#     response.raise_for_status()  # Проверка на ошибки 4xx/5xx
# # except requests.exceptions.HTTPError as err:
# #     print(f"Ошибка 1: {err}")
# except requests.exceptions.RequestException as err:
#     print(f"Ошибка 2 : {err}")

def test_21_vek():
    url = 'https://www.whitehouse.gov/'

    respons = requests.get(url)
    print(respons.status_code)
    check.equal(respons.status_code, 200, f'Статус код равен {respons.status_code}')