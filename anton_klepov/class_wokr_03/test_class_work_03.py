import requests
import pytest
import pytest_check as check

TEST_NAMES = [
    'anton',
    'aries',
    'elibri',
    '102',
    '***ar***'
]
# def test_class01():
#
#     url = 'https://randomuser.me/api'
#     respons = requests.get(url)
#
#     # print(respons.json())
#     # print(respons.text)
#     data = respons.json()
#     # print(test_result['results'][0]['location']['street']['number'])
#     # assert 'location' in test_result['results'][0], 'location ключа нет'
#     # check.is_in('gender', data['results'][0], "gender ключа нет")
#     # сheck.is_in('location', data['results'][0], "location ключа нет")
#     # number = data['results'][0]['location']['street']['number']
#     # print(number)


# def test_class02():
#
#     url = 'http://universities.hipolabs.com/search?country=Kazakhstan'
#     respons = requests.get(url)
#     data = respons.json()
#     check.equal(data[0]['alpha_two_code'], 'KZ')

@pytest.mark.parametrize("name", TEST_NAMES)
def test_nationalize_api(name):
    url = "https://api.nationalize.io/"
    params = {"name": name}

    response = requests.get(url, params=params)
    assert response.status_code == 200, f'ожидается код 200 получен {esponse.status_code}'
    data = response.json()
    assert 'name' in data, 'ответ не содержит ключ "name"'
    assert 'country' in data, 'ответ не содержит ключ "country"'

    assert data['name'] == name, f'Ожидалось имя {name}, получено {data["name"]}'

    check.is_in('name', data, 'ответ не содержит ключ "name"')
    check.is_in('country', data, 'ответ не содержит ключ "country"')
    check.equal(data['name'], name)

    for country in data['country']:
        assert 'country_id' in country, 'нет country_id в объекте старны'
        assert 'probability' in country, 'нет probability в объекте старны'
