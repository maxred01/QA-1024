import requests

#Задание 1
# response = requests.get('https://httpbin.org/json')
# print (response.text)
# print(response.status_code)
# print(f"Title: {response.json()['slideshow']['title']}")

#Задание 2

response = requests.post('https://httpbin.org/post', data={'username': 'test_user', 'password': 'qwerty'})
print (response.text)
print(f'Содержимое ключа Form',(response.json()['form']))
try:
    response.raise_for_status()  # Проверка на ошибки 4xx/5xx
except requests.exceptions.HTTPError:
    print(f"Ошибка: {requests.exceptions.HTTPError}")
except requests.exceptions.RequestException:
    print('Сервер недоступен')





