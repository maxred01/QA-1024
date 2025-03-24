import allure
import requests


# @allure.epic("Проверка на корректность ввода логин и пароль")
# @allure.feature("Проверка на правильность авторизации")
# @allure.story("Проверка на статус код")
# @allure.title("Проверка статус кода сайта 21vek.by")
# @allure.description("Тест проверяет статус код для сайта 21vek.by")
# @allure.link("https://google.com", name="Документация")
# @allure.issue("ISSUE-123")
# @allure.testcase("TC-456")
# @allure.severity(allure.severity_level.CRITICAL)
# def test_hoster_status_code(username=None):
#     # Set the dynamic title for the test
#     allure.dynamic.title(f"Тест логина для пользователя: {username}" if username else "Тест без пользователя")
#
#     url = 'https://www.21vek.by/'
#
#     # Make a GET request to the URL
#     response = requests.get(url)
#
#     # Attach log text (ensure this is meaningful in your context)
#     allure.attach("Текст лога: Проверка статус кода", name="log", attachment_type=allure.attachment_type.TEXT)
#
#     # Attach a screenshot if it exists
#     try:
#         allure.attach.file("./screenshot.png", name="Скриншот", attachment_type=allure.attachment_type.PNG)
#     except FileNotFoundError:
#         allure.attach("Скриншот не найден", name="Скриншот", attachment_type=allure.attachment_type.TEXT)
#
#     with allure.step("Проверка статус кода 200"):
#         assert response.status_code == 200, f'статус код равен {response.status_code}'
#
# import allure
#
# @allure.title("Проверка логина с валидными данными")
# @allure.description("Тест проверяет успешный вход в систему")
# def test_login():
#     # Код теста
#     pass
#
# @allure.severity(allure.severity_level.CRITICAL)
# def test_critical_feature():
#     pass

# @allure.link("https://example.com", name="Документация")
# @allure.issue("ISSUE-123")
# @allure.testcase("TC-456")
# def test_with_links():
#     pass


import allure
import pytest

# @allure.epic("Пользовательские операции")
# @allure.feature("Профиль")
# class TestProfile:
#     @allure.story("Изменение пароля")
#     @allure.severity(allure.severity_level.NORMAL)
#     @pytest.mark.parametrize("old_pass, new_pass", [("12345", "67890")])
#     def test_change_password(self, old_pass, new_pass):
#         with allure.step("Войти в профиль"):
#             pass
#         with allure.step("Изменить пароль"):
#             allure.attach(f"Старый пароль: {old_pass}\nНовый пароль: {new_pass}", name="Данные")


def test_attach_data():
    # Текстовое вложение
    allure.attach("Текст лога", name="log", attachment_type=allure.attachment_type.TEXT)

    # Скриншот (пример)
    allure.attach.file("./screenshot.png", name="Скриншот", attachment_type=allure.attachment_type.PNG)