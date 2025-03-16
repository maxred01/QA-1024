import requests

url = 'https://httpbin.org/post'
data = {
    'username': 'test_user',
    'password': 'qwerty'
}
response = requests.post(url, data)
if response.status_code == 200:
    print(response.json()['form'])
elif response.status_code != 200 and response.status_code < 400:
    print(f'Ошибка: {response.status_code}')
try:
    response = requests.post(url, data)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print(f"Ошибка: {err}")
