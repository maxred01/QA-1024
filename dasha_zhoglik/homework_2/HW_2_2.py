import requests
data = {'username': 'test_user', 'password': 'qwerty'}
response = requests.post('https://httpbin.org/post', data=data)


if response.status_code != 200:
    print(f"Ошибка: {response.status_code}")
else:
    form_data = response.json().get('form', {})
    print("Содержимое ключа form:", form_data)