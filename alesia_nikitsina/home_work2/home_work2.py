import requests
response=requests.get('https://httpbin.org/json')
data=response.json
response.status_code==200,f'ожидался ответ 200'
assert 'slideshow' in data
var = {'title'} in {'slideshow'}
title='slideshow','title'
print(f'Title:{'title'}')
