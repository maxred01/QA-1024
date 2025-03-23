from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/buttons")
driver.maximize_window()

actions = ActionChains(driver)

double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
actions.double_click(double_click_btn).perform()
time.sleep(1)
double_click_message = driver.find_element(By.ID, "doubleClickMessage").text
assert double_click_message == "Вы сделали двойной клик", "Ошибка: сообщение о двойном клике не найдено"

right_click_btn = driver.find_element(By.ID, "rightClickBtn")
actions.context_click(right_click_btn).perform()
time.sleep(1)
right_click_message = driver.find_element(By.ID, "rightClickMessage").text
assert right_click_message == "Вы сделали правый клик", "Ошибка: сообщение о правом клике не найдено"

click_me_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
click_me_btn.click()
time.sleep(1)
dynamic_click_message = driver.find_element(By.ID, "dynamicClickMessage").text
assert dynamic_click_message == "Вы сделали динамический клик", "Ошибка: сообщение о динамическом клике не найдено"

print("Все тесты пройдены успешно!")

driver.quit()
