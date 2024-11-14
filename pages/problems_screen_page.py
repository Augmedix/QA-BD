"""
Locators & functionalities for Problem Screen.
"""
import datetime
import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

from data.data import Data
from pages.appointment_screen_page import AppointmentScreenPage
from pages.base_page import BasePage
from pages.home_screen_page import HomeScreenPage

data = Data()


class ProblemsScreenPage(BasePage):
    """
    Locators & functionalities for Problem Screen.
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.home_screen = HomeScreenPage(self.driver)
        self.appointment_screen = AppointmentScreenPage(self.driver)

    BACK_SCHEDULE_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Schedule"]')
    PATIENT_NAME =(AppiumBy.XPATH,
                   '//XCUIElementTypeButton[@name="Schedule"] /following-sibling::XCUIElementTypeStaticText')
    SEND_BUTTON = (AppiumBy.XPATH,
                   '//XCUIElementTypeButton[@name="Schedule"] /preceding-sibling::XCUIElementTypeButton')
    NOTE_UPLOADING_MODAL_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Uploading Notes .. "]')
    KABOB_OPTION = (AppiumBy.NAME, 'kabob')
    PROBLEMS_TAB = (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="problemTabIconNew"]/parent::XCUIElementTypeButton')
    TRANSCRIPTS_TAB = (AppiumBy.XPATH,
                       '//XCUIElementTypeImage[@name="transcriptTabIcon"]/parent::XCUIElementTypeButton')
    NOTE_TAB = (AppiumBy.XPATH, '//*[@name="noteTabIcon"]')
    EMPTY_STATE_ADD_PROBLEM_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="+ Add Problems"]')
    EMPTY_STATE_GET_STARTED_TEXT = \
        (AppiumBy.XPATH,
         '//XCUIElementTypeButton[@name="+ Add Problems"] /following-sibling::XCUIElementTypeStaticText')
    ADD_PROBLEMS_ICON = (AppiumBy.XPATH,
                         '//XCUIElementTypeButton[@name="Schedule"] /following-sibling::XCUIElementTypeButton')
    PROBLEMS_CAROUSEl = (AppiumBy.XPATH, '//XCUIElementTypeCollectionView')
    PROBLEMS_CAROUSEl_LIST = (AppiumBy.XPATH, '//XCUIElementTypeCollectionView[1] //XCUIElementTypeStaticText')
    LOADING_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Loading..."]')
    SAVING_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Saving..."]')

    NOTE_UPLOAD_STATUS_MESSAGE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"upload")]')
    OK_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Ok"]')

    # Add Modal
    SELECT_ICON = (AppiumBy.XPATH, '(//XCUIElementTypeOther /XCUIElementTypeButton[2])[2]')
    CANCEL_ICON = \
        (AppiumBy.XPATH,
         '(//XCUIElementTypeOther /XCUIElementTypeButton[2])[2] /preceding-sibling::XCUIElementTypeButton')
    ADD_POP_UP_MODAL_TITLE = \
        (AppiumBy.XPATH,
         '(//XCUIElementTypeOther /XCUIElementTypeButton[2])[2] /preceding::XCUIElementTypeStaticText[1]')
    SEARCH_ADD_CUSTOM_INPUT_FIELD = \
        (AppiumBy.XPATH,
         '(//XCUIElementTypeOther /XCUIElementTypeButton[2])[2] /following-sibling::XCUIElementTypeTextField')
    ADD_MODAL_LIST_ITEMS = (AppiumBy.XPATH, '//XCUIElementTypeTable /XCUIElementTypeCell /XCUIElementTypeStaticText')

    # Add problem Modal
    PROBLEMS_ACTIVE_TAB = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Active"]')
    PROBLEMS_COMMON_TAB = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Common"]')
    PROBLEM_CHECKED_BOX = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="ic check box"]')
    PROBLEM_UNCHECKED_BOX = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="ic check box outline blank"]')
    ADD_PROBLEM_MODAL_PROBLEM_NAMES_LIST = (AppiumBy.XPATH, '//XCUIElementTypeTable //XCUIElementTypeStaticText[2]')

    # DESCRIPTOR = (AppiumBy.XPATH, '//XCUIElementTypeCell //XCUIElementTypeOther /XCUIElementTypeStaticText')
    DATE_PICKER = (AppiumBy.XPATH, '//XCUIElementTypePickerWheel')

    SYMPTOMS_BLOCKS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Symptoms"]')
    ADD_SYMPTOMS_BUTTON = \
        (AppiumBy.XPATH,
         '//XCUIElementTypeStaticText[@name="Symptoms"] /preceding-sibling::XCUIElementTypeButton'
         ' | //XCUIElementTypeStaticText[@name="Symptoms"] /following-sibling::XCUIElementTypeButton')
    CURRENT_MEDICATION_BLOCKS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Current medications")]')
    ADD_CURRENT_MEDICATION_BUTTON =\
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Current medications")]'
                         ' /preceding-sibling::XCUIElementTypeButton'
                         ' | //XCUIElementTypeStaticText[contains(@name,"Current medications")]'
                         ' /following-sibling::XCUIElementTypeButton')
    TREATMENT_PROCEDURES_BLOCKS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Treatment procedure")]')
    ADD_TREATMENT_PROCEDURES_BUTTON = \
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Treatment procedure")]'
                         ' /preceding-sibling::XCUIElementTypeButton'
                         ' | //XCUIElementTypeStaticText[contains(@name,"Treatment procedure")]'
                         ' /following-sibling::XCUIElementTypeButton')
    LIFESTYLE_TREATMENTS_BLOCKS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Lifestyle treatments"]')
    ADD_LIFESTYLE_TREATMENTS_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Lifestyle treatments"]'
                                                       ' /preceding-sibling::XCUIElementTypeButton'
                                                       ' | //XCUIElementTypeStaticText[@name="Lifestyle treatments"]'
                                                       ' /following-sibling::XCUIElementTypeButton')
    RECENT_LAB_BLOCKS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Recent Lab")]')
    ADD_RECENT_LAB_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Recent Lab")]'
                                             ' /preceding-sibling::XCUIElementTypeButton'
                                             ' | //XCUIElementTypeStaticText[contains(@name,"Recent Lab")]'
                                             ' /following-sibling::XCUIElementTypeButton')
    RECENT_IMAGING_BLOCKS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Recent imaging")]')
    ADD_RECENT_IMAGING_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Recent imaging")]'
                                                 ' /preceding-sibling::XCUIElementTypeButton '
                                                 '| //XCUIElementTypeStaticText[contains(@name,"Recent imaging")] '
                                                 '/following-sibling::XCUIElementTypeButton')
    RECENT_DIAGNOSTICS_BLOCKS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Recent diagnostics")]')
    ADD_RECENT_DIAGNOSTICS_BUTTON =\
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Recent diagnostics")]'
                         ' /preceding-sibling::XCUIElementTypeButton'
                         ' | //XCUIElementTypeStaticText[contains(@name,"Recent diagnostics")]'
                         ' /following-sibling::XCUIElementTypeButton')
    STATUS_BLOCKS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Status")]')
    ADD_STATUS_BUTTON =\
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Status")]'
                         ' /preceding-sibling::XCUIElementTypeButton'
                         ' | //XCUIElementTypeStaticText[contains(@name,"Status")]'
                         ' /following-sibling::XCUIElementTypeButton')
    PROGRESSION_BLOCKS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Progression")]')
    ADD_PROGRESSION_BUTTON =\
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Progression")]'
                         ' /preceding-sibling::XCUIElementTypeButton'
                         ' | //XCUIElementTypeStaticText[contains(@name,"Progression")]'
                         ' /following-sibling::XCUIElementTypeButton')
    MEDICATIONS_BLOCKS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Medications")]')
    ADD_MEDICATIONS_BUTTON =\
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Medications")]'
                         ' /preceding-sibling::XCUIElementTypeButton'
                         ' | //XCUIElementTypeStaticText[contains(@name,"Medications")]'
                         ' /following-sibling::XCUIElementTypeButton')
    LAB_BLOCKS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Labs")]')
    ADD_LAB_BUTTON =\
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Labs"] /preceding-sibling::XCUIElementTypeButton'
                         ' | //XCUIElementTypeStaticText[@name="Labs"] /following-sibling::XCUIElementTypeButton')
    IMAGING_BLOCKS = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Imaging")]')
    ADD_IMAGING_BUTTON =\
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Imaging")]'
                         ' /preceding-sibling::XCUIElementTypeButton '
                         '| //XCUIElementTypeStaticText[contains(@name,"Imaging")]'
                         ' /following-sibling::XCUIElementTypeButton')
    DIAGNOSTIC_PROCEDURES_BLOCKS =\
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Diagnostic procedures")]')
    ADD_DIAGNOSTIC_PROCEDURES_BUTTON =\
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Diagnostic procedures")]'
                         ' /preceding-sibling::XCUIElementTypeButton'
                         ' | //XCUIElementTypeStaticText[contains(@name,"Diagnostic procedures")]'
                         ' /following-sibling::XCUIElementTypeButton')

    ACUTE_HPI_SYMPTOMS_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_HPI_SYMPTOMS_NAME}")]')
    CHRONIC_HPI_SYMPTOMS_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_SYMPTOMS_NAME}")]')

    ACUTE_HPI_CURRENT_MEDICATION_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_HPI_CURRENT_MEDICATION_NAME}")]')
    ACUTE_HPI_CURRENT_MEDICATION_DOSAGE_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_HPI_CURRENT_MEDICATION_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField[1]')
    ACUTE_HPI_CURRENT_MEDICATION_FREQUENCY_BUTTON = \
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_HPI_CURRENT_MEDICATION_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField[2]')

    CHRONIC_HPI_CURRENT_MEDICATION_DESCRIPTOR = \
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_CURRENT_MEDICATION_NAME}")]')
    CHRONIC_HPI_CURRENT_MEDICATION_DOSAGE_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_CURRENT_MEDICATION_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField[1]')
    CHRONIC_HPI_CURRENT_MEDICATION_FREQUENCY_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_CURRENT_MEDICATION_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField[2]')

    ACUTE_HPI_LIFESTYLE_TREATMENT_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_HPI_LIFESTYLE_TREATMENT_NAME}")]')
    ACUTE_HPI_LIFESTYLE_TREATMENT_DETAILS_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_HPI_LIFESTYLE_TREATMENT_NAME}")]'
                         f' /following-sibling::XCUIElementTypeButton')

    CHRONIC_HPI_LIFESTYLE_TREATMENT_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_LIFESTYLE_TREATMENT_NAME}")]')
    CHRONIC_HPI_LIFESTYLE_TREATMENT_DETAILS_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_LIFESTYLE_TREATMENT_NAME}")]'
                         f' /following-sibling::XCUIElementTypeButton')

    ACUTE_HPI_TREATMENT_PROCEDURE_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_HPI_TREATMENT_PROCEDURE_NAME}")]')
    ACUTE_HPI_TREATMENT_PROCEDURE_DESCRIPTOR_GROUP = \
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_HPI_TREATMENT_PROCEDURE_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField '
                         f'| //XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_HPI_TREATMENT_PROCEDURE_NAME}")]'
                         f' /following-sibling::XCUIElementTypeButton')

    CHRONIC_HPI_TREATMENT_PROCEDURE_DESCRIPTOR = \
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_TREATMENT_PROCEDURE_NAME}")]')
    CHRONIC_HPI_TREATMENT_PROCEDURE_DESCRIPTOR_GROUP = \
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_TREATMENT_PROCEDURE_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField'
                         f' | //XCUIElementTypeStaticText[contains(@name,'
                         f'"{data.CHRONIC_HPI_TREATMENT_PROCEDURE_NAME}")] /following-sibling::XCUIElementTypeButton')

    CHRONIC_HPI_RECENT_LAB_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_RECENT_LAB_NAME}")]')
    CHRONIC_HPI_RECENT_LAB_DETAILS =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_RECENT_LAB_NAME}")]'
                         f' /following-sibling::XCUIElementTypeButton')
    CHRONIC_HPI_RECENT_LAB_RESULT_BUTTON = \
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_RECENT_LAB_NAME}")]'
                         f' /parent:: XCUIElementTypeOther /following-sibling::XCUIElementTypeOther'
                         f' /XCUIElementTypeTextField')
    CHRONIC_HPI_RECENT_LAB_DATE_BUTTON = \
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_RECENT_LAB_NAME}")]'
                         f' /parent:: XCUIElementTypeOther /following-sibling::XCUIElementTypeOther'
                         f' /XCUIElementTypeButton')

    CHRONIC_HPI_RECENT_IMAGING_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_RECENT_IMAGING_NAME}")]')
    CHRONIC_HPI_RECENT_IMAGING_DETAILS = \
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_RECENT_IMAGING_NAME}")]'
                         f' /following-sibling::XCUIElementTypeButton')
    CHRONIC_HPI_RECENT_IMAGING_RESULT_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_RECENT_IMAGING_NAME}")]'
                         f' /parent:: XCUIElementTypeOther /following-sibling::XCUIElementTypeOther'
                         f' /XCUIElementTypeTextField')
    CHRONIC_HPI_RECENT_IMAGING_DATE_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_RECENT_IMAGING_NAME}")]'
                         f' /parent:: XCUIElementTypeOther /following-sibling::XCUIElementTypeOther'
                         f' /XCUIElementTypeButton')

    CHRONIC_HPI_RECENT_DIAGNOSTIC_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_RECENT_DIAGNOSTIC_NAME}")]')
    CHRONIC_HPI_RECENT_DIAGNOSTIC_DETAILS =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_RECENT_DIAGNOSTIC_NAME}")]'
                         f' /following-sibling::XCUIElementTypeButton')
    CHRONIC_HPI_RECENT_DIAGNOSTIC_RESULT_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_RECENT_DIAGNOSTIC_NAME}")]'
                         f' /parent:: XCUIElementTypeOther /following-sibling::XCUIElementTypeOther'
                         f' /XCUIElementTypeTextField')
    CHRONIC_HPI_RECENT_DIAGNOSTIC_DATE_BUTTON = \
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_HPI_RECENT_DIAGNOSTIC_NAME}")]'
                         f' /parent:: XCUIElementTypeOther /following-sibling::XCUIElementTypeOther'
                         f' /XCUIElementTypeButton')

    AP_STATUS_BUTTON = \
        (AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"Status")] /parent:: XCUIElementTypeOther'
                         ' /following-sibling::XCUIElementTypeCell //XCUIElementTypeTextField')

    ACUTE_AP_PROGRESSION_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_PROGRESSION_NAME}")]')
    CHRONIC_AP_PROGRESSION_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_PROGRESSION_NAME}")]')

    ACUTE_AP_MEDICATION_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_MEDICATION_NAME}")]')
    ACUTE_AP_ACTION_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_MEDICATION_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField[1]')
    ACUTE_AP_MEDICATION_DOSAGE_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_MEDICATION_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField[2]')
    ACUTE_AP_MEDICATION_FREQUENCY_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_MEDICATION_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField[3]')

    CHRONIC_AP_MEDICATION_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_MEDICATION_NAME}")]')
    CHRONIC_AP_MEDICATION_ACTION_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_MEDICATION_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField[1]')
    CHRONIC_AP_MEDICATION_DOSAGE_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_MEDICATION_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField[2]')
    CHRONIC_AP_MEDICATION_FREQUENCY_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_MEDICATION_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField[3]')

    ACUTE_AP_LIFESTYLE_TREATMENT_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_LIFESTYLE_TREATMENT_NAME}")]')
    ACUTE_AP_LIFESTYLE_TREATMENT_DETAILS_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_LIFESTYLE_TREATMENT_NAME}")]'
                         f' /following-sibling::XCUIElementTypeButton')

    CHRONIC_AP_LIFESTYLE_TREATMENT_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_LIFESTYLE_TREATMENT_NAME}")]')
    CHRONIC_AP_LIFESTYLE_TREATMENT_DETAILS_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_LIFESTYLE_TREATMENT_NAME}")]'
                         f' /following-sibling::XCUIElementTypeButton')

    ACUTE_AP_TREATMENT_PROCEDURE_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_TREATMENT_PROCEDURE_NAME}")]')
    ACUTE_AP_TREATMENT_PROCEDURE_DESCRIPTOR_GROUP =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_TREATMENT_PROCEDURE_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField')
    ACUTE_AP_TREATMENT_PROCEDURE_DETAILS_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_TREATMENT_PROCEDURE_NAME}")]'
                         f' /following-sibling::XCUIElementTypeButton')

    CHRONIC_AP_TREATMENT_PROCEDURE_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_TREATMENT_PROCEDURE_NAME}")]')
    CHRONIC_AP_TREATMENT_PROCEDURE_DESCRIPTOR_GROUP =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_TREATMENT_PROCEDURE_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField')
    CHRONIC_AP_TREATMENT_PROCEDURE_DETAILS_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_TREATMENT_PROCEDURE_NAME}")]'
                         f' /following-sibling::XCUIElementTypeButton')

    ACUTE_AP_LAB_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_LAB_NAME}")]')
    ACUTE_AP_LAB_DESCRIPTOR_GROUP =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_LAB_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField')

    CHRONIC_AP_LAB_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_LAB_NAME}")]')
    CHRONIC_AP_LAB_DESCRIPTOR_GROUP =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_LAB_NAME}")]'
                         f' /following-sibling::XCUIElementTypeTextField')

    ACUTE_AP_IMAGING_DESCRIPTOR = \
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_IMAGING_NAME}")]')
    ACUTE_AP_IMAGING_DETAILS_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_IMAGING_NAME}")]'
                         f' /parent::XCUIElementTypeOther /following-sibling::XCUIElementTypeButton')

    CHRONIC_AP_IMAGING_DESCRIPTOR = \
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_IMAGING_NAME}")]')
    CHRONIC_AP_IMAGING_DETAILS_BUTTON = \
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_IMAGING_NAME}")]'
                         f' /parent::XCUIElementTypeOther /following-sibling::XCUIElementTypeButton')

    ACUTE_AP_DIAGNOSTIC_PROCEDURE_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_DIAGNOSTIC_PROCEDURE_NAME}")]')
    ACUTE_AP_DIAGNOSTIC_PROCEDURE_DETAILS_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.ACUTE_AP_DIAGNOSTIC_PROCEDURE_NAME}")]'
                         f' /parent::XCUIElementTypeOther /following-sibling::XCUIElementTypeButton')

    CHRONIC_AP_DIAGNOSTIC_PROCEDURE_DESCRIPTOR =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_DIAGNOSTIC_PROCEDURE_NAME}")]')
    CHRONIC_AP_DIAGNOSTIC_PROCEDURE_DETAILS_BUTTON =\
        (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{data.CHRONIC_AP_DIAGNOSTIC_PROCEDURE_NAME}")]'
                         f' /parent::XCUIElementTypeOther /following-sibling::XCUIElementTypeButton')

    REMOVE_DESCRIPTOR_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="crossIcon"]')

    def navigate_to_problem_screen_from_home_screen(self, username, password):
        self.home_screen.do_login(username, password)
        self.wait_for_visibility_and_invisibility_of(self.home_screen.LOGGING_IN_TEXT)
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        self.appointment_screen.crete_non_ehr_appointments('Test problem')
        appointment_time, patient_name = self.appointment_screen\
            .get_selected_appointment_info(self.appointment_screen.NEW_APPOINTMENT)
        self.appointment_screen.wait_and_click(self.appointment_screen
                                               .get_selected_appointment_locator(appointment_time, patient_name))
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        self.wait_and_click(self.PROBLEMS_TAB)
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        return appointment_time, patient_name

    def add_problem(self, problem_name, problem_type):
        self.enter_text_at(self.SEARCH_ADD_CUSTOM_INPUT_FIELD, problem_name, max_wait=2)
        _type = (AppiumBy.XPATH, f'//XCUIElementTypeTable //XCUIElementTypeStaticText[contains(@name,"{problem_name}")]'
                                 f' /preceding-sibling::XCUIElementTypeStaticText')
        box = (AppiumBy.XPATH, f'//XCUIElementTypeTable //XCUIElementTypeStaticText[contains(@name,"{problem_name}")]'
                               f' /preceding-sibling::XCUIElementTypeButton')
        list_of_problems = self.get_elements(self.ADD_PROBLEM_MODAL_PROBLEM_NAMES_LIST)
        for problem in list_of_problems:
            if problem.text == problem_name:
                if self.get_element(_type).text == problem_type:
                    self.wait_and_click(box)
                    self.wait_and_click(self.SELECT_ICON)
                    self.wait_for_invisibility_of(self.SAVING_MODAL)
                    break

    def add_problem_from_suggestion(self, problem_name, problem_type):
        # self.wait_for_existence_of_all(self.ADD_MODAL_LIST_ITEMS)
        time.sleep(3)
        name = (AppiumBy.XPATH, f'(//XCUIElementTypeStaticText[@name="{problem_name}"])[1]')
        _type = (AppiumBy.XPATH,
                f'//XCUIElementTypeTable //XCUIElementTypeStaticText[contains(@name,"{problem_name}")]'
                f' /preceding-sibling::XCUIElementTypeStaticText')
        box = (AppiumBy.XPATH,
               f'//XCUIElementTypeTable //XCUIElementTypeStaticText[contains(@name,"{problem_name}")]'
               f' /preceding-sibling::XCUIElementTypeButton')
        self.scroll_to_locator(name)
        list_of_problems = self.get_elements(name)
        for problem in list_of_problems:
            if problem.text == problem_name:
                if self.get_element(_type).text == problem_type:
                    self.click_and_wait(box)
                    self.click_and_wait(self.SELECT_ICON)
                    self.wait_for_invisibility_of(self.SAVING_MODAL)
                    break

    def remove_problem(self, problem_name):
        if self.is_element_visible(self.ADD_PROBLEMS_ICON, 1):
            self.click_and_wait(self.ADD_PROBLEMS_ICON)
            self.wait_and_click(self.PROBLEMS_ACTIVE_TAB)
            for problem in self.get_elements(self.ADD_PROBLEM_MODAL_PROBLEM_NAMES_LIST):
                if problem.text == problem_name:
                    problem.click()
            self.wait_and_click(self.SELECT_ICON)
            self.wait_for_invisibility_of(self.SAVING_MODAL)

    def remove_all_problem(self):
        if self.is_element_visible(self.ADD_PROBLEMS_ICON):
            self.click_and_wait(self.ADD_PROBLEMS_ICON)
            self.wait_and_click(self.PROBLEMS_ACTIVE_TAB)
            for problem in self.get_elements(self.PROBLEM_CHECKED_BOX):
                problem.click()
            self.wait_and_click(self.SELECT_ICON)
            self.wait_for_invisibility_of(self.SAVING_MODAL)

    def tap_on_problem_from_carousel(self, problem_name):
        if not self.get_element(self.PROBLEMS_TAB).is_selected():
            self.wait_and_click(self.PROBLEMS_TAB)
            self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        if self.is_element_visible(self.carousel_problem_locator(problem_name), 2):
            self.wait_and_click(self.carousel_problem_locator(problem_name))

    def add_descriptor_by_search(self, *descriptor_names):
        for descriptor_name in descriptor_names:
            self.enter_text_at(self.SEARCH_ADD_CUSTOM_INPUT_FIELD, descriptor_name, max_wait=10)
            list_of_descriptor = self.get_elements(self.ADD_MODAL_LIST_ITEMS)
            for descriptor in list_of_descriptor:
                if descriptor.text == descriptor_name:
                    descriptor.click()
                    break
        self.wait_and_click(self.SELECT_ICON)

    def add_descriptor(self, *names):
        """
        Add descriptor from suggestion
        :param names: name for which descriptor need to be added
        """
        list_of_descriptor = self.get_elements(self.ADD_MODAL_LIST_ITEMS)
        for name in names:
            for descriptor in list_of_descriptor:
                if descriptor.text == name:
                    descriptor.click()
                    list_of_descriptor.remove(descriptor)
                    break
        self.wait_and_click(self.SELECT_ICON)


    def click_on_add_block_button(self, problem_name, add_block_locator):
        self.tap_on_problem_from_carousel(problem_name)
        self.scroll_to_locator(add_block_locator)
        self.wait_and_click(add_block_locator)
        if not self.is_element_visible(self.ADD_POP_UP_MODAL_TITLE, 2):
            self.swipe_down()
            if self.is_element_visible(add_block_locator, 3):
                self.wait_and_click(add_block_locator)

    def remove_added_item(self, item_locator):
        """
        remove descriptor block
        :param item_locator: item_locator for which descriptor need to be removed
        """
        self.swipe_on_element(item_locator, 'left')
        self.wait_and_click(self.REMOVE_DESCRIPTOR_BUTTON)

    def carousel_problem_locator(self, problem_name):
        return AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@name,"{problem_name}")]'

    def block_descriptor_locator(self, descriptor_name):
        """
        Returns By locator for block descriptor on problem screen
        :param descriptor_name: descriptor name for which locator is to be extracted
        :return: returns by locator tuple for descriptor name provided
        """
        return (AppiumBy.XPATH, f'//XCUIElementTypeStaticText[contains(@value,"{descriptor_name}")]')

    def descriptor_dropdown_locator(self, descriptor_name, dropdown_position=1):
        """
        Returns By locator for dropdown descriptor like dosage, frequency, action, detail dropdown on problem screen
        :param descriptor_name: descriptor name for which block descriptor dropdown is to be extracted
        :param dropdown_position: dropdown position for which dropdown is
         to be extracted when multiple present within a block descriptor
        :return: returns by locator tuple for descriptor dropdown
        """
        return AppiumBy.XPATH, f'//XCUIElementTypeStaticText[@name="{descriptor_name}"]' \
                               f' /following-sibling::XCUIElementTypeTextField[{dropdown_position}]'

    def descriptor_text_input_locator(self, descriptor_name):
        """
        Returns By locator for free text input descriptor like detail, value, findings on problem screen
        :param descriptor_name: descriptor name for which block descriptor free input is to be extracted
        :return: returns by locator tuple for descriptor free input field
        """
        return AppiumBy.XPATH, f'//XCUIElementTypeStaticText[@name="{descriptor_name}"]' \
                               f' /following-sibling::XCUIElementTypeButton'

    def descriptor_ap_test_text_input_locator(self, descriptor_name):
        """
        Returns By locator for free text input imaging, and diagnostic procedure descriptor on problem screen
        :param descriptor_name: descriptor name for which block descriptor free input is to be extracted
        :return: returns by locator tuple for descriptor free input field
        """
        return AppiumBy.XPATH, f'//XCUIElementTypeStaticText[@name="{descriptor_name}"]' \
                               f' /parent::XCUIElementTypeOther /following-sibling::XCUIElementTypeButton'

    def descriptor_impression_dropdown_locator(self, descriptor_name):
        """
        Returns By locator for impression dropdown descriptor on problem screen
        :param descriptor_name: descriptor name for which block descriptor impression dropdown is to be extracted
        :return: returns by locator tuple for descriptor impression dropdown
        """
        return AppiumBy.XPATH, f'//XCUIElementTypeStaticText[@name="{descriptor_name}"]/parent::XCUIElementTypeOther' \
                               f' /following-sibling::XCUIElementTypeOther /XCUIElementTypeTextField'

    def descriptor_date_locator(self, descriptor_name):
        """
        Returns By locator for date descriptor on problem screen
        :param descriptor_name: descriptor name for which block descriptor date is to be extracted
        :return: returns by locator tuple for descriptor date
        """
        return AppiumBy.XPATH, f'//XCUIElementTypeStaticText[@name="{descriptor_name}"]/parent::XCUIElementTypeOther' \
                               f'/following-sibling::XCUIElementTypeOther /XCUIElementTypeButton'

    def select_from_dropdown(self, value):
        """
        select descriptor value from dropdown
        :param value: value for which dropdown value need to be selected
        """
        list_of_descriptor = self.get_elements(self.ADD_MODAL_LIST_ITEMS)
        for descriptor in list_of_descriptor:
            if descriptor.text == value:
                descriptor.click()
                break

    def set_descriptor_dropdown_value(self, value, descriptor_name, dropdown_position=1):
        """
        select value for dropdown descriptor like dosage, frequency, action, detail dropdown on problem screen
        :param value: value for which value need to be set as dropdown current selection
        :param descriptor_name: descriptor name for which block descriptor dropdown is to be updated
        :param dropdown_position: dropdown position for which dropdown is to be
         updated when multiple present within a block descriptor
        """
        self.wait_and_click(self.descriptor_dropdown_locator(descriptor_name, dropdown_position))
        self.select_from_dropdown(value)
        self.wait_for_invisibility_of(self.SAVING_MODAL)

    def set_impression_dropdown_value(self, value, descriptor_name):
        """
        select value for impression dropdown descriptor on problem screen
        :param value: value for which value need to be set as impression current selection
        :param descriptor_name: descriptor name for which block descriptor impression is to be updated
        """
        self.wait_and_click(self.descriptor_impression_dropdown_locator(descriptor_name))
        self.select_from_dropdown(value)
        self.wait_for_invisibility_of(self.SAVING_MODAL)

    def add_text_on_descriptor_input_field(self, value, descriptor_name):
        """
        Add free text input descriptor like detail, value, findings on problem screen
        :param value: value for which value need to be added on free text input field
        :param descriptor_name: descriptor name for which block descriptor free input field is to be updated
        """
        self.enter_text_at(self.descriptor_text_input_locator(descriptor_name), value, 3)
        self.wait_and_click(self.SELECT_ICON)
        self.wait_for_invisibility_of(self.SAVING_MODAL)

    def add_text_on_ap_test_descriptor_input_field(self, value, descriptor_name):
        """
         Add free text on free text input imaging, and diagnostic procedure field on problem screen
         :param value: value for which value need to be added on free text input field
         :param descriptor_name: descriptor name for which block descriptor free input field is to be updated
         """
        self.enter_text_at(self.descriptor_ap_test_text_input_locator(descriptor_name), value, 3)
        self.wait_and_click(self.SELECT_ICON)

    def set_date(self, set_date, descriptor_name):
        """
        set value for date descriptor on problem screen and the date format must be in yyyy-mm-dd 2021-05-14
        :param set_date: set date for which value need to be set as date
        :param descriptor_name: descriptor name for which block descriptor date is to be updated
        """
        date = datetime.datetime.strptime(set_date, '%Y-%m-%d')
        self.click_and_wait(self.descriptor_date_locator(descriptor_name), 1)
        self.get_element(self.DATE_PICKER).send_keys(date.strftime('%B'))
        date_elements = self.get_elements(self.DATE_PICKER)
        if date_elements[0].text == date.strftime('%B'):
            date_elements[1].send_keys(date.day)
            date_elements[2].send_keys(date.year)
        else:
            date_elements[0].send_keys(date.day)
            date_elements[1].send_keys(date.strftime('%B'))
            date_elements[2].send_keys(date.year)
        self.wait_and_click(self.SELECT_ICON)
        self.wait_for_invisibility_of(self.SAVING_MODAL)


    def add_hpi_current_medications(self, complaint_name, descriptor_name, dosage, frequency):
        self.click_on_add_block_button(complaint_name, self.ADD_CURRENT_MEDICATION_BUTTON)
        self.add_descriptor(descriptor_name)
        self.set_descriptor_dropdown_value(dosage, descriptor_name)
        self.set_descriptor_dropdown_value(frequency, descriptor_name, 2)

    def add_hpi_symptoms(self, complaint_name, descriptor_name):
        self.click_on_add_block_button(complaint_name, self.ADD_SYMPTOMS_BUTTON)
        self.add_descriptor(descriptor_name)

    def add_hpi_lifestyle_treatments(self, complaint_name, descriptor_name, detail):
        self.click_on_add_block_button(complaint_name, self.ADD_LIFESTYLE_TREATMENTS_BUTTON)
        self.add_descriptor(descriptor_name)
        self.add_text_on_descriptor_input_field(detail, descriptor_name)

    def add_hpi_recent_labs(self, complaint_name, descriptor_name, value, impression, date):
        self.click_on_add_block_button(complaint_name, self.ADD_RECENT_LAB_BUTTON)
        self.add_descriptor(descriptor_name)
        self.add_text_on_descriptor_input_field(value, descriptor_name)
        self.set_impression_dropdown_value(impression, descriptor_name)
        self.set_date(date, descriptor_name)

    def add_hpi_treatment_procedures(self, complaint_name, descriptor_name, relief):
        self.click_on_add_block_button(complaint_name, self.ADD_TREATMENT_PROCEDURES_BUTTON)
        self.add_descriptor_by_search(descriptor_name)
        self.set_descriptor_dropdown_value(relief, descriptor_name)

    def add_hpi_recent_imaging(self, complaint_name, descriptor_name, finding, impression, date):
        self.click_on_add_block_button(complaint_name, self.ADD_RECENT_IMAGING_BUTTON)
        self.add_descriptor_by_search(descriptor_name)
        self.add_text_on_descriptor_input_field(finding, descriptor_name)
        self.set_impression_dropdown_value(impression, descriptor_name)
        self.set_date(date, descriptor_name)

    def add_hpi_recent_diagnostics(self, complaint_name, descriptor_name, finding, impression, date):
        self.click_on_add_block_button(complaint_name, self.ADD_RECENT_DIAGNOSTICS_BUTTON)
        self.add_descriptor_by_search(descriptor_name)
        self.add_text_on_descriptor_input_field(finding, descriptor_name)
        self.set_impression_dropdown_value(impression, descriptor_name)
        self.set_date(date, descriptor_name)

    def add_ap_status(self, complaint_name, descriptor_name):
        self.click_on_add_block_button(complaint_name, self.ADD_STATUS_BUTTON)
        self.select_from_dropdown(descriptor_name)

    def add_ap_progression(self, complaint_name, descriptor_name):
        self.click_on_add_block_button(complaint_name, self.ADD_PROGRESSION_BUTTON)
        self.add_descriptor(descriptor_name)

    def add_ap_medications(self, complaint_name, descriptor_name, action, dosage, frequency):
        self.click_on_add_block_button(complaint_name, self.ADD_MEDICATIONS_BUTTON)
        self.add_descriptor(descriptor_name)
        self.set_descriptor_dropdown_value(action, descriptor_name)
        self.set_descriptor_dropdown_value(dosage, descriptor_name, 2)
        self.set_descriptor_dropdown_value(frequency, descriptor_name, 3)

    def add_ap_lifestyle_treatments(self, complaint_name, descriptor_name, detail):
        self.click_on_add_block_button(complaint_name, self.ADD_LIFESTYLE_TREATMENTS_BUTTON)
        self.add_descriptor(descriptor_name)
        self.add_text_on_descriptor_input_field(detail, descriptor_name)

    def add_ap_labs(self, complaint_name, descriptor_name, detail):
        self.click_on_add_block_button(complaint_name, self.ADD_LAB_BUTTON)
        self.add_descriptor(descriptor_name)
        self.set_descriptor_dropdown_value(detail, descriptor_name)

    def add_ap_imaging(self, complaint_name, descriptor_name, imaging):
        self.click_on_add_block_button(complaint_name, self.ADD_IMAGING_BUTTON)
        self.add_descriptor_by_search(descriptor_name)
        self.add_text_on_ap_test_descriptor_input_field(imaging, descriptor_name)

    def add_ap_diagnostic_procedures(self, complaint_name, descriptor_name, diagnostic_procedures):
        self.click_on_add_block_button(complaint_name, self.ADD_DIAGNOSTIC_PROCEDURES_BUTTON)
        self.add_descriptor_by_search(descriptor_name)
        self.add_text_on_ap_test_descriptor_input_field(diagnostic_procedures, descriptor_name)

    def add_ap_treatment_procedure(self, complaint_name, descriptor_name, opinion, detail):
        self.click_on_add_block_button(complaint_name, self.ADD_TREATMENT_PROCEDURES_BUTTON)
        self.add_descriptor_by_search(descriptor_name)
        self.swipe_down()
        self.set_descriptor_dropdown_value(opinion, descriptor_name)
        self.add_text_on_descriptor_input_field(detail, descriptor_name)

    def perform_ehr_send_note(self):
        if self.is_element_visible(self.EMPTY_STATE_ADD_PROBLEM_BUTTON, 10):
            self.wait_and_click(self.EMPTY_STATE_ADD_PROBLEM_BUTTON)
            self.add_problem(data.CHRONIC_PROBLEM_NAME, 'CHRONIC')
        self.click_on_add_block_button(data.CHRONIC_PROBLEM_NAME, self.ADD_SYMPTOMS_BUTTON)
        self.add_descriptor(data.CHRONIC_HPI_SYMPTOMS['name'])
        self.wait_and_click(self.NOTE_TAB)
        self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        if not self.is_clickable(self.SEND_BUTTON):
            self.wait_and_click(self.PROBLEMS_TAB)
            self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
            self.wait_and_click(self.NOTE_TAB)
            self.wait_for_visibility_and_invisibility_of(self.LOADING_MODAL)
        self.wait_and_click(self.SEND_BUTTON)
        try:
            if self.is_element_visible(self.NOTE_UPLOAD_STATUS_MESSAGE, 12):
                self.wait_and_click(self.OK_BUTTON, 1)
        except TimeoutException:
            print('Auto accepted')

    def add_problem_in_empty_state(self, problem_name, problem_type):
        self.wait_and_click(self.PROBLEMS_TAB)
        self.wait_for_invisibility_of(self.LOADING_MODAL)
        self.wait_and_click(self.EMPTY_STATE_ADD_PROBLEM_BUTTON)
        self.add_problem(problem_name, problem_type)
        self.wait_for_invisibility_of(self.SAVING_MODAL)
