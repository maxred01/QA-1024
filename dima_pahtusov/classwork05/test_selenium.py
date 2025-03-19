import time
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_hoster():

    driver = webdriver.Chrome()


    driver.get("https://www.hoster.by")
    driver.maximize_window()
    time.sleep(2)

    button = driver.find_element(By.XPATH, '//button[@class="m-button red"]')
    if button.is_displayed():
        button.click()

    time.sleep(2)
    text_error = driver.find_element(By.XPATH, '//span[@class="input-domen-error hide"]')

    assert text_error.text == 'Укажите доменное имя'
    input = driver.find_element(By.XPATH, '//input[@class="m-input m-b1"]')
    text_name = 'testmaxtest'
    input.send_keys(text_name)

    assert text_error.is_displayed() == False
    button.click()
    time.sleep(2)
    results_domain_name = driver.find_element(By.XPATH, '(//div[@class="m-domain-results-cell domain-name-cell"])[1]')

    assert results_domain_name.is_displayed() == True
    assert results_domain_name.text == text_name + '.by'
    time.sleep(2)

    # Закрыть браузер    driver.close()
    driver.quit()