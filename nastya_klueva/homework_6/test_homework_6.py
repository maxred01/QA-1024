import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.execute_script("window.scrollBy(0, 100);")
    yield driver
    driver.quit()


# для проверки выбора радио-кнопки "Yes"
def test_yes_radio_button(driver):
    driver.get("https://demoqa.com/radio-button")

    # Проверяем выбор "Yes"
    yes_radio_btn = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    yes_radio_btn.click()

    # Используем XPath, чтобы найти текст внутри тега <span>
    yes_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[@class='mt-3']/span[text()='Yes']"))
    ).text

    assert yes_message == "Yes", "Ошибка о выборе 'Yes'"


# Тест для проверки выбора радио-кнопки "Impressive"
def test_impressive_radio_button(driver):
    driver.get("https://demoqa.com/radio-button")

    # выбор "Impressive"
    impressive_radio_btn = driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
    impressive_radio_btn.click()

    # XPath, чтобы найти текст внутри тега <span>
    impressive_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[@class='mt-3']/span[text()='Impressive']"))
    ).text

    assert impressive_message == "Impressive", "Ошибка о выборе 'Impressive'"


# для проверки выбора радио-кнопки "No"
def test_no_radio_button(driver):
    driver.get("https://demoqa.com/radio-button")

    # Проверяем выбор "No"
    no_radio_btn = driver.find_element(By.XPATH, "//label[@for='noRadio']")
    no_radio_btn.click()


    no_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[@class='mt-3']/span[text()='No']"))
    ).text

    assert no_message == "No", "Ошибка о выборе 'No'"



if __name__ == "__main__":
    pytest.main()
