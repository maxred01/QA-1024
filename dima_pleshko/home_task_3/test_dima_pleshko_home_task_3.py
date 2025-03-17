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
def test_nationalize_api_easy(name):
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
    ['Jake', 'PH'],
    ['', None]
]

@pytest.mark.parametrize('name, country_id',TEST_NAMES_COUNTRIES_CASE_2 )
def test_nationalize_api_normal(name, country_id):
    params_name = {'name': name}
    response = requests.get(url, params=params_name)
    response = response.json()
    check.is_in('country_id', response['country'][0], 'No key value country')
    print(response)
    list_country_id =[]
    for i in range(len(response['country'])):
        check.between(response['country'][i]['probability'], 0.0, 1.0)
        list_country_id.append(response['country'][i]['country_id'])
    check.is_in(country_id, list_country_id,f'No {country_id} in country_id' )


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
    yield 'XSS', '<script>alert(1)</script>'
    yield 'double_name', 'Allie Kate'
    yield 'Cyrillic_and_Latin', 'Mishа'

@pytest.mark.parametrize("case_name,input_data", generate_edge_cases())
def test_nationalize_api_hard(case_name, input_data):
    params_name = {'input_data': input_data}
    response = requests.get(url, params=params_name)
    try:
        assert response.status_code == 422, f'Error, status code{response.status_code}'
        print(f'Status code: {response.status_code}')
        if '<script>' in input_data:
            print(f'Check, XSS request: {response.text}')
    except requests.exceptions.HTTPError as error_code:
        print(f"Ошибка 400-500: {error_code}")


