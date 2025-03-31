from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def double_click_test(driver):
    double_click_btn = driver.find_element(By.XPATH, "//button[@id='doubleClickBtn']")
    actions = ActionChains(driver)
    actions.double_click(double_click_btn).perform()
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 500);")

    message = driver.find_element(By.XPATH, "//*[@id='doubleClickMessage']").text
    assert message == "You have done a double click", "Ошибка: сообщение о двойном клике не найдено"
    print("Двойной клик сделан")


def right_click_test(driver):
    right_click_btn = driver.find_element(By.XPATH, "//button[@id='rightClickBtn']")
    actions = ActionChains(driver)
    actions.context_click(right_click_btn).perform()
    time.sleep(1)

    message = driver.find_element(By.XPATH, "//*[@id='rightClickMessage']").text
    assert message == "You have done a right click", "Ошибка: сообщение о правом клике не найдено"
    print("Правый клик сделан")

def click_me_test(driver):
    click_me_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    click_me_btn.click()
    time.sleep(1)

    message = driver.find_element(By.XPATH, "//*[@id='dynamicClickMessage']").text
    assert message == "You have done a dynamic click", "Ошибка: сообщение о динамическом клике не найдено"
    print("Обычный клик сделан")

def main():
    browser = webdriver.Chrome()
    browser.get("https://demoqa.com/buttons")
    browser.maximize_window()

    double_click_test(browser)
    right_click_test(browser)
    click_me_test(browser)

    browser.quit()

if __name__ == "__main__":
    main()
