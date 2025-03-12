import pytest
import requests
import pytest_check as check

# def test_class():
    # url = 'https://randomuser.me/api/'
    #
    # response = requests.get(url)
    # res_dict = response.json()
    # assert 'location' in res_dict['results'][0], "no location"
    # print(res_dict['results'][0]['location']['street']['number'])
    # url = 'http://universities.hipolabs.com/search?country=Kazakhstan'
    # response = requests.get(url)
    # res_dict = response.json()
    # check.equal(res_dict[0]['alpha_two_code'], "KZ", "Not equal")

TEST_NAMES = {
    'dima',
    '',
    '2313',
    'https://api.nationalize.io/',
    'thumbs_up',
    '👍',
    'tim Lopkin',
    'SELECT * from country where country_id = \'US\'',
}


@pytest.mark.parametrize("name", TEST_NAMES)
def test_nationalize_api(name):
    url = "https://api.nationalize.io/"
    params = {"name": name}
    respones = requests.get(url, params=params)

    assert respones.status_code == 200, f'not valid status code {respones.status_code}'

    respons = respones.json()

    check.is_in("name", respons, 'No param "name"')
    check.is_in("country", respons, 'No param "name"')

    check.equal(respons['name'], name)
