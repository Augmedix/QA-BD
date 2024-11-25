"""
Locators & functionalities for Problem Screen.
"""
import time

from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage
from pages.home_screen_page import HomeScreenPage
from pages.support_screen_page import SupportScreenPage
from data.data import Data

data = Data()

class ResetPasswordScreenPage(BasePage):
    """
    Locators & functionalities for Problem Screen.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home_screen_page = HomeScreenPage(self.driver)
        self.support_screen_page = SupportScreenPage(self.driver)


    INSTRUCTION = (AppiumBy.ACCESSIBILITY_ID, 'Enter your email. We’ll send you a link to reset your password.')
    INSTRUCTION_TEXT = (AppiumBy.ACCESSIBILITY_ID, 'Enter your email. We’ll send you a link to reset your password.')
    SUPPORT_NUMBER_TEXT = (AppiumBy.ACCESSIBILITY_ID, 'Support Number')
    SEND_RESET_LINK_TO_EMAIL_BTN = (AppiumBy.IOS_CLASS_CHAIN,
                                    '**/XCUIElementTypeStaticText[`label == "Send Reset Link To Email "`]')
    HAVING_DIFFICULTIES_BUTTON = (AppiumBy.IOS_CLASS_CHAIN,
                                  '**/XCUIElementTypeStaticText[`label == "Having difficulties?"`]')
    SENDING_MODAL = (AppiumBy.ACCESSIBILITY_ID, 'Sending...')
    RESET_LINK_SENT_SUCCESS_MSG = (AppiumBy.ACCESSIBILITY_ID,
                                   'Password reset instructions have been sent to your email. Please follow the instruction then return to login.')
    # RESET_LINK_SENT_SUCCESS_MSG = \
    #     (AppiumBy.IOS_CLASS_CHAIN,
    #      '**/XCUIElementTypeStaticText[`label'
    #      ' == "Password reset instructions have been sent to your email.'
    #      ' Please follow the instruction then return to login."`]')
    RESET_LINK_SENT_SUCCESS_SYMBOL = (AppiumBy.ACCESSIBILITY_ID, 'resetPasswordEmailSent')
    LOGIN_BTN = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Log In"`]')
    RESENDING_BTN = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Try resending it."`]')
    BACK_BTN = (AppiumBy.XPATH,'//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[1]')
    # BACK_BTN = \
    #     (AppiumBy.IOS_CLASS_CHAIN,
    #      '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther'
    #      '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[1]')

    def navigate_to_reset_password_screen(self):
        self.home_screen_page.handle_face_id_modal()
        # Hide the done
        if self.is_element_visible(self.home_screen_page.KEYBOARD_DONE_BUTTON, 2):
            self.home_screen_page.click_and_wait(self.home_screen_page.KEYBOARD_DONE_BUTTON, 1)
        self.support_screen_page.navigate_to_support_screen_from_home_screen()
        self.support_screen_page.click_and_wait(self.support_screen_page.RESET_PASSWORD_BUTTON, 1)

    def send_password_request_email_from_app(self):
        self.reset_password_screen_page = ResetPasswordScreenPage(self.driver)
        self.navigate_to_reset_password_screen()
        self.enter_text_at(self.home_screen_page.EMAIL_FIELD, data.password_reset_provider,
                                            3)
        # Hide the done button to click on send reset link button
        self.click_and_wait(self.home_screen_page.KEYBOARD_DONE_BUTTON, 1)
        self.reset_password_screen_page.wait_and_click(self.reset_password_screen_page.SEND_RESET_LINK_TO_EMAIL_BTN,
                                                       3)
        self.reset_password_screen_page.wait_for_visibility_of(
            self.reset_password_screen_page.RESET_LINK_SENT_SUCCESS_MSG, 5)
        time.sleep(30)
        print('Reset password request sent from app!')

