import requests
import pytest

TEST_NAMES = [
    "anna",
    "MAX",
    "123",
    "иван",
    ""
]
@pytest.mark.parametrize("name", TEST_NAMES)
def test_homework_01(name):
    url = "https://api.nationalize.io/"
    params = {"name": name}
    response = requests.get(url, params=params)
    assert response.status_code == 200, f"Ошибка  код не 200 для имени '{name}'"
    data = response.json()
    assert 'name' in data, f"Ошибка, поле 'name' отсутствует в ответе '{name}'"
    assert data['name'] == name, f"Ошибка, имя в ответе не совпадает '{name}'"








