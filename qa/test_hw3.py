from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()

def test_logo_displayed(driver):
    logo_displayed = driver.find_element(By.CSS_SELECTOR, ".tn-elem__19217104631710153310155 img")
    assert logo_displayed.is_displayed()


def test_link_programs(driver):
    link_programs = driver.find_element(By.CSS_SELECTOR, ".tn-elem__1921710463176285426165569250")
    assert link_programs.is_displayed()

def test_link_payment_methods(driver):
    link_payment_methods = driver.find_element(By.CSS_SELECTOR, ".tn-elem__1921710463176285426166311940")
    assert link_payment_methods.is_displayed()

def test_link_about(driver):
    link_about = driver.find_element(By.CSS_SELECTOR, '.tn-elem__1921710463176285426166799010')
    assert link_about.is_displayed()

def test_link_reviews(driver):
    link_reviews = driver.find_element(By.CSS_SELECTOR, '.tn-elem__1921710463176285426167863090')
    assert link_reviews.is_displayed()

def test_language_buttons_displayed(driver):

    lang_buttons = {
        "ru": ".tn-elem__19217104631710152827519 a",
        "de": ".tn-elem__19217104631710153064158 a",
    }

    for lang, selector in lang_buttons.items():
        button = driver.find_element(By.CSS_SELECTOR, selector)
        assert button.is_displayed(), f"Кнопка переключения на '{lang}' не видна"

def test_call_button_and_popup_text(driver):
    driver.get("https://itcareerhub.de/reviews")
    call_button = driver.find_element(By.CSS_SELECTOR,  ".tn-elem__8549008291712565397743 img")
    call_button.click()
    sleep(1)
    popup_text = driver.find_element(By.CSS_SELECTOR,  ".tn-elem__13803069911711363912027")
    assert popup_text.text == "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"


























