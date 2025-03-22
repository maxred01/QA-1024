#Написать автотест для сайта https://demoqa.com/buttons на Python + Selenium, который проверит корректность
#работы трех типов кликов (двойной, правой кнопкой, обычный) и отображение соответствующих сообщений

import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_click():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'https://demoqa.com/buttons'
    driver.get(url)
    element = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.XPATH, '//button[text()="Click Me"]'))
    )
    try:
        element.click()
        text_msg = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'dynamicClickMessage'))
        )
        print(text_msg.text)
    except:
        print('It doesn\'t work.')

    time.sleep(5)
    driver.close()
    driver.quit()

def test_double_click():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'https://demoqa.com/buttons'
    driver.get(url)
    element = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.ID, 'doubleClickBtn'))
    )
    action = ActionChains(driver)
    try:
        action.double_click(on_element=element).perform()
        text_msg = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'doubleClickMessage'))
        )
        print(text_msg.text)
    except:
        print('It doesn\'t work.')

    time.sleep(5)
    driver.close()
    driver.quit()

def test_right_click():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'https://demoqa.com/buttons'
    driver.get(url)
    element = WebDriverWait(driver, 2).until(
    EC.element_to_be_clickable((By.ID, 'rightClickBtn'))
    )
    action = ActionChains(driver)
    try:
        action.context_click(element).perform()
        text_msg = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'rightClickMessage'))
        )
        print(text_msg.text)
    except:
        print('\nIt doesn\'t work.')

    time.sleep(5)
    driver.close()
    driver.quit()



