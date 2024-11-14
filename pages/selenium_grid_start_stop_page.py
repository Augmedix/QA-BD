import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from data.data import Data
from pages.base_page import BasePage

class SeleniumGridStartStopPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.data = Data()