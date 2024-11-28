import urllib.parse
from test.ui.pages.admin_pages.admin_home_page import AdminHomePage
import test.ui.conftest as cnf
from test.ui.data.data import Data
from test.ui.pages.admin_pages.admin_login_page import LoginPage
from test.ui.pages.admin_pages.admin_provider_page import AdminProviderPage
from test.ui.pages.appointment_screen_page import AppointmentScreenPage
from test.ui.pages.home_screen_page import HomeScreenPage
from test.ui.testcases.base_test import BaseTest
from test.ui.utils.email_client import EmailClient
import allure
import pytest


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

    """ @pytest.fixture
    def click_on_back_button_after_testcase(self):
        yield
        self.home_screen_page.click_and_wait(self.reset_password_screen_page.BACK_BTN, 1) """

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
    



    
##TEST