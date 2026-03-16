from selenium.webdriver.common.by import By
from Lesson6.HW6.pages.base_page import BasePage


class CheckoutPage(BasePage):
    first_name_field = (By.ID, "first-name")
    last_name_field = (By.ID, "last-name")
    postal_code_field = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    total_amount = (By.CSS_SELECTOR, "[data-test='total-label']")

    def __init__(self, driver):
        super().__init__(driver)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.type_text(self.first_name_field, first_name)
        self.type_text(self.last_name_field, last_name)
        self.type_text(self.postal_code_field, postal_code)
        self.click(self.continue_button)

    def get_total_amount(self):
        return self.get_text(self.total_amount)
