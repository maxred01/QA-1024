import pytest

def get_response(name, country_id):
    response = {
        "name": name,
        "country": country_id if country_id else "Unknown",
        "probability": 0.95 if name else 0.0,
        "country_id": country_id if country_id else None
    }
    return response

@pytest.mark.parametrize(
    "name, country_id",
    [("alex", "US"), ("olga", None), ("", "RU")]
)
def test_response_structure(name, country_id):

    response = get_response(name, country_id)

    assert isinstance(response["country"], str), \
        f"Field 'country' should be a string, but got {type(response['country'])}"

    assert 0 <= response["probability"] <= 1, \
        f"Field 'probability' should be between 0 and 1, but got {response['probability']}"

    if country_id is not None:
        assert response["country_id"] == country_id, \
            f"Field 'country_id' should match the provided country_id, but got {response['country_id']}"
    else:
        assert response["country_id"] is None, \
            f"Field 'country_id' should be None when country_id is not provided, but got {response['country_id']}"