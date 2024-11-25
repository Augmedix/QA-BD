"""
Locators & functionalities for Transcript Screen.
"""
import time
from data.data import Data

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

from data.data import Data
from pages.api_pages.transcript_api_page import TranscriptApiPage
from pages.appointment_screen_page import AppointmentScreenPage
from pages.base_page import BasePage
from pages.home_screen_page import HomeScreenPage


class SettingsPage(BasePage):
    """
    Locators & functionalities for Transcript Screen.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home_screen = HomeScreenPage(self.driver)
        self.appointment_screen = AppointmentScreenPage(self.driver)

    SETTINGS_NAVIGATION_BAR = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar[@name="Settings"]')
    SETTINGS_PAGE_TITLE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Settings"]')
    BACK_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Back"]')
    BACK_BUTTON_ARROW = (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="smallBackIcon"]')
    BACK_BUTTON_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Back"]')
    PREFERENCES_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Preferences"]')
    PREFERENCES_BUTTON_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Preferences"]')
    PREFERENCES_BUTTON_ARROW = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Preferences"]/XCUIElementTypeImage')
    PREFERENCES_NAVIGATION_BAR = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar[@name="Preferences"]')
    PREFERENCES_BACK_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Settings"]')

    def navigate_to_the_settings_screen(self):
        if self.is_element_visible(self.SETTINGS_NAVIGATION_BAR, 1):
            print("User is on the settings page")
        elif self.is_element_visible(self.PREFERENCES_NAVIGATION_BAR, 1):
            print("User is on the preference screen")
            self.click_and_wait(self.PREFERENCES_BACK_BUTTON, 1)
        elif self.is_element_visible(self.appointment_screen.HAMBURGER_MENU, 4):
            print("User is in appointment screen")
            self.appointment_screen.click_and_wait(self.appointment_screen.HAMBURGER_MENU, 1)
            print("Clicked on the menu button")
            if self.is_element_visible(self.appointment_screen.SETTINGS_BUTTON, 4):
                print("Menu section is open")
                self.click_and_wait(self.appointment_screen.SETTINGS_BUTTON, 1)
                print("Clicked on the settings button")


