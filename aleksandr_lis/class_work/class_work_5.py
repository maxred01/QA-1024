import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Укажите путь к драйверу (пример для Windows)
def test_hoster():
    driver = webdriver.Chrome()

# Открыть страницу
    driver.get("https://www.hoster.by")
    driver.maximize_window()

    button = driver.find_element(By.XPATH, '//button[@class="m-button red"]')
    button.click()
    text_error = driver.find_element(By.XPATH, '//span[@class="input-domen-error hide"]')
    assert text_error.text =='Укажите доменное имя'
    assert text_error.is_displayed() == False
    button.click()
    time.sleep(2)
    results_domain_name = driver.find_element(By.XPATH, '(//div[@class="m-domain-results-cell domain-name-cell"])[1]')

    assert results_domain_name.is_displayed() == True
    assert results_domain_name.text == text_name + '.by'
    time.sleep(2)

    # Закрыть браузер    driver.close()
    driver.quit()
    time.sleep(5)

# Закрыть браузер
    driver.quit()