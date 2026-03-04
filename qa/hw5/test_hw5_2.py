from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.execute_cdp_cmd("Network.enable", {})  # убираю попап
    driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": [  # убираю попап
        "*fundingchoicesmessages.google.com/*",
        "*consent.google.com/*",
    ]})
    yield driver
    driver.quit()



# ===================== ЗАДАНИЕ 2 =====================

def test_drag_and_drop(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe.demo-frame"))
    )
    driver.switch_to.frame(iframe)

    photos = driver.find_elements(By.CSS_SELECTOR, "#gallery li")
    assert len(photos) == 4, f"Ожидалось 4 фото, найдено {len(photos)}"

    trash = driver.find_element(By.ID, "trash")

    ActionChains(driver).drag_and_drop(photos[0], trash).perform()

    WebDriverWait(driver, 5).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "#trash li")) == 1
    )

    trash_count = len(driver.find_elements(By.CSS_SELECTOR, "#trash li"))
    gallery_count = len(driver.find_elements(By.CSS_SELECTOR, "#gallery li"))

    assert trash_count == 1, f"В корзине ожидалась 1 фото, найдено {trash_count}"
    assert gallery_count == 3, f"В галерее ожидалось 3 фото, найдено {gallery_count}"

    # driver.switch_to.default_content()