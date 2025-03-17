import requests
import pytest
import pytest_check as check

TEST_NAMES=[
    "sasha",
    "nastya"
]
# def test_class01():
#     url = "http://randomuser.me/api/"
#     respons = requests.get(url)
#     data = respons.json()
#     # if data['results']['gender'] == 'male':
#     #     print('male')
#     assert 'location' in data['results'][0], "ошибка"
#     print(data['results'][0]['location']['street']['number'])
#
#     check.is_in('location', data['results'][0], "ошибка")

    #     print(data["gender"])
    # print(respons.json())
def test_class02():
    url= 'http://universities.hipolabs.com/search?country=Kazakhstan'
    response = requests.get(url)
    data = response.json()

    check.equal(data[0]["alpha_two_code"], "KZ")

@pytest.mark.parametrize("name", TEST_NAMES)
def test_nationalize_api(name):
    url = "https://api.nationalize.io/"
    params = {"name": name}

    response = requests.get(url, params=params)

    assert response.status_code == 200, f"Получен код {response.status_code}"
    data = response.json()

    check.is_in("name", data, "Ответ")
    check.is_in("country", data, "Ответ2")

    check.equal(data["name"], name)

    # assert "name" in data, "Ошибка с именем"
    # assert "country" in data, "Ошибка с страна"
    #
    # assert data["name"] == name, "error"
    #
    # for country in data["country"]:
    #     assert "country_id" in country, "нет"
    #     assert "probability" in country, "нет"