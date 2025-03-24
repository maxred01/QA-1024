import time
from argparse import Action
from lib2to3.pgen2.driver import Driver

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_demoqa():
    driver = webdriver.Chrome()

    driver.get("https://demoqa.com/buttons")
    driver.maximize_window()


    Action = ActionChains(driver)

    double_click_one = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
    Action.double_click(double_click_one).perform()
    text_error_one = driver.find_element(By.XPATH, '//p[@id="doubleClickMessage"]')
    assert text_error_one.text == 'You have done a double click'

    time.sleep(2)

    right_click = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
    Action.context_click(right_click).perform()
    text_error_right = driver.find_element(By.XPATH, '//p[@id="rightClickMessage"]')
    assert text_error_right.text == 'You have done a right click'

    time.sleep(2)

    click_me = driver.find_element(By.XPATH, '//button[text()="Click Me"]').click()
    text_error_click = driver.find_element(By.XPATH, '//p[@id="dynamicClickMessage"]')
    assert text_error_click.text == 'You have done a dynamic click'


    time.sleep(5)
    # Закрыть браузер
    driver.close()
    driver.quit()

