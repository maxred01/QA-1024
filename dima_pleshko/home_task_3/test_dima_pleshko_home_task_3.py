import requests
import pytest
import pytest_check as check
import string

# Задача: Протестируйте эндпоинт GET https://api.nationalize.io/ с разными именами
# Требования:
# Создайте параметризованный тест для 5 разных имен
# Проверьте:
# Статус-код ответа (200)
# Наличие поля name в ответе
# Совпадение имени в ответе с запрошенным

TEST_NAMES=[
    'George',
    'Dzmitry',
    'Oliver',
    'Maria',
    'Ruby'
]
url="https://api.nationalize.io/"

@pytest.mark.parametrize('name',TEST_NAMES)
def test_nationalize_api(name):
    params = {'name': name}
    response = requests.get(url, params=params)
    assert response.status_code == 200, f'Error, status code: {response.status_code}'
    response = response.json()
    print(response)
    check.is_in("name", response, "Ответ не содержит ключ 'name'")
    check.equal(response['name'], name)

# Задача: Добавьте проверки структуры ответа для разных комбинаций параметров
# Требования:
# Используйте параметризацию для:
# Имен (минимум 3 случая)
# Необязательного параметра country_id (например, "RU", "US", None)
# Проверьте:
# Формат данных в поле country
# Диапазон значений probability (0-1)
# Наличие country_id в ответе при указании параметра

TEST_NAMES_COUNTRIES_CASE_2 = [
    ['Jake', 'US'],
    ['Tom', 'BY'],
    ['Jake', 'None']
]

@pytest.mark.parametrize('name, country_id',TEST_NAMES_COUNTRIES_CASE_2 )
def test_nationalize_api(name, country_id):
    params_name = {'name': name}
    response = requests.get(url, params=params_name)
    response = response.json()
    check.is_in('country_id', response['country'][0], 'No key value country')
    for i in range(len(response['country'])):
        check.between(response['country'][i]['probability'], 0.0, 1.0)
        check.equal(response['country'] is not None, True, 'No country')

# Требования:
# Создайте параметризованные тесты для:
# Некорректных типов данных (числа, списки, специальные символы)
# Длинных строк (>100 символов)
# XSS-инъекций (пример: "<script>alert(1)</script>")
# Проверьте:
# Обработку ошибок сервером
# Отсутствие уязвимостей
# Соответствие ошибок спецификации API

def generate_edge_cases():
    yield 'empty_string', ''
    yield 'space', ' '
    yield 'long_string', 'a'*100
    yield 'special_chars', '!@#$%^&*()'
    yield 'img.jpg', 'https://i.pinimg.com/originals/24/ac/ef/24acef8b3a6a45d7239480bcc4ff0193.jpg'
    yield 'self_reference','https://api.nationalize.io/'
    yield 'XSS', 'script>alert("Allows XSS")</script>'
    yield 'double_name', 'Allie Kate'
    yield 'Cyrillic_and_Latin', 'Mishа'

@pytest.mark.parametrize("case_name,input_data", generate_edge_cases())
def test_edge_cases(case_name, input_data):
    params_name = {'input_data': input_data}
    response = requests.get(url, params=params_name)
    try:
        print(f'\n{case_name}')
        response.raise_for_status()
    except requests.exceptions.HTTPError as error_code:
        print(f"Mistake 400-500: {error_code}")
    except requests.exceptions.RequestException as error_code:
        print(f"Mistake  something else: {error_code}")

