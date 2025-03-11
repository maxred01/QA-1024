import requests
response=requests.post('https://httpbin.org/post',data = {'username': 'test_user', 'password': 'qwerty'})
data=response.json()
title=data['form']
try:
    response.raise_for_status()
    print(f'{title}')
except requests.exceptions.HTTPError as err:
    print(f"Ошибка: {err}")
except requests.exceptions.ConnectionError:
    print(f'Ошибка соединения: ')