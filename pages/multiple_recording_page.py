import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from data.data import Data
from pages.base_page import BasePage


class MultipleRecordingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.data = Data()

    MULTIPLE_RECORDING_PATIENT1_NAME = (AppiumBy.ACCESSIBILITY_ID,Data().MULTIPLE_RECORDING_PATIENT1_NAME)