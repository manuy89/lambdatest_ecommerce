from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):

    email_address_field = (By.XPATH, '//input[@id="input-email"]')
    password_field = (By.XPATH, '//input[@id="input-password"]')
    login_button = (By.XPATH, '//input[@value="Login"]')
    forgot_password = (By.LINK_TEXT, 'Forgotten Password')
    warning_message = (By. CSS_SELECTOR, '#account-login .alert')

    def __init__(self, driver):
        super().__init__(driver)

    def set_email(self, email):
        self.set_value(self.email_address_field, email)

    def set_password(self, password):
        self.set_value(self.password_field, password)

    def click_login_button(self):
        self.click(self.login_button)

    def click_forgot_password(self):
        self.click(self.forgot_password)

    def get_warning_mesage(self):
        return self.get_text(self.warning_message)
    
    def log_into_application(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()
        