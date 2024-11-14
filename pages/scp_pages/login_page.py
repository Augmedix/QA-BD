"""
Locators & methods for Login page.
"""
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.scp_pages.home_page import HomePage
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):
    """
    Locators & methods for Login page.
    """
    EMAIL_ADDRESS = (By.ID, 'ajs-login-email')
    PASSWORD = (By.ID, 'ajs-login-password')
    LOGIN_BTN = (By.ID, 'ajs-login-submit-btn')

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
            self.driver.get(pytest.url)
            print("URL: ", self.driver.get(pytest.url))
            self.wait_for_visibility_of(self.LOGIN_BTN)
            time.sleep(3)

    def is_logged_in(self, wait: bool = False):
        return self.get_total_count(self.LOGIN_BTN, wait) == 0

    def submit_login_data(self, username, password, invalid_login=False):
        HomePage(self.driver).wait_for_loader(max_wait_time_for_visibility=2)
        self.enter_text_at(self.EMAIL_ADDRESS, username, 1)
        self.enter_text_at(self.PASSWORD, password, 1)
        self.click_and_wait(self.LOGIN_BTN)
        if invalid_login:
            self.wait_for_visibility_of(self.ALL_INVALID_LOGIN_ERROR_LOCATOR)

    def login_to_scp(self, username, password=pytest.configs.get_config('scribe_password'), invalid_login=False,
                     wait_for_login_page:bool = True, handle_alert:bool = False):
        home_page = HomePage(self.driver)
        if handle_alert:
            home_page.handle_alert(10)
        if self.is_logged_in(wait_for_login_page):
            print('User is already logged in...')
        else:
            self.submit_login_data(username, password, invalid_login)
            if not invalid_login:
                self.wait_for_visibility_of(home_page.SIGNOUT_LINK, max_wait=10)

            home_page.wait_for_loader()
            print('Scribe is logged in...')