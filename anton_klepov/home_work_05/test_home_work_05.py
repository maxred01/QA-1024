import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_hw_05():
    driver = webdriver.Chrome()
    url = 'https://demoqa.com/buttons'
    driver.get(url)
    driver.maximize_window()
    action = ActionChains(driver)
    time.sleep(5)

    # прокрутка страницы
    driver.execute_script('window.scrollBy(0, 400)')
    time.sleep(5)

    # двойное нажатие мыши
    btn_double_click = driver.find_element(By.XPATH, '//button[@id="doubleClickBtn"]')
    action.double_click(btn_double_click).perform()
    msg_double_click = driver.find_element(By.XPATH, '//p[@id="doubleClickMessage"]')
    assert msg_double_click.text == 'You have done a double click'
    time.sleep(1)
    # нажатие правой кнопкой мыши
    btn_right_click = driver.find_element(By.XPATH, '//button[@id="rightClickBtn"]')
    action.context_click(btn_right_click).perform()
    msg_right_click = driver.find_element(By.XPATH, '//p[@id="rightClickMessage"]')
    assert msg_right_click.text == 'You have done a right click'
    time.sleep(1)
    # нажатие левой кнопкой мыши
    btn_click = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    action.click(btn_click).perform()
    msg_click = driver.find_element(By.XPATH, '//p[@id="dynamicClickMessage"]')
    assert msg_click.text == 'You have done a dynamic click'
    time.sleep(1)

    driver.quit()


