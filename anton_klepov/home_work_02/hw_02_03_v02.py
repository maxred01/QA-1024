import requests

with requests.Session() as session:
    # Сохраняет куки и заголовки между запросами
    session.get('https://httpbin.org/cookies/set/session/12345')
    response = session.get('https://httpbin.org/cookies')
    print(f'Cookie: {response.json()['cookies']}')

with open('file.txt', 'rb') as f:
    # содержание файла: Anton QA
    file_response = session.post('https://httpbin.org/post', files={'file': f})
    file_size = len(file_response.json()['files']['file'])
    print(f'Размер файла {"file.txt"}: {file_size} Bytes')
