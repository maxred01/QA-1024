from binascii import crc_hqx
from http.client import responses
#rom tabnanny import check
from typing import assert_type

import requests

#import requests

# response = requests.get('https://api.github.com')

#assert response.status_code == 403
##import requests
#import requests

#params = {'page': 2, 'limit': 10}
#response = requests.get('https://httpbin.org/get', params=params)

#print(response.url)

#assert response.url == 'https://httpbin.org/get?page=2&limit=10'

#user_agent = 'MyApp/1.0'

#headers = {
#    'User-Agent': user_agent,
#    'Authorization': token
#}

#response = requests.get('http://httpbin.org/headers', headers=headers)  # Исправлено: requests, а не request
#print(response.json()['headers'])


#assert response.json()['headers']['Authorization'] == token
#assert response.json()['headers']['User-Agent'] == user_agent

#import pytest-check()
#def test_21_vek():
 # url = 'http:whitehouse.gov/'
#respons = requests.get(url)
#print(respons.status_code)
#check.equel(respons.status_code, 200, f f'Статус код не равен {respons.status_code}')


import requests
import pytest_check as check
def test_21_vek():
    url = 'http://whitehouse.gov/'
    response = requests.get(url)
    print(response.status_code)
    check.equal(response.status_code == 200, f'Статус код не равен 200, получен {response.status_code}')




