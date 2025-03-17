#task 1
import requests

url = "https://httpbin.org/json"

response = requests.get(url)
response.raise_for_status()
print(response)

resp_json = response.json()
slideshow_title = resp_json["slideshow"]["title"]
print(f"Title: {slideshow_title}")


#task 2
url = "https://httpbin.org/post"
data2 = {'username': 'test_user', 'password': 'qwerty'}

try:
    response = requests.post(url, data = data2)
    response.raise_for_status()

    result = response.json()
    print(result)
    print("Поля:", result["form"])

#если ответ не 200
except requests.exceptions.HTTPError as err:
    print(f"Ошибка: {response.status_code}")
except requests.exceptions.RequestException as err:
    print("Сервер недоступен")

#3
session = requests.Session()
session.get("https://httpbin.org/cookies/set/test_cookie/12345")

response_cookies = session.get("https://httpbin.org/cookies")
cookies = response_cookies.json()

file_name = "test.txt"
with open(file_name, "w") as f:
    f.write("Тестовый файл")
#доделаю