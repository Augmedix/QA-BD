"""
Locators & functionalities for Password Screen.
"""
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class PasswordExpiredScreenPage(BasePage):
    """
    Locators & functionalities for Password Screen.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    PASSWORD_EXPIRED_SCREEN_TITLE = \
        (AppiumBy.XPATH,
         '//XCUIElementTypeStaticText[@name="Your Password has expired. Please reset your password, and continue."]')
    RESET_PASSWORD_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Reset Password"]')
    HAVING_DIFFICULTIES_BUTTON = (AppiumBy.IOS_CLASS_CHAIN,
                                  '**/XCUIElementTypeStaticText[`label == "Having difficulties?"`]')
    BACK_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton')
    AUGMEDIX_LOGO =(AppiumBy.ACCESSIBILITY_ID, 'AugmedixLogo')

