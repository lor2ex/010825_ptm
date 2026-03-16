from selenium.webdriver.common.by import By
from Lesson6.HW6.pages.base_page import BasePage

class CartPage(BasePage):
    checkout_button = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def proceed_to_checkout(self):
        self.click(self.checkout_button)