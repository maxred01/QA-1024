import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def test_double_click():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)
    double_click_one = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
    actions.double_click(double_click_one).perform()
    text_error_one = driver.find_element(By.XPATH, '//p[@id="doubleClickMessage"]')
    assert text_error_one.text == 'You have done a double click'

    time.sleep(2)

def test_right_click():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/buttons")
    actions = ActionChains(driver)
    right_click = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
    actions.context_click(right_click).perform()
    text_error_right = driver.find_element(By.XPATH, '//p[@id="rightClickMessage"]')
    assert text_error_right.text == 'You have done a right click'
    time.sleep(5)
    driver.quit()
