import pytest
import requests
import pytest_check as check

#url = 'https://universities.hipolabs.com/search?country=Kazakhstan'
#respons = requests.get(url)
#print(respons.json())

TEST_NAMES = [
    "Alex"
    "Inna"
    "Bob"
    "Serg"
]

@pytest.mark.parametrize("name", TEST_NAMES)
def test_nationalize_api(name):
    url = "https://api.nationalize.io/"
    params = {"name": name}
    response = requests.get(url, params = params)
    assert response.status_code == 200, f"ожидался ответ 200, получен {response.status_code}"
    data = response.json()
    check.is_in("name", data, "Ответ содержит ключ 'name'")
    check.is_in("country", data, "Ответ содержит ключ 'country'")
    check.equal(data["name"], "Inna")

'''def test_class_work():
    url = 'https://universities.hipolabs.com/search?country=Kazakhstan'
    respons = requests.get(url)
    data = respons.json()
    #check.is_in(domains, data['alpha_two_code'][0], "domains нет ключа")
    check.equests(data['alpha_two_code'], "Kz")'''


