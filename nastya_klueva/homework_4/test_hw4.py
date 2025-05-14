import allure
import requests
import pytest


@allure.epic("Проверка сайта")
@allure.feature("Основные проверки")
class TestWebsiteChecks:

    @allure.story("Проверка статус кода")
    @allure.title("Проверка статус кода сайта onliner.by")
    @allure.description("Тест проверяет статус код для сайта onliner.by")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("username", [None, "test_user"], ids=["without_user", "with_user"])
    def test_hoster_status_code(self, username):
        """Тест проверки статус кода с возможностью указания пользователя"""
        allure.dynamic.title(f"Тест для пользователя: {username}" if username else "Тест без пользователя")
        url = 'https://www.onliner.by/'

        with allure.step(f"Отправка GET запроса к {url}"):
            response = requests.get(url)
            allure.attach(f"Response: {response.status_code}", name="response",
                          attachment_type=allure.attachment_type.TEXT)

        with allure.step("Проверка статус кода"):
            assert response.status_code == 200, f'Ожидался код 200, получен {response.status_code}'