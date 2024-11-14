"""
Locators & methods for Pause Activity screensaver.
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PauseActivityModal(BasePage):
    """
    Locators & methods for Pause Activity screensaver.
    """
    SCREENSAVER_LOCATOR = (By.CSS_SELECTOR, '.screen__saver')
    SCREENSAVER_TIMER_LOCATOR = (By.CLASS_NAME, 'screen__saver__counter')
    SCREENSAVER_TITLE_LOCATOR = (By.CLASS_NAME, 'screen__saver__title')
    SCREENSAVER_TEXT_LOCATOR = (By.CLASS_NAME, 'screen__saver__text')
    CONTINUE_WORKING_BTN_LOCATOR = (By.CSS_SELECTOR, '.screen__saver__text ~ button')

    SCREENSAVER_MESSAGE = 'Your note progress is temporarily paused while you or your clinician take a break or' \
                          ' do other tasks. When you’re ready to continue with your notes tap below or' \
                          ' the paused button in the top nav bar.'

    def continue_working(self):
        self.click_and_wait(self.CONTINUE_WORKING_BTN_LOCATOR)

    def is_screensaver_appeared(self):
        return not self.get_attribute(self.SCREENSAVER_LOCATOR, 'class').endswith('is--hidden')

    def is_screensaver_disappeared(self):
        return self.get_attribute(self.SCREENSAVER_LOCATOR, 'class').endswith('is--hidden')

    def verify_pause_activity_screensaver_appeared_properly(self):
        is_title_appeared = self.get_text_by_locator(self.SCREENSAVER_TITLE_LOCATOR) == 'Your work is paused'
        is_screensaver_message_ok = self.get_text_by_locator(self.SCREENSAVER_TEXT_LOCATOR) == self.SCREENSAVER_MESSAGE
        is_continue_btn_appeared = self.get_text_by_locator(self.CONTINUE_WORKING_BTN_LOCATOR) == 'Continue working'

        return [is_title_appeared, is_screensaver_message_ok, is_continue_btn_appeared]
