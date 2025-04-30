import requests
import allure


@allure.epic("Базовая проверка")
@allure.title("Проверка статус кода сайта ya.ru")
@allure.description("Тест проверяет статус код для сайта ya.ru")
@allure.link("https://ya.ru/", name="Техническая документация")
@allure.issue("ISSUE-ya.ru")
@allure.testcase("TC-ya.ru")
@allure.severity(allure.severity_level.CRITICAL)
def test_hoster_status_code():
    url = 'https://ya.ru/'

    respons = requests.get(url)
    respons_date = respons.content
    with allure.step("Проверка статус кода 201"):
        allure.attach(respons_date, name="log", attachment_type=allure.attachment_type.TEXT)
        assert respons.status_code == 201, f'статус код равен {respons.status_code}'

