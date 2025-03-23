import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Укажите путь к драйверу (пример для Windows)
driver = webdriver.Chrome()

# Открыть страницу
driver.get("https://demoqa.com/buttons")
driver.maximize_window()
button_double = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/button')
actions = ActionChains(driver)
actions.double_click(button_double).perform()
time.sleep(5)
button_right_click = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/button')
actions.context_click(button_right_click).perform()
time.sleep(5)
button_single_click = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button')
button_single_click.click()
time.sleep(5)
driver.quit()