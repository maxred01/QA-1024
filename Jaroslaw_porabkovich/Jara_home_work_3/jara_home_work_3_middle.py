import pytest
import requests
B_URL="https://api.nationalize.io/"

@pytest.mark.parametrize("name, country_id",[("rick", "RU"), ("Mila","BY" ),("Vlad","None")])
def test_easy(name,country_id):
    params={"name":name}
    if country_id:
        params["country_id"]=country_id

    response = requests.get(f"https://api.nationalize.io/",params=params)
    assert response.status_code == 200
    response_json = response.json()
    assert "name" in  response_json, f'Поле "name" отсутствует в ответе для имени {name}'
    assert "country_id" in response_json,f'Поле "country_id" отсутствует в ответе для имени {country_id}'
    assert isinstance(response_json["country_id"],list), f"Поле 'country_id' должно быть списком, получено {type(response_json['country'])}"
# доделать диапазон значений!!!
    assert response_json['name'] == name, f' имя в ответе ({response_json['name']}) не совпадает с запрошенным ({name})'

