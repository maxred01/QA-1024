# raise_for_status()
# Уровень 1: Отработка GET-запросов и парсинга JSON

import requests
response = requests.get("https://httpbin.org/json").json()
print(f"Title: {response['slideshow']['title']}")
print()


# Уровень 2: Работа с POST-запросами и обработка ошибок.
try:
    response = requests.post("https://httpbin.org/post", data={'username': 'test_user', 'password': 'qwerty'})
    response.raise_for_status()
    print(response.json()["form"])

except requests.exceptions.HTTPError:
    print(f"Ошибка: {response.status_code}")

except requests.exceptions.RequestException:
    print("Сервер недоступен")
print()



# Уровень 3: Работа с сессиями, куками и файлами.
with requests.Session() as session:
    # Сохраняет куки и заголовки между запросами
    session.get('https://httpbin.org/cookies/set/session/12345')
    response = session.get('https://httpbin.org/cookies')
    print(response.json())













