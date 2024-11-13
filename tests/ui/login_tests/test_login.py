import time

import allure
import pytest

# from pages.forgot_password_page import ForgotPasswordPage
from ui.pages.home_page import HomePage
from ui.pages.login_page import LoginPage
# from pages.note_builder.organize_tab import OrganizeTab
from test_data.ui_data.test_input_data import user_input_data
from ui.base_test import BaseTest

data = user_input_data()

class TestLogin(BaseTest):
    """This module contains test Login sanity test cases"""

    def setup_class(self):
        """Inside setup suite appium driver initiate example"""

        self.login_page = LoginPage(self.driver)
        self.home_page = HomePage(self.driver)
        # self.forgot_password_page = ForgotPasswordPage(self.driver)
        # self.organize_tab = OrganizeTab(self.driver)

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.sanity
    def test_login_with_valid_username_and_password(self):
        self.login_page.login_to_scp(pytest.configs.get_config('login_scribe2'), pytest.configs.get_config('password'))
        with allure.step('Test user is logged in and redirected to login Dashboard page.'):
            assert self.login_page.get_text_by_locator(HomePage.DASHBOARD_MSG_LOCATOR) == HomePage.DASHBOARD_MSG

    @pytest.mark.sanity
    def test_logout_from_scribe_portal(self):
        self.home_page.click_and_wait(HomePage.SIGNOUT_LINK)
        with allure.step('After logout, Login Page should be displayed'):
            assert self.login_page.is_element_visible(LoginPage.LOGIN_BTN, 5)