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
permanent_adress = driver.find_element(By.ID, 'permanentAddress')
full_name.send_keys('jara')
time.sleep(2)
email.send_keys("jara@mail.ru")
time.sleep(2)
current_address.send_keys("Marksa st.34")
time.sleep(2)
permanent_adress.send_keys('lenina st.22')
time.sleep(2)
driver.execute_script("window.scrollBy(0,800);")
time.sleep(2)
button_submit = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div/button')
button_submit.click()
time.sleep(2)



driver.close()
driver.quit()
