"""
Locators & functionalities for Note Screen.
"""
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

from pages.appointment_screen_page import AppointmentScreenPage
from pages.base_page import BasePage
from pages.home_screen_page import HomeScreenPage
from pages.problems_screen_page import ProblemsScreenPage


class NoteScreenPage(BasePage):
    """
    Locators & functionalities for Note Screen.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home_screen = HomeScreenPage(self.driver)
        self.appointment_screen = AppointmentScreenPage(self.driver)
        self.problems_screen = ProblemsScreenPage(self.driver)

    BACK_SCHEDULE_BUTTON = (AppiumBy.XPATH, '//*[@name="Tracker" and @type="XCUIElementTypeButton"]')
    PROBLEMS_TAB = (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="problemTabIconNew"]/parent::XCUIElementTypeButton')
    TRANSCRIPTS_TAB = (AppiumBy.XPATH,
                       '//XCUIElementTypeImage[@name="transcriptTabIcon"]/parent::XCUIElementTypeButton')
    TEST_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,'Test Note')
    NOTE_TAB = (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="noteTabIcon"]/parent::XCUIElementTypeButton')
    NOTE_ID = (AppiumBy.XPATH, '//XCUIElementTypeCell /XCUIElementTypeButton')
    PATIENT_NAME = (AppiumBy.XPATH,
                    '//XCUIElementTypeButton[@name="Schedule"] /following-sibling::XCUIElementTypeStaticText')
    SEND_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Tracker"]/preceding-sibling::XCUIElementTypeOther//XCUIElementTypeButton')
    AI_GENERATED_DISCLAIMER = (AppiumBy.XPATH,
                               '//XCUIElementTypeStaticText[contains(@name,"AI-generated note, updated")]')
    NOTE_UPLOAD_EHR_ICON = (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="noteUploadedToEhr"]')
    NOTE_PROCESSING_ICON = (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="spinner_static"]')
    NOTE_UPLOAD_ICON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Tracker"]/preceding-sibling::XCUIElementTypeOther//XCUIElementTypeImage')

    NOTE_UPLOADING_MODUL_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Uploading Notes .. "]')
    ADD_RE_EVAL_BUTTON = (AppiumBy.IOS_CLASS_CHAIN,'**/XCUIElementTypeButton[`label == "+ Add Re-eval"`]')
    NOTE_TEXT = (AppiumBy.XPATH,'//*[@type="XCUIElementTypeTable"]/*[16]/*[@type="XCUIElementTypeTextView"]')
    HPI_HEADER = (AppiumBy.NAME, 'HPI')
    AP_HEADER = (AppiumBy.NAME, 'A/P')
    PE_HEADER = (AppiumBy.NAME, 'PE')
    ROS_HEADER = (AppiumBy.NAME, 'ROS')
    PATIENT_INFO = (AppiumBy.XPATH,
                    '//XCUIElementTypeStaticText[@name="HPI"] /following-sibling::XCUIElementTypeStaticText')
    NOTE_UPLOAD_STATUS_MESSAGE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"upload")]')
    OK_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Ok"]')
    LOADING_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Loading..."]')
    KEYBOARD_DOWN = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="keyboardDown"]')
    SAVING_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Saving..."]')

    def hpi_problem_locator(self, problem_name):
        return AppiumBy.XPATH, f'(//XCUIElementTypeStaticText[@name="{problem_name}"])[1]'

    def ap_problem_locator(self, problem_name):
        return AppiumBy.XPATH, f'(//XCUIElementTypeStaticText[@name="{problem_name}"])[2]'

    def note_locator(self, name):
        return AppiumBy.XPATH, f'//XCUIElementTypeTextView[contains(@value,"{name}")]'

    def navigate_to_note_screen_from_home_screen(self, username, password):
        self.home_screen.login_with_password(username, password)
        self.wait_for_visibility_and_invisibility_of(self.home_screen.LOGGING_IN_TEXT)
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        patient_name = 'Test Note'
        self.appointment_screen.crete_non_ehr_appointments(patient_name)
        
        self.wait_and_click(self.TEST_PATIENT_NAME, 3)
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        self.problems_screen.click_and_wait(self.problems_screen.NOTE_TAB)
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        return patient_name

    def is_note_generate(self, expected_note):
        status = False
        time.sleep(3)
        self.wait_and_click(self.NOTE_TAB)
        try:
            self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
            self.wait_for_visibility_of(self.note_locator(expected_note), 2)
        except TimeoutException:
            self.wait_and_click(self.PROBLEMS_TAB)
            self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
            self.wait_and_click(self.NOTE_TAB)
            self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        if self.is_element_visible(self.note_locator(expected_note), 1):
            if self.get_text_by_locator(self.note_locator(expected_note)) == expected_note:
                status = True
        self.wait_and_click(self.PROBLEMS_TAB)
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        return status

    def is_send_button_clickable(self, max_wait=120):
        try:
            self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
            self.wait_for_element_to_clickable(self.SEND_BUTTON, max_wait=max_wait)
        except TimeoutException:
            self.wait_and_click(self.TRANSCRIPTS_TAB)
            self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
            self.wait_and_click(self.NOTE_TAB)
            self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
            self.wait_for_element_to_clickable(self.SEND_BUTTON, max_wait=max_wait)

    def add_note_on_empty_state(self):
        self.wait_and_click(self.ADD_RE_EVAL_BUTTON, 3)
        self.enter_text_at(self.NOTE_TEXT, 'Test patient note added', 1)
        self.click_and_wait(self.KEYBOARD_DOWN)
        self.wait_for_visibility_and_invisibility_of(self.SAVING_MODAL)

    def get_manually_updated_ml_generated_note_content(self, manual_text):
        self.wait_for_visibility_of(self.AI_GENERATED_DISCLAIMER)
        self.wait_and_click(self.NOTE_TEXT)
        self.get_element(self.NOTE_TEXT).send_keys(manual_text)
        self.click_and_wait(self.KEYBOARD_DOWN)
        self.wait_for_visibility_and_invisibility_of(self.SAVING_MODAL)
        updated_text = self.get_attribute(self.NOTE_TEXT, 'value')
        return updated_text

    def perform_note_upload(self):
        self.click_and_wait(self.NOTE_TAB)
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        if not self.is_clickable(self.SEND_BUTTON):
            self.add_note_on_empty_state()
        self.wait_and_click(self.SEND_BUTTON)
        try:
            if self.is_element_visible(self.NOTE_UPLOAD_STATUS_MESSAGE, 12):
                self.wait_and_click(self.OK_BUTTON, 1)
        except TimeoutException:
            print('Note send failed')

    def review_note_content(self):
        self.click_and_wait(self.NOTE_TAB)
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        if not self.is_clickable(self.SEND_BUTTON):
            self.add_note_on_empty_state()
