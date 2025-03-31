import pytest
import requests

url = "https://api.nationalize.io/"
names = ["anna", "MAX", "123", "иван", ""]

@pytest.mark.parametrize("name", ["anna", "MAX", "123", "иван", ""])
def test_task1(name):
    response = requests.get(url, params={"name": name})
    json_data = response.json()

    assert response.status_code == 200
    assert json_data.get("name", "") == name


#2
@pytest.mark.parametrize("name", ["alex", "olga", ""])
def test_tsk2(name):
    response = requests.get(url, params={"name": name})
    json_data = response.json()

    assert response.status_code == 200
    assert isinstance(json_data.get("country", []), list)
    assert all(0 <= c.get("probability", 0) <= 1 for c in json_data["country"])
