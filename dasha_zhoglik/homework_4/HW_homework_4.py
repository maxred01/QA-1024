import allure
import requests


# @allure.epic("Проверка кнопки Вход")
# @allure.feature("Проверка на правильность авторизации")
# @allure.story("Проверка на статус код")
# @allure.title("Проверка статус кода сайта onliner.by")
# @allure.description("Тест проверяет статус код для сайта onliner.by")
# # @allure.link("https://google.com", name="Документация")
# @allure.issue("ISSUE-123")
# @allure.testcase("TC-456")
# @allure.severity(allure.severity_level.CRITICAL)
# def test_hoster_status_code(username=None):
#
#     allure.dynamic.title(f"Тест логина для пользователя: {username}" if username else "Тест без пользователя")
#     url = 'https://www.onliner.by/'
#
#
#     response = requests.get(url)
#
#     allure.attach("Текст лога: Проверка статус кода", name="log", attachment_type=allure.attachment_type.TEXT)
#
#     try:
#         allure.attach.file("./screenshot.png", name="Скриншот", attachment_type=allure.attachment_type.PNG)
#     except FileNotFoundError:
#         allure.attach("Скриншот не найден", name="Скриншот", attachment_type=allure.attachment_type.TEXT)
#     with allure.step("Проверка статус кода 200"):
#         assert response.status_code == 200, f'статус код равен {response.status_code}'
def test_attach_data():
    # Текстовое вложение
    allure.attach("Текст лога", name="log", attachment_type=allure.attachment_type.TEXT)

    # Скриншот (пример)
    allure.attach.file("./screenshot.png", name="Скриншот", attachment_type=allure.attachment_type.PNG)