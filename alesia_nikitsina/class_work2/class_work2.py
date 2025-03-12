import requests

#response = requests.get('https://api.github.com')
#assert response.status_code==200,f'Статус код равен 200:статус код равен'{response.status_code}

#response=response.json()
#assert response ['authorizations_url']=="https://api.github.com/authorizations"


#params = {'page': 2, 'limit': 10}
#response = requests.get('https://httpbin.org/get', params=params)
#print(response.url)  # URL с параметрами: https://httpbin.org/get?page=2&limit=10

#assert response.url=='https://httpbin.org/get?page=2&limit=10'

#response = requests.post('https://httpbin.org/post', data={'key': 'value'})
#print(response.text)
#response=response.json()
#assert response ['url']=="https://httpbin.org/post"

User_Agent='MyApp/1.0'
headers = {
    'User-Agent': 'MyApp/1.0',
    'Authorization': 'Bearer YOUR_TOKEN'
}

response = requests.get('https://httpbin.org/headers', headers=headers)
print(response.text)
print(response.json()['headers'])
assert response.json()['headers']['User-Agent']=="MyApp/1.0"