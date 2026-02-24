from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_section_payment_methods(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(3)
    payment_methods_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    payment_methods_link.click()
    sleep(2)
    driver.save_screenshot("./section_payment_methods.png")