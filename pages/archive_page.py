import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from data.data import Data
from pages.base_page import BasePage
from pages.basic_behavior_page import BasicBehaviorPage
from pages.transcripts_screen_page import TranscriptsScreenPage
from pages.basic_behavior_page import BasicBehaviorPage
from pages.scp_pages.home_page import HomePage
from pages.scp_pages.note_builder.organize_tab import OrganizeTab
from utils.upload_go_audio.upload_audio import upload_audio_to_go_note


class Archive_Page(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.data = Data()

    ARCHIVE_APPOINTMENT_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'crossIcon')
    TRACKER_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().TRACKER_ARCHIVE_PATIENT_NAME)
    TODO_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().TODO_ARCHIVE_PATIENT_NAME)
    NOTE_STATUS_ONE_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().NOTE_STATUS_1_PATIENT_NAME)
    NOTE_STATUS_FOUR_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().NOTE_STATUS_4_PATIENT_NAME)
    NOTE_STATUS_NINE_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().NOTE_STATUS_9_PATIENT_NAME)
    ARCHIVING_MODAL = (AppiumBy.ACCESSIBILITY_ID,'Archiving...')
    CONNECTING_MODAL = (AppiumBy.ACCESSIBILITY_ID,'Connecting...')
    EMPTY_APPOINTMENT_LIST = (AppiumBy.ACCESSIBILITY_ID,'Empty list')
    RECORDING_START_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'recordingStartIconBlue')
    ADD_NEW_RECORDING_MODAL = (AppiumBy.ACCESSIBILITY_ID,'Add a new recording?')
    RECORD_BUTTON_MODAL = (AppiumBy.IOS_CLASS_CHAIN,'**/XCUIElementTypeButton[`label == "Record"`]')
    CANCEL_BUTTON_MODAL = (AppiumBy.IOS_CLASS_CHAIN,'**/XCUIElementTypeButton[`label == "Cancel"`]')
    RECORDING_STOP_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'recordingStopIconBlue')
    PROCESSING_MODAL = (AppiumBy.ACCESSIBILITY_ID,'Processing...')
    REQUEST_PERMISSION_MODAL = (AppiumBy.ACCESSIBILITY_ID,'This app requires your permission to record from microphone to transcribe your voice notes.')
    REQUEST_PERMISSION_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'Request Permission')
    MICROPHONE_ACCESS_MODAL = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[contains(@name, "Would Like to Access the Microphone")]')
    NOTE_UPLOAD_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'noteUploadedToEhr')

    def upload_audio_and_wait_for_transcript(self,note_id,file_path,username,password,
                                             transcript_header,wait_time_for_transcript=120):
        upload_audio_to_go_note(note_id, file_path, username, password)
        if not self.is_element_visible(transcript_header,wait_time_for_transcript):
            self.click_and_wait(BasicBehaviorPage.NOTE_TAB_BUTTON,1)
            self.click_and_wait(BasicBehaviorPage.TRANSCRIPT_TAB_BUTTON,1)
            self.wait_for_visibility_of(transcript_header,5)
        self.click_and_wait(transcript_header,1)
        self.wait_for_visibility_of(TranscriptsScreenPage.TRANSCRIPT_TEXT,10)

    def archive_appointment(self,patient_name_locator):
        self.wait_for_visibility_of(patient_name_locator, 40)
        self.wait_for_element_to_clickable(patient_name_locator,10)
        self.swipe_on_element(patient_name_locator,'left')
        self.click_and_wait(self.ARCHIVE_APPOINTMENT_BUTTON,1)

    def upload_note(self,patient_name_locator):
        # NOTE_UPLOAD_BUTTON_XPATH_STRING = (AppiumBy.XPATH,
        #                                    f'//*[@type="XCUIElementTypeImage" and ./preceding-sibling::*[@name="{patient_name}"]]')
        # self.wait_for_visibility_of(NOTE_UPLOAD_BUTTON_XPATH_STRING,100)
        self.basic_behavior_page = BasicBehaviorPage(self.driver)
        self.wait_for_element_to_clickable(self.basic_behavior_page.NOTE_UPLOAD_BUTTON,60)
        self.click_and_wait(self.basic_behavior_page.NOTE_UPLOAD_BUTTON,2)
        self.wait_for_visibility_of(patient_name_locator,10)
