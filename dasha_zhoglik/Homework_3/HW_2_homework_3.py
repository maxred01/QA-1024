import pytest
import requests

API_URL = "http://example.com/api"

test_data = [
    (12345, "Некорректный тип данных: число"),
    (["test"], "Некорректный тип данных: список"),
    ("a" * 150, "Длинная строка (>100 символов)"),
    ("<script>alert(1)</script>", "XSS инъекция: <script>"),
    ("<img src=x onerror=alert(1)>", "XSS инъекция: <img>")
]

@pytest.mark.parametrize("payload, description", test_data)
def test_invalid_data(payload, description):

    response = requests.post(API_URL, json={"data": payload})

    assert response.status_code in [400, 422], \
        f"Ожидаемый код ошибки 400 или 422, но получили {response.status_code} для {description}"

    assert "error" in response.json(), f"Отсутствует поле 'error' в ответе для {description}"
    assert isinstance(response.json().get("error"), str), f"Поле 'error' должно быть строкой для {description}"

    assert "<script>" not in response.text, f"Ответ содержит уязвимость XSS для {description}"
    assert "<img" not in response.text, f"Ответ содержит уязвимость XSS для {description}"