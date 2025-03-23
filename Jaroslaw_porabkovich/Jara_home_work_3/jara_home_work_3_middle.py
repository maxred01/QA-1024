import pytest
import requests
B_URL="https://api.nationalize.io/"

@pytest.mark.parametrize("name, country",[("rick", "RU"), ("Mila","BY" ),("Vlad","None")])
def test_easy(name,country):
    params={"name":name}
    if country:
        params["country"]=country

    response = requests.get(f"https://api.nationalize.io/",params=params)
    assert response.status_code == 200
    response_json = response.json()
    assert "name" in  response_json, f'Поле "name" отсутствует в ответе для имени {name}'
    assert "country" in response_json,f'Поле "country" отсутствует в ответе для имени {country}'
    assert isinstance(response_json["country"],list), f"Поле 'country' должно быть списком, получено {type(response_json['country'])}"
    for country in response_json["country"]:
        probability=country["probability"]
        assert 0 <= probability <= 1
    assert response_json['name'] == name, f' имя в ответе ({response_json['name']}) не совпадает с запрошенным ({name})'

