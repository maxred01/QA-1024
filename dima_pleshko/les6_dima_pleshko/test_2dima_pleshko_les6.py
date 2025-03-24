import time


import pytest_check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_menu():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'https://demoqa.com/checkbox'
    driver.get(url)
    driver.execute_script("window.scrollBy(0, 400)")

    XPATH_DATE = [
        '/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/span/button',
        '/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/ol/li[1]/span/button',
        '/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/ol/li[3]/span/button',
        '/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/ol/li[1]/ol/li[2]/span/label/span[1]',
        '/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/ol/li[3]/ol/li[2]/span/label/span[1]'
    ]

    for xpath in XPATH_DATE:
        search_home = driver.find_element(By.XPATH, xpath)
        search_home.click()
        time.sleep(1)

    CHECK_VALUE = [
        ['/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/span[3]', 'tree-node-excelFile', 'excelFile'],
        ['/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/span[2]', 'tree-node-commands', 'commands'],
    ]

    for xpath, ident, date in CHECK_VALUE:
        check_box = driver.find_element(By.ID, ident).get_attribute(
            "type")
        pytest_check.is_true(check_box, 'not check')

        text = WebDriverWait(driver, 1).until(
            EC.visibility_of_element_located((By.XPATH, xpath)))
        pytest_check.is_in(date, text.text, 'No such data')


    time.sleep(5)
    driver.close()
    driver.quit()
