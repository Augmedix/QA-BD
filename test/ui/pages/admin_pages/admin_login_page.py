"""
Locators & methods for Login page.
"""
import time

import pytest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.admin_pages.admin_home_page import AdminHomePage


class LoginPage(BasePage):
    """
    Locators & methods for Login page.
    """
    EMAIL_ADDRESS = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    LOGIN_BTN = (By.XPATH, '//button[text()="Log In"]')

    RESET_PASSWORD_LINK_LOCATOR = (By.CLASS_NAME, 'login__block__reset__pass')

    REQUIRED_EMAIL_ERROR_LOCATOR = (By.ID, 'ajs-login-error-email-required')
    INVALID_EMAIL_ERROR_LOCATOR = (By.ID, 'ajs-login-error-email-invalid')
    EMPTY_PASSWORD_ERROR_LOCATOR = (By.ID, 'ajs-login-password-empty')
    INVALID_LOGIN_ERROR_LOCATOR = (By.CSS_SELECTOR, '.alert.alert-danger')
    ALL_INVALID_LOGIN_ERROR_LOCATOR = (
        By.CSS_SELECTOR,
        '#ajs-login-error-email-required,'
        '#ajs-login-error-email-invalid, #ajs-login-password-empty, '
        '.alert.alert-danger'
    )

    REQUIRED_EMAIL_ERROR_MSG = 'Email address is required'
    INVALID_EMAIL_ERROR_MSG = 'Email address must be a valid email address'
    EMPTY_PASSWORD_ERROR_MSG = 'Password field is empty'
    INVALID_LOGIN_MSG = 'Sorry, your username or password is incorrect. Please try again.'
    LOCKED_ERROR_MSG = 'Account is currently blocked'
    SESSION_EXPIRATION_MSG = 'Session has expired. Please login again.'

    def goto_login_page(self):
        if self.get_total_count(self.LOGIN_BTN) == 0:
            self.driver.get(pytest.admin_url)
            self.wait_for_visibility_of(self.LOGIN_BTN)
            time.sleep(3)

    def is_logged_in(self):
        return self.get_total_count(self.LOGIN_BTN) == 0

    def submit_login_data(self, username, password):
        # HomePage(self.driver).wait_for_loader(max_wait_time_for_visibility=2)
        self.enter_text_at(self.EMAIL_ADDRESS, username)
        self.enter_text_at(self.PASSWORD, password)
        self.click_and_wait(self.LOGIN_BTN)

    def login_to_admin_portal(self, username=pytest.configs.get_config('admin_user'),
                             password=pytest.configs.get_config('admin_password')):
        if self.is_logged_in():
            print('User is already logged in...')
        else:
            self.submit_login_data(username, password)
            # HomePage(self.driver).wait_for_loader()
            print('Admin is logged in...')