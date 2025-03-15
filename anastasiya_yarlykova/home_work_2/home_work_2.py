import requests


response = requests.get('https://httpbin.org/json')
data = response.json()
print(f"Title: {data['slideshow']['title']}")




data = {'username': 'test_user', 'password': 'qwerty'}
try:
    response = requests.post('https://httpbin.org/post', data=data)
    response.raise_for_status()
    print(response.json()['form'])
except requests.exceptions.HTTPError as err:
    print(f"Ошибка {err.response.status_code}")
except requests.exceptions.RequestException:
    print("Сервер не доступен")



with requests.Session() as session:
    session.get('https://httpbin.org/cookies/set/test_cookie/12345')
    cookies_response = session.get('https://httpbin.org/cookies')
    cookie_mean = cookies_response.json()['cookies']['test_cookie']
    
print(f"Cookie:{cookie_mean}")


with open('text.txt', 'w') as file:
    file.write('Hi')
with open('text.txt', 'rb') as file:
    file_response = session.post('https://httpbin.org/post', files={'file': file})
    file_size = len(file_response.json()['files']['file'])


print(f"File size: {file_size} bytes")
