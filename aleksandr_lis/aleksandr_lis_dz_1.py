import requests

response = requests.get('https://httpbin.org/json')
data = response.json()
title = data.get('slideshow', {}).get('title', 'Заголовок не найден')
print(f'Title: {title}')
