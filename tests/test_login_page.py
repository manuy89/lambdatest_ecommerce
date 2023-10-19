from pages.login_page import LoginPage
from utilities.test_data import LoginTestData
from tests.base_test import BaseTest

class TestLogin(BaseTest):

    def test_valid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.set_email(LoginTestData.email)
        login_page.set_password(LoginTestData.password)
        login_page.click_login_button()

        actual_title = login_page.get_title()

        assert actual_title == 'My Account'
