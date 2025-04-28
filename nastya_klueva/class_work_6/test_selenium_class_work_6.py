from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Открыть страницу
driver.get("https://demoqa.com/text-box")
driver.maximize_window()

full_name = 'Anastasiya'
email = 'nastya@gmail.com'
current_address = 'г. Минск, пр-т Рокоссовского'
permanent_email = 'г. Минск, пр-т Рокоссовского 2'

test_full_name = driver.find_element(By.ID, 'userName')
test_email = driver.find_element(By.ID, 'userEmail')
test_c_adr = driver.find_element(By.ID, 'currentAddress')
test_p_adr = driver.find_element(By.ID, 'permanentAddress')
button_sent = driver.find_element(By.ID, 'submit')

test_full_name.send_keys(full_name)
time.sleep(2)
test_email.send_keys(email)
time.sleep(2)
test_c_adr.send_keys(current_address)
time.sleep(2)
test_p_adr.send_keys(permanent_email)
time.sleep(2)
button_sent.click()

