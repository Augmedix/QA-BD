import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import allure

from test.ui.data.data import Data
from test.ui.pages.base_page import BasePage


class HomeScreenPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.data = Data()

    FACE_ID_PERMISSION_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeAlert[contains(@name,"to use Face ID?")]')
    ALLLOW_BTN_SEND_NOTIFI_MODAL = (AppiumBy.XPATH, '//*[@name="Allow"]')
    DO_NOT_ALLOW_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Don’t Allow")
    FACE_ID_NOT_ALLOWED_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeAlert[@name="Face ID Not Allowed"]')
    DO_NOT_ALLOW_BUTTON_AT_FACE_ID_NOT_ALLOWED_MODAL = (AppiumBy.ACCESSIBILITY_ID, "Don't Allow")
    AX_LOGO = (AppiumBy.ACCESSIBILITY_ID, 'AugmedixLogo')
    GET_STARTED_LABEL = (AppiumBy.ACCESSIBILITY_ID, 'Please login to get started.')

    EMAIL_FIELD = (AppiumBy.XPATH, "//XCUIElementTypeTextField")
    PASSWORD_FIELD = (AppiumBy.XPATH, '//XCUIElementTypeSecureTextField')
    KEYBOARD_DONE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Done')
    KEYBOARD_RETURN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Return')
    FACE_ID = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Button"]')
    LOGIN_BUTTON = (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@label='Log In']")
    SCAN_QR_CODE_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Scan QR code from computer"]')
    HAVING_DIFFICULTIES_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Having difficulties?"]')
    LOGGING_IN_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Logging In"]/parent::XCUIElementTypeOther')
    LOGGING_IN_TEXT = (AppiumBy.ACCESSIBILITY_ID, 'Logging In')
    DONT_HAVE_AN_ACCOUNT_TEXT = (AppiumBy.ACCESSIBILITY_ID, "Don't have account?")
    SIGN_UP_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Sign up')
    INVALID_CREDENTIAL_TEXT = (AppiumBy.ACCESSIBILITY_ID, 'Password is invalid')
    INVALID_USERNAME_CREDENTIAL_TEXT = (AppiumBy.ACCESSIBILITY_ID, 'Username is invalid')

    LYNX_SPLASH_SCREEN = \
        (AppiumBy.XPATH,
         '//XCUIElementTypeApplication[contains(@name, "Lynx")]/XCUIElementTypeWindow[2]/XCUIElementTypeOther/XCUIElementTypeOther[1]')
    SECURE_LAYER_DASHBOARD = \
        (AppiumBy.XPATH,
         '//XCUIElementTypeApplication[contains(@name, "Lynx")]/XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther')
    FACE_ID_NOT_ENROLLED_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeAlert[@name="Face ID Not Enrolled"]')
    Ok_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Ok')
    CANCEL_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Cancel')
    DONT_ENROLL_BUTTON_OF_FACE_ID_NOT_ENROLLED_MODAL = (AppiumBy.ACCESSIBILITY_ID, "Don't Enroll")
    HAMBURGER_MENU = (AppiumBy.XPATH, '//XCUIElementTypeNavigationBar/XCUIElementTypeButton')
    LOGOUT_BUTTON = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Log Out"]')

    FACE_ID_NOT_RECOGNIZED_MODAL = (AppiumBy.XPATH, '//XCUIElementTypeAlert[@name="Face Not Recognized"]')
    TRY_FACE_ID_AGAIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Try Face ID Again')
    ENTER_USERNAME_PASSWORD_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Enter Username/Password')
    FACE_ID_MODALS = (AppiumBy.XPATH, '//XCUIElementTypeAlert')
    FACE_ID_PERMISSION_MODAL_MESSAGES = ['Do you want to allow “Lynx Dev” to use Face ID?',
                                         'Do you want to allow “Lynx Stage” to use Face ID?',
                                         'Do you want to allow “Augmedix Go” to use Face ID?']
    BLUETOOTH_PERMISSION_MODAL = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "Would Like to Use Bluetooth")]')
    NOTIFICATION_PERMISSION_MODAL = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[contains(@name, "Would Like to Send You Notifications")]')
    OK_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'OK')
    ALLOW_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Allow')
    FEEDBACK_CROSS = (AppiumBy.ACCESSIBILITY_ID, 'Close')
    FEEDBACK_TITLE = (AppiumBy.ACCESSIBILITY_ID, 'Daily Check-in')
    FEEDBACK_STAR = (AppiumBy.ACCESSIBILITY_ID, 'Rating')
    COMPLETENESS_IMPROVEMENT_CATEGORY = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Completeness"]')
    THIRTY_MINUTES_SAVED_LOCATOR = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "30 mins"`]')
    STRONGLY_AGREE_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther')
    FEEDBACK_DONE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Horizontal scroll bar, 1 page')
    FEEDBACK_SEND_BUTTON = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeButton[`label == "Send"`]')
    WELCOME_BACK_PASSCODE_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Welcome Back,"]')
    WELCOME_BACK_SESSION_EXPIRED_PASSCODE_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Welcome back,"]')
    WELCOME_BACK_IDENTITY_CONFIRM_TEXT = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Welcome back,"]')
    ATHENA_HEALTH_EHR = (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="Augmedix Go"]/XCUIElementTypeImage[2]')
    NEXT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Next')
    USER_PROFILE_TITLE = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="User Profile"]')
    FIRST_NAME_FIELD = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "First name"`]')
    LAST_NAME_FIELD = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "Last name"`]')
    WORK_EMAIL_FIELD = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "Email"`]')
    NPI_NUM_FIELD = (AppiumBy.IOS_CLASS_CHAIN,
                     '**/XCUIElementTypeOther[`label == "Augmedix Go"`]/XCUIElementTypeOther[7]/XCUIElementTypeTextField')
    PHONE_NUM_FIELD = (AppiumBy.IOS_CLASS_CHAIN,
                       '**/XCUIElementTypeOther[`label == "Augmedix Go"`]/XCUIElementTypeOther[8]/XCUIElementTypeTextField')
    SPECIALTY_DROPDOWN = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`value == "Specialty"`]')
    ANESTHESIA_SPECIALTY_SELECT = (AppiumBy.ACCESSIBILITY_ID, 'Anesthesia')
    ATHENA_PRACTICE_ID = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "Practice ID"`]')
    # PRACTICE_NAME_FIELD = (AppiumBy.IOS_CLASS_CHAIN,'**/XCUIElementTypeTextField[`value == "Name"`]')
    PRACTICE_NAME_FIELD = (
        AppiumBy.XPATH, '//XCUIElementTypeOther[@name="Augmedix Go"]/XCUIElementTypeOther[12]/XCUIElementTypeTextField')
    BUSINESS_ADDRESS_FIELD = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "Address"`]')
    STATE_DROPDOWN = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`value == "State"`]')
    ALASKA_STATE_SELECT = (AppiumBy.ACCESSIBILITY_ID, 'Alaska')
    ZIP_CODE_FIELD = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeTextField[`value == "Code"`]')
    # POLICY_AGREEMENT = (AppiumBy.ACCESSIBILITY_ID,'I agree to the Augmedix Privacy Policy, Terms and Conditions')
    POLICY_AGREEMENT = (AppiumBy.XPATH,
                        '//*[@name="I agree to the Augmedix" and ./following-sibling::*[@name="Privacy Policy, Terms and Conditions"]]')
    # BUSINESS_AGREEMENT = (AppiumBy.ACCESSIBILITY_ID,'I agree to the Augmedix Business Associate Agreement')
    BUSINESS_AGREEMENT = (AppiumBy.XPATH,
                          '//*[@name="I agree to the Augmedix" and ./following-sibling::*[@name="Business Associate Agreement"]]')
    ACCOUNT_INITIATED_TEXT = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeOther[`label == "Account initiated"`]')
    ACCOUNT_INITIATED_MSG = (AppiumBy.ACCESSIBILITY_ID,
                             'An Augmedix team member will be reaching out within 1 business day to help with next steps.')
    IMPROVE_SECURITY_MODAL = (AppiumBy.XPATH, '//*[@value="Improve Security"]')
    DISMISS_BUTTON = (AppiumBy.XPATH, '//*[@name="Dismiss"]')
    CLOSE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Close')
    CONNECT_TO_ACCESSORIES_MODAL = (AppiumBy.XPATH,
                                    '//XCUIElementTypeStaticText[contains(@name,"to Connect to Accessories")] | //XCUIElementTypeStaticText[contains(@name,"would like to use Bluetooth for new connections")]')
    PASSCODE_SCREEN_RESET_LINK = (
        AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "(Not you? Tap here to change.)"`]')
    FIRST_PIN = (AppiumBy.XPATH,
                 '//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[1]')
    SECOND_PIN = (AppiumBy.XPATH,
                  '//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[2]')
    THIRD_PIN = (AppiumBy.XPATH,
                 '//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[3]')
    FOURTH_PIN = (AppiumBy.XPATH,
                  '//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]')
    PASSCODE_SCREEN_PROVIDER_NAME = (AppiumBy.ACCESSIBILITY_ID, 'Random Name')
    PASSCODE_SCREEN_PINS = (AppiumBy.XPATH,
                            '//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]')
    PASSCODE_LOGIN_KEYBOARD = (AppiumBy.XPATH,
                               '//XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]')
    PASSCODE_LOGIN_PASS = (AppiumBy.XPATH, '//XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeImage')
    INCORRECT_PASSCODE_LOGIN_PASS = (
        AppiumBy.XPATH, '//XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeImage')
    APP_UPDATE_MODAL = (AppiumBy.XPATH, '//*[@type="XCUIElementTypeOther" and ./*[@value="Update Available"]]')
    SKIP_BUTTON = (AppiumBy.XPATH, '//*[@name="Skip"]')
    INCORRECT_PIN_TEXT = (AppiumBy.ACCESSIBILITY_ID, 'Incorrect PIN')
    NOT_YOU_TAP_HERE = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name = "(Not you? Tap here to change.)"]')

    BOTTOM_TAB_URL_INPUT_LOCATOR = (AppiumBy.NAME, 'TabBarItemTitle')
    URL_INPUT_LOCATOR = (AppiumBy.NAME, 'URL')
    RELOAD_URL_LOCATOR = (AppiumBy.NAME, 'ReloadButton')
    GO_URL_LOCATOR = (AppiumBy.NAME, 'Go')

    GWP_AUGMEDIX_LOGO_IMG_LOCATOR = (AppiumBy.XPATH, "//XCUIElementTypeOther[@name='Augmedix Go']/XCUIElementTypeImage")
    GWP_SET_PASSWORD_HEADER_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Set Password"]')
    GWP_PASSWORD_LABEL_LOCATOR = (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='Password']")
    GWP_CONFIRM_PASSWORD_LABEL_LOCATOR = (
        AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='Confirm password']")
    GWP_SHOW_PASSWORD_LABEL_LOCATOR = (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@name='Show password']")
    GWP_PASSWORD_INPUT_LOCATOR = (AppiumBy.XPATH, '(//XCUIElementTypeSecureTextField[@value="*******"])[1]')
    GWP_CONFIRM_PASSWORD_INPUT_LOCATOR = GWP_PASSWORD_INPUT_LOCATOR
    GWP_SHOW_PASSWORD_INPUT_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeSwitch[@name="Show password"]')
    GWP_BUTTON_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Next"]')
    GWP_VALIDATION_LIST_LOCATOR = (AppiumBy.XPATH, "//ul[contains(@class, '_validation_list')]")
    GWP_8_PLUS_CHARACTER_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="8+ characters"]')
    GWP_UPPERCASE_LETTER_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Uppercase letter (A-Z)"]')
    GWP_LOWERCASE_LETTER_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Lowercase letter (a-z)"]')
    GWP_NUMBER_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Number (0-9)"]')
    GWP_REPEATED_CHARACTER_LOCATOR = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="No more than 3 repeated characters"]')
    GWP_PASSWORD_MATCH_CHARACTER_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Passwords match"]')
    GWP_ALLOW_LOCATION_LOCATOR = (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Allow Once']")
    AUGMEDIX_GO_APP_APP_STORE_TITLE_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@value="Augmedix Go"]')
    AUGMEDIX_GO_APP_APP_STORE_DOWNLOAD_BUTTON_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeButton[@label="GET"]')
    APP_STORE_LOCATION_PERMISSION_MODAL_TITLE_LOCATOR = (AppiumBy.XPATH,'//*[@value="Allow “App Store” to use your approximate location?"]')
    APP_STORE_ALLOW_LOCATION_LOCATOR = (AppiumBy.XPATH, "//XCUIElementTypeButton[@name='Allow Once']")
    BACK_BUTTON_LOCATOR = (AppiumBy.XPATH,
                           '//XCUIElementTypeApplication[@name="Lynx Stage"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton')
    CREATE_A_PIN_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@value="Create a PIN"]')
    CREATE_PIN_INSTRUCTION_LOCATOR = (AppiumBy.XPATH,
                                      '//XCUIElementTypeStaticText[@value="Your PIN will allow quick access to the app after inactivity. For your security, you\'ll need to re-enter your password every 12 hours."]')
    VERIFY_PIN_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@value="Verify your PIN"]')
    BACK_BUTTON_ICON_LOCATOR = (AppiumBy.XPATH,
                                '//XCUIElementTypeApplication[@name="Lynx Stage"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton')
    PASSCODE_SET_SUCCESS_LOCATOR = (
        AppiumBy.XPATH, '//XCUIElementTypeStaticText[@value="Your passcode has been updated!"]')
    SESSION_EXPIRED_MODAL = (AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Session Expiring"`]')
    NON_SECURE_LAYER_SESSION_EXPIRED_MODAL = (AppiumBy.ACCESSIBILITY_ID, 'Due to inactivity your session is expired')
    # button - accessibilty yes, no
    CONTINUE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, 'Continue')
    PASSCODE_CONFIRM_SCREEN_PROVIDER_NAME = (AppiumBy.ACCESSIBILITY_ID, Data().PASSCODE_CONFIRM_SCREEN_PROVIDER_NAME)
    FIRST_INCORRECT_PASSCODE_MESSAGE_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, '2 attempts left, then forced relogin')
    SECOND_INCORRECT_PASSCODE_MESSAGE_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, '1 attempts left, then forced relogin')
    PASSCODE_SCREEN_BACK_BUTTON = (AppiumBy.XPATH,
                                   '//XCUIElementTypeWindow/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeButton')

    SESSION_EXPIRING_MODAL_TITLE_LOCATOR = (AppiumBy.XPATH, "//XCUIElementTypeStaticText[@value='Session Expiring']")
    SESSION_EXPIRING_MODAL_BODY_TEXT_LOCATOR = (
        AppiumBy.XPATH, "//XCUIElementTypeStaticText[@value='Your session will expire soon. Do you need more time?']")
    SESSION_EXPIRING_MODAL_NO_BUTTON_LOCATOR = (AppiumBy.XPATH, "//XCUIElementTypeButton[@label='No']")
    SESSION_EXPIRING_MODAL_YES_BUTTON_LOCATOR = (AppiumBy.XPATH, "//XCUIElementTypeButton[@label='Yes']")
    PASSCODE_CONTINUE_BUTTON_LOCATOR = (AppiumBy.XPATH, "//XCUIElementTypeButton[@label='Continue']")
    SESSION_EXPIRED_MODAL_TEXT_LOCATOR = (
        AppiumBy.XPATH, "//XCUIElementTypeStaticText[@value='Due to inactivity your session is expired']")
    SESSION_EXPIRED_OK_BUTTON_LOCATOR = (AppiumBy.XPATH, "//XCUIElementTypeButton[@label='Ok']")

    SKIP_DOWNLOAD_APP_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Skip"]')
    BACK_BUTTON_SUPPORT_SCREEN_LOCATOR = (AppiumBy.XPATH, '//*[@type="XCUIElementTypeButton" and ./following-sibling::*[@name="Support"]]')

    def current_textarea_text(self):
        current_message_text = self.get_js_executed_result('#ajs-quick-message-body-text', 'value')
        print("current message txt " + current_message_text)
        return current_message_text

    def handle_face_id_modal(self):
        try:
            self.wait_for_visibility_of(self.FACE_ID_MODALS, 8)
            alert_text = self.get_text_by_locator(self.FACE_ID_MODALS)
            if alert_text in self.FACE_ID_PERMISSION_MODAL_MESSAGES:
                self.click_and_wait(self.DO_NOT_ALLOW_BUTTON, 1)
                self.wait_for_visibility_of(self.FACE_ID_MODALS, 4)
                self.click_and_wait(self.DO_NOT_ALLOW_BUTTON_AT_FACE_ID_NOT_ALLOWED_MODAL, 1)

            elif alert_text == 'Face ID Not Allowed':
                self.click_and_wait(self.DO_NOT_ALLOW_BUTTON_AT_FACE_ID_NOT_ALLOWED_MODAL, 1)

            elif alert_text == 'Face Not Recognized':
                if self.is_element_visible(self.ENTER_USERNAME_PASSWORD_BUTTON, 2):
                    self.click_and_wait(self.ENTER_USERNAME_PASSWORD_BUTTON, 1)
                elif self.is_element_visible(self.CANCEL_BUTTON, 2):
                    self.click_and_wait(self.CANCEL_BUTTON, 5)

            else:
                print(f'{self.get_text_by_locator(self.FACE_ID_MODALS)} modal is present')
        except (NoSuchElementException, TimeoutException):
            print('Face id modal is not displayed')

    def logout_from_app(self):
        self.wait_for_visibility_of(self.HAMBURGER_MENU, 15)
        self.click_and_wait(self.HAMBURGER_MENU, 1)
        self.wait_for_visibility_of(self.LOGOUT_BUTTON, 5)
        self.click_and_wait(self.LOGOUT_BUTTON, 1)
        self.wait_for_visibility_of(self.EMAIL_FIELD, 10)

    # def do_login(self, username, password):
    #     self.handle_face_id_modal()
    #     self.enter_text_at(self.EMAIL_FIELD, username, 3)
    #     self.enter_text_at(self.PASSWORD_FIELD, password, 2)
    #     self.click_and_wait(self.KEYBOARD_DONE_BUTTON, 1)
    #     self.click_and_wait(self.LOGIN_BUTTON)

    def handle_improve_security_modal(self):
        if self.is_element_visible(self.IMPROVE_SECURITY_MODAL, 2):
            self.click_and_wait(self.DISMISS_BUTTON, 1)

    def login_with_password(self, username, password,
                            handle_post_login: bool = True, check_for_passcode=False):
        self.handle_notification_modal()
        self.enter_text_at(self.EMAIL_FIELD, username, max_wait=10)
        self.click_and_wait(self.KEYBOARD_DONE_BUTTON, 1)
        self.click_and_wait(self.LOGIN_BUTTON, 2)
        self.enter_text_at(self.PASSWORD_FIELD, password, max_wait=30)
        self.click_and_wait(self.KEYBOARD_DONE_BUTTON, 1)
        self.click_and_wait(self.LOGIN_BUTTON, 1)
        if check_for_passcode:
            self.handle_passcode_for_new_user()
        if handle_post_login:
            self.handle_post_login_events()
        # self.handle_bluetooth_permission_modal()

    def login_with_passcode(self, correct_passcode: bool = True):
        if correct_passcode:
            for _ in range(4):
                self.click_and_wait(self.PASSCODE_LOGIN_PASS)
            self.handle_post_login_events(1)
            self.handle_app_update_modal()
        else:
            for _ in range(4):
                self.click_and_wait(self.INCORRECT_PASSCODE_LOGIN_PASS)

    def handle_post_login_events(self, wait_for_EOD=3):
        """
        Handle EOD feedback and other prompts if they appear after logging in

        Args:
            wait_for_EOD: wait time for EOD summary page to be visible. Default value 4 seconds
        """
        self.handle_bluetooth_permission_modal()

        if (self.is_element_visible(self.FEEDBACK_TITLE, wait_for_EOD)):
            self.click_and_wait(self.FEEDBACK_STAR)
            self.click_and_wait(self.THIRTY_MINUTES_SAVED_LOCATOR)
            self.click_and_wait(self.STRONGLY_AGREE_LOCATOR)
            self.click_and_wait(self.FEEDBACK_SEND_BUTTON)

        self.handle_connect_to_accessories_modal()
        self.handle_update_app_modal()

    def handle_update_app_modal(self):
        if self.is_element_visible(self.SKIP_DOWNLOAD_APP_LOCATOR, 5):
            self.click_and_wait_for_invisibility(self.SKIP_DOWNLOAD_APP_LOCATOR, 5)
            print('Update app modal handled')

    def handle_bluetooth_permission_modal(self):
        if self.is_element_visible(self.BLUETOOTH_PERMISSION_MODAL, 15):
            if self.is_element_visible(self.OK_BUTTON, 1):
                self.click_and_wait(self.OK_BUTTON, 1)
            else:
                self.click_and_wait(self.ALLOW_BUTTON, 1)
        else:
            print("Bluetooth permission modal not present")

    def complete_athena_sign_up_steps_from_app(self):
        provider_email = self.data.SIGNUP_WORK_EMAIL
        self.click_and_wait(self.SIGN_UP_BUTTON, 2)
        self.wait_for_visibility_of(self.ATHENA_HEALTH_EHR, 60)
        self.click_and_wait(self.ATHENA_HEALTH_EHR, 1)
        self.click_and_wait(self.NEXT_BUTTON, 2)
        self.wait_for_visibility_of(self.USER_PROFILE_TITLE, 20)
        ### ENTER PROFILE DETAILS
        self.enter_text_at(self.FIRST_NAME_FIELD, self.data.SIGNUP_FIRST_NAME)
        self.enter_text_at(self.LAST_NAME_FIELD, self.data.SIGNUP_LAST_NAME)
        self.enter_text_at(self.WORK_EMAIL_FIELD, provider_email)
        self.enter_text_at(self.NPI_NUM_FIELD, self.data.SIGNUP_NPI_NUMBER)
        self.enter_text_at(self.PHONE_NUM_FIELD, self.data.SIGNUP_PHONE_NUMBER)
        self.click_and_wait(self.SPECIALTY_DROPDOWN, 1)
        self.wait_for_visibility_of(self.ANESTHESIA_SPECIALTY_SELECT, 5)
        self.click_and_wait(self.ANESTHESIA_SPECIALTY_SELECT, 1)
        self.enter_text_at(self.ATHENA_PRACTICE_ID, self.data.ATHENA_PRAC_ID)
        self.click_and_wait(self.KEYBOARD_DONE_BUTTON, 1)
        self.enter_text_at(self.PRACTICE_NAME_FIELD, self.data.PRACTICE_NAME)
        self.enter_text_at(self.BUSINESS_ADDRESS_FIELD, self.data.BUSINESS_ADDRESS)
        self.click_and_wait(self.STATE_DROPDOWN, 1)
        self.wait_for_visibility_of(self.ALASKA_STATE_SELECT, 5)
        self.click_and_wait(self.ALASKA_STATE_SELECT, 1)
        self.enter_text_at(self.ZIP_CODE_FIELD, self.data.ZIP_CODE)
        self.click_and_wait(self.KEYBOARD_DONE_BUTTON, 1)
        self.click_and_wait(self.POLICY_AGREEMENT, 1)
        self.click_and_wait(self.BUSINESS_AGREEMENT, 1)
        self.click_and_wait(self.NEXT_BUTTON, 1)
        self.wait_for_visibility_of(self.ACCOUNT_INITIATED_TEXT, 60)
        return provider_email

    def handle_connect_to_accessories_modal(self):
        if self.is_element_visible(self.CONNECT_TO_ACCESSORIES_MODAL, 2):
            self.click_and_wait(self.CLOSE_BUTTON, 1)

    def handle_app_update_modal(self):
        if self.is_element_visible(self.APP_UPDATE_MODAL, 2):
            self.click_and_wait(self.SKIP_BUTTON)

    def navigate_to_password_reset_url(self, url, create_password=True):
        if create_password:
            final_url = pytest.configs.get_config('go_web_portal_url') + url
        else:
            final_url = url
        print(final_url)
        self.click_and_wait_for_visibility(self.BOTTOM_TAB_URL_INPUT_LOCATOR,
                                           self.URL_INPUT_LOCATOR, 5)
        self.enter_text_at(self.URL_INPUT_LOCATOR, final_url)
        self.click_and_wait(self.GO_URL_LOCATOR, 5)
        print('Url should be refreshed in mobile browser')

    def reset_password_from_gwp(self, url, password):
        self.navigate_to_password_reset_url(url)
        self.enter_text_at(HomeScreenPage.GWP_PASSWORD_INPUT_LOCATOR, password)
        self.click_and_wait(HomeScreenPage.KEYBOARD_DONE_BUTTON, 1)
        self.enter_text_at(HomeScreenPage.GWP_CONFIRM_PASSWORD_INPUT_LOCATOR, password)
        self.click_and_wait(HomeScreenPage.KEYBOARD_DONE_BUTTON, 1)
        self.click_and_wait(HomeScreenPage.GWP_BUTTON_LOCATOR, 5)

    def retry_click_passcode(self, valid=True, retries=4):
        locator = ''
        if valid:
            locator = self.PASSCODE_LOGIN_PASS
        else:
            locator = self.INCORRECT_PASSCODE_LOGIN_PASS

        for index in range(retries):
            self.click_and_wait(locator)
        print(f'Passcode element clicked {retries} times')

    def handle_notification_modal(self):
        if self.is_element_visible(self.NOTIFICATION_PERMISSION_MODAL, 3):
            self.click_and_wait(self.ALLOW_BUTTON)
            print('Notification allow button clicked')
        else:
            print('Send notification modal does not appear')

    def handle_passcode_for_new_user(self):
        for _ in range(2):
            if self.is_element_visible(HomeScreenPage.PASSCODE_SCREEN_PINS, 5):
                self.retry_click_passcode()
            else:
                break

    def common_home_screen_components_assertions(self):
        with allure.step('Home screen components are displayed'):
            assert self.is_element_visible(self.AX_LOGO, 5)
            assert self.is_element_visible(self.GET_STARTED_LABEL, 1)
            assert self.is_element_visible(self.EMAIL_FIELD, 1)
            assert self.is_element_visible(self.SIGN_UP_BUTTON, 1)
        with allure.step('Face ID button should be displayed and clickable'):
            assert self.is_element_visible(self.FACE_ID, 1)
            assert self.is_clickable(self.FACE_ID, 1)
        with allure.step('Log in button should be displayed and clickable'):
            assert self.is_element_visible(self.LOGIN_BUTTON, 1)
            assert self.is_clickable(self.LOGIN_BUTTON, 1)

    def handle_app_store_location_permission_modal(self):
        if self.is_element_visible(self.APP_STORE_LOCATION_PERMISSION_MODAL_TITLE_LOCATOR,3):
            self.click_and_wait_for_invisibility(self.APP_STORE_ALLOW_LOCATION_LOCATOR,3)
            print('App store location permission modal handled')
        else:
            print('App store location permission modal did not appear')
