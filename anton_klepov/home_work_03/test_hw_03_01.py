import pytest
import requests

TEST_NAMES = [
    "anna",
    "MAX",
    "123",
    "иван",
    ""
]

@pytest.mark.parametrize('name', TEST_NAMES)
def test_chek_hw_01(name):
    url = 'https://api.nationalize.io/'
    params = {'name': name}
    response = requests.get(url, params=params)
    assert response.status_code == 200, f'Ожидается код 200, получен код {response.status_code}'
    data = response.json()
    assert 'name' in data, f'ответ не содержит имя {"name"}'
    assert data["name"] == name, f'ожидалось имя {name}, получено {data["name"]}'
