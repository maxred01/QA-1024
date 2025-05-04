from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()

driver.get("https://demoqa.com/radio-button")
driver.maximize_window()
# scrolls = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[3]/div/div/iframe")
loc_yes = driver.find_element(By.ID, "yesRadio")
loc_impressive = driver.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']")
loc_no = driver.find_element(By.CSS_SELECTOR, "label[for='noRadio']")
# text_message_yes = driver.find_element(By.XPATH, "//span[@class='text-success']")
# message_no = driver.find_element(By.XPATH, "//span[contains(text(),'Impressive')]").text
# messages = [message_yes,message_no]
# locators = [loc_yes,loc_impressive,loc_no]
#
# # ansvers = ['Yes','Impressive']
#
# for loc in locators:
#     ActionChains(driver).move_to_element(loc).click().perform()
#     time.sleep(3)
#     loc.click()
#     # time.sleep(3)
#     # assert f'{ansvers}' in f'{messages}'


ActionChains(driver).move_to_element(loc_yes).click()
# time.sleep(3)
# text_message_yes = driver.find_element(By.XPATH, "//span[@class='text-success']")
# # text_message_yes = WebDriverWait(driver, 10).until(
# #         EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'text-success')]"))
# # )
# assert text_message_yes.text == 'yes'
ActionChains(driver).move_to_element(loc_impressive).click().perform()
ActionChains(driver).move_to_element(loc_no).click().perform()
# loc_yes.click()
# assert
# ActionChains(driver).move_to_element(loc_yes).click().perform()
