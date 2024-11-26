"""
Locators & methods for Admin Portal.
"""

from selenium.webdriver.common.by import By

from test.ui.pages.admin_pages.admin_home_page import AdminHomePage
from test.ui.pages.base_page import BasePage


class AdminProviderPage(BasePage):
    """
    This is the page where logged-in user is landed on.
    """
    # pylint: disable=too-many-arguments

    LOG_OUT_BTN_LOCATOR = (By.XPATH, '//button[text()="Log out"]')

    PROVIDER_SIDEBAR_OPTION_LINK_LOCATOR = (By.CSS_SELECTOR, 'a[href="/provider"]')
    ADD_PROVIDER_BUTTON_LOCATOR = (By.XPATH, '//button[text()="+ Add Provider"]')
    LATEST_PROVIDER_ROW_LOCATOR = (By.XPATH, '(//tbody//tr)[1]//td')
    PROVIDER_SEARCH_LOCATOR = (By.CSS_SELECTOR, 'input[placeholder="Filter Provider"]')
    PROVIDER_DETAILS_THREE_DOTS_LOCATOR = (By.CSS_SELECTOR, 'div[class*="_dropdown__header_"] img')
    EDIT_PROVIDER_LOCATOR = (By.XPATH, '//div[text()="Edit Provider"]')
    RESET_PROVIDER_LOCATOR = (By.XPATH, '//div[text()="Reset Password"]')
    CONFIRM_BUTTON_LOCATOR = (By.XPATH, "//button[text()='Confirm']")
    ERROR_TEXT_LOCATOR = (By.XPATH, "//div[text()='Something went wrong']")
    PROVIDER_UPDATED_LOCATOR = (By.XPATH, '//div[text()="Provider updated"]')

    FIRST_NAME_INPUT_LOCATOR = (By.NAME, 'firstName')
    LAST_NAME_INPUT_LOCATOR = (By.NAME, 'lastName')
    EMAIL_INPUT_LOCATOR = (By.NAME, 'email')
    PHONE_NO_INPUT_LOCATOR = (By.NAME, 'phoneNo')
    NPI_INPUT_LOCATOR = (By.NAME, 'npi')
    SITE_INPUT_LOCATOR = (By.ID, 'react-select-2-input')
    TIMEZONE_INPUT_LOCATOR = (By.ID, 'react-select-3-input')
    UNIQUE_ID_INPUT_LOCATOR = (By.NAME, 'providerUID')
    SPOKEN_LANGUAGE_LOCATOR = (By.XPATH, "//div[contains(@class, 'css-') and contains(text(), 'English')]")
    PROFILE_INFORMATION_LOCATOR = (By.XPATH,
                                   "//div[contains(@class, '_accordion__header') and .//span[text()='Profile information'] and .//img[@alt='Down Arrow']]")
    SPECIALTY_INPUT_LOCATOR = (By.ID, 'react-select-11-input')
    EHR_INPUT_LOCATOR = (By.ID, 'react-select-12-input')
    EHR_PRACTICE_ID_INPUT_LOCATOR = (By.NAME, 'profileInformation.ehrPracticeId')
    PRACTICE_NAME_INPUT_LOCATOR = (By.NAME, 'profileInformation.practiceName')
    STATE_INPUT_LOCATOR = (By.NAME, 'providerUID')
    ADDRESS_INPUT_LOCATOR = (By.NAME, 'profileInformation.businessAddress')
    ZIPCODE_INPUT_LOCATOR = (By.NAME, 'profileInformation.zipCode')

    GO_PROVIDER_FLAG_LOCATOR = (By.ID, 'ax-go')
    NRT_PROVIDER_FLAG_LOCATOR = (By.ID, 'ax-notes')
    UPDATE_PROVIDER_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Update Provider"]')

    PROVIDER_STATUS_LOCATOR = (By.XPATH,
                               "(//span[text()='Security']/parent::div/parent::div//input[@class and "
                               "@role='combobox'])[2]/parent::div/preceding-sibling::div")
    ACTIVE_PROVIDER_STATUS_LOCATOR = (
        By.XPATH, '//input[@id="react-select-6-input"]/parent::div/preceding-sibling::div')
    ENABLE_ED_FLAG_LOCATOR = (By.XPATH, "//label[contains(text(), 'Enable ED Specialty')]/input[@type='checkbox']")
    ENABLE_ROS_FLAG_LOCATOR = (
        By.XPATH, "//label[contains(text(), 'Enable ROS section for provider')]/input[@type='checkbox']")
    ENABLE_NUDGE_FLAG_LOCATOR = (By.XPATH, "//label[contains(text(), 'Enable Nudges in Go')]/input[@type='checkbox']")
    ENABLE_PIN_FLAG_LOCATOR = (By.XPATH, "//h5[text()='PIN Login']/parent::div//input[@type='checkbox']")

    def get_latest_provider_info(self):
        td_elements = self.get_elements(self.LATEST_PROVIDER_ROW_LOCATOR)
        # Extract the text from each <td> and store in a list
        td_texts = [td.text for td in td_elements]
        return td_texts

    def search_provider(self, email):
        self.enter_text_at(self.PROVIDER_SEARCH_LOCATOR, email)
        self.wait_for_visibility_of(self.LATEST_PROVIDER_ROW_LOCATOR, 10)
        print('Searched provider should be shown')

    def navigate_to_edit_provider_page(self):
        self.click_and_wait_for_visibility(self.PROVIDER_DETAILS_THREE_DOTS_LOCATOR,
                                           self.EDIT_PROVIDER_LOCATOR, 5)
        self.click_and_wait(self.EDIT_PROVIDER_LOCATOR, 5)
        print('Edit provider page should be visible')

    def request_password_reset(self, provider_email):
        AdminHomePage(self.driver).navigate_to_provider_list_page()
        self.search_provider(provider_email)
        self.click_and_wait_for_visibility(self.PROVIDER_DETAILS_THREE_DOTS_LOCATOR,
                                           self.RESET_PROVIDER_LOCATOR, 5)
        self.click_and_wait_for_visibility(self.RESET_PROVIDER_LOCATOR,
                                           self.CONFIRM_BUTTON_LOCATOR, 5)
        self.click_and_wait(self.CONFIRM_BUTTON_LOCATOR)

    def enable_ed_flag(self):
        self.scroll_into_view(AdminProviderPage.ENABLE_ROS_FLAG_LOCATOR)
        if self.get_element(AdminProviderPage.ENABLE_ED_FLAG_LOCATOR, 5).is_selected():
            print('Already ED Flag Enabled')
        else:
            self.click_and_wait(AdminProviderPage.ENABLE_ED_FLAG_LOCATOR, 5)
            self.scroll_into_view(AdminProviderPage.UPDATE_PROVIDER_BUTTON_LOCATOR)
            self.click_and_wait(AdminProviderPage.UPDATE_PROVIDER_BUTTON_LOCATOR, 5)
            print('ED Flag should be enabled')

    def enable_pin_flag(self):
        self.scroll_into_view(AdminProviderPage.ENABLE_NUDGE_FLAG_LOCATOR)
        if self.get_element(AdminProviderPage.ENABLE_PIN_FLAG_LOCATOR, 5).is_selected():
            print('Already ED Flag Enabled')
        else:
            self.click_and_wait(AdminProviderPage.ENABLE_PIN_FLAG_LOCATOR, 5)
            self.scroll_into_view(AdminProviderPage.UPDATE_PROVIDER_BUTTON_LOCATOR)
            self.click_and_wait(AdminProviderPage.UPDATE_PROVIDER_BUTTON_LOCATOR, 5)
            print('ED Flag should be enabled')

    def disable_pin_flag(self):
        self.scroll_into_view(AdminProviderPage.ENABLE_NUDGE_FLAG_LOCATOR)
        if self.get_element(AdminProviderPage.ENABLE_PIN_FLAG_LOCATOR, 5).is_selected():
            self.click_and_wait(AdminProviderPage.ENABLE_PIN_FLAG_LOCATOR, 5)
            self.scroll_into_view(AdminProviderPage.UPDATE_PROVIDER_BUTTON_LOCATOR)
            self.click_and_wait(AdminProviderPage.UPDATE_PROVIDER_BUTTON_LOCATOR, 5)
            print('Pin flag should be disabled')
        else:
            print('Pin flag is not selected')
