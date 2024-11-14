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
from pages.note_screen_page import NoteScreenPage
from pages.problems_screen_page import ProblemsScreenPage
from pages.settings_page import SettingsPage
from utils.json_data_handler import JsonDataHandler
from utils.upload_go_audio.upload_audio import upload_audio_to_go_note


class PreferencesPage(BasePage):
    """
    Locators & functionalities for Transcript Screen.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home_screen = HomeScreenPage(self.driver)
        self.appointment_screen = AppointmentScreenPage(self.driver)
        self.problems_screen = ProblemsScreenPage(self.driver)
        self.note_screen = NoteScreenPage(self.driver)
        self.transcript_api_page = TranscriptApiPage()
        self.settings_page = SettingsPage(self.driver)

    PREFERENCES_NAVIGATION_BAR = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar[@name="Preferences"]')
    PREFERENCES_PAGE_TITLE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Preferences"]')
    BACK_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Settings"]')
    BACK_BUTTON_ARROW = (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="smallBackIcon"]')
    BACK_BUTTON_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Settings"]')
    HPI_SECTION_HEADER = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="HPI"]')
    HPI_SECTION_CHECKBOX = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="HPI"]'
                                            '/following-sibling::XCUIElementTypeSwitch[1]')

    HPI_SECTION_STYLE_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="HPI"]'
                                              '/following-sibling::XCUIElementTypeStaticText[@name="Style"][1]')
    HPI_SECTION_STYLE_TOGGLE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="HPI"]'
                                                '/following-sibling::XCUIElementTypeSegmentedControl[1]')
    HPI_SECTION_STYLE_CONCISE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="HPI"]'
                                                 '/following-sibling::XCUIElementTypeSegmentedControl[1]'
                                                 '/XCUIElementTypeButton[@name="Concise"]')
    HPI_SECTION_STYLE_NARRATIVE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="HPI"]'
                                                   '/following-sibling::XCUIElementTypeSegmentedControl[1]'
                                                   '/XCUIElementTypeButton[@name="Narrative"]')
    HPI_SECTION_STYLE_INSTRUCTION_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="HPI"]'
                                                            '/following-sibling::XCUIElementTypeButton[@name="i"][1]')

    INSTRUCTION_MODAL_TITLE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Sentence Style Example"]')
    INSTRUCTION_MODAL_CLOSE_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Close"]')
    INSTRUCTION_MODAL_FIRST_CONTENT_TITLE = (AppiumBy.XPATH, '//*[@name="Sentence Style Example"]'
                                                              '/following-sibling::XCUIElementTypeStaticText[1]')
    INSTRUCTION_MODAL_FIRST_CONTENT = (AppiumBy.XPATH, '//*[@name="Sentence Style Example"]'
                                                       '/following-sibling::XCUIElementTypeStaticText[2]')
    INSTRUCTION_MODAL_SECOND_CONTENT_TITLE = (AppiumBy.XPATH, '//*[@name="Sentence Style Example"]'
                                                               '/following-sibling::XCUIElementTypeStaticText[3]')
    INSTRUCTION_MODAL_SECOND_CONTENT = (AppiumBy.XPATH, '//*[@name="Sentence Style Example"]'
                                                        '/following-sibling::XCUIElementTypeStaticText[4]')

    ROS_SECTION_HEADER = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="ROS"]')
    ROS_SECTION_CHECKBOX = (AppiumBy.XPATH,
                            '//XCUIElementTypeStaticText[@name="ROS"]/following-sibling::XCUIElementTypeSwitch[1]')

    PE_SECTION_HEADER = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="PE"]')
    PE_SECTION_CHECKBOX = (AppiumBy.XPATH,
                           '//XCUIElementTypeStaticText[@name="PE"]/following-sibling::XCUIElementTypeSwitch[1]')

    MDM_SECTION_HEADER = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="MDM"]')
    MDM_SECTION_CHECKBOX = (AppiumBy.XPATH,
                            '//XCUIElementTypeStaticText[@name="MDM"]/following-sibling::XCUIElementTypeSwitch[1]')

    MDM_SECTION_STYLE_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="MDM"]'
                                              '/following-sibling::XCUIElementTypeStaticText[@name="Style"][1]')
    MDM_SECTION_STYLE_TOGGLE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="MDM"]'
                                                '/following-sibling::XCUIElementTypeSegmentedControl[1]')

    MDM_SECTION_STYLE_CONCISE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="MDM"]'
                                                 '/following-sibling::XCUIElementTypeSegmentedControl[1]'
                                                 '/XCUIElementTypeButton[@name="Concise"]')
    MDM_SECTION_STYLE_NARRATIVE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="MDM"]'
                                                   '/following-sibling::XCUIElementTypeSegmentedControl[1]'
                                                   '/XCUIElementTypeButton[@name="Narrative"]')
    MDM_SECTION_STYLE_INSTRUCTION_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="MDM"]'
                                                            '/following-sibling::XCUIElementTypeButton[@name="i"][1]')

    AP_SECTION_HEADER = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="A/P"]')
    AP_SECTION_CHECKBOX = (AppiumBy.XPATH,
                           '//XCUIElementTypeStaticText[@name="A/P"]/following-sibling::XCUIElementTypeSwitch[1]')

    AP_SECTION_STYLE_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="A/P"]'
                                             '/following-sibling::XCUIElementTypeStaticText[@name="Style"][1]')
    AP_SECTION_STYLE_TOGGLE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="AP"]'
                                               '/following-sibling::XCUIElementTypeSegmentedControl[1]')
    AP_SECTION_STYLE_CONCISE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="A/P"]'
                                                '/following-sibling::XCUIElementTypeSegmentedControl[1]'
                                                '/XCUIElementTypeButton[@name="Concise"]')
    AP_SECTION_STYLE_NARRATIVE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="A/P"]'
                                                  '/following-sibling::XCUIElementTypeSegmentedControl[1]'
                                                  '/XCUIElementTypeButton[@name="Narrative"]')
    AP_SECTION_STYLE_INSTRUCTION_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="A/P"]'
                                                           '/following-sibling::XCUIElementTypeButton[@name="i"][1]')

    INTERVAL_HISTORY_SECTION_HEADER = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Interval History"]')
    INTERVAL_HISTORY_SECTION_CHECKBOX = (AppiumBy.XPATH,
                                         '//XCUIElementTypeStaticText[@name="Interval History"]'
                                         '/following-sibling::XCUIElementTypeSwitch[1]')

    UPDATE_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Update"]')
    UPDATING_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Updating..."]')

    def navigate_to_the_preference_screen(self):
        if self.is_element_visible(self.PREFERENCES_NAVIGATION_BAR, 2):
            print("User is on the preference screen")
        else:
            self.settings_page.navigate_to_the_settings_screen()
            self.click_and_wait(self.settings_page.PREFERENCES_BUTTON, 3)
            print("Clicked on the Preference option")

    def navigate_to_the_appointment_screen(self):
        self.click_and_wait(self.BACK_BUTTON, 2)
        print("Clicked on the settings back button")
        if self.is_element_visible(self.settings_page.SETTINGS_NAVIGATION_BAR, 1):
            print("User is in settings screen")
            self.click_and_wait(self.settings_page.BACK_BUTTON, 2)
            print("Clicked on the back button")
        if self.is_element_visible(self.appointment_screen.HAMBURGER_MENU, 5):
            print("User is in appointment screen")

    def navigate_to_the_appointment_then_return_to_the_preference_screen(self):
        self.navigate_to_the_appointment_screen()
        self.navigate_to_the_preference_screen()

    def select_element(self, locator):
        if not self.is_element_selected(locator):
            self.click_and_wait(locator, 1)
            self.click_and_wait(self.UPDATE_BUTTON, 4)
        else:
            print("Already in selected state")

    def unselect_element(self, locator):
        if self.is_element_selected(locator):
            self.click_and_wait(locator, 1)
            self.click_and_wait(self.UPDATE_BUTTON, 4)
        else:
            print("Already in unselected state")