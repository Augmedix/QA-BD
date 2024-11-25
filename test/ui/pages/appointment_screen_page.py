"""
Locators & functionalities related to Appointment Screen.
"""
import time
import requests
import jwt
import pytest
import pytz
from jwt import DecodeError
from utils.request_handler import RequestHandler
import json
from datetime import datetime, timedelta
import random
from utils.api_request_data_handler import APIRequestDataHandler
import string
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from data.data import Data
from pages.base_page import BasePage
from pages.home_screen_page import HomeScreenPage
from pages.api_pages.appointment_api_page import AppointmentsApiPage
from utils.upload_go_audio.upload_audio import upload_audio_to_go_note


class AppointmentScreenPage(BasePage):
    """
    Locators & functionalities related to Appointment Screen.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home_screen = HomeScreenPage(self.driver)
        self.appointment_api_page = AppointmentsApiPage()
        self.api_url = pytest.configs.get_config('ehr_appointment_service')

    TRACKER_TAB = (AppiumBy.XPATH, '//*[@value="Tracker"]')
    TO_DO_TAB = (AppiumBy.XPATH, '//*[contains(@value, "To Do")]')
    HAMBURGER_MENU = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar/XCUIElementTypeButton')
    LOGOUT_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Log Out"]')
    SETTINGS_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Settings"]')
    SETTINGS_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="ic settings"]')
    

    # SELECT_BAR = (AppiumBy.ID, '45000000-0000-0000-C24E-000000000000')
    CONNECTING_MODAL = (AppiumBy.XPATH, '//*[@name="Connecting..."]')
    LOADING_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Loading..."]')
    PATIENT_APPOINTMENTS = (AppiumBy.XPATH, '//XCUIElementTypeCell')
    APPOINTMENT_TIME = (AppiumBy.XPATH, '//XCUIElementTypeCell /XCUIElementTypeStaticText[1]')
    PATIENT_NAME = (AppiumBy.XPATH, '//*[@type="XCUIElementTypeTable"]/*[2]/*[@type="XCUIElementTypeStaticText"]')
    NON_EHR_APPOINMENT = (AppiumBy.XPATH, '//*[@name="Test non-ehr user 1"]')
    APPOINTMENT_STATUS_ACTIVE = (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="editIcon"]')
    APPOINTMENT_STATUS_CONTENT_PROCESSING = (AppiumBy.XPATH, '//XCUIElementTypeOther[3]')
    APPOINTMENT_STATUS_SENT = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Sent"]')
    APPOINTMENT_STATUS_EXPIRES = (AppiumBy.XPATH, '//XCUIElementTypeButton[contains(@name,"Expires")]')

    # NOTE_STATUS_SIGNED = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Signed"]')
    ACTIVE_APPOINTMENT_PATIENT_NAME = \
        (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="editIcon"] /preceding-sibling::XCUIElementTypeStaticText[1]')
    SERVICE_DAY_DATE = (AppiumBy.XPATH, '//XCUIElementTypeCell[1]//XCUIElementTypeStaticText[1]')

    NEW_APPOINTMENT = (AppiumBy.XPATH, '//XCUIElementTypeCell [not(./XCUIElementTypeButton)]'
                                       ' [not(./XCUIElementTypeImage)] [not(./XCUIElementTypeOther[3])]')
    EDITABLE_APPOINTMENT = (AppiumBy.XPATH, '//XCUIElementTypeCell [not(./XCUIElementTypeButton[@name="Sent"])]')
    ACTIVE_APPOINTMENT = (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="editIcon"] /parent::XCUIElementTypeCell')
    PROCESSING_APPOINTMENT = (AppiumBy.XPATH, '//XCUIElementTypeOther[3] /parent::XCUIElementTypeCell')
    SENT_APPOINTMENT = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Sent"] /parent::XCUIElementTypeCell')
    EXPIRES_APPOINTMENT = (AppiumBy.XPATH,
                           '//XCUIElementTypeButton[contains(@name,"Expires")] /parent::XCUIElementTypeCell')
    ADD_APPOINTMENT_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton')
    ADD_NEW_VISIT_MODAL_TITLE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Add New Visit"]')
    PATIENT_NAME_FIELD_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Patient Name"]')
    PATIENT_NAME_INPUT_FIELD = \
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Patient Name"]/following-sibling::XCUIElementTypeTextField')

    VISIT_TIME_TEXT = (AppiumBy.XPATH, '//XCUIcElementTypeStaticText[@name="Visit Time"]')
    VISIT_TIME = (AppiumBy.XPATH,
                  '//XCUIElementTypeStaticText[@name="Visit Time"] /following-sibling::XCUIElementTypeButton')
    VISIT_TIME_BUTTON = (AppiumBy.XPATH,
                         '//XCUIElementTypeStaticText[@name="Visit Time"]/following-sibling::XCUIElementTypeButton')
    TIME_PICKER = (AppiumBy.XPATH, '//XCUIElementTypePickerWheel')
    SELECT_BUTTON = \
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Add New Visit"] /following-sibling::XCUIElementTypeButton')
    CANCEL_BUTTON = \
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Add New Visit"] /preceding-sibling::XCUIElementTypeButton')
    CREATING_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Creating..."]')
    UPDATING_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Updating..."]')
    ARCHIVE_APPOINTMENT_BUTTON = (AppiumBy.ACCESSIBILITY_ID,'crossIcon')
    MIC_ICON = (AppiumBy.XPATH,'//XCUIElementTypeCell[2]/XCUIElementTypeButton')
    EMPTY_APPOINTMENT_LIST = (AppiumBy.ACCESSIBILITY_ID,'Empty list')
    TRANSCRIPT_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID, Data().TRANSCRIPT_PATIENT_NAME)
    OK_BTN_BLUETOOTH_PERMITION_MODAL = (AppiumBy.XPATH, '//*[@name="OK"]')
    MULTILINGUAL_PATIENT_NAME = (AppiumBy.ACCESSIBILITY_ID, Data().TRANSCRIPT_PATIENT_MULTILINGUAL_NAME)
    CHANGE_LANGUAGE_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Change language"]')
    CHANGE_LANGUAGE_MODAL_CLOSE_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Change language"] '
                                                          '//preceding-sibling::XCUIElementTypeButton')
    ENGLISH_LANGUAGE_SELECTION_OPTION = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="English (EN)"]')
    SPANISH_LANGUAGE_SELECTION_OPTION = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Spanish (ES)"]')


    def get_selected_language_locator_for_visit(self, patient_name):
        return (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[@name="{patient_name}"]'
                                f'/following-sibling::XCUIElementTypeStaticText')

    def get_selected_appointment_locator(self, patient_name):
        return AppiumBy.XPATH, f'//XCUIElementTypeStaticText[@name="{patient_name}"]/parent::XCUIElementTypeCell'
    
    def get_sent_status_locator(self, patient_name):
        return AppiumBy.XPATH, f'//*[@name="{patient_name}"]/preceding-sibling::*[@type="XCUIElementTypeOther"]'



    def get_new_appointment(self):
        appointments = self.get_elements(self.PATIENT_APPOINTMENTS)
        for appointment in appointments:
            if not (self.get_child_element(appointment, self.APPOINTMENT_STATUS_SENT)
                    and self.get_child_element(appointment, self.APPOINTMENT_STATUS_ACTIVE)
                    and self.get_child_element(appointment, self.APPOINTMENT_STATUS_CONTENT_PROCESSING)):
                date_text = self.get_child_element(appointment, self.APPOINTMENT_TIME).text
                name_text = self.get_child_element(appointment, self.PATIENT_NAME).text
                return appointment, date_text, name_text
        print('No New Appointment available')
        return None

    def get_selected_appointment_info(self, locator):
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        self.wait_for_existence_of_all(self.PATIENT_APPOINTMENTS, 10)
        self.scroll_to_locator(locator)
        time.sleep(5)
        #appointment = self.get_element(locator)
        #appointment_time = self.get_attribute(self.APPOINTMENT_TIME, 'value')
        patient_name = self.get_attribute(locator, 'value')
        return patient_name

    def get_appointment_element(self, patient_name):
        self.wait_for_invisibility_of(self.LOADING_MODAL)
        self.wait_for_existence_of_all(self.PATIENT_APPOINTMENTS, 30)
        self.scroll_to_locator(self.get_selected_appointment_locator(patient_name))
        appointment = self.get_element(self.get_selected_appointment_locator(patient_name))
        return appointment

    

    def generate_random_patient_name(self, base_name="Test non-ehr user"):
        # Generate a random string of 4 digits to append to the base name
        random_suffix = ''.join(random.choices(string.digits, k=4))
        return f"{base_name} {random_suffix}"

    def get_non_ehr_appointment_locator(self, patient_name):
        # Format the XPath to include the dynamically generated patient name
        return (AppiumBy.XPATH, f'//*[@name="{patient_name}"]')
    
    def crete_non_ehr_appointments(self, name='Test non-ehr user'):
        time.sleep(1)
        self.wait_and_click(self.ADD_APPOINTMENT_BUTTON)
        self.enter_text_at(self.PATIENT_NAME_INPUT_FIELD, name, 2)
        self.wait_and_click(self.SELECT_BUTTON)
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        time.sleep(4)

    def create_non_ehr_appointments(self):
        # Generate a random patient name
        patient_name = self.generate_random_patient_name()
        
        # Perform actions to create the appointment
        time.sleep(1)
        self.wait_and_click(self.ADD_APPOINTMENT_BUTTON)
        self.enter_text_at(self.PATIENT_NAME_INPUT_FIELD, patient_name, 2)
        self.wait_and_click(self.SELECT_BUTTON)
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        
        # Get the locator for the newly created appointment
        appointment_locator = self.get_non_ehr_appointment_locator(patient_name)
        
        # Return both the patient name and the locator
        return patient_name, appointment_locator
    

    def create_non_ehr_patient_16_hours_before_device_time(self, email, password, provider_id):
        # Generate a random patient name
        patient_name = self.generate_random_patient_name()

        # Get the current device time in UST timezone
        ust_timezone = pytz.timezone('America/Chicago')  # UST equivalent (or adjust according to location)
        current_time_ust = datetime.now(ust_timezone)
        
        # Calculate the time 16 hours before the current time
        appointment_time = current_time_ust - timedelta(hours=16)
        
        # Format the date and time for the API request
        formatted_date = appointment_time.strftime('%Y-%m-%d')
        formatted_time = appointment_time.strftime('%I:%M %p')  # Format the time as "HH:MM AM/PM"

        request_data = APIRequestDataHandler('appointments_data')
        token = RequestHandler.get_auth_token(user_name=email, password=password)

        # Define the request body
        payload = {
            "startTime": formatted_time,
            "doctorId": provider_id,
            "patient": {
                "firstName": patient_name
            },
            "date": formatted_date
        }

        # Define headers (add the authentication token)
        headers = request_data.get_modified_headers(Authorization=f'Bearer {token}')
        print(f"Headers: {headers}")
        print(f"Token: {token}")
        
        # Send the POST request to create the appointment
        payload = json.dumps(payload, indent=4)
        appointments_path = 'lynx/appointment'
        response = RequestHandler.get_api_response(base_url=self.api_url, request_path=appointments_path,
                                                headers=headers, request_type='POST', payload=payload)
        
        if response.status_code == 201 or response.status_code == 200:
            print(f"Appointment created for patient {patient_name} at {formatted_time} on {formatted_date}")
        else:
            print(f"Failed to create appointment: {response.status_code} - {response.text}")
            return None

        # Get the locator for the created patient
        appointment_locator = self.get_non_ehr_appointment_locator(patient_name)
        print('Locator: ', appointment_locator)
        
        # Return the patient name, appointment locator, and API response
        return patient_name, appointment_locator



    def navigate_home_screen_to_appointment_screen(self, username, password):
        self.home_screen.login_with_password(username, password, handle_post_login=True)
        self.wait_for_visibility_and_invisibility_of(self.CONNECTING_MODAL, 6)
        """ if self.is_element_visible(self.OK_BTN_BLUETOOTH_PERMITION_MODAL, 3):
            self.click_and_wait(self.OK_BTN_BLUETOOTH_PERMITION_MODAL)
        else:
            print('Bluetooth permission modal does not appear') """
        """ self.crete_non_ehr_appointments('Test non-ehr user 1')
        # self.crete_non_ehr_appointments("Test non-ehr user 2")
        schedule_appointment_time, schedule_appointment_patient_name = \
            self.get_selected_appointment_info(self.NEW_APPOINTMENT)
        self.wait_and_click(self.TO_DO_TAB)
        todo_appointment_time, todo_appointment_patient_name = self.get_selected_appointment_info(self.NEW_APPOINTMENT)
        return schedule_appointment_time, schedule_appointment_patient_name,\
            todo_appointment_time, todo_appointment_patient_name """

    def is_appointment_status_visible(self, appointment_element, status_locator):
        status_element = self.get_child_element(appointment_element, status_locator)
        if status_element:
            return status_element.is_displayed()
        return status_element


    def get_appointments_count(self):
        try:
            return self.get_total_count(self.PATIENT_APPOINTMENTS)
        except NoSuchElementException:
            return 0

    def get_create_appointment_time(self):
        creating_time = self.get_text_by_locator(self.VISIT_TIME)
         # Parse the time string to a datetime object
        time_obj = datetime.strptime(creating_time, '%I:%M %p')
        
        # Format the hour, minute, and AM/PM
        hour = time_obj.strftime('%I').lstrip('0')  # Remove leading zero from hour
        minute = time_obj.strftime('%M')
        am_pm = time_obj.strftime('%p').lower()  # Get AM/PM in lowercase
        
        # Combine formatted parts
        formatted_time = f"{hour}:{minute}{am_pm}"
        return formatted_time
    
    def upload_audio_to_a_go_note(self, user_name, password, patient_name, doctor_id):
        note_id = self.appointment_api_page.get_note_id_by_note_name(user_name=user_name, password=password, patient_name=patient_name, doctor_id=doctor_id)
        upload_audio_to_go_note(auth_token=False, note_id=note_id, username=user_name, password=password, file_path='utils/upload_go_audio/Visit8-v6_20221212.mp3')