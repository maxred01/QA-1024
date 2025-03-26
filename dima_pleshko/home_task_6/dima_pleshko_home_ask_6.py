import time

import pytest
import pytest_check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TEST_VALUE = [
    ['//label[@for="yesRadio"]', '/html/body/div[2]/div/div/div/div[2]/div[2]/p/span', 'Yes'],
    ['//label[@for="impressiveRadio"]', '/html/body/div[2]/div/div/div/div[2]/div[2]/p/span', 'Impressive'],
    ['//label[@for="noRadio"]', '/html/body/div[2]/div/div/div/div[2]/div[2]/p/span', 'No']
]

@pytest.mark.parametrize('but_xpath, xpath, answer', TEST_VALUE)
def test_menu(but_xpath, xpath, answer):
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'https://demoqa.com/radio-button'
    driver.get(url)
    driver.execute_script("window.scrollBy(0, 200)")
    button = WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located((By.XPATH, but_xpath)))
    button.click()
    text = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, xpath)))
    pytest_check.is_in(answer, text.text, 'No such data')

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import allure
# import time
# import pytest_check as check
#
#
# @pytest.mark.parametrize()
# def test_menu():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     url = 'https://demoqa.com/radio-button'
#     driver.get(url)
#     driver.execute_script("window.scrollBy(0, 200)")
#
#     elements_radio = [
#         (driver.find_element(By.XPATH, '//label[@for="yesRadio"]'), driver.find_element(By.ID, 'yesRadio'), 'Yes'),
#         (driver.find_element(By.XPATH, '//label[@for="impressiveRadio"]'), driver.find_element(By.ID, 'yesRadio'), 'Impressive'),
#         (driver.find_element(By.XPATH, '//label[@for="noRadio"]'), driver.find_element(By.XPATH, '//span[@class="text-success"]'), 'No')
#     ]
#
#     for elements, elements_text_messege, elements_text in elements_radio:
#         with allure.step(f'Поля "{elements_text}" на отображение'):
#             check.is_true(elements.is_displayed())
#             elements.click()
#             time.sleep(1)
#             check.is_true(elements.is_displayed())
#             driver.find_element(By.XPATH, '//span[@class="text-success"]')