import pytest
import requests
import pytest_check as check


def test_class01():
    url = 'https://randomuser.me/api/'

    respons = requests.get(url)

    data = respons.json()

    assert 'location' in data['results'][0], "location ключ есть"
    print(data['results'][0]['location']['street']['number'])


def test_class02():
    url = 'http://universities.hipolabs.com/search?country=Kazakhstan'
    respons = requests.get(url)
    data = respons.json()

    check.equal(data[0]['alpha_two_code'],'KZ')

TEST_NAME = [
    "Peter",
    "Helen",
]
@pytest.mark.parametrize("name", TEST_NAME)

def test_nationalize_api(name):
    url = "https://api.nationalize.io/"
    params = {"name": name}

    response = requests.get(url, params=params)

    assert response.status_code == 200, f"Ожидался  код 200, получен {response.status_code}"

    data = response.json()

    check.is_in("name", data, "Ответ не содержит ключ 'name'")
    check.is_in("country", data, "Ответ не содержит ключ 'country'")

    check.equal(data ["name"], name)


