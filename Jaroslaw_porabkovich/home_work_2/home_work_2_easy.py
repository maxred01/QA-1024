import requests
response=requests.get('https://httpbin.org/json' )
data = response.json()
title = data['slideshow']['title']
print(f'Title:{title}')
