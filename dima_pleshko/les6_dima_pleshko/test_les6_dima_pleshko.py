import time
import pytest

import allure
import pytest_check
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TEST_DATA = [
    'Dima',
    'Dima@gmail.com',
    'Stoletov',
    'Tyta'
]

@allure.feature('Проверка формы')
def test_chek_input_veiv():
    name = 'Dima'
    email = 'Dima@gmail.com'
    cur_address = 'Stoletov'
    per_address = 'Tyta'
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = 'https://demoqa.com/text-box'
    driver.get(url)
    time.sleep(5)
    driver.execute_script("window.scrollBy(0, 500)")
    search_box_name = driver.find_element(By.ID, 'userName')
    search_box_name.send_keys(name)
    search_box_email = driver.find_element(By.ID, 'userEmail')
    search_box_email.send_keys(email)
    search_box_cur_address = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div[2]/textarea')
    search_box_cur_address.send_keys(cur_address)
    search_box_per_address = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[4]/div[2]/textarea')
    search_box_per_address.send_keys(per_address)

    element = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div/button'))
    )
    element.click()

    text_msg_name = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, 'name'))
    )
    text_msg_email = WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located((By.ID, 'email'))
    )
    text_msg_cur_address = WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[3]'))
    )
    text_msg_per_address = WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[4]'))
    )

    try:
        pytest_check.is_in(name, text_msg_name.text, 'No such data')
        pytest_check.is_in(email, text_msg_email.text, 'No such data')
        pytest_check.is_in(cur_address,text_msg_cur_address, 'No such data')
        pytest_check.is_in(per_address, text_msg_per_address, 'No such data')
    except:
        print('It\'s not work')
#
    time.sleep(5)
    driver.close()
    driver.quit()


