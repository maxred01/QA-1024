import requests
url = "https://httpbin.org/json"
response = requests.get("https://httpbin.org/json")
if response.status_code == 200:
    data = response.json()
    title = data['slideshow']['title']
    print(f"Title: {title}")
else:
    print(f"Ошибка: {response.status_code}")