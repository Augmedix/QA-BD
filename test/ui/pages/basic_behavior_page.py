import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from data.data import Data
from pages.base_page import BasePage
from pages.home_screen_page import HomeScreenPage
from pages.appointment_screen_page import AppointmentScreenPage
from pages.scp_pages.home_page import HomePage
from pages.scp_pages.note_builder.organize_tab import OrganizeTab
from pages.transcripts_screen_page import TranscriptsScreenPage
from utils.helper import generate_random_alphanumeric_string, get_date_time_by_zone, get_formatted_time_of_lamdatest_device
from utils.upload_go_audio.upload_audio import upload_audio_to_go_note


class BasicBehaviorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.data = Data()

    SHORT_AUDIO_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().SHORT_AUDIO_PATIENT_NAME)
    LONG_AUDIO_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().LONG_AUDIO_PATIENT_NAME)
    SCP_PATIENT_EDIT_REMOVE_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().SCP_PATIENT_EDIT_REMOVE_NAME)
    MDM_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().MDM_PATIENT_NAME)
    MDM_DISABLED_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().MDM_DISABLED_PATIENT_NAME)
    RE_EVAL_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().RE_EVAL_PATIENT_NAME)
    RE_EVAL_PATIENT_2_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().RE_EVAL_PATIENT_2_NAME)
    NO_EDIT_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().NO_EDIT_PATIENT_NAME)
    NO_EDIT_PATIENT_2_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().NO_EDIT_PATIENT_2_NAME)
    RE_EVAL_PATIENT_3_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().RE_EVAL_PATIENT_3_NAME)
    FIRST_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().FIRST_PATIENT_NAME)
    SECOND_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().SECOND_PATIENT_NAME)
    THIRD_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().THIRD_PATIENT_NAME)
    REMOVE_UPLOAD_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().REMOVE_UPLOAD_PATIENT_NAME)
    ADD_CONTENT_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().ADD_CONTENT_PATIENT_NAME)
    EHR_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().EHR_PATIENT_NAME)
    GO_ED_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().GO_ED_PATIENT_NAME)
    EHR_JENKINS_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().EHR_JENKINS_PATIENT_NAME)
    AGE_AND_SEX_LOCATOR = (AppiumBy.ACCESSIBILITY_ID,Data().AGE_AND_SEX)
    THREE_DIGIT_ROOM_NUMBER_LOCATOR = (AppiumBy.ACCESSIBILITY_ID,Data().THREE_DIGIT_ROOM_NUMBER)
    CHIEF_COMPLAINT_LOCATOR = (AppiumBy.ACCESSIBILITY_ID,Data().CHIEF_COMPLAINT)
    MULTIPLE_CHIEF_COMPLAINT_LOCATOR = (AppiumBy.ACCESSIBILITY_ID,Data().MULTIPLE_CHIEF_COMPLAINTS)
    # SHORT_PATIENT_EDIT_ADD_NAME = (AppiumBy.ACCESSIBILITY_ID,)
    NEW_NOTE_SIGN = (AppiumBy.XPATH,'//XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeButton[2]')
    LOADING_MODAL = (AppiumBy.ACCESSIBILITY_ID,'Loading...')
    FIRST_TRANSCRIPT_HEADER = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[contains(@name,"1_")]')
    SECOND_TRANSCRIPT_HEADER = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[contains(@name,"2_")]')
    THIRD_TRANSCRIPT_HEADER = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[contains(@name,"3_")]')
    TRANSCRIPT = (AppiumBy.IOS_PREDICATE,'type == "XCUIElementTypeTable"')
    NOTE_TAB_BUTTON = (AppiumBy.XPATH,'//XCUIElementTypeButton[XCUIElementTypeImage[@name="noteTabIcon"]]')
    TRANSCRIPT_TAB_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'transcriptTabIcon')
    AI_GENERATED_MSG = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[contains(@name,"AI-generated note, updated")]')
    NOTE_HEADER = (AppiumBy.IOS_CLASS_CHAIN,'**/XCUIElementTypeStaticText[`label == "Note"`]')
    HPI_HEADER = (AppiumBy.ACCESSIBILITY_ID,'HPI')
    ROS_HEADER = (AppiumBy.ACCESSIBILITY_ID,'ROS')
    PE_HEADER = (AppiumBy.ACCESSIBILITY_ID,'PE')
    MDM_HEADER = (AppiumBy.ACCESSIBILITY_ID,'MDM')
    NOTE_ID = (AppiumBy.ACCESSIBILITY_ID,'Note ID')
    AP_HEADER = (AppiumBy.ACCESSIBILITY_ID,'A/P')
    ADD_RE_EVAL_BUTTON = (AppiumBy.IOS_CLASS_CHAIN,'**/XCUIElementTypeButton[`label == "+ Add Re-eval"`]')
    NOTE_TEXTS_LOCATOR = (AppiumBy.XPATH,'//*[contains(@type, "XCUIElementTypeTextView")]')
    NO_TRANSCRIPTS_MESSAGE = (AppiumBy.ACCESSIBILITY_ID,'No Transcripts')
    TRANSCRIPT_TEXTS_LOCATOR = (AppiumBy.XPATH,'//XCUIElementTypeCell/XCUIElementTypeStaticText')
    MDM_EMPTY_TEXT_BOX = (AppiumBy.XPATH,'//*[@type="XCUIElementTypeTable"]/*[13]/*[@type="XCUIElementTypeTextView"]')
    INTERNET_CONNECTION_OFFlINE_MODAL = (AppiumBy.ACCESSIBILITY_ID,'The Internet connection appears to be offline')
    RE_EVAL_CONTAINER_TITLE = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[contains(@name,"Progress #")]')
    # RE_EVAL_CONTAINER_TIMESTAMP = (AppiumBy.ACCESSIBILITY_ID,
    #                                f'Time {get_date_time_by_zone(date_format="%-I:%M%p",_timezone="GMT").replace("M", "").lower()}')
    RE_EVAL_CONTAINER_TIMESTAMP = (AppiumBy.XPATH,'//XCUIElementTypeStaticText[contains(@name,"Time ")]')
    # RE_EVAL_UNLINKED_ICON = (AppiumBy.ACCESSIBILITY_ID,'EHR_synced')
    RE_EVAL_UNLINKED_ICON = (AppiumBy.XPATH,'//*[@type="XCUIElementTypeImage" and ./preceding-sibling::*[@type="XCUIElementTypeOther"]]')

    # def get_re_eval_timestamp_locator(self):
    #     lamdatest_time = get_formatted_time_of_lamdatest_device(self.driver,_date_format="%-I:%M%p").replace('m', '').lower()
    #     return (AppiumBy.ACCESSIBILITY_ID,f'Time {lamdatest_time}')
    NOTE_UPLOAD_BUTTON = (AppiumBy.XPATH,'//*[@type="XCUIElementTypeButton" and ./following-sibling::*[@type="XCUIElementTypeImage"]]')
    NOTE_UPLOAD_IMAGE = (AppiumBy.ACCESSIBILITY_ID,'noteUploadedToEhr')
    NOTE_HEADER_SECTION = (AppiumBy.XPATH,'//*[@type="XCUIElementTypeTable"]/*[1]/*[2]/*[@type="XCUIElementTypeOther"]')
    FIRST_RE_EVAL_HEADER_SECTION = (AppiumBy.XPATH,'//*[@type="XCUIElementTypeCell" and ./*[@name="Progress #1"]]')
    SECOND_RE_EVAL_HEADER_SECTION = (AppiumBy.XPATH,'//*[@type="XCUIElementTypeCell" and ./*[@name="Progress #2"]]')
    THIRD_RE_EVAL_HEADER_SECTION = (AppiumBy.XPATH,'//*[@type="XCUIElementTypeCell" and ./*[@name="Progress #3"]]')
    FIRST_RE_EVAL_HEADER_TEXT = (AppiumBy.ACCESSIBILITY_ID,'Progress #1')
    SECOND_RE_EVAL_HEADER_TEXT = (AppiumBy.ACCESSIBILITY_ID,'Progress #2')
    THIRD_RE_EVAL_HEADER_TEXT = (AppiumBy.ACCESSIBILITY_ID,'Progress #3')
    FIRST_RE_EVAL_CONTENT_LOCATOR = (AppiumBy.XPATH,f'//*[@value="{Data().FIRST_RE_EVAL_TEXT}"]')
    SECOND_RE_EVAL_CONTENT_LOCATOR = (AppiumBy.XPATH,f'//*[@value="{Data().SECOND_RE_EVAL_TEXT}"]')
    THIRD_RE_EVAL_CONTENT_LOCATOR = (AppiumBy.XPATH,f'//*[@value="{Data().THIRD_RE_EVAL_TEXT}"]')
    NOTE_UPLOAD_FAILED_MODAL = (AppiumBy.XPATH,'//*[@type="XCUIElementTypeOther" and ./*[@type="XCUIElementTypeScrollView"]]')
    NOTE_UPLOAD_FAILED_BODY = (AppiumBy.ACCESSIBILITY_ID,'Note failed to upload. Please try again.')
    NOTE_UPLOAD_FAILE_OK_BTN = (AppiumBy.ACCESSIBILITY_ID,'Ok')

    def create_note_and_get_noteid_in_scp(self,patient_name,scp_driver,start_time=None):
        scp_home_page = HomePage(scp_driver)
        organize_tab = OrganizeTab(scp_driver)
        scp_home_page.add_patient()
        organize_tab.set_organize_tab_value(patient_name=patient_name,start_time=start_time)
        scp_home_page.save_note()
        note_id = scp_home_page.get_selected_note_id()
        print(note_id)
        return note_id
    
    # def common_assertions_for_transcript_screen(self,patient_name_locator, number_of_recordings:bool = 1):
    #     assert self.is_element_visible(patient_name_locator,5)
    #     assert self.is_element_visible(self.FIRST_TRANSCRIPT_HEADER,120)
    #     assert not self.is_element_visible(self.NO_TRANSCRIPTS_MESSAGE,2)
    #     text_elements = self.get_elements(self.TRANSCRIPT_TEXTS_LOCATOR)
    #     print(len(text_elements))
    #     assert len(text_elements) > 0
    #     if number_of_recordings == 2:
    #         self.wait_and_click(self.SECOND_TRANSCRIPT_HEADER,100)
    #         assert self.is_element_visible(patient_name_locator,5)
    #         assert self.is_element_visible(self.SECOND_TRANSCRIPT_HEADER,120)
    #         assert not self.is_element_visible(self.NO_TRANSCRIPTS_MESSAGE,2)
    #         text_elements = self.get_elements(self.TRANSCRIPT_TEXTS_LOCATOR)
    #         print(len(text_elements))
    #         assert len(text_elements) > 0
    #     if number_of_recordings == 3:
    #         self.wait_and_click(self.SECOND_TRANSCRIPT_HEADER,100)
    #         assert self.is_element_visible(patient_name_locator,5)
    #         assert self.is_element_visible(self.THIRD_TRANSCRIPT_HEADER,120)
    #         assert not self.is_element_visible(self.NO_TRANSCRIPTS_MESSAGE,2)
    #         text_elements = self.get_elements(self.TRANSCRIPT_TEXTS_LOCATOR)
    #         print(len(text_elements))
    #         assert len(text_elements) > 0
    #         self.wait_and_click(self.THIRD_TRANSCRIPT_HEADER,100)
    #         assert self.is_element_visible(patient_name_locator,5)
    #         assert self.is_element_visible(self.THIRD_TRANSCRIPT_HEADER,120)
    #         assert not self.is_element_visible(self.NO_TRANSCRIPTS_MESSAGE,2)
    #         text_elements = self.get_elements(self.TRANSCRIPT_TEXTS_LOCATOR)
    #         print(len(text_elements))
    #         assert len(text_elements) > 0

    def common_assertions_for_transcript_screen(self, patient_name_locator, number_of_recordings: int = 1,
                                                note_uploaded: bool = False):
        def validate_transcript(header_locator):
            assert self.is_element_visible(patient_name_locator, 5)
            assert self.is_element_visible(header_locator, 120)
            assert not self.is_element_visible(self.NO_TRANSCRIPTS_MESSAGE, 2)
            assert self.is_element_visible(AppointmentScreenPage.TRACKER_TAB,2)
            assert self.is_element_visible(TranscriptsScreenPage.SEARCH_BUTTON,2)
            if number_of_recordings < 6 and not note_uploaded:
                assert self.is_element_visible(TranscriptsScreenPage.RECORDING_START_BUTTON,2)
            else:
                assert not self.is_element_visible(TranscriptsScreenPage.RECORDING_START_BUTTON,2)
            text_elements = self.get_elements(self.TRANSCRIPT_TEXTS_LOCATOR)
            print(len(text_elements))
            assert len(text_elements) > 0

        if number_of_recordings == 0:
            assert self.is_element_visible(patient_name_locator, 5)
            assert self.is_element_visible(self.NO_TRANSCRIPTS_MESSAGE, 2)
            assert self.is_element_visible(AppointmentScreenPage.TRACKER_TAB,2)
            assert self.is_element_visible(TranscriptsScreenPage.SEARCH_BUTTON,2)
            if not note_uploaded:
                assert self.is_element_visible(TranscriptsScreenPage.RECORDING_START_BUTTON)
            else:
                assert not self.is_element_visible(TranscriptsScreenPage.RECORDING_START_BUTTON)
            text_elements = self.get_elements(self.TRANSCRIPT_TEXTS_LOCATOR)
            print(len(text_elements))
            assert len(text_elements) == 0

        if number_of_recordings >= 1:
            # Validate the first transcript
            self.wait_and_click(self.FIRST_TRANSCRIPT_HEADER, 100)
            validate_transcript(self.FIRST_TRANSCRIPT_HEADER)

        # For additional recordings, click and validate accordingly
        if number_of_recordings >= 2:
            self.wait_and_click(self.SECOND_TRANSCRIPT_HEADER, 100)
            validate_transcript(self.SECOND_TRANSCRIPT_HEADER)

        if number_of_recordings == 3:
            self.wait_and_click(self.THIRD_TRANSCRIPT_HEADER, 100)
            validate_transcript(self.THIRD_TRANSCRIPT_HEADER)


    def common_assertions_for_note_screen(self, AI_MESSAGE_CHECK:bool = True, empty_note:bool = False,
                                          note_uploaded:bool = False):
        if AI_MESSAGE_CHECK and not note_uploaded:
            assert self.is_element_visible(self.AI_GENERATED_MSG,3)
        assert self.is_element_visible(self.NOTE_HEADER,3)
        assert self.is_element_visible(self.HPI_HEADER,3)
        self.scroll_to_get_element(self.ROS_HEADER)
        assert self.is_element_visible(self.ROS_HEADER,3)
        self.scroll_to_get_element(self.PE_HEADER)
        assert self.is_element_visible(self.PE_HEADER,3)
        self.scroll_to_get_element(self.MDM_HEADER)
        assert self.is_element_visible(self.MDM_HEADER,3)
        self.scroll_to_get_element(self.NOTE_ID)
        assert self.is_element_visible(self.NOTE_ID,3)
        text_elements = self.get_elements(self.NOTE_TEXTS_LOCATOR)
        if empty_note:
            print(len(text_elements))
            assert len(text_elements) == 4
        else:
            print(len(text_elements))
            assert len(text_elements) > 4
        assert self.is_element_visible(self.ADD_RE_EVAL_BUTTON,3)

    def create_appointment_from_app(self, patient_name, unique_name:bool = True, change_time:bool = False, offset = 0.15):
        if unique_name:
            patient_name_unique = patient_name + generate_random_alphanumeric_string(3)
            print(patient_name_unique)
            self.click_and_wait(AppointmentScreenPage.ADD_APPOINTMENT_BUTTON,1)
            self.enter_text_at(AppointmentScreenPage.PATIENT_NAME_INPUT_FIELD, 
                                            patient_name_unique, 1)
            if change_time:
                self.click_and_wait(AppointmentScreenPage.VISIT_TIME_BUTTON,1)
                self.adjust_ios_time_picker(minutes_order='next', minutes_offset=offset)

            self.click_and_wait_for_invisibility(AppointmentScreenPage.SELECT_BUTTON,5)
            xpath_string =  (AppiumBy.ACCESSIBILITY_ID,f'{patient_name_unique}')
            self.wait_for_visibility_of(xpath_string,10)
            return patient_name_unique, xpath_string
        else:
            self.click_and_wait(AppointmentScreenPage.ADD_APPOINTMENT_BUTTON,1)
            self.enter_text_at(AppointmentScreenPage.PATIENT_NAME_INPUT_FIELD, 
                                            patient_name, 1)
            if change_time:
                self.click_and_wait(AppointmentScreenPage.VISIT_TIME_BUTTON,1)
                self.adjust_ios_time_picker(minutes_order='next', minutes_offset=offset)
            self.click_and_wait_for_invisibility(AppointmentScreenPage.SELECT_BUTTON,5)
            xpath_string =  (AppiumBy.ACCESSIBILITY_ID,f'{patient_name}')
            self.wait_for_visibility_of(xpath_string,10)
        
    def common_note_keyboard_edit_steps(self,edit_type:str, patient_name_locator):
        '''
        edit_type: 'Add' or 'Remove'. Add if texts to be added. Remove if texts to be removed.
        patient_name_xpath: xpath locator of patient's name
        '''
        if edit_type == 'Add':
            self.enter_text_at_first_locator(self.NOTE_TEXTS_LOCATOR,
                                                        self.data.ADD_TEXT_TO_NOTE,False, 3)
        else:
            self.clear_texts(self.NOTE_TEXTS_LOCATOR, 3)

        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        self.click_and_wait(AppointmentScreenPage.TRACKER_TAB,4)
        self.click_and_wait(patient_name_locator,4)
        self.click_and_wait(self.NOTE_TAB_BUTTON,4)
        first_element = self.get_first_element(self.NOTE_TEXTS_LOCATOR)
        return first_element
    
    def add_re_eval_text(self, custom_text:str = Data().ADD_TEXT_TO_NOTE):
        self.wait_and_click(self.ADD_RE_EVAL_BUTTON,3)
        self.enter_text_at_last_locator(self.NOTE_TEXTS_LOCATOR,custom_text,max_wait=60)
        self.click_and_wait(HomeScreenPage(self.driver).KEYBOARD_RETURN_BUTTON,3)

    def navigate_to_note_screen_from_tracker(self, patient_name_locator):
        self.wait_for_visibility_of(patient_name_locator,10)
        self.click_and_wait(patient_name_locator,4)
        self.wait_and_click(self.NOTE_TAB_BUTTON,4)

    def upload_note(self,patient_name_locator,wait_for_upload_button:int = 100):
        self.wait_for_element_to_clickable(self.NOTE_UPLOAD_BUTTON,wait_for_upload_button)
        self.click_and_wait(self.NOTE_UPLOAD_BUTTON,2)
        self.wait_for_visibility_of(patient_name_locator,10)

    def upload_audio_and_wait_for_transcript(self,note_id,file_path,username,password,
                                             transcript_header,wait_time_for_transcript=120):
        upload_audio_to_go_note(note_id, file_path, username, password)
        if not self.is_element_visible(transcript_header,wait_time_for_transcript):
            self.click_and_wait(self.NOTE_TAB_BUTTON,1)
            self.click_and_wait(self.TRANSCRIPT_TAB_BUTTON,1)
            self.wait_for_visibility_of(transcript_header,5)
        self.click_and_wait(transcript_header,1)
        self.wait_for_visibility_of(TranscriptsScreenPage.TRANSCRIPT_TEXT,10)