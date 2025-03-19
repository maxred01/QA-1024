import requests
#
# url = 'http://randomuser.me/api/'
#
# respons = requests.get(url)
# print(respons.json())
# data = respons.json()
# assert 'location' in data['results'][0], "location ключа нет"
# print (data['results'][0]['location']['street']['number'])


import requests
import pytest
import pytest_check as check



def test_class_work():
    url = 'http://universities.hipolabs.com/search?country=Kazakhstan'
    respons = requests.get(url)
    data = respons.json()

    check.equal(data[0]['alpha_two_code'], 'KZ')

TEST_NAMES='dima'

@pytest.mark.parametrize("name", TEST_NAMES)
def test_nationalize_api(name):
    url = "https://api.nationalize.io/"
    params = {"name": name}

    respons = requests.get(url, params=params)
    assert respons.status_code == 200
    data = respons.json()
    check.is_in('name', data, "Ответ не содержит ключа 'name'")
    check.is_in('country',data, "Ответ не содержит ключ 'country'")
    check.equal(data["name"], name)












