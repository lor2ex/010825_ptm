from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest



@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_button_name_change(driver):
    driver.get('http://uitestingplayground.com/textinput')
    wait = WebDriverWait(driver, 5)  # Ожидание до 5 секунд

    button_name = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
    button_name.send_keys("ITCH")

    blue_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    blue_button.click()
    blue_button_new_name = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#updatingButton"), "ITCH"))
    assert blue_button_new_name


def test_load_images(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
    wait = WebDriverWait(driver, 10)
    last_img = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape")))
    assert last_img.is_displayed()


def test_attribute_3_image(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
    wait = WebDriverWait(driver, 10)
    third_img = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#award")))
    alt_value = third_img.get_attribute("alt")
    assert alt_value == "award"
