import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://demoqa.com/checkbox")
driver.maximize_window()
button_home = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/span/button')
button_home.click()
time.sleep(2)
button_desktop = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/ol/li[1]/span/button')
button_desktop.click()
time.sleep(2)
chcek = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/ol/li[1]/ol/li[1]/span/label/span[1]')
chcek.click()
time.sleep(2)
button_download = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/ol/li[3]/span/button')
button_download.click()
time.sleep(2)
chcek_2 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div/ol/li/ol/li[3]/ol/li[2]/span/label/span[1]')
chcek_2.click()
time.sleep(2)
box_1 = driver.find_element(By.XPATH,'//input[@id="tree-node-notes"]')
if box_1.is_selected():
    print ('выбран')
else:
    print('не выбран')
box_2 = driver.find_element(By.XPATH,'//input[@id="tree-node-excelFile"]')
if box_2.is_selected():
    print ('выбран')
else:
    print('не выбран')

driver.close()
driver.quit()