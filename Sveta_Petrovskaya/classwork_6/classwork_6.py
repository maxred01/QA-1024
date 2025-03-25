import time
import allure
import pytest_check as check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.story('Заполнение формы')
@allure.feature('Проверка формы')
@allure.title('Проверка отображения и нажатия кнопки')
def test_is_displayed():
    with webdriver.Chrome() as driver:
        driver.maximize_window()
        driver.get("https://demoqa.com/text-box")

        but_1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="submit"]'))
        )
        but_1.click()

        check.is_true(but_1.is_displayed(), "Кнопка должна быть видима")

        time.sleep(5)