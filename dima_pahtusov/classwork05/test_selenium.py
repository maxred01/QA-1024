import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Укажите путь к драйверу (пример для Windows)
driver = webdriver.Chrome()

# Открыть страницу
driver.get("https://hoster.by/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/div/div/div[2]/div[1]/button').click()
time.sleep(5)


# Закрыть браузер
driver.quit()