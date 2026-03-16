import pytest
from selenium import webdriver
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def setup(request):
    options = Options()

    # ⬇️ Ключевые строки — убирают окно о пароле
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    })

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    request.cls.driver = driver
    request.cls.cart_page = CartPage(driver)
    request.cls.checkout_page = CheckoutPage(driver)
    request.cls.inventory_page = InventoryPage(driver)
    request.cls.login_page = LoginPage(driver)

    yield
    driver.quit()