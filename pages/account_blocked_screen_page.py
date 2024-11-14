"""
Blocked account screen.
"""
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from pages.base_page import BasePage
from pages.home_screen_page import HomeScreenPage


class AccountBlockedScreenPage(BasePage):
    """
    Contains locators & functionalities for blocked screen.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home_screen = HomeScreenPage(self.driver)

    ACCOUNT_BLOCKED_ERROR = \
        (AppiumBy.ACCESSIBILITY_ID,
         'You’ve exceeded the maximum number of login attempts. To unlock your account, please reset your password.')
    RESET_PASSWORD_BUTTON = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Reset Password"`]')
    HAVING_DIFFICULTIES_BUTTON = (AppiumBy.IOS_CLASS_CHAIN,
                                  '**/XCUIElementTypeStaticText[`label == "Having difficulties?"`]')
    BACK_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton')
    AUGMEDIX_LOGO =(AppiumBy.ACCESSIBILITY_ID, 'AugmedixLogo')

    def block_account(self, email, wrong_password):
        self.home_screen.handle_face_id_modal()
        # Do log in with wrong password 4 times to block the account
        try:
            for _ in range(4):
                self.enter_text_at(self.home_screen.EMAIL_FIELD, email, 10)
                self.click_and_wait(self.home_screen.LOGIN_BUTTON, 3)
                self.enter_text_at(self.home_screen.PASSWORD_FIELD, wrong_password, 10)
                self.click_and_wait(self.home_screen.KEYBOARD_DONE_BUTTON, 1)
                self.click_and_wait(self.home_screen.LOGIN_BUTTON, 3)
        except (TimeoutException, NoSuchElementException):
            print('Account already blocked')
