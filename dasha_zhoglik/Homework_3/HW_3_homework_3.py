import requests
import pytest
names = ["anna", "MAX", "123", "иван", ""]

@pytest.mark.parametrize("name", names)
def test_nationalize_api(name):
    url = f'https://api.nationalize.io/?name={name}'
    response = requests.get(url)

    assert response.status_code == 200, f"Ошибка: статус-код не 200 для имени '{name}'"

    response_data = response.json()
    assert 'name' in response_data, f"Ошибка: поле 'name' отсутствует в ответе для имени '{name}'"

    assert response_data['name'].lower() == name.lower(), f"Ошибка: имя в ответе не совпадает с '{name}'"