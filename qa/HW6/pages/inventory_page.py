from selenium.webdriver.common.by import By
from Lesson6.HW6.pages.base_page import BasePage


class InventoryPage(BasePage):
    backpack_add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    bolt_add_button = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    onesie_add_button = (By.ID, "add-to-cart-sauce-labs-onesie")
    cart_button = (By.ID, "shopping_cart_container")

    def __init__(self, driver):
        super().__init__(driver)


    def add_products_to_cart(self):
        self.click(self.backpack_add_button)
        self.click(self.bolt_add_button)
        self.click(self.onesie_add_button)

    def go_to_cart(self):
        self.click(self.cart_button)
