import requests
import allure
import pytest


@allure.epic("Базовая проверка")
@allure.feature("Базовые сценарии")
@allure.story("Статус код")
@allure.title("Проверка статус кода сайта 21vek.by")
@allure.description("Тест проверяет статус код для сайта 21vek.by")
@allure.link("https://yandex.by/", name="Документация")
@allure.issue("ISSUE-123")
@allure.testcase("TC-456")
@allure.severity(allure.severity_level.CRITICAL)
def test_21vek_status_code():
    url = 'https://www.21vek.by/'
    respons = rekuest.get(url, params=name)
    allure.dynamic.title(f"Тест логина для пользователя: {name}")
    respons_data = requests.post(json)


    with allure.step("Проверка статус кода 200"):
        allure.attach("Текст лога", name="log", attachment_type=allure.attachment_type.JSON)
        assert respons.status_code == 200, f'статус код равен {respons.status_code}'


