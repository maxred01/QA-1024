import requests
import allure

NAME=[
    'sasha'
    'masha'
]
@allure.epic("Базовая проверка")
@allure.feature("Базовые сценарии")
@allure.story("Статус код")
@allure.title("Проверка статус кода сайта 21vek.by")
@allure.description("Тест проверяет статус код для сайта 21vek.by")
@allure.link("https://google.com", name="Документация")
@allure.issue("ISSUE-123")
@allure.testcase("TC-456")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize('name',NAME)
def test_21vek_status_code():
    url = 'https://www.21vek.by/'
    respons = requests.get(url, params=name)
    allure.dynamic.title(f'test login for users: {name}')
    respons_data=respons.text

    with allure.step("Проверка статус кода 200"):
        allure.attach(respons_data,name='log',attachment_type=allure.attachment_type.TEXT)
        assert respons.status_code == 200, f'статус код равен {respons.status_code}'
