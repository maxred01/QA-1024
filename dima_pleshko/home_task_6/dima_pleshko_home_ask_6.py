# import time
#
# import pytest
# import pytest_check
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# TEST_VALUE = [
#     ['//label[@for="yesRadio"]', '/html/body/div[2]/div/div/div/div[2]/div[2]/p/span', 'Yes'],
#     ['//label[@for="impressiveRadio"]', '/html/body/div[2]/div/div/div/div[2]/div[2]/p/span', 'Impressive'],
#     ['//label[@for="noRadio"]', '/html/body/div[2]/div/div/div/div[2]/div[2]/p/span', 'No']
# ]
#
# @pytest.mark.parametrize('but_xpath, xpath, answer', TEST_VALUE)
# def test_menu(but_xpath, xpath, answer):
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     url = 'https://demoqa.com/radio-button'
#     driver.get(url)
#     driver.execute_script("window.scrollBy(0, 200)")
#     button = WebDriverWait(driver, 3).until(
#         EC.visibility_of_element_located((By.XPATH, but_xpath)))
#     button.click()
#     text = WebDriverWait(driver, 2).until(
#         EC.visibility_of_element_located((By.XPATH, xpath)))
#     pytest_check.is_in(answer, text.text, 'No such data')
#from email.contentmanager import get_text_content

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time
import pytest_check as check


def test_menu():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'https://demoqa.com/radio-button'
    driver.get(url)
    driver.execute_script("window.scrollBy(0, 200)")

    elements_radio = [
        (driver.find_element(By.XPATH, '//label[@for="yesRadio"]'), "//span[contains(@class,'text-success')]", 'Yes'),
        (driver.find_element(By.XPATH, '//label[@for="impressiveRadio"]'), "//span[contains(@class,'text-success')]", 'Impressive'),
        (driver.find_element(By.XPATH, '//label[@for="noRadio"]'), "//span[contains(@class,'text-success')]", 'No')
    ]

    for elements, elements_text_message_xpath, elements_text in elements_radio:
        check.is_true(elements.is_displayed())
        elements.click()
        time.sleep(1)
        massage = driver.find_element(By.XPATH, elements_text_message_xpath).text
        check.is_true(massage == elements_text, f'No massage')
