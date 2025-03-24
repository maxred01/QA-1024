import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()

driver.get("https://demoqa.com/buttons")
driver.maximize_window()
button_double = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/button')
actions = ActionChains(driver)
actions.double_click(button_double).perform()
doubleClick_message = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/p[1]')
assert doubleClick_message.text == 'You have done a double click'
time.sleep(5)
button_right_click = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/button')
scroll = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[3]')
actions.scroll_to_element(scroll).perform()
actions.context_click(button_right_click).perform()
rightClick_message = driver.find_element(By.XPATH, '//*[@id="rightClickMessage"]')
assert rightClick_message.text == 'You have done a right click'
time.sleep(5)
button_single_click = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button')
button_single_click.click()
oneClick_message = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/p[3]')
assert oneClick_message.text == 'You have done a dynamic click'
time.sleep(5)
driver.quit()
