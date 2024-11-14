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
from utils.json_data_handler import JsonDataHandler
from utils.upload_go_audio.upload_audio import upload_audio_to_go_note


class TranscriptsScreenPage(BasePage):
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

    BACK_SCHEDULE_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Schedule"]')
    TRACKER_BACK_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Tracker"]')
    PROBLEMS_TAB = (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="problemTabIconNew"]/parent::XCUIElementTypeButton')
    TRANSCRIPTS_TAB = (AppiumBy.XPATH,
                       '//XCUIElementTypeImage[@name="transcriptTabIcon"]/parent::XCUIElementTypeButton')
    NOTE_TAB = (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="transcriptTabIcon"]/parent::XCUIElementTypeButton/following-sibling::XCUIElementTypeButton')
    PATIENT_NAME = (AppiumBy.XPATH, '(//XCUIElementTypeStaticText)[2]')
    RECORDING_CAROUSEl = (AppiumBy.XPATH, '//XCUIElementTypeCollectionView')
    AUDIO_FILES = (AppiumBy.XPATH, '//XCUIElementTypeCollectionView //XCUIElementTypeStaticText')
    FIRST_AUDIO_FILE = (AppiumBy.NAME, '1_12:27')
    LAST_AUDIO_FILE = (AppiumBy.NAME, '5_01:19')

    # Search
    SEARCH_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeOther /XCUIElementTypeButton[1]')
    SEARCH_BAR = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="previousButton"]/parent::XCUIElementTypeOther')
    SEARCH_TEXT_INPUT_FIELD = \
        (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="previousButton"] /preceding-sibling::XCUIElementTypeTextField')
    SEARCH_RESULT_POSITION_AND_FOUND = \
        (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="previousButton"]/preceding-sibling::XCUIElementTypeStaticText')
    SEARCH_RESULT_PREVIOUS_BUTTON = (AppiumBy.NAME, 'previousButton')
    SEARCH_RESULT_NEXT_BUTTON = (AppiumBy.NAME, 'nextButton')
    KEYBOARD_DONE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Done')
    SEARCH_RESULT_IN_TRANSCRIPT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"metformin")]')

    TRANSCRIPT_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeCell /XCUIElementTypeStaticText[last()]')
    TRANSCRIPT_SECTION = (AppiumBy.XPATH, '//XCUIElementTypeTable')
    TRANSCRIPT_PROCESSING = (AppiumBy.ACCESSIBILITY_ID, 'Recording is processing...')
    LOADING_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Loading..."]')
    PROCESSING_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Processing..."]')

    # Recording
    RECORDING_START_BUTTON = (AppiumBy.NAME, 'recordingStartIconBlue')
    RECORDING_STOP_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[contains(@name,"recordingStopIcon")]')
    RECORDING_TIMER = \
        (AppiumBy.XPATH,
         '//XCUIElementTypeButton[contains(@name,"recordingStopIcon")] /preceding-sibling::XCUIElementTypeTextView')

    ACCESS_MICROPHONE_REQUEST_MESSAGE = \
        (AppiumBy.XPATH,
         '//XCUIElementTypeStaticText[@name="This app requires your permission to record'
         ' from microphone to transcribe your voice notes."]')
    ACCESS_MICROPHONE_REQUEST_PERMISSION_BUTTON = (
        AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Request Permission"]')
    ACCESS_MICROPHONE_REQUEST_SKIP_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Skip"]')

    ACCESS_MICROPHONE_ALERT_TITLE = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "Access the Microphone")]')
    ACCESS_MICROPHONE_ALERT_MESSAGE = \
        (AppiumBy.XPATH,
         '//XCUIElementTypeStaticText[contains(@name, "Access the Microphone")]'
         ' /following-sibling::XCUIElementTypeStaticText')
    ACCESS_MICROPHONE_OK_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="OK"]')
    ACCESS_MICROPHONE_DO_NOT_ALLOW_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Don’t Allow"]')

    ADD_MULTIPLE_RECORDING_ALERT_TITLE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Add a new recording?"]')
    ADD_MULTIPLE_RECORDING_ALERT_MESSAGE = \
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Recording again will remove the note generated'
                         ' and any edits you have made. Are you sure you want to proceed?"]')
    ADD_MULTIPLE_RECORDING_ALERT_RECORD_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Record"]')
    ADD_MULTIPLE_RECORDING_ALERT_CANCEL_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Cancel"]')
    TRANSCRIPT_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().TRANSCRIPT_PATIENT1_NAME)
    TRANSCRIPT_PATIENT2_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().TRANSCRIPT_PATIENT2_NAME)
    NO_TRANSCRIPTS_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, 'No Transcripts')
    FIRST_LINE_TRANSCRIPT = (AppiumBy.ACCESSIBILITY_ID, 'Hey. How are you doing?')
    LAST_LINE_TRANSCRIPT = (AppiumBy.ACCESSIBILITY_ID, 'Thank you.')
    DELETE_RECORDING_MODAL = (AppiumBy.ACCESSIBILITY_ID, 'Delete Recording?')
    DELETE_RECORDING_MODAL_TEXT = (AppiumBy.ACCESSIBILITY_ID, 'Recording audio and content will be permanently deleted for the selected transcript.')
    DELETE_RECORDING_MODAL_CANCEL_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Cancel"]')
    DELETE_RECORDING_MODAL_DELETE_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Delete"]')
    DELETING_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Deleting..."]')
    DELETE_X_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeCollectionView //XCUIElementTypeButton')


    def get_locator_for_delete_button(self, file_length_text):
        return (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name, "{file_length_text}")]/ancestor::XCUIElementTypeOther[2] //XCUIElementTypeButton')

    def get_locator_for_recording_file(self, file_length_text):
        return (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name, "{file_length_text}")]')

    def select_audio(self, file_length_text):
        self.wait_and_click(self.get_locator_for_recording_file(file_length_text))

    def get_patient_name_and_note_id_after_navigating_to_transcripts_screen(self, username, password):
        self.home_screen.login_with_password(username, password)
        self.appointment_screen.crete_non_ehr_appointments(Data().TRANSCRIPT_PATIENT_NAME)
        self.click_and_wait(self.appointment_screen.TRANSCRIPT_PATIENT_NAME, 6)
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        note_id = self.get_note_id()
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        return Data().TRANSCRIPT_PATIENT_NAME, note_id

    def get_note_id(self):
        self.click_and_wait(self.NOTE_TAB, 4)
        note_id = self.note_screen.get_text_by_locator(self.note_screen.NOTE_ID)
        self.note_screen.click_and_wait(self.note_screen.TRANSCRIPTS_TAB)
        return note_id

    def logout_and_return_back_to_transcript_page(self, username, password):
        self.click_and_wait(self.TRACKER_BACK_BUTTON)
        self.home_screen.logout_from_app()
        self.home_screen.login_with_password(username, password)
        self.click_and_wait(self.appointment_screen.TRANSCRIPT_PATIENT_NAME, 6)

    def return_back_to_tracker(self):
        if self.is_element_visible(self.TRACKER_BACK_BUTTON, 4):
            self.click_and_wait(self.TRACKER_BACK_BUTTON)


    def current_search_position(self):
        result_text = self.get_text_by_locator(self.SEARCH_RESULT_POSITION_AND_FOUND)
        text_list = result_text.split('/')
        return int(text_list[0])

    def is_ml_highlight_data_in_transcript(self, texts, ml_keyword):
        for text in texts:
            if ml_keyword in text:
                print(f'"{ml_keyword}" is present in "{text}"')
                return True
        return False

    def get_expected_ml_highlight_words(self):
        conversations = JsonDataHandler('transcript_response').get_key_value('conversations')
        ml_highlight_transcript = []
        for data in conversations:
            if data['metadata']['highlight']:
                ml_highlight_transcript.extend(data['metadata']['highlight'])
        return ml_highlight_transcript

    def get_expected_transcripts(self, transcript_name:str):
        conversations = JsonDataHandler(transcript_name).get_key_value('conversations')
        transcripts = []
        for data in conversations:
            transcripts.append(data['words'])
        return transcripts

    def wait_for_transcript(self):
        self.wait_and_click(self.TRANSCRIPTS_TAB)
        max_try = 0
        while not self.is_element_visible(self.TRANSCRIPT_TEXT) and max_try < 5:
            max_try += 1
            time.sleep(60)
            self.click_and_wait(self.NOTE_TAB)
            time.sleep(15)
            self.click_and_wait(self.TRANSCRIPTS_TAB)

    def start_recording(self):
        self.wait_and_click(self.RECORDING_START_BUTTON)
        self.handle_microphone_permission()
        self.handle_multiple_recording_modal()

    def perform_recording(self, duration=15):
        self.start_recording()
        time.sleep(duration)
        self.click_and_wait(self.RECORDING_STOP_BUTTON)

    def upload_audio(self, username, password, note_id,
                      file_path='utils/upload_go_audio/Visit8-v6_20221212.mp4', precessing_time=180, token = False):
        upload_audio_to_go_note(username=username, password=password, note_id=note_id, file_path=file_path, auth_token=token)
        # try:
        #     self.wait_for_visibility_of(self.TRANSCRIPT_TEXT, precessing_time)
        # except TimeoutException:
        #     self.click_and_wait(self.PROBLEMS_TAB)
        #     self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        #     self.wait_and_click(self.TRANSCRIPTS_TAB)
        #     self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)

    def handle_microphone_permission(self):
        if self.is_element_visible(self.ACCESS_MICROPHONE_REQUEST_MESSAGE, 1):
            self.click_and_wait(self.ACCESS_MICROPHONE_REQUEST_PERMISSION_BUTTON)
        else:
            print('Microphone permission request modal is not visible')

        if self.is_element_visible(self.ACCESS_MICROPHONE_ALERT_TITLE, 2):
            self.click_and_wait(self.ACCESS_MICROPHONE_OK_BUTTON)
        else:
            print('No microphone access popup modal')

    def handle_multiple_recording_modal(self):
        if self.is_element_visible(self.ADD_MULTIPLE_RECORDING_ALERT_TITLE, 1):
            self.click_and_wait(self.ADD_MULTIPLE_RECORDING_ALERT_RECORD_BUTTON)
        else:
            print('No multiple recording alert modal is visible')

    def upload_and_wait_for_transcript_if_not_available(self, email, password, note_id, file_path='utils/upload_go_audio/Visit8-v6_20221212.mp3'):
        if self.is_element_visible(self.NO_TRANSCRIPTS_MESSAGE, 5):
            self.transcript_api_page.upload_an_audio_file_and_get_transcription(
                token=False, headers=False, email=email, password=password, note_id=note_id,
                file_path= file_path)
            self.wait_for_transcript()

        else:
            print("Transcript is available")

    def upload_audio_file(self, email, password, note_id, file_path='utils/upload_go_audio/Visit8-v6_20221212.mp3'):
        current_count = self.get_available_transcript_count()
        self.transcript_api_page.upload_an_audio_file_and_get_transcription(
            token=False, headers=False, email=email, password=password, note_id=note_id,
            file_path=file_path)

        max_try = 0
        while self.get_total_count(self.AUDIO_FILES) == current_count and max_try < 5:
            max_try += 1
            self.click_and_wait(self.NOTE_TAB, 5)
            self.click_and_wait(self.TRANSCRIPTS_TAB, 5)
            try:
                self.wait_for_element_count_to_be(self.AUDIO_FILES, current_count+1, 15)
            except TimeoutException:
                print('New Transcript is not available' )

    def get_available_transcript_count(self):
        if self.is_element_visible(self.AUDIO_FILES, 1):
            return self.get_total_count(self.AUDIO_FILES)
        else:
            print("No Recording is available")
            return 0

    def delete_transcript(self):
        self.click_and_wait(self.DELETE_X_BUTTON, 2)
        self.click_and_wait(self.DELETE_RECORDING_MODAL_DELETE_BUTTON, 5)
        print("Deleted a Transcript")

    def wait_for_required_number_of_transcript_to_be_available_on_transcript_screen(self, email, password, note_id,
                                                                                    transcript_count,
                                                                                    files=Data().AUDIO_FILES):
        self.click_and_wait(self.TRANSCRIPTS_TAB, 3)
        current_count = self.get_available_transcript_count()
        if current_count == transcript_count:
            print(f'{current_count} number transcript is available')
        elif current_count > transcript_count:
            while current_count != transcript_count:
                self.delete_transcript()
                current_count = self.get_available_transcript_count()
        else:
            while current_count < transcript_count:
                self.transcript_api_page.upload_an_audio_file_and_get_transcription(
                    token=False, headers=False, email=email, password=password, note_id=note_id,
                    file_path=files[current_count])
                self.click_and_wait(self.NOTE_TAB, 5)
                self.click_and_wait(self.TRANSCRIPTS_TAB, 6)
                current_count = self.get_available_transcript_count()



