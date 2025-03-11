import requests
import pytest_check as check

#params={'page': 2, 'limit':10}
#response = requests.get('https://httpbin.org/get', params=params)
#print(response.url)
#assert response.url == 'https://httpbin.org/get?page=2&limit=10'

#response = requests.post('https://httpbin.org/post', data={'key': 'value'})
#print(response.text)
#response = response.json()

#assert response['url'] == 'https://httpbin.org/post'
#headers = {
 #   'User-Agent': f'{user_agent}',
  #  'Authorization': 'Bearer YOUR_TOKEN'
#}

#response = requests.get('https://httpbin.org/headers', headers=headers)
#print(response.json()['headers'])
#assert response.json()['headers']['User-Agent'] == user_agent

#try:
 #   response = requests.get('https://httpbin.org/status/400')
  #  response.raise_for_status()  # Проверка на ошибки 4xx/5xx
#except requests.exceptions.HTTPError as err:
 #   print(f"Ошибка: {err}")
#except requests.exceptions.RequestException as err:
 #   print(f"Ошибка: {err}")
def test_21_vek():
    url='https://www.21vek.by/'
    response=requests.get(url)
    print(response.status_code)
    check.equal(response.status_code,200,f'статус код {response.status_code}')
