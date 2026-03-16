import pytest
from Lesson6.HW6.pages.cart_page import CartPage
from Lesson6.HW6.pages.checkout_page import CheckoutPage
from Lesson6.HW6.pages.inventory_page import InventoryPage
from Lesson6.HW6.pages.login_page import LoginPage

@pytest.mark.usefixtures("setup")
class BaseTest:
    cart_page: CartPage
    checkout_page: CheckoutPage
    inventory_page: InventoryPage
    login_page: LoginPage

