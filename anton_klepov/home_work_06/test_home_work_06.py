import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_hw_05():
    driver = webdriver.Chrome()
    url = 'https://demoqa.com/radio-button'
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)

    # прокрутка страницы
    driver.execute_script('window.scrollBy(0, 400)')
    time.sleep(5)

    # radio button Yes
    radio_btn_yes = driver.find_element(By.XPATH, "//label[contains(text(),'Yes')]")
    radio_btn_yes.click()
    time.sleep(1)
    msg_radio_btn_yes = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/p')
    assert msg_radio_btn_yes.text == 'You have selected Yes'
    time.sleep(1)

    # radio button Impressive
    radio_btn_impressive = driver.find_element(By.XPATH, "//label[contains(text(),'Impressive')]")
    radio_btn_impressive.click()
    time.sleep(1)
    msg_radio_btn_impressive = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[2]/div[2]/p')
    assert msg_radio_btn_impressive.text == 'You have selected Impressive'
    time.sleep(1)

    # radio button No
    radio_btn_no = driver.find_element(By.XPATH, "//label[contains(text(),'No')]")
    radio_btn_no.click()
    time.sleep(1)
    assert "custom-control-label disabled" in radio_btn_no.get_attribute("class"), 'Radio Button "No" Enable!'
    time.sleep(1)

    driver.quit()


