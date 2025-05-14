import requests
import pytest
import pytest_check as check


TEST_NAMES=[
    "anna"
    , "MAX"
    , "123"
    , "иван"
    , ""
]

@pytest.mark.parametrize("name", TEST_NAMES)
def test_nationalize_api(name):
    url = "https://api.nationalize.io/"
    params = {"name": name}

    respons = requests.get(url, params=params)
    assert respons.status_code == 200
    data = respons.json()
    check.is_in('name', data, "Ответ не содержит ключа 'name'")
    check.equal(data["name"], name)

