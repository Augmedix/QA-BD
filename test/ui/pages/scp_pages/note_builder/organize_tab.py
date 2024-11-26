"""
Contains locators & methods for Organize tab.
"""
import random
from datetime import datetime

import pytest
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

import test.ui.pages
from test.ui.pages.base_page import BasePage
import test.ui.pages.scp_pages
import test.ui.pages.scp_pages.home_page
from test.ui.utils.helper import get_current_time_stamp


class OrganizeTab(BasePage):
    """
    Contains locators & methods for Organize tab.
    """
    ORGANIZE_CONTAINER = (By.CSS_SELECTOR, 'app-nb-organize section.nbblock__container')
    SEARCH_RESULT = (By.CSS_SELECTOR, 'app-nb-block-header-input .nbdropdown__item')

    # Patient locator
    PATIENT_NAME_FIELD_NAME_HEADER = (By.CSS_SELECTOR, '.nbblock__item__header__hl')
    PATIENT_NAME_INPUT = (By.XPATH, '//*[text()="Name"]/following-sibling::div//input')

    GENDER_SEARCH_INPUT = (By.XPATH, '//*[text()="Gender"]/following-sibling::div//input')
    GENDER_ITEMS = (By.XPATH, '//*[text()="Gender"]/parent::*/following-sibling::*//li')
    SELECTED_GENDER = (
        By.XPATH,
        '//*[text()="Gender"]/parent::*/following-sibling::*'
        '//li[contains(@class, "active")]'
    )

    AGE_FIELD = (By.XPATH, '//*[text()="Age"]/following-sibling::div//input')
    AGE_FORMAT_ITEMS = (By.XPATH, '//*[text()="Age"]/parent::*/following-sibling::*//li')
    SELECTED_AGE_FORMAT = (
        By.XPATH,
        '//*[text()="Age"]/parent::*/following-sibling::*'
        '//li[contains(@class, "active")]'
    )

    # Visit locator
    VISIT_TYPE_SEARCH_INPUT = (By.XPATH, '//*[text()="Type"]/following-sibling::div//input')
    VISIT_TYPE_ITEMS = (By.XPATH, '//*[text()="Type"]/parent::*/following-sibling::*//li')
    SELECTED_VISIT_TYPE = (
        By.XPATH,
        '//*[text()="Type"]/parent::*/following-sibling::*'
        '//li[contains(@class, "active")]'
    )

    VISIT_START_TIME = (By.XPATH, '//*[text()="Start time"]/following-sibling::div//input')


    SERVICE_TYPE_SEARCH_INPUT = (By.XPATH, '//*[text()="Service type"]/following-sibling::div//input')
    SERVICE_TYPE_ITEMS = (By.XPATH, '//*[text()="Service type"]/parent::*/following-sibling::*//li')
    SELECTED_SERVICE_TYPE = (
        By.XPATH,
        '//*[text()="Service type"]/parent::*/following-sibling::*'
        '//li[contains(@class, "active")]'
    )
    TELEHEALTH_ITEMS = (By.XPATH, '//*[text()="Telehealth"]//following-sibling::*//li')
    SELECTED_TELEHEALTH = (
        By.XPATH,
        '//*[text()="Telehealth"]//following-sibling::*'
        '//li[contains(@class, "active")]'
    )
    TIME_SPENT_INPUT = (By.XPATH, '(//input[@type="number"])[2]')

    # Templates locator
    TEMPLATES_HEADER = (By.XPATH, '//div[@class="nbblock__item__header__hl" and text()="Templates"]')
    VISIT_TYPE_COMPLAINT_SEARCH_INPUT = (By.XPATH, '(//input[@type="text"])[7]')
    COMPLAINT_SEARCH_INPUT = (By.XPATH, '(//input[@type="text"])[8]')
    COMPLAINT_SEARCH_RESULTS_BODY = (By.CSS_SELECTOR, 'app-nb-block-remote-header-input ul')
    COMPLAINT_SEARCH_RESULTS_ROW = (By.CSS_SELECTOR, 'app-nb-block-remote-header-input li')
    COMPLAINT_SEARCH_RESULTS_NAME = (
        By.CSS_SELECTOR,
        'app-nb-block-remote-header-input li .nbdropdown__item__primary'
    )
    COMPLAINT_SEARCH_RESULTS_TYPE = (
        By.CSS_SELECTOR,
        'app-nb-block-remote-header-input li .nbdropdown__item__secondary '
        'span:nth-child(1)'
    )
    COMPLAINT_SEARCH_RESULTS_SPECIALTY = (
        By.CSS_SELECTOR,
        'app-nb-block-remote-header-input li .nbdropdown__item__secondary '
        'span:nth-child(2)'
    )
    COMPLAINT_SEARCH_RESULTS_NEXT = (
        By.XPATH,
        '//li[contains(@class, "nbdropdown__item--paginator")]'
        '//*[contains(text(), "Next")]'
    )
    COMPLAINT_SEARCH_RESULTS_PREVIOUS = (
        By.XPATH,
        '//li[contains(@class, "nbdropdown__item--paginator")]'
        '//*[contains(text(), "Previous")]'
    )

    CHIEF_COMPLAINT_LIST_LOCATOR = (
        By.XPATH,
        '//*[text()="Visit type"]/parent::*/following-sibling::*//li'
    )
    ACUTE_COMPLAINT_LIST_LOCATOR = (
        By.XPATH,
        '//*[text()="Acute"]/following-sibling::*'
        '//li[not(contains(@class, "nbtag__item--none"))]'
    )
    CHRONIC_COMPLAINT_LIST_LOCATOR = (
        By.XPATH,
        '//*[text()="Chronic"]/following-sibling::*'
        '//li[not(contains(@class, "nbtag__item--none"))]'
    )

    VISIT_TYPE_COMPLAINT_LIST = (
        By.XPATH,
        '//*[text()="Visit type"]/parent::*/following-sibling::*//li//span'
    )
    ACUTE_COMPLAINT_LIST = (
        By.XPATH,
        '//*[text()="Acute"]/following-sibling::*'
        '//li[not(contains(@class, "nbtag__item--none"))]//span'
    )
    CHRONIC_COMPLAINT_LIST = (
        By.XPATH,
        '//*[text()="Chronic"]/following-sibling::*'
        '//li[not(contains(@class, "nbtag__item--none"))]//span'
    )

    ALL_SELECTED_COMPLAINT_LIST = (
        By.XPATH,
        '//app-nb-organize-template'
        '//li[contains(@class,"nbtag__item--active") and not(contains(@class,"nbtag__item--none"))]'
        '//span'
    )
    SELECTED_VISIT_TYPE_COMPLAINT = (
        By.XPATH,
        '//*[text()="Visit type"]/parent::*/following-sibling::*'
        '//li[contains(@class, "nbtag__item--active")]//span'
    )
    SELECTED_ACUTE_COMPLAINT = (
        By.XPATH,
        '//*[text()="Acute"]/following-sibling::*'
        '//li[contains(@class,"nbtag__item--active") and not(contains(@class,"nbtag__item--none"))]'
        '//span'
    )
    SELECTED_CHRONIC_COMPLAINT = (
        By.XPATH,
        '//*[text()="Chronic"]/following-sibling::*'
        '//li[contains(@class, "nbtag__item--active") and not(contains(@class, "nbtag__item--none"))]'
        '//span'
    )
    CHIEF_COMPLAINT = (
        By.XPATH,
        '//app-nb-organize-template'
        '//li[contains(@class,"nbtag__item--active") and not(contains(@class,"nbtag__item--none"))]'
        '//span[contains(text(), "(CC)")]'
    )


    notes = (By.XPATH, '(//div[contains(@class,"nbcanvas-sentence")])[3]')
    NB_CANVAS_PATIENT_NAME = (By.CLASS_NAME, 'nbcanvas-header__primary')

    def __init__(self, driver):
        super().__init__(driver)
        self.home_page = pages.scp_pages.home_page.HomePage(driver)

    def is_organize_tab_visible(self):
        return self.is_element_visible(self.ORGANIZE_CONTAINER, 10)

    def is_empty_input_warning_visible(self, input_name):
        warning_locator = (By.XPATH, f'//div[text()="{input_name}"]/parent::div/parent::div')
        return 'is--error' in self.get_attribute(warning_locator, 'class')

    def is_gender_selected(self):
        """
        Test whether any of the gender options is selected.
        Returns: boolean: True/False based of selection.
        """
        gender_options_attribute_list = self.get_list_of_attributes_from_locator(self.GENDER_ITEMS, 'class')
        return any(('nbtag__item--active' in gender_option) for gender_option in gender_options_attribute_list)

    def is_age_selected(self):
        age_options_attribute_list = self.get_list_of_attributes_from_locator(self.AGE_FORMAT_ITEMS, 'class')
        return any(('--active' in age_option) for age_option in age_options_attribute_list)

    def is_visit_type_selected(self):
        """
        Test whether any of the visit options is selected.
        Returns: boolean: True/False based of selection.
        """
        visit_options_attribute_list = self.get_list_of_attributes_from_locator(self.VISIT_TYPE_ITEMS, 'class')
        return any(('--active' in visit_option) for visit_option in visit_options_attribute_list)

    def is_service_type_selected(self):
        """
        Test whether any of the service options is selected.
        Returns: boolean: True/False based of selection.
        """
        service_options_attribute_list = self.get_list_of_attributes_from_locator(self.SERVICE_TYPE_ITEMS, 'class')
        return any(('--active' in service_option) for service_option in service_options_attribute_list)

    def is_telehealth_selected(self):
        """
        Test whether any of the Telehealth is selected.
        Returns: boolean: True/False based of selection.
        """
        telehealth_options_attribute_list = self.get_list_of_attributes_from_locator(self.SELECTED_TELEHEALTH, 'class')
        return any(('--active' in telehealth_option) for telehealth_option in telehealth_options_attribute_list)

    def is_chief_complaint_selected(self):
        """
        Test whether any of the Chief Complaints is selected.
        Returns:boolean: True/False based of selection.
        """
        chief_complaint_attribute_list = self.get_list_of_attributes_from_locator(self.CHIEF_COMPLAINT_LIST_LOCATOR,
                                                                                  'class')
        return any(('--active' in chief_complaint) for chief_complaint in chief_complaint_attribute_list)

    def is_acute_complaint_selected(self):
        """
        Test whether any of the Acute Complaints is selected.
        Returns: boolean: True/False based of selection.
        """
        acute_complaint_attribute_list = self.get_list_of_attributes_from_locator(self.ACUTE_COMPLAINT_LIST_LOCATOR,
                                                                                  'class')
        return any(('--active' in acute_complaint) for acute_complaint in acute_complaint_attribute_list)

    def get_patient_name(self):
        return self.get_attribute(self.PATIENT_NAME_INPUT, 'value')

    def get_patient_name_from_nb_canvas(self):
        return self.get_text_by_locator(self.NB_CANVAS_PATIENT_NAME)

    def edit_patient_name(self, value):
        self.press_back_space(self.PATIENT_NAME_INPUT)
        self.enter_text_at(value, self.PATIENT_NAME_INPUT, clear_existing=False)

    def clear_patient_name(self):
        self.clear_field(self.PATIENT_NAME_INPUT)

    def click_on_gender(self, gender):
        self.click_and_wait((By.XPATH, f'//li/*[text()="{gender}"]'), 5)

    def get_selected_gender(self):
        return self.get_text_by_locator(self.SELECTED_GENDER)

    def search_on_gender(self, gender):
        self.enter_text_at(gender, self.GENDER_SEARCH_INPUT)

    def patient_gender_search_result(self):
        self.wait_for_visibility_of(self.SEARCH_RESULT, 10)
        return self.get_text_by_locator(self.SEARCH_RESULT)

    def click_on_age_format(self, age_format):
        self.click_and_wait((By.XPATH, f'//li/*[text()="{age_format}"]'))

    def get_selected_age_format(self):
        return self.get_text_by_locator(self.SELECTED_AGE_FORMAT)

    def get_entered_age(self):
        """
            this method return int type value because age is a number type input
        """
        entered_age = self.get_attribute(self.AGE_FIELD, 'value')
        return int(entered_age) if entered_age != '' else entered_age

    def clear_patient_age(self):
        self.clear_field(self.AGE_FIELD)

    def click_on_visit_type(self, visit_type):
        self.click_and_wait((By.XPATH, f'//li/*[text()="{visit_type}"]'))

    def get_selected_visit_type(self):
        return self.get_text_by_locator(self.SELECTED_VISIT_TYPE)

    def search_on_visit_type(self, visit_type):
        self.enter_text_at(visit_type, self.VISIT_TYPE_SEARCH_INPUT)

    def visit_type_search_result(self):
        self.wait_for_visibility_of(self.SEARCH_RESULT, 10)
        return self.get_text_by_locator(self.SEARCH_RESULT)

    def get_entered_start_time(self):
        return self.get_attribute(self.VISIT_START_TIME, 'value')

    def click_on_service_type(self, service_type):
        self.click_and_wait((By.XPATH, f'//li/*[text()="{service_type}"]'))

    def get_selected_service_type_list(self):
        return self.get_list_of_text_from_locator(self.SELECTED_SERVICE_TYPE)

    def search_on_service_type(self, service_type):
        self.enter_text_at(service_type, self.SERVICE_TYPE_SEARCH_INPUT)

    def service_type_search_result(self):
        self.wait_for_visibility_of(self.SEARCH_RESULT, 10)
        return self.get_text_by_locator(self.SEARCH_RESULT)

    def enter_value_in_time_spent_input_field(self, value):
        self.clear_field_and_send_keys(value, self.TIME_SPENT_INPUT)

    def get_value_from_time_spent_field(self):
        time_spent = self.get_attribute(self.TIME_SPENT_INPUT, 'value')
        return int(time_spent) if time_spent != '' else time_spent

    @staticmethod
    def remove_cc(complaint_name):
        return complaint_name.replace('(CC)', '').strip()

    def get_chief_complaint(self):
        complaint_text = self.get_text_by_locator(self.CHIEF_COMPLAINT)
        return self.remove_cc(complaint_text)

    def get_selected_visit_type_complaint_list(self):
        visit_type_complaint_list = self.get_list_of_text_from_locator(self.SELECTED_VISIT_TYPE_COMPLAINT)
        return [self.remove_cc(complaint) for complaint in visit_type_complaint_list]

    def get_selected_acute_complaint_list(self):
        acute_complaint_list = self.get_list_of_text_from_locator(self.SELECTED_ACUTE_COMPLAINT)
        return [self.remove_cc(complaint) for complaint in acute_complaint_list]

    def get_selected_chronic_complaint_list(self):
        chronic_complaint_list = self.get_list_of_text_from_locator(self.SELECTED_CHRONIC_COMPLAINT)
        return [self.remove_cc(complaint) for complaint in chronic_complaint_list]

    def get_complaint_search_results_row_count(self):
        return self.get_total_count(self.COMPLAINT_SEARCH_RESULTS_ROW)

    def get_complaint_search_results(self):
        """
            This method return a list of complaint name from search results
        """
        search_results = []
        for index in range(self.get_total_count(self.COMPLAINT_SEARCH_RESULTS_NAME)):
            search_results.append({
                'complaint_name': self.get_elements(self.COMPLAINT_SEARCH_RESULTS_NAME)[index].text,
                'complaint_type': self.get_elements(self.COMPLAINT_SEARCH_RESULTS_TYPE)[index].text,
                'specialty': self.get_elements(self.COMPLAINT_SEARCH_RESULTS_SPECIALTY)[index].text
            })
        return search_results

    def get_custom_complaint_search_results(self):
        """
            This method return a list of custom complaint search results
        """
        return self.get_list_of_text_from_locator(self.COMPLAINT_SEARCH_RESULTS_ROW)

    def complaint_search_results_next(self):
        self.scroll_into_view(self.COMPLAINT_SEARCH_RESULTS_NEXT)
        self.click_and_wait(self.COMPLAINT_SEARCH_RESULTS_NEXT)

    def is_next_button_visible(self):
        return self.get_total_count(self.COMPLAINT_SEARCH_RESULTS_NEXT) == 1

    def complaint_search_results_previous(self):
        self.scroll_into_view(self.COMPLAINT_SEARCH_RESULTS_PREVIOUS)
        self.click_and_wait(self.COMPLAINT_SEARCH_RESULTS_PREVIOUS)

    def is_previous_button_visible(self):
        return self.get_total_count(self.COMPLAINT_SEARCH_RESULTS_PREVIOUS) == 1

    def is_selection_list(self, locator, expected_attribute_value='tag__list__item'):
        selection_items = self.get_elements(locator)
        return all(list(map(lambda item: item.get_attribute('class') == expected_attribute_value, selection_items)))

    # pylint: disable=too-many-arguments
    def enter_patient_data(self, patient_name=f'Patient_{get_current_time_stamp()}', gender='male',
                           age='18', visit_type='new', start_time=None, service_type='In-person',
                           visit_type_complaint=pytest.configs.get_config('visit_complaint_name'),
                           complaint_acute='', complaint_chronic=''):

        self.set_organize_tab_value(
            patient_name=patient_name,
            gender=gender,
            age=age,
            visit_type=visit_type,
            start_time=start_time,
            service_type=service_type,
            complaint_visit=visit_type_complaint,
            complaint_acute=complaint_acute,
            complaint_chronic=complaint_chronic
        )

    # pylint: disable=too-many-arguments
    def set_organize_tab_value(self,
                               patient_name='',
                               gender='',
                               age='',
                               visit_type='',
                               start_time=None,
                               service_type='',
                               complaint_visit='',
                               complaint_acute='',
                               complaint_chronic=''):

        if patient_name:
            self.enter_text_at(self.PATIENT_NAME_INPUT, patient_name, max_wait=30)

        if gender:
            self.click_on_gender(gender)

        if age:
            self.enter_text_at(self.AGE_FIELD, age)

        if visit_type:
            self.click_on_visit_type(visit_type)

        if start_time is not None:
            self.enter_text_at(self.VISIT_START_TIME, start_time)

        if service_type:
            self.click_on_service_type(service_type)

        if complaint_visit:
            self.search_and_select_visit_type_complaint(complaint_visit)

        if complaint_acute:
            self.search_and_select_acute_complaint(complaint_acute)

        if complaint_chronic:
            self.search_and_select_chronic_complaint(complaint_chronic)

    def is_complaint_selected(self, complaint_name, complaint_type):
        selected_complaint_list = []
        if complaint_type == 'visit':
            selected_complaint_list = self.get_selected_visit_type_complaint_list()
        elif complaint_type == 'acute':
            selected_complaint_list = self.get_selected_acute_complaint_list()
        elif complaint_type == 'chronic':
            selected_complaint_list = self.get_selected_chronic_complaint_list()

        return complaint_name in selected_complaint_list


    def select_visit_type_complaint(self, target_complaint, custom=False, specialty='Primary'):
        found = False
        if self.get_total_count(self.VISIT_TYPE_COMPLAINT_LIST) > 0:
            for complaint_element in self.get_elements(self.VISIT_TYPE_COMPLAINT_LIST):
                if self.get_text_by_element(complaint_element) == target_complaint:
                    if not self.is_complaint_selected(target_complaint, 'visit'):
                        try:
                            self.click_and_wait_by_element(complaint_element, 1)
                        except ElementClickInterceptedException:
                            self.click_and_wait(self.TEMPLATES_HEADER)
                            self.click_and_wait_by_element(complaint_element, 1)
                        print(f'"{target_complaint}" complaint selected from organize tab.')
                    else:
                        print(f'"{target_complaint}" complaint already selected in organize tab.')
                    found = True
                    break
            if not found:
                self.search_and_select_visit_type_complaint(
                    target_complaint,
                    custom=custom,
                    specialty=specialty
                )
        else:
            self.search_and_select_visit_type_complaint(
                target_complaint,
                custom=custom,
                specialty=specialty
            )

    def click_on_visit_type_complaint_search_input(self):
        self.wait_for_element_to_clickable(self.VISIT_TYPE_COMPLAINT_SEARCH_INPUT, 10)
        self.click_and_wait(self.VISIT_TYPE_COMPLAINT_SEARCH_INPUT)
        self.home_page.wait_for_loader()

    def search_visit_type_complaint(self, visit_type_complaint):
        self.click_on_visit_type_complaint_search_input()
        self.enter_text_at(visit_type_complaint, self.VISIT_TYPE_COMPLAINT_SEARCH_INPUT)
        self.home_page.wait_for_loader()
        self.wait_for_visibility_of(self.COMPLAINT_SEARCH_RESULTS_ROW)

    def search_and_select_visit_type_complaint(self, target_complaint, custom=False, specialty='Primary'):
        if custom:
            target_complaint_locator = (
                By.XPATH,
                f'//app-nb-block-remote-header-input'
                f'//li[text()="+ Add new visit "]'
                f'//b[text()=\'"{target_complaint}"\']'
                f'//ancestor::li[@data-item]'
            )
        else:
            target_complaint_locator = (
                By.XPATH,
                f'//app-nb-block-remote-header-input//li'
                f'//*[text()="{target_complaint}"]'
                f'//following-sibling::div/span[text()="VISIT"]'
                f'//following-sibling::span[text()="{specialty}"]'
                f'//ancestor::li[@data-item]'
            )
        self.search_visit_type_complaint(target_complaint)
        self.wait_for_visibility_of(target_complaint_locator)
        self.click_and_wait(target_complaint_locator)
        self.home_page.wait_for_loader()
        self.click_and_wait(self.TEMPLATES_HEADER)
        print(f'"{target_complaint}" complaint selected from organize tab.')

    def select_acute_complaint(self, target_complaint, custom=False, specialty='Primary'):
        found = False
        if self.get_total_count(self.ACUTE_COMPLAINT_LIST) > 0:
            for complaint_element in self.get_elements(self.ACUTE_COMPLAINT_LIST):
                if self.get_text_by_element(complaint_element) == target_complaint:
                    if not self.is_complaint_selected(target_complaint, 'acute'):
                        try:
                            self.click_and_wait_by_element(complaint_element, 1)
                        except ElementClickInterceptedException:
                            self.click_and_wait(self.TEMPLATES_HEADER)
                            self.click_and_wait_by_element(complaint_element, 1)
                        print(f'"{target_complaint}" complaint selected from organize tab.')
                    else:
                        print(f'"{target_complaint}" complaint already selected in organize tab.')
                    found = True
                    break
            if not found:
                self.search_and_select_acute_complaint(
                    target_complaint,
                    custom=custom,
                    specialty=specialty
                )
        else:
            self.search_and_select_acute_complaint(
                target_complaint,
                custom=custom,
                specialty=specialty
            )

    def click_on_complaint_search_input(self):
        self.wait_for_element_to_clickable(self.COMPLAINT_SEARCH_INPUT, 10)
        self.click_and_wait(self.COMPLAINT_SEARCH_INPUT)
        self.home_page.wait_for_loader()

    def search_acute_complaint(self, acute_complaint):
        self.click_on_complaint_search_input()
        self.enter_text_at(acute_complaint, self.COMPLAINT_SEARCH_INPUT)
        self.home_page.wait_for_loader()
        self.wait_for_visibility_of(self.COMPLAINT_SEARCH_RESULTS_ROW)

    def search_and_select_acute_complaint(self, target_complaint, custom=False, specialty='Primary'):
        if custom:
            target_complaint_locator = (
                By.XPATH,
                f'//app-nb-block-remote-header-input'
                f'//li[text()="+ Add new acute "]'
                f'//b[text()=\'"{target_complaint}"\']'
                f'//ancestor::li[@data-item]'
            )
        else:
            target_complaint_locator = (
                By.XPATH,
                f'//app-nb-block-remote-header-input//li'
                f'//*[text()="{target_complaint}"]'
                f'//following-sibling::div/span[text()="ACUTE"]'
                f'//following-sibling::span[text()="{specialty}"]'
                f'//ancestor::li[@data-item]'
            )
        self.search_acute_complaint(target_complaint)
        self.wait_for_visibility_of(target_complaint_locator)
        self.click_and_wait(target_complaint_locator)
        self.home_page.wait_for_loader()
        self.click_and_wait(self.TEMPLATES_HEADER)
        print(f'"{target_complaint}" complaint selected from organize tab.')

    def select_chronic_complaint(self, target_complaint, custom=False, specialty='Primary'):
        found = False
        if self.get_total_count(self.CHRONIC_COMPLAINT_LIST) > 0:
            for complaint_element in self.get_elements(self.CHRONIC_COMPLAINT_LIST):
                if self.get_text_by_element(complaint_element) == target_complaint:
                    if not self.is_complaint_selected(target_complaint, 'chronic'):
                        try:
                            self.click_and_wait_by_element(complaint_element, 1)
                        except ElementClickInterceptedException:
                            self.click_and_wait(self.TEMPLATES_HEADER)
                            self.click_and_wait_by_element(complaint_element, 1)
                        print(f'"{target_complaint}" complaint selected from organize tab.')
                    else:
                        print(f'"{target_complaint}" complaint already selected in organize tab.')
                    found = True
                    break
            if not found:
                self.search_and_select_chronic_complaint(
                    target_complaint,
                    custom=custom,
                    specialty=specialty)
        else:
            self.search_and_select_chronic_complaint(
                target_complaint,
                custom=custom,
                specialty=specialty
            )

    def search_chronic_complaint(self, chronic_complaint):
        self.click_on_complaint_search_input()
        self.enter_text_at(chronic_complaint, self.COMPLAINT_SEARCH_INPUT)
        self.home_page.wait_for_loader()
        self.wait_for_visibility_of(self.COMPLAINT_SEARCH_RESULTS_ROW)

    def search_and_select_chronic_complaint(self, target_complaint, custom=False, specialty='Primary'):
        if custom:
            target_complaint_locator = (
                By.XPATH,
                f'//app-nb-block-remote-header-input'
                f'//li[text()="+ Add new chronic "]'
                f'//b[text()=\'"{target_complaint}"\']'
                f'//ancestor::li[@data-item]'
            )
        else:
            target_complaint_locator = (
                By.XPATH,
                f'//app-nb-block-remote-header-input//li'
                f'//*[text()="{target_complaint}"]'
                f'//following-sibling::div/span[text()="CHRONIC"]'
                f'//following-sibling::span[text()="{specialty}"]'
                f'//ancestor::li[@data-item]'
            )
        self.search_chronic_complaint(target_complaint)
        self.wait_for_visibility_of(target_complaint_locator)
        self.click_and_wait(target_complaint_locator)
        self.home_page.wait_for_loader()
        self.click_and_wait(self.TEMPLATES_HEADER)
        print(f'"{target_complaint}" complaint selected from organize tab.')

    def select_complaint_from_search_results_using_keyboard(self, complaint_serial):
        actions = ActionChains(self.driver)
        for _ in range(complaint_serial):
            actions.send_keys(Keys.DOWN).perform()
        actions.send_keys(Keys.ENTER).perform()

    def deselect_complaint(self, target_complaint_name):
        for complaint_element in self.get_elements(self.ALL_SELECTED_COMPLAINT_LIST):
            actual_complaint_name = self.remove_cc(self.get_text_by_element(complaint_element))
            if target_complaint_name == actual_complaint_name:
                self.click_and_wait_by_element(complaint_element, 1)
                break

    def click_arrow_up_for_increment(self, locator):
        self.press_arrow_up(locator)

    def click_arrow_down_for_decrement(self, locator):
        self.press_arrow_down(locator)

    def patient_name_using_note_id(self):
        """
            This method return patient name using selected note id
        """
        selected_note_id = self.home_page.get_note_id_from_locator(self.home_page.SELECTED_NOTE)
        return f'Test Patient-{selected_note_id}'

    def random_gender(self):
        gender_list = self.get_list_of_text_from_locator(self.GENDER_ITEMS)
        return random.choice(gender_list)

    def random_visit_type(self):
        visit_type_list = self.get_list_of_text_from_locator(self.VISIT_TYPE_ITEMS)
        return random.choice(visit_type_list)

    def value_for_start_time_input(self):
        provider_current_time = self.home_page.get_scp_provider_current_time()
        time = datetime.strptime(provider_current_time, '%I:%M %p').strftime('%I:%M %p')
        return time.replace(' ', '')
