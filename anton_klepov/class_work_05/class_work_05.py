import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_hoster():
    # Укажите путь к драйверу (пример для Windows)
    driver = webdriver.Chrome()

    # Открыть страницу
    driver.get("https://www.hoster.by")
    driver.maximize_window()
    time.sleep(5)

    # driver.find_element(By.XPATH, '/html/body/div[5]/div[1]/div[1]/div/div/div[2]/div[1]/button').click()
    button = driver.find_element(By.XPATH, '//button[@class="m-button red"]')
    if button.is_displayed():
        button.click()

    text_error = driver.find_element(By.XPATH, '//span[@class="input-domen-error hide"]')
    print(text_error.text)
    assert text_error.text == 'Укажите доменное имя'
    time.sleep(5)
    text_title = driver.find_element(By.XPATH, '//h1[@class="intro-title m-font-hl1"]')
    print(text_title.text)
    assert text_title.text == 'Все для онлайн-проектов и их защиты!'
    # Закрыть браузер
    driver.close()
    driver.quit()
