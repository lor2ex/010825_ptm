from selenium.webdriver.common.by import By
from Lesson6.HW6.pages.base_page import BasePage


class LoginPage(BasePage):
    USER_NAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)

    def success_login(self, username, password):
        self.type_text(self.USER_NAME_FIELD, username)
        self.type_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

