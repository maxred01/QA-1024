#import requests
#from nose import tools as check
import pytest
import requests

from Sveta_Petrovskaya.Homework_2.homework_2 import response


#def test_class_work():

    #url = 'https://universities.hipolabs.com/search?country=Kazakhstan'

    #response = requests.get(url)

   # data = response.json()

    #check.equal(data[0]['alpha_two_code'], 'KZ', 'Значение не равно KZ')
    #print(data[0]['name'])

#names_to_test = ["Sveta", "Anna", "Nastya"]
#@pytest.mark.parametrize("name", response)
#def test_nationalize_api(name, reguests=None):
    #url = "https://api.nationalize.io/"
    #params = {"name": name}
    #response = {'name': name}
    #response = reguests.get(url, params=params)
    #assert response.status_code == 200, f"Unexpected status code for {name}: {response.status_code}"
    #response_json = response.json()
    #assert 'name' in response_json, f"'name' ключ отсутствует в ответе {name}"
    #assert response_json['name'] == name, f"Имя в ответе не совпадает с запрашиваемым {name}"


TEST_NAMES = ["Sveta", "Nastya", "Anna"]


@pytest.mark.parametrize("name", TEST_NAMES)
def test_nationalize_api(name):
    url = "https://api.nationalize.io/"
    params = {"name": name}

    response = requests.get(url, params=params)

    assert response.status_code == 200, f'Ожидается код 200, получен {response.status_code}'

    data = response.json()

    assert 'name' in data, "Ответ не содержит ключ 'name'"
    assert 'country' in data, "Ответ не содержит ключ 'country'"

    assert data['name'] == name, f"Имя в ответе не совпадает с запрашиваемым: {data['name']}"

    for country in data['country']:
        assert 'country_id' in country, 'Нет country_id в стране'
        assert 'probability' in country, 'Нет probability в стране'




