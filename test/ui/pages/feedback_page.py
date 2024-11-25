"""This page contains Feedback page object methods & locators"""
import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

from conftest import get_selected_device
from data.data import Data
from pages.base_page import BasePage
from pages.home_screen_page import HomeScreenPage
# from pages.login_page_docapp import LoginPageDocapp
from pages.scp_pages.login_page import LoginPage
from pages.scp_pages.home_page import HomePage


data = Data()

class FeedbackPage(BasePage):
    """This page contains Feedback page object methods & locators"""

    DAILY_CHECK_IN_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, 'Daily Check-in')
    RATE_YOUR_EXPERIENCE_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, 'Rate your experience')
    RATING_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, 'Rating')
    AUGMEDIX_GO_HELP_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, 'Augmedix Go helped you save time on your shift by:')
    AUGMEDIX_GO_RELIEVE_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, 'Augmedix Go relieves the cognitive load of documentation.')
    OTHER_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, 'Other feedback')
    STRONG_DISAGREE_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, 'Strong Disagree')
    STRONG_AGREE_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, 'Strong Agree')
    TEXT_FEEDBACK_TEXT_AREA_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeTextView[@value="Type here..."]')
    SEND_BUTTON_LOCATOR = (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Send"]')
    OTHER_LOCATOR = (AppiumBy.ACCESSIBILITY_ID, 'Other feedback')


    FEEDBACK_MODAL_CROSS = (By.ID, 'ivCancel')
    FEEDBACK_SERVICE_TITLE = (By.ID, 'tvTitle')
    FEEDBACK_RATING_ERROR_LOCATOR = (By.ID, 'tvRatingError')
    RATING_BAR_LOCATOR = (By.ID, 'ratingBar')
    FEEDBACK_SERVICE_RATING_STAR_WHITE = (By.XPATH, '//android.widget.ImageView[1]')
    FEEDBACK_SERVICE_RATING_STAR_YELLOW = (By.ID, 'btn_start')
    FEEDBACK_IMPROVE_SUGGESTION_TEXT = (By.XPATH, '//android.widget.TextView[3]')
    FEEDBACK_IMPROVE_SUGGESTION_PILL = (By.XPATH, '//android.widget.TextView[@text="Completeness"]')
    FEEDBACK_SERVICE_SHOUTOUT_TEXT = (By.XPATH, '//android.widget.TextView[@text="Service shoutouts?"]')
    FEEDBACK_SERVICE_SHOUTOUT_PILL = (By.XPATH, '//android.widget.TextView[@text="Great notes"]')
    FEEDBACK_TEXT = (By.XPATH, '//android.widget.EditText[@text="Any additional details to share?"]')
    FEEDBACK_MIC_ICON = (By.ID, 'ivRecord')
    FEEDBACK_TEXT_FOOTNOTE = (
        By.XPATH,
        '//android.widget.TextView[@text="Feedback is not directly shared with your specialist."]')
    FEEDBACK_DONE_GREY = (By.ID, 'buttonDone')
    FEEDBACK_IMPROVEMENT_LIST_LOCATOR = (
        By.XPATH, '//android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.TextView')
    FEEDBACK_STAR_RATING_LIST_LOCATOR = (By.XPATH, '//android.widget.LinearLayout/android.widget.ImageView')
    FEEDBACK_SERVICE_RATING_STAR_TEXT = (By.ID, 'tvRatingName')
    FEEDBACK_SERVICE_SHOUTOUT_LIST_LOCATOR = (
        By.XPATH, '//android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.TextView')
    FEEDBACK_STAR_FOUR_STAR_LOCATOR = (By.XPATH, '//android.widget.LinearLayout/android.widget.ImageView[4]')
    FEEDBACK_IMPROVEMENT_COPMLETENESS_LOCATOR = (
        By.XPATH,
        '//android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[1]')
    FEEDBACK_IMPROVEMENT_TEMPLATE_USE_LOCATOR = (
        By.XPATH,
        '//android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[4]')
    FEEDBACK_IMPROVEMENT_LOGIN_LOCATOR = (
        By.XPATH,
        '//android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[7]')
    FEEDBACK_IMPROVEMENT_APP_STABILITY_LOCATOR = (
        By.XPATH,
        '//android.widget.LinearLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[10]')
    FEEDBACK_SERVICE_SHOUTOUT_TIME_SAVER_LOCATOR = (
        By.XPATH,
        '//android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[2]')
    FEEDBACK_SERVICE_SHOUTOUT_VALUED_TEAM_MEMBER_LOCATOR = (
        By.XPATH,
        '//android.widget.LinearLayout[2]/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[4]')
    FEEDBACK_AUDIO_RECORDING_TIME_LOCATOR = (By.ID, 'tvRecordingTime')
    FEEDBACK_RECORDING_ADDED_LOCATOR = (By.ID, 'tvRecordingAdded')
    FEEDBACK_DONE_BUTTON_LOCATOR = (By.ID, 'buttonDone')
    THANK_YOU_TEXT_LOCATOR = (By.ID, 'txt_session_title')
    THANK_YOU_SUMMARY_LOCATOR = (By.ID, 'txt_session')
    THANK_YOU_PATIENT_COUNT_LOCATOR = (By.ID, 'txt_patient_count')
    THANK_YOU_PATIENT_DURATION_LOCATOR = (By.ID, 'txt_duration')
    THANK_YOU_BUTTON_DONE_LOCATOR = (By.ID, 'btn_done')
    FEEDBACK_COMMENT_BOX_LOCATOR = (By.ID, 'etComment')
    FEEDBACK_COMMENT_LOCATOR = (By.ID, 'etComment')
    FEEDBACK_RECORDING_STOP_BUTTON_LOCATOR = (By.XPATH, '//android.view.ViewGroup/android.widget.ImageView[2]')
    FEEDBACK_RECORDING_INPROGRESS_TEXT_LOCATOR = (
        By.XPATH, '//android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.TextView')
    FEEDBACK_DONE_BTN = (By.ID, 'buttonDone')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.login_page = LoginPageDocapp(self.driver)

    def eod_selection(self, feedback_criteria):
        self.wait_for_visibility_of(self.FEEDBACK_SERVICE_TITLE, 10)
        if feedback_criteria:
            if 'rating' in feedback_criteria:
                self.provide_star_rating(feedback_criteria['rating'])

            if 'improvements' in feedback_criteria:
                self.select_any_improvement_category(feedback_criteria['improvements'])

            if 'shoutouts' in feedback_criteria:
                self.select_any_shoutout_category(feedback_criteria['shoutouts'])

            if 'textFeedback' in feedback_criteria:
                self.insert_text_feedback(feedback_criteria['textFeedback'])

            if 'audioFeedback' in feedback_criteria:
                self.get_audio_recording_data_after_recording(feedback_criteria['audioFeedback'])

    def click_done_button(self):
        self.click_and_wait(self.FEEDBACK_DONE_BUTTON_LOCATOR)
        return self.driver.get_device_time()

    def provide_star_rating(self, rating_num):
        rating = rating_num - 1
        rating_bar = self.get_element(self.RATING_BAR_LOCATOR, 10)
        rating_element = rating_bar.find_element(By.XPATH, f'//android.widget.ImageView[@index={rating}]')
        rating_element.click()
        print(f'Rating no {rating_num} has been clicked')

    def select_any_improvement_category(self, improvements):
        if improvements:
            if all(isinstance(sublist, list) for sublist in improvements):
                improvements = [item for sublist in improvements for item in sublist]

            for improvement_items in improvements:
                self.click_and_wait((By.XPATH, f'//android.widget.TextView[@text="{improvement_items}"]'), 1)
                print(f'Improvement category {improvement_items} has been clicked')

    def select_any_shoutout_category(self, shoutouts):
        self.scroll_down_mobile()
        if shoutouts:
            if all(isinstance(sublist, list) for sublist in shoutouts):
                shoutouts = [item for sublist in shoutouts for item in sublist]

            for shoutout in shoutouts:
                self.click_and_wait((By.XPATH, f'//android.widget.TextView[@text="{shoutout}"]'), 1)
                print(f'Shoutout category {shoutout} has been clicked')

    def insert_text_feedback(self, text_feedback_text):
        self.scroll_down_mobile()
        self.enter_text_at(text_feedback_text, self.FEEDBACK_COMMENT_BOX_LOCATOR)

    def get_text_feedback_value(self):
        self.wait_for_visibility_of(self.FEEDBACK_COMMENT_LOCATOR, 10)
        return self.get_text_by_locator(self.FEEDBACK_COMMENT_LOCATOR, 5)

    def clear_text_feedback(self):
        self.get_element(self.FEEDBACK_COMMENT_LOCATOR, 5).clear()
        print('text feedback cleared')

    def start_audio_recording(self):
        self.scroll_down_mobile()
        self.clear_text_feedback()
        time.sleep(5)
        self.wait_for_visibility_of(self.FEEDBACK_MIC_ICON, 5)
        self.click_and_wait(self.FEEDBACK_MIC_ICON)

    def is_audio_recording_started(self):
        comment_area_visible = self.is_element_visible(self.FEEDBACK_COMMENT_BOX_LOCATOR, 5)
        stop_recording_button_visible = self.is_element_visible(self.FEEDBACK_RECORDING_STOP_BUTTON_LOCATOR, 5)
        recording_counter_visible = self.is_element_visible(self.FEEDBACK_AUDIO_RECORDING_TIME_LOCATOR, 5)
        return not comment_area_visible and stop_recording_button_visible and recording_counter_visible

    def stop_audio_recording(self):
        self.click_and_wait(self.FEEDBACK_RECORDING_STOP_BUTTON_LOCATOR)

    def get_audio_recording_data_after_recording(self, recording_time):
        self.click_and_wait(self.FEEDBACK_MIC_ICON)
        audio_recording_time = self.get_element(self.FEEDBACK_AUDIO_RECORDING_TIME_LOCATOR, 5)
        current_recording_time = 0
        try:
            while audio_recording_time.is_displayed() and current_recording_time <= recording_time:
                recording_duration = audio_recording_time.text.strip()
                minutes, seconds = map(int, recording_duration.split(':'))
                current_recording_time = minutes * 60 + seconds
                if current_recording_time >= recording_time:
                    break
        except StaleElementReferenceException:
            print('Recording stopped automatically')

        if self.is_element_visible(self.FEEDBACK_RECORDING_STOP_BUTTON_LOCATOR, 5):
            self.click_and_wait(self.FEEDBACK_RECORDING_STOP_BUTTON_LOCATOR)

        return {
            'recording added text': self.get_text_by_locator(self.FEEDBACK_RECORDING_ADDED_LOCATOR, 10),
            'last recorded duration': current_recording_time,
        }

    def initiate_feedback_if_ready(self):
        self.home_screen = HomeScreenPage(self.driver)
        device_time = self.driver.execute_script("mobile: getDeviceTime")
        print(f"Current device time: {device_time}")
        self.home_screen.login_with_password(username=data.feedback_provider,
                                             password=data.provider_password)
        self.driver = get_selected_device(change_device_time=True)
        device_time = self.driver.execute_script("mobile: getDeviceTime")
        print(f"Current device time: {device_time}")

        self.home_screen = HomeScreenPage(self.driver)
        self.home_screen.login_with_password(username=data.feedback_provider,
                                             password=data.provider_password)


    def get_initiate_feedback_data_after_submit(self, browser_instance):
        self.initialize_feedback(browser_instance)
        home_page_scp = HomePage(browser_instance)
        total_hours = home_page_scp.get_attribute(HomePage.TOTAL_HOURS_VALUE, 'value')
        total_patients = home_page_scp.get_attribute(HomePage.TOTAL_PATIENT_INPUT, 'value')
        device_time = self.driver.get_device_time()
        self.click_on_feedback_send_button(home_page_scp)
        return {
            'total_hours': total_hours,
            'total_patients': total_patients,
            'device_time': device_time
        }

    def initialize_feedback(self, browser_instance):
        print('initiating feedback')
        login_page_scp = LoginPage(browser_instance)
        home_page_scp = HomePage(browser_instance)
        login_page_scp.login_to_scp(pytest.configs.get_config('feedback_regression_scribe'))
        home_page_scp.disconnect_from_provider()
        home_page_scp.connect_to_provider('Test Provider, Live_...', 'Primary scribe')
        self.driver.reset()
        self.login_page.login_doc_app_with_credentials('feedback_regression_provider')
        home_page_scp.wait_for_streaming_to_be_started()
        home_page_scp.wait_for_loader()
        home_page_scp.click_and_wait_for_visibility(HomePage.INITIATE_RECAP_BUTTON_LOCATOR,
                                                     HomePage.INITIATE_RECAP_SEND_BUTTON_LOCATOR)

    def click_on_feedback_send_button(self, scp_driver_instance):
        scp_driver_instance.click_and_wait_for_invisibility(HomePage.INITIATE_RECAP_SEND_BUTTON_LOCATOR, 10)

    def check_done_button_status(self):
        done_button = self.get_element(self.FEEDBACK_DONE_BTN, 2)
        return done_button.is_enabled()

    def clear_text_feedback_for_audio_feedback(self, feedback_criteria):
        if 'audioFeedback' in feedback_criteria:
            self.clear_text_feedback()

    def is_feedback_screen_visible(self, waiting_time=10):
        return self.is_element_visible(FeedbackPage.FEEDBACK_STAR_RATING_LIST_LOCATOR, waiting_time)

    def is_get_started_screen_visible(self):
        return self.get_element(FeedbackPage.FEEDBACK_STAR_RATING_LIST_LOCATOR).is_displayed()

    def get_inactivity_timeout_data(self, waiting_time=350):
        # Record the start time
        start_time = time.time()
        get_started_screen_visible = self.is_element_visible(LoginPageDocapp.START_BUTTON, waiting_time)
        # Record the end time
        end_time = time.time()
        return {
            'elapsed_time': end_time - start_time,
            'get_started_screen_visible': get_started_screen_visible
        }

    def close_feedback_page(self):
        self.click_and_wait_for_invisibility(self.FEEDBACK_MODAL_CROSS, 5)
        print('Feedback modal closed')

    def exit_using_feedback(self):
        """
        Provide EOD feedback

        Args:
            self: instance of the page for the test script
        """

        # Click on 4 stars
        self.wait_for_visibility_of(self.FEEDBACK_STAR_FOUR_STAR_LOCATOR).click()

        # Click on done button
        self.wait_for_visibility_of(self.FEEDBACK_DONE_BUTTON_LOCATOR, 10).click()
        self.wait_for_visibility_of(self.THANK_YOU_BUTTON_DONE_LOCATOR).click()
