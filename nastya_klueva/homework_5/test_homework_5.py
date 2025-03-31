from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/buttons")
time.sleep(2)

actions = ActionChains(driver)

def test_double_click():
    button = driver.find_element(By.ID, "doubleClickBtn")
    actions.double_click(button).perform()
    assert driver.find_element(By.ID, "doubleClickMessage").text == "You have done a double click"
    time.sleep(2)
def test_right_click():
    button = driver.find_element(By.ID, "rightClickBtn")
    actions.context_click(button).perform()
    assert driver.find_element(By.ID, "rightClickMessage").text == "You have done a right click"
    time.sleep(2)
def test_dynamic_click():
    driver.find_element(By.XPATH, "//button[text()='Click Me']").click()
    assert driver.find_element(By.ID, "dynamicClickMessage").text == "You have done a dynamic click"
    time.sleep(2)

    
test_double_click()
driver.execute_script("window.scrollBy(0, 500);")
test_right_click()
test_dynamic_click()

driver.quit()
