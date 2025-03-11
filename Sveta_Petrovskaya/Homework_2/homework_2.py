import requests


#Отработка GET-запросов и парсинга JSON
response = requests.get("https://httpbin.org/json").json()
print(f"Title: {response['slideshow']['title']}")
print()

#Работа с POST-запросами и обработка ошибок.
try:
    response = requests.post("https://httpbin.org/post", data={'username': 'test_user', 'password': 'qwerty'})
    response.raise_for_status()
    print(response.json()["form"])
except requests.exceptions.HTTPError:
    print(f"Ошибка: {response.status_code}")
except requests.exceptions.RequestException:
    print("Сервер недоступен")
print()

#Работа с сессиями, куками и файлами.
with requests.Session() as s:
    # Устанавливаем куку
    response = s.get("https://httpbin.org/cookies/set/test_cookie/12345")
    response.raise_for_status()

    # Получаем куку
    response = s.get("https://httpbin.org/cookies")
    response.raise_for_status()
    cookie = response.json()["cookies"].get("test_cookie", "Не найдено")

    # Создаём файл
    file_content = "Hello, world!"
    with open("test.txt", "w") as f:
        f.write(file_content)

    # Загружаем файл
    with open("test.txt", "rb") as f:
        response = s.post("https://httpbin.org/post", files={"file": f})
        response.raise_for_status()
    print(f"Cookie: {cookie}")
    print(f"File size: {len(file_content)}")