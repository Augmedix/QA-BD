import time

import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

import conftest as cnf
from pages.admin_pages.admin_home_page import AdminHomePage
from pages.admin_pages.admin_login_page import LoginPage
from pages.admin_pages.admin_provider_page import AdminProviderPage
from pages.reset_password_screen_page import ResetPasswordScreenPage
from pages.home_screen_page import HomeScreenPage
from pages.appointment_screen_page import AppointmentScreenPage
from testcases.base_test import BaseTest
from data.data import Data
from pages.support_screen_page import SupportScreenPage
from utils.email_client import EmailClient
import urllib.parse


class TestHomeScreen(BaseTest):
    # """
    # Test cases related to home screen.
    # Test types: Sanity.
    # """

    auto_accept_alert = True
    def setup_class(self):
        self.browser_driver = cnf.get_requested_browser()
        self.admin_login_page = LoginPage(self.browser_driver)
        self.admin_home_page = AdminHomePage(self.browser_driver)
        self.admin_provider_page = AdminProviderPage(self.browser_driver)
        self.home_screen_page = HomeScreenPage(self.appium_driver)
        self.reset_password_screen_page = ResetPasswordScreenPage(self.appium_driver)
        self.support_screen_page = SupportScreenPage(self.appium_driver)
        self.appointment_screen_page = AppointmentScreenPage(self.appium_driver)
        self.data = Data()
        self.email_client = EmailClient()
        self.home_screen_page.handle_improve_security_modal()
        self.home_screen_page.handle_notification_modal()
        self.passcode = [self.home_screen_page.FIRST_PIN,
                         self.home_screen_page.SECOND_PIN,
                         self.home_screen_page.THIRD_PIN,
                         self.home_screen_page.FOURTH_PIN]

    @pytest.fixture
    def reset_app(self):
        self.home_screen_page.reset_app()

    @pytest.fixture
    def click_on_back_button_after_testcase(self):
        yield
        self.home_screen_page.click_and_wait(self.reset_password_screen_page.BACK_BTN, 1)

    @pytest.fixture
    def navigate_back_to_app_after_testcase(self):
        yield
        self.home_screen_page.open_the_app()

    @pytest.fixture
    def click_on_passcode_screen_back_button(self):
        yield
        self.home_screen_page.click_and_wait(self.home_screen_page.PASSCODE_SCREEN_BACK_BUTTON,1)

    @pytest.fixture
    def create_new_account_and_login_to_app(self):
        pytest.provider_email = self.home_screen_page.complete_athena_sign_up_steps_from_app()
        self.admin_login_page.goto_login_page()
        self.admin_login_page.login_to_admin_portal()
        self.admin_home_page.navigate_to_provider_list_page()
        self.admin_provider_page.search_provider(pytest.provider_email)
        self.admin_provider_page.navigate_to_edit_provider_page()
        self.admin_provider_page.enter_text_at(AdminProviderPage.UNIQUE_ID_INPUT_LOCATOR, 'TEST-TEST')
        self.admin_provider_page.click_and_wait(AdminProviderPage.UPDATE_PROVIDER_BUTTON_LOCATOR, 0)
        self.admin_provider_page.enable_ed_flag()
        self.admin_provider_page.request_password_reset(pytest.provider_email)
        password_reset_token = self.email_client.wait_to_get_password_reset_token(pytest.provider_email,
                                                                                  pytest.configs.get_config(
                                                                                      'go_provider_create_password_mail_subject'))
        encoded_token = urllib.parse.quote(password_reset_token)
        self.home_screen_page.reset_password_from_gwp(encoded_token, self.data.reset_password)
        self.home_screen_page.close_the_app()
        self.home_screen_page.open_the_app()
        self.home_screen_page.login_with_password(pytest.provider_email, self.data.reset_password)

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.usefixtures("navigate_back_to_app_after_testcase")
    @pytest.mark.sanity
    def test_sign_up_from_app(self):
        with allure.step('Sign up related text and button are present'):
            assert self.home_screen_page.is_element_visible(self.home_screen_page.DONT_HAVE_AN_ACCOUNT_TEXT,3)

            assert self.home_screen_page.get_text_by_locator(self.home_screen_page.DONT_HAVE_AN_ACCOUNT_TEXT,
                                                             1) == self.data.DONT_HAVE_AN_ACCOUNT_TEXT
            assert self.home_screen_page.is_element_visible(self.home_screen_page.SIGN_UP_BUTTON, 3)

        self.home_screen_page.complete_athena_sign_up_steps_from_app()
        with allure.step('Sign up should be completed and navigated to account initiated page'):
            assert self.home_screen_page.is_element_visible(self.home_screen_page.ACCOUNT_INITIATED_TEXT, 3)
            assert self.home_screen_page.get_text_by_locator(self.home_screen_page.ACCOUNT_INITIATED_TEXT, 3)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.ACCOUNT_INITIATED_MSG, 3)
            assert self.home_screen_page.get_text_by_locator(self.home_screen_page.ACCOUNT_INITIATED_MSG, 3)

    @pytest.mark.regression
    def test_sign_up_from_app_creates_account_in_admin_portal(self):
        pytest.provider_email = self.home_screen_page.complete_athena_sign_up_steps_from_app()
        pytest.EMAIL_FIELD = (AppiumBy.XPATH, f"//XCUIElementTypeTextField[@value='{pytest.provider_email}']")
        self.admin_login_page.goto_login_page()
        self.admin_login_page.login_to_admin_portal()
        self.admin_home_page.navigate_to_provider_list_page()
        self.admin_provider_page.search_provider(pytest.provider_email)
        actual_info_list = self.admin_provider_page.get_latest_provider_info()
        with allure.step('Searched provider data should match'):
            assert actual_info_list == [self.data.SIGNUP_LAST_NAME, self.data.SIGNUP_FIRST_NAME, pytest.provider_email,
                                        'Default Signup Initial Site', 'pending', '']

        self.admin_provider_page.navigate_to_edit_provider_page()

        with allure.step('Provider edit page data should match'):
            assert self.admin_provider_page.get_attribute(AdminProviderPage.FIRST_NAME_INPUT_LOCATOR,
                                                          'value') == self.data.SIGNUP_FIRST_NAME
            assert self.admin_provider_page.get_attribute(AdminProviderPage.LAST_NAME_INPUT_LOCATOR,
                                                          'value') == self.data.SIGNUP_LAST_NAME
            assert self.admin_provider_page.get_attribute(AdminProviderPage.EMAIL_INPUT_LOCATOR,
                                                          'value') == pytest.provider_email
            assert self.admin_provider_page.get_attribute(AdminProviderPage.PHONE_NO_INPUT_LOCATOR,
                                                          'value') == self.data.SIGNUP_PHONE_NUMBER
            assert self.admin_provider_page.get_attribute(AdminProviderPage.NPI_INPUT_LOCATOR,
                                                          'value') == self.data.SIGNUP_NPI_NUMBER
            assert self.admin_provider_page.get_attribute(AdminProviderPage.UNIQUE_ID_INPUT_LOCATOR,
                                                          'value') == ''
            assert self.admin_provider_page.get_element(AdminProviderPage.GO_PROVIDER_FLAG_LOCATOR).is_selected()
            assert not self.admin_provider_page.get_element(AdminProviderPage.NRT_PROVIDER_FLAG_LOCATOR).is_selected()
            assert self.admin_provider_page.is_text_proper(AdminProviderPage.PROVIDER_STATUS_LOCATOR, 'Pending')

            self.admin_provider_page.click_and_wait(AdminProviderPage.PROFILE_INFORMATION_LOCATOR, 10)
            self.admin_provider_page.scroll_into_view(AdminProviderPage.ZIPCODE_INPUT_LOCATOR)

            # assert self.admin_provider_page.get_attribute(AdminProviderPage.EHR_INPUT_LOCATOR,
            #                                               'value') == self.data.ATHENA_PRAC_ID
            assert self.admin_provider_page.get_attribute(AdminProviderPage.PRACTICE_NAME_INPUT_LOCATOR,
                                                          'value') == self.data.PRACTICE_NAME
            assert self.admin_provider_page.get_attribute(AdminProviderPage.ADDRESS_INPUT_LOCATOR,
                                                          'value') == self.data.BUSINESS_ADDRESS
            assert self.admin_provider_page.get_attribute(AdminProviderPage.ZIPCODE_INPUT_LOCATOR,
                                                          'value') == self.data.ZIP_CODE

    @pytest.mark.regression
    def test_new_provider_email_creation_email_content(self):
        with allure.step('New Provider signup mail should match'):
            result_from_email_as_text = self.email_client.get_email_as_html(pytest.configs.get_config('email_to'),
                                                                            'Augmedix Go - New sign-up!')
            print(result_from_email_as_text)
            expected_info = """![](https://augmedix.com/wp-content/uploads/2022/02/Primary-Logo-1.png)### New Sign-up!First name:  RandomLast name:  NameWork email:  variable_emailNPI number:  1245319599Phone number:  (013) 746-2836Specialty:  AnesthesiaAthena Practice ID:  123Practice name:  RandomBusiness address:  Florida/AlaskaState:  AlaskaZip code:  3533EHR:  athenaProduct:  Go"""
            expected_info = expected_info.replace('variable_email', pytest.provider_email)
            print(expected_info)
            assert expected_info == result_from_email_as_text

    @pytest.mark.regression
    def test_without_unique_id_reset_password_resetting_password_from_admin_will_show_error(self):
        with allure.step('Without unique id, the new provider can not reset password'):
            self.admin_provider_page.request_password_reset(pytest.provider_email)
            assert self.admin_provider_page.is_element_visible(AdminProviderPage.ERROR_TEXT_LOCATOR, 60)

    @pytest.mark.regression
    def test_success_reset_password_from_admin(self):
        with allure.step('After updating unique id, the new provider can reset password'):
            self.admin_home_page.navigate_to_provider_list_page()
            self.admin_provider_page.search_provider(pytest.provider_email)
            self.admin_provider_page.navigate_to_edit_provider_page()
            self.admin_provider_page.enter_text_at(AdminProviderPage.UNIQUE_ID_INPUT_LOCATOR, 'TEST-TEST')
            self.admin_provider_page.click_and_wait(AdminProviderPage.UPDATE_PROVIDER_BUTTON_LOCATOR, 0)
            assert self.admin_provider_page.is_element_visible(AdminProviderPage.PROVIDER_UPDATED_LOCATOR, 60)
            assert self.admin_provider_page.get_attribute(AdminProviderPage.UNIQUE_ID_INPUT_LOCATOR,
                                                          'value') == 'TEST-TEST'

    @pytest.mark.regression
    def test_get_password_reset_token_from_email_and_reset_password(self):
        with allure.step('Get password reset token from email & navigate to Reset page'):
            self.admin_provider_page.request_password_reset(pytest.provider_email)
            password_reset_token = self.email_client.wait_to_get_password_reset_token(pytest.provider_email,
                                                                                      pytest.configs.get_config(
                                                                                          'go_provider_create_password_mail_subject'))
            # URL encoding
            encoded_token = urllib.parse.quote(password_reset_token)
            self.home_screen_page.navigate_to_password_reset_url(encoded_token)

        with allure.step('Validate UI elements of Reset Page'):
            assert self.home_screen_page.is_element_visible(HomeScreenPage.GWP_AUGMEDIX_LOGO_IMG_LOCATOR, 5)
            assert self.home_screen_page.is_element_visible(HomeScreenPage.GWP_PASSWORD_INPUT_LOCATOR, 5)
            assert self.home_screen_page.is_element_visible(HomeScreenPage.GWP_CONFIRM_PASSWORD_INPUT_LOCATOR,
                                                            5)
            # assert self.home_screen_page.is_element_visible(HomeScreenPage.GWP_SHOW_PASSWORD_INPUT_LOCATOR, 5)
            assert self.home_screen_page.is_element_visible(HomeScreenPage.GWP_SHOW_PASSWORD_LABEL_LOCATOR, 15)
            assert self.home_screen_page.is_element_visible(HomeScreenPage.GWP_BUTTON_LOCATOR, 5)
            assert self.home_screen_page.is_element_visible(HomeScreenPage.GWP_8_PLUS_CHARACTER_LOCATOR, 5)
            assert self.home_screen_page.is_element_visible(HomeScreenPage.GWP_UPPERCASE_LETTER_LOCATOR, 5)
            assert self.home_screen_page.is_element_visible(HomeScreenPage.GWP_LOWERCASE_LETTER_LOCATOR, 5)
            assert self.home_screen_page.is_element_visible(HomeScreenPage.GWP_NUMBER_LOCATOR, 5)
            assert self.home_screen_page.is_element_visible(HomeScreenPage.GWP_REPEATED_CHARACTER_LOCATOR, 5)
            assert self.home_screen_page.is_element_visible(HomeScreenPage.GWP_PASSWORD_MATCH_CHARACTER_LOCATOR,
                                                            5)

        self.home_screen_page.enter_text_at(HomeScreenPage.GWP_PASSWORD_INPUT_LOCATOR, self.data.reset_password)
        self.home_screen_page.click_and_wait(HomeScreenPage.KEYBOARD_DONE_BUTTON, 1)
        self.home_screen_page.enter_text_at(HomeScreenPage.GWP_CONFIRM_PASSWORD_INPUT_LOCATOR, self.data.reset_password)
        self.home_screen_page.click_and_wait(HomeScreenPage.KEYBOARD_DONE_BUTTON, 1)
        self.home_screen_page.click_and_wait(HomeScreenPage.GWP_BUTTON_LOCATOR, 5)
        # with allure.step('Provider should be taken to the App store Augmedix Go app page'):
            # assert self.home_screen_page.is_element_visible(HomeScreenPage.AUGMEDIX_GO_APP_APP_STORE_TITLE_LOCATOR,
            #                                                 10)
            # assert self.home_screen_page.is_element_visible(HomeScreenPage.
            #                                                 AUGMEDIX_GO_APP_APP_STORE_DOWNLOAD_BUTTON_LOCATOR,
            #                                                 10)

    @pytest.mark.regression
    def test_provider_status_in_admin(self):
        with allure.step('After successfully reseting password, the provider status should be Active'):
            self.admin_home_page.navigate_to_provider_list_page()
            self.admin_provider_page.search_provider(pytest.provider_email)
            self.admin_provider_page.navigate_to_edit_provider_page()
            assert self.admin_provider_page.is_text_proper(AdminProviderPage.PROVIDER_STATUS_LOCATOR,
                                                           'Active')

    @pytest.mark.regression
    def test_newly_created_provider_can_login_to_ed_app(self):
        self.admin_provider_page.scroll_into_view(AdminProviderPage.ENABLE_ROS_FLAG_LOCATOR)
        self.admin_provider_page.click_and_wait(AdminProviderPage.ENABLE_ED_FLAG_LOCATOR, 5)
        self.admin_provider_page.scroll_into_view(AdminProviderPage.UPDATE_PROVIDER_BUTTON_LOCATOR)
        self.admin_provider_page.click_and_wait(AdminProviderPage.UPDATE_PROVIDER_BUTTON_LOCATOR, 5)
        self.home_screen_page.open_the_app()
        self.home_screen_page.handle_app_store_location_permission_modal()
        self.home_screen_page.handle_improve_security_modal()
        self.home_screen_page.login_with_password(pytest.provider_email,
                                                  self.data.reset_password, True)
        with allure.step('Newly created provider can successfully login with email & password'):
            assert self.home_screen_page.is_element_visible(HomeScreenPage.CREATE_A_PIN_LOCATOR, 5)

    @pytest.mark.regression
    def test_ui_elements_of_create_pin_screen(self):
        with allure.step('Passcode screen should be displayed with proper UI after reopening the app'):
            # assert self.home_screen_page.is_element_visible(self.home_screen_page.BACK_BUTTON_ICON_LOCATOR, 5)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.CREATE_A_PIN_LOCATOR, 5)
            # assert self.home_screen_page.is_element_visible(self.home_screen_page.BACK_BUTTON_LOCATOR, 2)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.CREATE_PIN_INSTRUCTION_LOCATOR, 2)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_SCREEN_PINS, 2)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_LOGIN_KEYBOARD, 2)

    @pytest.mark.regression
    def test_confirm_pin_screen(self):
        self.home_screen_page.retry_click_passcode(retries=4)
        with allure.step('Passcode screen should be displayed with proper UI after reopening the app'):
            # assert self.home_screen_page.is_element_visible(self.home_screen_page.BACK_BUTTON_ICON_LOCATOR, 5)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.VERIFY_PIN_LOCATOR, 5)
            # assert self.home_screen_page.is_element_visible(self.home_screen_page.BACK_BUTTON_LOCATOR, 2)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.CREATE_PIN_INSTRUCTION_LOCATOR, 2)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_SCREEN_PINS, 2)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_LOGIN_KEYBOARD, 2)

        self.home_screen_page.retry_click_passcode(retries=4)
        self.home_screen_page.handle_post_login_events()
        with allure.step('After confirming passcode, the provider navigated to tracker tab'):
            # assert self.home_screen_page.is_element_visible(HomeScreenPage.PASSCODE_SET_SUCCESS_LOCATOR, 5)
            assert self.home_screen_page.is_element_visible(AppointmentScreenPage.TRACKER_TAB, 10)

    @pytest.mark.regression
    def test_login_with_new_device(self):
        self.appium_driver2 = cnf.get_selected_device(change_device_time=True)
        self.home_screen_page = HomeScreenPage(self.appium_driver2)
        self.home_screen_page.login_with_password(pytest.provider_email, self.data.reset_password)
        with allure.step('Passcode screen should be displayed with proper UI after reopening the app'):
            assert not self.home_screen_page.is_element_visible(self.home_screen_page.WELCOME_BACK_PASSCODE_TEXT, 5)
            assert not self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_SCREEN_PROVIDER_NAME, 2)
            assert not self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_SCREEN_RESET_LINK, 2)
            assert not self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_SCREEN_PINS, 2)
            assert not self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_LOGIN_KEYBOARD, 2)
        with allure.step('After confirming passcode, the provider navigated to tracker tab'):
            # assert self.home_screen_page.is_element_visible(HomeScreenPage.PASSCODE_SET_SUCCESS_LOCATOR, 5)
            assert self.home_screen_page.is_element_visible(AppointmentScreenPage.TRACKER_TAB, 10)
        self.appium_driver2.quit()
        self.home_screen_page = HomeScreenPage(self.appium_driver)

    @pytest.mark.regression
    def test_provider_gets_passcode_screen_after_reopening_app_within_12_hours(self):
        self.home_screen_page.close_the_app()
        self.home_screen_page.open_the_app()
        with allure.step('Passcode screen should be displayed with proper UI after reopening the app'):
            assert self.home_screen_page.is_element_visible(self.home_screen_page.WELCOME_BACK_PASSCODE_TEXT, 5)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_SCREEN_PROVIDER_NAME, 2)
            assert self.home_screen_page.get_text_by_locator(self.home_screen_page.PASSCODE_SCREEN_PROVIDER_NAME,
                                                             2) == self.data.SIGNUP_FIRST_NAME + ' ' + self.data.SIGNUP_LAST_NAME
            assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_SCREEN_RESET_LINK, 2)
            assert self.home_screen_page.get_text_by_locator(self.home_screen_page.PASSCODE_SCREEN_RESET_LINK,
                                                             2) == self.data.PASSCODE_SCREEN_RESET_LINK_TEXT
            assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_SCREEN_PINS, 2)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_LOGIN_KEYBOARD, 2)

        self.home_screen_page.login_with_passcode()
        with allure.step('User should be able to login everytime successfully using PINCODE for 12 hours'):
            assert self.home_screen_page.is_element_visible(self.appointment_screen_page.TRACKER_TAB, 10)

    @pytest.mark.regression
    def test_provider_gets_password_screen_after_logout_12_hours(self):
        self.appium_driver3 = cnf.get_selected_device(change_device_time=True)
        self.home_screen_page = HomeScreenPage(self.appium_driver3)
        self.reset_password_screen_page = ResetPasswordScreenPage(self.appium_driver3)
        self.support_screen_page = SupportScreenPage(self.appium_driver3)
        self.appointment_screen_page = AppointmentScreenPage(self.appium_driver3)
        self.home_screen_page.open_the_app()
        self.home_screen_page.login_with_password(pytest.provider_email, self.data.reset_password)
        with allure.step('Welcome passcode screen should not be displayed'):
            assert not self.home_screen_page.is_element_visible(self.home_screen_page.WELCOME_BACK_PASSCODE_TEXT,
                                                                5)
        self.appium_driver3.quit()
        self.home_screen_page = HomeScreenPage(self.appium_driver)
        self.reset_password_screen_page = ResetPasswordScreenPage(self.appium_driver)
        self.support_screen_page = SupportScreenPage(self.appium_driver)
        self.appointment_screen_page = AppointmentScreenPage(self.appium_driver)

    @pytest.mark.regression
    def test_app_reset_from_passcode_screen(self):
        self.home_screen_page.close_the_app()
        self.home_screen_page.open_the_app()
        self.home_screen_page.click_and_wait(HomeScreenPage.PASSCODE_SCREEN_RESET_LINK, 5)
        with allure.step('App should get reset and user should be presented with LOGIN screen.'):
            with allure.step('Home screen components are displayed'):
                assert self.home_screen_page.is_element_visible(self.home_screen_page.AX_LOGO, 5)
                assert self.home_screen_page.is_element_visible(self.home_screen_page.GET_STARTED_LABEL, 1)
                assert self.home_screen_page.is_element_visible(self.home_screen_page.EMAIL_FIELD, 1)
                assert not self.home_screen_page.is_element_visible(self.home_screen_page.PASSWORD_FIELD, 1)
            with allure.step('Face ID button should be displayed and clickable'):
                assert self.home_screen_page.is_element_visible(self.home_screen_page.FACE_ID, 1)
                assert self.home_screen_page.is_clickable(self.home_screen_page.FACE_ID, 1)
            with allure.step('Log in button should be displayed and clickable'):
                assert self.home_screen_page.is_element_visible(self.home_screen_page.LOGIN_BUTTON, 1)
                assert self.home_screen_page.is_clickable(self.home_screen_page.LOGIN_BUTTON, 1)

            assert self.home_screen_page.is_element_visible(HomeScreenPage.DONT_HAVE_AN_ACCOUNT_TEXT, 1)
            assert self.home_screen_page.is_element_visible(HomeScreenPage.SIGN_UP_BUTTON, 1)
            assert self.home_screen_page.is_element_visible(HomeScreenPage.HAVING_DIFFICULTIES_BUTTON, 1)
            with allure.step('Email input field should contain the signed out email address'):
                assert self.home_screen_page.is_text_proper(HomeScreenPage.EMAIL_FIELD, pytest.provider_email)

    @pytest.mark.regression
    def test_having_difficulties_button_from_home_screen(self):
        self.home_screen_page.click_and_wait(HomeScreenPage.HAVING_DIFFICULTIES_BUTTON, 5)
        with allure.step('User should navigate to support screen'):
            self.support_screen_page.common_support_screen_assertions()

    @pytest.mark.regression
    def test_incorrect_password_text_goes_away_after_3_seconds(self):
        self.home_screen_page.close_the_app()
        self.home_screen_page.open_the_app()
        self.home_screen_page.login_with_passcode(False)
        assert self.home_screen_page.is_element_visible(self.home_screen_page.FIRST_INCORRECT_PASSCODE_MESSAGE_LOCATOR, 15)
        # Record the start time
        start_time = time.time()
        self.home_screen_page.wait_for_invisibility_of(self.home_screen_page.FIRST_INCORRECT_PASSCODE_MESSAGE_LOCATOR, 10)
        with allure.step('INCORRECT PIN Should get cleared up after 3 seconds'):
            # Record the end time
            end_time = time.time()
            # Calculate the time taken
            time_taken = end_time - start_time
            print(time_taken)
            assert 1 <= time_taken <= 3

    @pytest.mark.regression
    def test_reset_pin_flow(self):
        self.home_screen_page.close_the_app()
        self.home_screen_page.open_the_app()
        self.home_screen_page.click_and_wait_for_visibility(HomeScreenPage.HAVING_DIFFICULTIES_BUTTON,
                                                            SupportScreenPage.RESET_PIN_BUTTON, 5)
        self.home_screen_page.click_and_wait(SupportScreenPage.RESET_PIN_BUTTON, 5)
        with allure.step('App should get reset and user should be presented with LOGIN screen.'):
            with allure.step('Home screen components are displayed'):
                assert self.home_screen_page.is_element_visible(self.home_screen_page.AX_LOGO, 5)
                assert self.home_screen_page.is_element_visible(self.home_screen_page.GET_STARTED_LABEL, 1)
                assert self.home_screen_page.is_element_visible(self.home_screen_page.EMAIL_FIELD, 1)
                assert not self.home_screen_page.is_element_visible(self.home_screen_page.PASSWORD_FIELD, 1)
            with allure.step('Face ID button should be displayed and clickable'):
                assert self.home_screen_page.is_element_visible(self.home_screen_page.FACE_ID, 1)
                assert self.home_screen_page.is_clickable(self.home_screen_page.FACE_ID, 1)
            with allure.step('Log in button should be displayed and clickable'):
                assert self.home_screen_page.is_element_visible(self.home_screen_page.LOGIN_BUTTON, 1)
                assert self.home_screen_page.is_clickable(self.home_screen_page.LOGIN_BUTTON, 1)

            assert self.home_screen_page.is_element_visible(HomeScreenPage.DONT_HAVE_AN_ACCOUNT_TEXT, 1)
            assert self.home_screen_page.is_element_visible(HomeScreenPage.SIGN_UP_BUTTON, 1)
            assert self.home_screen_page.is_element_visible(HomeScreenPage.HAVING_DIFFICULTIES_BUTTON, 1)
            with allure.step('Email input field should contain the signed out email address'):
                assert self.home_screen_page.is_text_proper(HomeScreenPage.EMAIL_FIELD, pytest.provider_email)

            self.home_screen_page.click_and_wait(HomeScreenPage.LOGIN_BUTTON, 2)
            self.home_screen_page.enter_text_at(HomeScreenPage.PASSWORD_FIELD, self.data.reset_password)
            self.home_screen_page.click_and_wait(HomeScreenPage.LOGIN_BUTTON, 2)
            with allure.step('Passcode screen should be displayed with proper UI after reopening the app'):
                # assert self.home_screen_page.is_element_visible(self.home_screen_page.BACK_BUTTON_ICON_LOCATOR, 5)
                assert self.home_screen_page.is_element_visible(self.home_screen_page.CREATE_A_PIN_LOCATOR, 5)
                # assert self.home_screen_page.is_element_visible(self.home_screen_page.BACK_BUTTON_LOCATOR, 2)
                assert self.home_screen_page.is_element_visible(self.home_screen_page.CREATE_PIN_INSTRUCTION_LOCATOR, 2)
                assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_SCREEN_PINS, 2)
                assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_LOGIN_KEYBOARD, 2)

            self.home_screen_page.retry_click_passcode()
            with allure.step('Passcode screen should be displayed with proper UI after reopening the app'):
                # assert self.home_screen_page.is_element_visible(self.home_screen_page.BACK_BUTTON_ICON_LOCATOR, 5)
                assert self.home_screen_page.is_element_visible(self.home_screen_page.VERIFY_PIN_LOCATOR, 5)
                # assert self.home_screen_page.is_element_visible(self.home_screen_page.BACK_BUTTON_LOCATOR, 2)
                assert self.home_screen_page.is_element_visible(self.home_screen_page.CREATE_PIN_INSTRUCTION_LOCATOR, 2)
                assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_SCREEN_PINS, 2)
                assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_LOGIN_KEYBOARD, 2)

            self.home_screen_page.retry_click_passcode()
            with allure.step('After confirming pin, the provider navigated to Tracker page'):
                # assert self.home_screen_page.is_element_visible(HomeScreenPage.PASSCODE_SET_SUCCESS_LOCATOR, 5)
                assert self.home_screen_page.is_element_visible(AppointmentScreenPage.TRACKER_TAB, 10)
            self.home_screen_page.logout_from_app()
            self.home_screen_page.close_the_app()
            self.home_screen_page.open_the_app()
            self.home_screen_page.login_with_password(pytest.provider_email, self.data.reset_password,False)
            with allure.step('Provider can login with the new pin'):
                assert self.home_screen_page.is_element_visible(AppointmentScreenPage.TRACKER_TAB, 10)

    @pytest.mark.regression
    def test_account_gets_blocked_due_to_5_invalid_passcode_login_attempts(self):
        pytest.skip()
        for _ in range(5):
            for _ in range(5):
                self.home_screen_page.click_and_wait(self.home_screen_page.INCORRECT_PASSCODE_LOGIN_PASS)

            with allure.step('Login should not work with incorrect passcode'):
                assert self.home_screen_page.is_element_visible(self.home_screen_page.INCORRECT_PIN_TEXT, 2)
                assert self.home_screen_page.get_text_by_locator(self.home_screen_page.INCORRECT_PIN_TEXT,
                                                                 2) == self.data.INCORRECT_PIN_TEXT
                assert not self.home_screen_page.is_element_visible(self.appointment_screen_page.TRACKER_TAB, 2)
            self.home_screen_page.wait_for_invisibility_of(self.home_screen_page.INCORRECT_PIN_TEXT, 2)
        assert self.home_screen_page.is_element_visible(self.home_screen_page.INCORRECT_PIN_TEXT, 2)

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.sanity
    @pytest.mark.usefixtures("reset_app")
    def test_add_value_in_email_field(self):
        self.home_screen_page.handle_notification_modal()
        with allure.step('Value can be added properly in email field'):
            self.home_screen_page.enter_text_at(self.home_screen_page.EMAIL_FIELD, self.data.home_screen_provider)
            assert self.home_screen_page.get_attribute(self.home_screen_page.EMAIL_FIELD,
                                                       'value') == self.data.home_screen_provider
            self.home_screen_page.click_and_wait(self.home_screen_page.KEYBOARD_DONE_BUTTON, 1)

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.sanity
    def test_add_value_in_password_field(self):
        self.home_screen_page.handle_notification_modal()
        with allure.step('Value can be added properly in password field'):
            self.home_screen_page.click_and_wait(HomeScreenPage.LOGIN_BUTTON, 2)
            self.home_screen_page.enter_text_at(self.home_screen_page.PASSWORD_FIELD, self.data.provider_password)
            assert self.home_screen_page.get_attribute(self.home_screen_page.PASSWORD_FIELD,
                                                       'value') == self.data.provider_password_in_bullet

            # Hide the done button to click on Login button
            self.home_screen_page.click_and_wait(self.home_screen_page.KEYBOARD_DONE_BUTTON, 1)

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.sanity
    @pytest.mark.usefixtures("reset_app")
    def test_login_with_invalid_credentials(self):
        with allure.step('Login should not work with valid email and invalid password'):
            self.home_screen_page.login_with_password(self.data.home_screen_provider, "invalid_pass", False)

            assert self.home_screen_page.is_element_visible(self.home_screen_page.INVALID_CREDENTIAL_TEXT, 3)
            # assert not self.home_screen_page.is_element_visible(self.home_screen_page.LOGGING_IN_MODAL, 3)
        with allure.step('Login should not work with invalid email and valid password'):
            self.home_screen_page.reset_app()
            self.home_screen_page.enter_text_at(self.home_screen_page.EMAIL_FIELD, "invalid_email@augmedix.com")
            self.home_screen_page.click_and_wait(self.home_screen_page.KEYBOARD_DONE_BUTTON, 1)
            self.home_screen_page.click_and_wait(HomeScreenPage.LOGIN_BUTTON)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.INVALID_USERNAME_CREDENTIAL_TEXT, 3)
            assert not self.home_screen_page.is_element_visible(self.home_screen_page.LOGGING_IN_MODAL, 3)

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.sanity
    @pytest.mark.usefixtures("reset_app")
    def test_login_with_valid_credentials(self):
        with allure.step('Login button should work properly'):
            self.home_screen_page.login_with_password(self.data.home_screen_provider, self.data.provider_password)
        # with allure.step('Logging in modal should be appear and then disappear'):      //Not able to capture
        #     assert self.home_screen_page.is_element_visible(self.home_screen_page.LOGGING_IN_MODAL,5)

        with allure.step('Appointment screen should be displayed with Tracker, To-DO tabs'):
            assert self.home_screen_page.is_element_visible(self.appointment_screen_page.TRACKER_TAB, 5)
            # assert self.home_screen_page.is_element_visible(self.appointment_screen_page.TO_DO_TAB, 1)

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.sanity
    @pytest.mark.usefixtures("reset_app")
    def test_passcode_screen_appears(self):
        with allure.step('Passcode screen should be displayed with proper UI after reopening the app'):
            assert self.home_screen_page.is_element_visible(self.home_screen_page.WELCOME_BACK_PASSCODE_TEXT, 5)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_SCREEN_PROVIDER_NAME, 2)
            assert self.home_screen_page.get_text_by_locator(self.home_screen_page.PASSCODE_SCREEN_PROVIDER_NAME,
                                                             2) == self.data.HOME_SCREEN_PROVIDER_NAME
            assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_SCREEN_RESET_LINK, 2)
            assert self.home_screen_page.get_text_by_locator(self.home_screen_page.PASSCODE_SCREEN_RESET_LINK,
                                                             2) == self.data.PASSCODE_SCREEN_RESET_LINK_TEXT
            assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_SCREEN_PINS, 2)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.PASSCODE_LOGIN_KEYBOARD, 2)

    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.sanity
    @pytest.mark.usefixtures("reset_app")
    def test_login_with_incorrect_passcode(self):
        self.home_screen_page.login_with_passcode(False)
        with allure.step('Login should not work with incorrect passcode'):
            assert self.home_screen_page.is_element_visible(self.home_screen_page.FIRST_INCORRECT_PASSCODE_MESSAGE_LOCATOR,
                                                            2)
            assert not self.home_screen_page.is_element_visible(self.appointment_screen_page.TRACKER_TAB, 2)


    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.sanity
    @pytest.mark.usefixtures("reset_app")
    def test_login_with_correct_passcode(self):
        for _ in self.passcode:
            self.home_screen_page.click_and_wait(self.home_screen_page.PASSCODE_LOGIN_PASS)

        self.home_screen_page.handle_post_login_events(1)
        self.home_screen_page.handle_app_update_modal()

        with allure.step('Appointment screen should be displayed with Tracker, To-DO tabs'):
            assert self.home_screen_page.is_element_visible(self.appointment_screen_page.TRACKER_TAB, 5)
            # assert self.home_screen_page.is_element_visible(self.appointment_screen_page.TO_DO_TAB, 1)
            

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_home_screen_components(self):
        self.home_screen_page.logout_from_app()
        with allure.step('Home screen components are displayed'):
            assert self.home_screen_page.is_element_visible(self.home_screen_page.AX_LOGO, 5)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.GET_STARTED_LABEL, 1)
            assert self.home_screen_page.is_element_visible(pytest.EMAIL_FIELD, 1)
            assert self.home_screen_page.is_element_visible(self.home_screen_page.SIGN_UP_BUTTON, 1)
        with allure.step('Face ID button should be displayed and clickable'):
            assert self.home_screen_page.is_element_visible(self.home_screen_page.FACE_ID, 1)
            assert self.home_screen_page.is_clickable(self.home_screen_page.FACE_ID, 1)
        with allure.step('Log in button should be displayed and clickable'):
            assert self.home_screen_page.is_element_visible(self.home_screen_page.LOGIN_BUTTON, 1)
            assert self.home_screen_page.is_clickable(self.home_screen_page.LOGIN_BUTTON, 1)


    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_invalid_passcode_shows_number_of_attempts_left(self):
        self.home_screen_page.login_with_password(self.data.home_screen_provider,self.data.provider_password, False)
        self.home_screen_page.wait_for_visibility_of(self.appointment_screen_page.TRACKER_TAB,5)
        self.home_screen_page.close_the_app()
        self.home_screen_page.open_the_app()

        self.home_screen_page.wait_for_visibility_of(self.home_screen_page.WELCOME_BACK_PASSCODE_TEXT,5)
        self.home_screen_page.login_with_passcode(correct_passcode=False)
        with allure.step('Verify message is shown for first incorrect passcode'):
            assert self.home_screen_page.is_element_visible(self.home_screen_page.FIRST_INCORRECT_PASSCODE_MESSAGE_LOCATOR,2)
            # assert self.home_screen_page.is_text_proper(self.home_screen_page.FIRST_INCORRECT_PASSCODE_MESSAGE_LOCATOR,
            #                                                  self.data.FIRST_INCORRECT_PASSCODE_MESSAGE_TEXT)
        
        self.home_screen_page.wait_for_invisibility_of(self.home_screen_page.FIRST_INCORRECT_PASSCODE_MESSAGE_LOCATOR,5)
        self.home_screen_page.login_with_passcode(correct_passcode=False)
        with allure.step('Verify message is shown for second incorrect passcode'):
            assert self.home_screen_page.is_element_visible(self.home_screen_page.SECOND_INCORRECT_PASSCODE_MESSAGE_LOCATOR,2)
            # assert self.home_screen_page.is_text_proper(self.home_screen_page.SECOND_INCORRECT_PASSCODE_MESSAGE_LOCATOR,
            #                                                  self.data.SECOND_INCORRECT_PASSCODE_MESSAGE_TEXT)
            
        self.home_screen_page.wait_for_invisibility_of(self.home_screen_page.SECOND_INCORRECT_PASSCODE_MESSAGE_LOCATOR,5)    
        self.home_screen_page.login_with_passcode(correct_passcode=False)
        with allure.step('Verify for third incorrect passcode, provider will be navigated to login screen'):
            self.home_screen_page.common_home_screen_components_assertions()

    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures("click_on_passcode_screen_back_button")
    @pytest.mark.regression
    def test_passcode_fail_counter_resets_after_login(self):
        self.home_screen_page.login_with_password(self.data.home_screen_provider, self.data.provider_password, False)
        self.home_screen_page.close_the_app()
        self.home_screen_page.open_the_app()
        self.home_screen_page.login_with_passcode(False)
        self.home_screen_page.wait_for_invisibility_of(self.home_screen_page.FIRST_INCORRECT_PASSCODE_MESSAGE_LOCATOR,5)
        self.home_screen_page.login_with_passcode()
        self.home_screen_page.handle_post_login_events()
        self.home_screen_page.wait_for_visibility_of(self.appointment_screen_page.TRACKER_TAB,5)
        self.home_screen_page.close_the_app()
        self.home_screen_page.open_the_app()
        self.home_screen_page.login_with_passcode(False)
        with allure.step('Incorrect passcode message for first attempt should be shown'):
            assert self.home_screen_page.is_element_visible(self.home_screen_page.FIRST_INCORRECT_PASSCODE_MESSAGE_LOCATOR,2)
            # assert self.home_screen_page.is_text_proper(self.home_screen_page.FIRST_INCORRECT_PASSCODE_MESSAGE_LOCATOR,
            #                                             self.data.FIRST_INCORRECT_PASSCODE_MESSAGE_TEXT)
            
    
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.usefixtures("click_on_passcode_screen_back_button")
    @pytest.mark.regression
    def test_passcode_fail_counter_does_not_reset_after_taking_app_to_background(self):
        self.home_screen_page.login_with_password(self.data.home_screen_provider,self.data.provider_password, False)
        self.home_screen_page.wait_for_visibility_of(self.appointment_screen_page.TRACKER_TAB,5)
        self.home_screen_page.close_the_app()
        self.home_screen_page.open_the_app()
        self.home_screen_page.login_with_passcode(False)
        self.home_screen_page.wait_for_invisibility_of(self.home_screen_page.FIRST_INCORRECT_PASSCODE_MESSAGE_LOCATOR,5)
        self.home_screen_page.send_app_to_background(60)
        self.home_screen_page.wait_for_visibility_of(self.home_screen_page.WELCOME_BACK_PASSCODE_TEXT,5)
        self.home_screen_page.login_with_passcode(False)
        with allure.step('Incorrect passcode after bringing back app from background should show incorrect passcode message for second attempt'):
            assert self.home_screen_page.is_element_visible(self.home_screen_page.SECOND_INCORRECT_PASSCODE_MESSAGE_LOCATOR,2)
            # assert self.home_screen_page.is_text_proper(self.home_screen_page.SECOND_INCORRECT_PASSCODE_MESSAGE_LOCATOR,
            #                                             self.data.SECOND_INCORRECT_PASSCODE_MESSAGE_TEXT)
