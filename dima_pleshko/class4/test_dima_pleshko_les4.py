import pytest
import requests
import allure


@allure.epic("Базовая проверка")
@allure.feature("Базовые сценарии")
@allure.story("Статус код")
@allure.title("Проверка статус кода сайта 21vek.by")
@allure.description("Тест проверяет статус код для сайта 21vek.by")
@allure.link("https://github.com/maxred01/QA-1024/wiki/Allure", name="Документация")
@allure.issue("ISSUE-12")
@allure.testcase("TC-46")
@allure.severity(allure.severity_level.CRITICAL)
def test_hoster_status_code():
    url = 'https://www.21vek.by/'
    with allure.step("Выполняем get запрос на сайт https://www.21vek.by/"):
        response = requests.get(url)

    with allure.step("Проверка статус кода 200"):
        assert response.status_code == 200, f'статус код равен {response.status_code}'

@allure.epic("Базовая проверка")
@allure.feature("Базовые сценарии")
@allure.story("Статус код")
@allure.title("Проверка статус кода сайта 21vek.by")
@allure.description("Тест проверяет статус код для сайта 21vek.by")
@allure.link("https://github.com/maxred01/QA-1024/wiki/Allure", name="Документация")
@allure.issue("ISSUE-12")
@allure.testcase("TC-46")
@allure.severity(allure.severity_level.CRITICAL)
#@pytest.mark.parametrize("word, langs", [("раз", "pass1"), ("user2", "pass2")])
def test_parametrized_login():
    url = 'https://www.saucedemo.com'
    response = requests.get(url)
    print(response.json())
    #allure.dynamic.title(f"Тест логина для пользователя: {lang}")
    assert response.status_code == 200, f'статус код равен {response.status_code}'
