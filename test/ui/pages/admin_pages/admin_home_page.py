"""
Locators & methods for Admin Portal.
"""


from test.ui.pages.base_page import BasePage

from selenium.webdriver.common.by import By


class AdminHomePage(BasePage):
    """
    This is the page where logged-in user is landed on.
    """
    # pylint: disable=too-many-arguments

    LOG_OUT_BTN_LOCATOR = (By.XPATH, '//button[text()="Log out"]')

    PROVIDER_SIDEBAR_OPTION_LINK_LOCATOR = (By.CSS_SELECTOR, 'a[href="/provider"]')
    ADD_PROVIDER_BUTTON_LOCATOR = (By.XPATH, '//button[text()="+ Add Provider"]')
    LATEST_PROVIDER_ROW_LOCATOR = (By.XPATH, '(//tbody//tr)[1]//td')

    def navigate_to_provider_list_page(self):
        self.click_and_wait_for_visibility(self.PROVIDER_SIDEBAR_OPTION_LINK_LOCATOR,
                                           self.LATEST_PROVIDER_ROW_LOCATOR, 10)
        print('Provider list should be shown')




