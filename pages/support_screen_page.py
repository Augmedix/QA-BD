"""
Locators & functionalities for Support Screen.
"""
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage
from pages.home_screen_page import HomeScreenPage


class SupportScreenPage(BasePage):
    """
    Locators & functionalities for Support Screen.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home_screen_page = HomeScreenPage(self.driver)

    SUPPORT_SCREEN_TITLE = (AppiumBy.ACCESSIBILITY_ID, 'Support')
    SUPPORT_NUMBER_TEXT = (AppiumBy.ACCESSIBILITY_ID, 'Support Number')
    SUPPORT_NUMBER = (AppiumBy.ACCESSIBILITY_ID, '(888) 304-0450')
    RESET_PASSWORD_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@value="Reset Password"]')
    RESET_PIN_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@value="Reset Pin"]')
    WIFI_SETTINGS_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Wifi Settings"]')
    RESET_APP_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Reset App"]')
    DEVICE_ID = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@value,"Device ID:")]')
    APP_VERSION = (AppiumBy.XPATH, "//XCUIElementTypeStaticText[contains(@value, 'App Version:')]")
    NATIVE_WIFI_SETTING_SCREEN = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar[@name="Settings"]')
    SUPPORT_BACK_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton')

    def navigate_to_support_screen_from_home_screen(self):
        if self.is_element_visible(self.home_screen_page.KEYBOARD_DONE_BUTTON, 2):
            self.home_screen_page.click_and_wait(self.home_screen_page.KEYBOARD_DONE_BUTTON, 1)
        self.wait_for_visibility_of(HomeScreenPage.HAVING_DIFFICULTIES_BUTTON, 3)
        self.click_and_wait(HomeScreenPage.HAVING_DIFFICULTIES_BUTTON, 1)
        self.is_element_visible(self.SUPPORT_SCREEN_TITLE, 3)

    def common_support_screen_assertions(self):
        assert self.home_screen_page.is_element_visible(self.SUPPORT_SCREEN_TITLE, 5)
        assert self.home_screen_page.is_element_visible(self.SUPPORT_NUMBER_TEXT, 1)
        assert self.home_screen_page.is_element_visible(self.SUPPORT_NUMBER, 1)
        assert self.home_screen_page.is_element_visible(self.RESET_PASSWORD_BUTTON, 1)
        assert self.home_screen_page.is_element_visible(self.DEVICE_ID, 1)
        assert self.home_screen_page.is_element_visible(self.APP_VERSION, 1)
        assert self.home_screen_page.is_element_visible(self.SUPPORT_BACK_BUTTON, 1)
