import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_hw_05():
    driver = webdriver.Chrome('/usr/bin/chromedriver')
    url = 'https://demoqa.com/buttons'
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

