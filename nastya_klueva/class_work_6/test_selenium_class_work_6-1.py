import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest_check as check


@allure.story('Тесты проверки заполнения формы')
@allure.feature('Проверка формы')
def test_is_displayed():
    with webdriver.Chrome() as driver:
        driver.maximize_window()
        driver.get("https://demoqa.com/checkbox")

        # driver.execute_script('window.scrollBy(0, 800)')
        but_1 = driver.find_element(By.CLASS_NAME, 'rct-icon rct-icon-expand-close')
        but_1.click()
        time.sleep(5)

