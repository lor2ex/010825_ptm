from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()



# ===================== ЗАДАНИЕ 1 =====================


def test_iframe_text(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    wait = WebDriverWait(driver, 10)

    iframe = driver.find_element(By.ID, "my-iframe")
    driver.switch_to.frame(iframe)

    target = "semper posuere integer et senectus justo curabitur."

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "#content > p:nth-child(2)"),
            target
        )
    )

    paragraph = driver.find_element(By.CSS_SELECTOR, "#content > p:nth-child(2)")
    assert paragraph.is_displayed(), "Элемент с текстом не отображается"
    assert target in paragraph.text



# var 2
# def test_iframe_text(driver):
#     driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
#     wait = WebDriverWait(driver, 10)
#
#     iframe = driver.find_element(By.ID, "my-iframe")
#     driver.switch_to.frame(iframe)
#
#     target = "semper posuere integer et senectus justo curabitur."
#     paragraphs = wait.until(EC.text_to_be_present_in_element((
#         By.CSS_SELECTOR, "#content > p:nth-child(2)"), target)
#     )
#     assert paragraphs, "Элемент с текстом не отображается"







# var 3
# def test_iframe_text(driver):
#     driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
#
#     iframe = driver.find_element(By.ID, "my-iframe")
#     driver.switch_to.frame(iframe)
#
#     target = "semper posuere integer et senectus justo curabitur."
#     paragraphs = driver.find_elements(By.ID, "p")
#
#     element = None
#     for p in paragraphs:
#         if target in p.text.lower():
#             element = p
#             break
#
#     assert element is not None, f"Текст '{target}' не найден в iframe"
#     assert element.is_displayed(), "Элемент с текстом не отображается"
#
#     driver.switch_to.default_content()




