import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Укажите путь к драйверу (пример для Windows)
driver = webdriver.Chrome()

# Открыть страницу
driver.get("https://demoqa.com/checkbox")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, '//button[@class="rct-collapse rct-collapse-btn"]').click()
driver.find_element(By.XPATH, '//span[@class="rct-checkbox"]').click()



time.sleep(5


# Закрыть браузер
driver.quit()