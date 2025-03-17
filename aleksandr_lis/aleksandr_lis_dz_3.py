import pytest
import requests

TEST_NAMES = [
    "anna",
    "MAX",
    "123",
    "иван"
    ""
]
@pytest.mark.parametrize("name", TEST_NAMES)
def test_nationalize_api(name):
    url = "https://api.nationalize.io/"
    params = {"name": name}
    response = requests.get(url, params=params)

    assert response.status_code == 200, f"Ожидается код 200, получен: {response.status_code}"

    data = response.json()

    assert "name" in data, "Ответ не содержит ключ 'name' "

    assert "country" in data , "Ответ не содержит ключ 'country'' "


    assert data["name"]== name , f"Ожидалось имя  '{name}', получено '{data['name']}'"

    for country in data["country"]:
        assert "country_id" in country, "Нет country_id в обьекте страны"
        assert "probability" in country, "Нет probability в обьекте страны"

