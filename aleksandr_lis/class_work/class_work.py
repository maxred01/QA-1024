import requests
import pytest
import pytest_check
#params = {'page': 2, 'limit': 10}
#response = requests.get('https://httpbin.org/get', params=params)
#assert response.url == 'https://httpbin.org/get?page=2&limit=10'

  # URL с параметрами: https://httpbin.org/get?page=2&limit=10
#assert response['url'] == "https://httpbin.org/post"

#headers = {
   #response = requests.get('https://httpbin.org/headers', headers=headers)

#print(response.json()['headers'])
#assert response.json()['headers']['User-Agent'] == user_agent

#response = requests.get('https://httpbin.org/status/504')
    #response.raise_for_status()  # Проверка на ошибки 4xx/5xx
#except requests.exceptions.HTTPError as err:
   # print(f"Ошибка: {err}")
#def test_21_vek():
   # url = 'https://www.21vek.by/'
   # respons = requests.get(url)
   # print(respons.status_code)

import requests
url = 'hppt://randomuser/me/api/'
respons = requests.get(url)
print(respons.json())