import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Укажите путь к драйверу (пример для Windows)
driver = webdriver.Chrome()

# Открыть страницу
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)
