import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import allure

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://demoqa.com/radio-button")
    driver.maximize_window()
    yield driver
    time.sleep(4)
    driver.quit()

@allure.feature('Radio Button Tests')
class TestRadioButtons:

    @allure.title('Тест кнопки Yes')
    def test_yes_radio(self, driver):
        driver.find_element(By.XPATH, "//label[contains(text(),'Yes')]").click()
        result = driver.find_element(By.CLASS_NAME, "text-success").text
        assert result == "Yes", f"Ожидалось 'Yes', получено '{result}'"

    @allure.title('Тест кнопки Impressive')
    def test_impressive_radio(self, driver):
        driver.find_element(By.XPATH, "//label[contains(text(),'Impressive')]").click()
        result = driver.find_element(By.CLASS_NAME, "text-success").text
        assert result == "Impressive", f"Ожидалось 'Impressive', получено '{result}'"

    @allure.title('Тест кнопки No')
    def test_no_radio(self, driver):
        no_button = driver.find_element(By.XPATH, "//label[contains(text(),'No')]")
        assert "disabled" in no_button.get_attribute("class"), "Кнопка 'No' должна быть отключена"

if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=allure-results"])