import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Chrome()

driver.get("https://demoqa.com/radio-button")
driver.maximize_window()
# scrolls = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[3]/div/div/iframe")
loc_yes = driver.find_element(By.CSS_SELECTOR, "label[for='yesRadio']")
loc_impressive = driver.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']")
loc_no = driver.find_element(By.CSS_SELECTOR, "label[for='noRadio']")
# message_yes = driver.find_element(By.XPATH, "//span[contains(text(),'Yes')]").text
# message_no = driver.find_element(By.XPATH, "//span[contains(text(),'Impressive')]").text
# messages = [message_yes,message_no]
locators = [loc_yes,loc_impressive,loc_no]

# ansvers = ['Yes','Impressive']

for loc in locators:
    ActionChains(driver).move_to_element(loc).click().perform()
    time.sleep(3)
#     loc.click()
#     # time.sleep(3)
#     # assert f'{ansvers}' in f'{messages}'

# ActionChains(driver).move_to_element(loc_yes).click().perform()
# ActionChains(driver).move_to_element(loc_yes).click().perform()
# ActionChains(driver).move_to_element(loc_yes).click().perform()

