import requests
import os

with requests.Session() as session:
    # Сохраняет куки и заголовки между запросами
    session.get('https://httpbin.org/cookies/set/session/12345')
    response = session.get('https://httpbin.org/cookies')
    print(f'Cookie: {response.json()['cookies']}')

with open('file.txt', 'rb') as f:
    files = {'file': f}
    response = requests.post('https://httpbin.org/post', files=files)
    file_size = os.path.getsize('file.txt')
    print(f'Размер файла {"file.txt"}: {file_size} Bytes')