import requests
import pytest
import pytest_check

#
# response = requests.get('https://api.github.com')
#
# assert response.status_code == 200
#
# assert response['emails_url'] == "https://api.github.com/user/emails"
# print(response.status_code)
# print (response.json())

#params = {'page': 2, 'limit': 10}
#response = requests.get('https://httpbin.org/get', params=params)
#print(response.url)  # URL с параметрами: https://httpbin.org/get?page=2&limit=10
#assert response.url == "https://httpbin.org/get?page=2&limit=10"

# response = requests.post('https://httpbin.org/post', data={'key': 'value'})
# print (response.text)
# response = response.json()
# assert response ['url'] == "https://httpbin.org/post"


# user = 'MyApp/1.0'
# headers = {
#     'User-Agent': f'{user}',
#     'Authorization': 'Bearer YOUR_TOKEN'
# }
#
# response = requests.get('https://httpbin.org/headers', headers=headers)
# print (response.text)
# assert response.json()['headers']['User-Agent'] == user


# try:
#     response = requests.get('https://httpbin.org/status/507')
#     response.raise_for_status()  # Проверка на ошибки 4xx/5xx
# except requests.exceptions.HTTPError as err:
#     print(f"Ошибка: {err}")




