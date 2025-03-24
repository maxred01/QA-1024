import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()

driver.get("https://demoqa.com/text-box")
driver.maximize_window()
full_name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[1]/div[2]/input')
email = driver.find_element(By.ID, 'userEmail')
current_address = driver.find_element(By.ID, 'currentAddress')
permanent_address = driver.find_element(By.ID, 'permanentAddress')
full_name.send_keys('fox')
time.sleep(2)
email.send_keys('fox@tut.by')
time.sleep(2)
current_address.send_keys(1234)
time.sleep(2)
button_submit= driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div/button')
#permanent_address.send_keys(4321)
#text_name = driver.find_element(By.ID, 'name')
#text_email = driver.find_element(By.ID, 'email')
#text_current_address = driver.find_element(By.ID, 'currentAddress')
#text_permanent_address = driver.find_element(By.ID, 'permanentAddress')