"""Page object for AP"""
import random

import pytest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.note_builder.build_tab import BuildTab
from utils.helper import generate_random_alphanumeric_string


class ApTab(BasePage):
    """Page object for AP"""
    AP_COMPLAINT_LIST = (
        By.XPATH,
        '//app-nb-complaint-selection//ul//li[contains(@class, \'ng-star-inserted\')]',
    )
    AP_CANVAS_SECTION_TEXT = (
        By.XPATH,
        '(//div[@class=\'nbcanvas-sentence__list\'])[5]',
    )
    DATE_PICKER = (By.CSS_SELECTOR, 'app-nb-date input[type=\'date\']')
    COMPLAINT_SECTIONS_LOCATOR = (
        By.XPATH,
        '//app-nb-group//section[not(contains(@class, \'nbblock--child\'))]',
    )
    COMPLAINT_BLOCKS_TITLE_LOCATOR = (
        By.XPATH,
        '//app-nb-group//section[not(contains(@class, \'nbblock--child\'))]/div[1]',
    )

    # Assessment block locator
    STATUS_ITEMS = (By.XPATH, '//app-nb-single-select//li/span')
    PROGRESSION_ITEMS = (By.XPATH, '//app-nb-multi-select//li/span')
    STATUS_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-header-input //input)[1]')
    PROGRESSION_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-header-input //input)[2]')

    ASSESSMENT_STATUS_GROUP = (By.XPATH, '(//app-nb-block-item/div)[1]')
    ASSESSMENT_PROGRESSION_GROUP = (By.XPATH, '(//app-nb-block-item/div)[2]')

    # Medications block locator
    MEDICATION_SEARCH_INPUT = (By.XPATH, '//app-nb-block-remote-header-input//input')
    RECOMMENDATION_SINGLE_ITEMS = (By.XPATH, '(//app-nb-single-select)[1]//li//span')
    RECOMMENDATION_MULTI_ITEMS = (By.XPATH, '(//app-nb-multi-select)[2]//li//span')
    ACTION_ITEMS = (By.XPATH, '(//app-nb-single-select)[1]//li//span')
    DOSAGE_ITEMS = (By.XPATH, '(//app-nb-single-select)[2]//li//span')
    FREQUENCY_ITEMS = (By.XPATH, '(//app-nb-single-select)[3]//li//span')
    DETAILS_ITEMS = (By.XPATH, '(//app-nb-multi-select)[2]//li//span')
    DETAILS_DEV_ITEMS = (By.XPATH, '(//app-nb-multi-select)[2]//li//span')
    SIDE_EFFECTS_ITEMS = (By.XPATH, '(//app-nb-single-select)[4]//li//span')

    # Treatment block locator
    LIFESTYLE_TREATMENTS_SEARCH_INPUT = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[1]',
    )
    TREATMENT_PROCEDURE_SEARCH_INPUT = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[2]',
    )
    TREATMENT_INPUT = (By.XPATH, '(//app-nb-text)//input')
    TREATMENT_ITEMS = (By.XPATH, '//app-nb-single-select//li/span')
    TREATMENT_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-header-input //input)[1]')
    ACUTE_TREATMENT_SEARCH_INPUT = (
        By.XPATH,
        '(//app-nb-block-remote-header-input //input)[1]',
    )
    XRAY_LOCATOR = (By.XPATH, '//div[@data-tooltip-bottom-left=\'Xray T-Spine\']')

    # Tests block locator
    PRIMARY_LABS_MULTI_ITEMS = (By.XPATH, '(//app-nb-multi-select)//li//span')
    PRIMARY_LABS_SINGLE_ITEMS = (By.XPATH, '(//app-nb-single-select)[1]//li//span')
    PRIMARY_IMAGING_INPUT = (By.XPATH, '(//app-nb-text)[1]//input')
    PRIMARY_IMAGING_SEARCH_INPUT = (
        By.XPATH,
        '(//app-nb-block-header-input //input)[2]',
    )
    PRIMARY_IMAGING_PART1_ITEMS = (By.XPATH, '(//app-nb-single-select)[2]//li//span')
    IMAGING_ITEMS = (By.XPATH, '(//app-nb-multi-select)[2]//li//span')
    PRIMARY_IMAGING_PART2_ITEMS = (By.XPATH, '(//app-nb-single-select)[3]//li//span')
    PRIMARY_DIAGNOSTIC_INPUT = (By.XPATH, '(//app-nb-text)[2]//input')

    ACUTE_LABS_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-header-input //input)[1]')
    LABS_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-remote-header-input //input)[1]')
    ACUTE_LABS_ITEMS = (By.XPATH, '(//app-nb-single-select)[1]//li//span')
    LABS_ITEMS = (By.XPATH, '(//app-nb-multi-select)[1]//li//span')
    ACUTE_IMAGING_SEARCH_INPUT = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[2]',
    )
    IMAGING_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-remote-header-input //input)[2]')
    ACUTE_IMAGING_INPUT = (By.CSS_SELECTOR, 'app-nb-text input')
    ACUTE_IMAGING_ITEMS = (By.XPATH, '(//app-nb-multi-select)[2]//li//span')
    ACUTE_DIAGNOSTIC_SEARCH_INPUT = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[3]',
    )
    ACUTE_DIAGNOSTIC_INPUT = (By.CSS_SELECTOR, 'app-nb-text input')

    CHRONIC_LABS_SEARCH_INPUT = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[1]',
    )
    CHRONIC_LABS_ITEMS = (By.XPATH, '(//app-nb-single-select)[1]//li//span')
    CHRONIC_DIAGNOSTIC_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-header-input//input)')
    CHRONIC_DIAGNOSTIC_ITEMS = (By.XPATH, '(//app-nb-multi-select)[2]//li//span')

    # Follow-UP block locator
    REFERRAL_INPUT = (By.XPATH, '(//app-nb-text)[1]//input[1]')
    REFERRAL_ITEMS = (By.XPATH, '(//app-nb-single-select)[1]//li//span')
    FOLLOW_UP_INPUT = (By.XPATH, '(//app-nb-text)[2]//input')
    FOLLOW_UP_PART1_ITEMS = (By.XPATH, '(//app-nb-single-select)[2]//li//span')
    FOLLOW_UP_PART2_ITEMS = (By.XPATH, '(//app-nb-single-select)[3]//li//span')
    REFERRAL_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-header-input //input)[1]')
    FOLLOW_UP_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-header-input //input)[2]')

    # Other block locator
    TIME_SPENT_INPUT = (By.XPATH, '(//app-nb-number)//input')
    TIME_SPENT_LIST = (By.XPATH, '(//app-nb-multi-select)//li//span')
    TIME_SPENT_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-header-input //input)[1]')

    # Canvas locator
    PRIMARY_STATUS_TEXT_EDITOR = (By.XPATH, '(//app-nb-text-editor)[9]')
    PRIMARY_PROGRESSION_TEXT_EDITOR = (By.XPATH, '(//app-nb-text-editor)[10]')
    PRIMARY_MEDICATION_TEXT_EDITOR = (By.XPATH, '(//app-nb-text-editor)[11]')
    PRIMARY_TREATMENT_TEXT_EDITOR = (By.XPATH, '(//app-nb-text-editor)[12]')
    PRIMARY_LABS_TEXT_EDITOR = (By.XPATH, '(//app-nb-text-editor)[13]')
    PRIMARY_IMAGING_TEXT_EDITOR = (By.XPATH, '(//app-nb-text-editor)[14]')
    PRIMARY_REFERRAL_TEXT_EDITOR = (By.XPATH, '(//app-nb-text-editor)[15]')
    PRIMARY_FOLLOW_UP_TEXT_EDITOR = (By.XPATH, '(//app-nb-text-editor)[16]')
    PRIMARY_OTHER_TEXT_EDITOR = (By.XPATH, '(//app-nb-text-editor)[17]')


    def select_dynamic_block(self, item_name, input_locator, generated_text):
        self.enter_text_at(item_name, input_locator)
        home_page = HomePage(self.driver)
        home_page.wait_for_loader()
        target_element = (
            By.XPATH,
            f'//app-nb-block-remote-header-input//li[@data-item]/div[text()="{item_name}"]',
        )
        self.click_and_wait(target_element)
        self.wait_for_visibility_of_text(
            self.AP_CANVAS_SECTION_TEXT, generated_text, 10
        )

    def is_dynamic_block_selected(self, name):
        child_element = f'//app-nb-multi-select//li/span[text()="{name}"]'
        parent_element = (
            self.get_element((By.XPATH, child_element), 5)
            .find_element(By.XPATH, './parent::li')
        )
        return 'nbtag__item--active' in self.get_attribute_from_element(parent_element, 'class')

    def is_item_selected(self, item_element):
        parent_element = item_element.find_element(By.XPATH, './parent::li')
        return 'nbtag__item--active' in self.get_attribute_from_element(
            parent_element, 'class'
        )

    def select_random_value_of_ap_visit_complaint(self):
        home_page = HomePage(self.driver)
        build_tab = BuildTab(self.driver)

        # Select visit type complaint for automation in AP tab
        build_tab.select_complaint_by_name(pytest.configs.get_config('visit_complaint_name'))

        # Select assessment block data
        build_tab.expand_blocks_by_text('Assessment')
        status_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1
        )
        progression_index = build_tab.get_random_index_from_list(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1
        )
        status_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1, status_index
        )
        progression_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1, progression_index
        )

        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1, status_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1, progression_index
        )

        assessment_free_text_value = f'{generate_random_alphanumeric_string(20)}.'
        build_tab.add_text_in_free_text_box(1, assessment_free_text_value)
        build_tab.collapse_blocks_by_text('Assessment')

        # Select medication block data
        build_tab.expand_blocks_by_text('Medications')
        medication_name = 'doxepin'
        build_tab.search_and_select(build_tab.SEARCH_INPUT1, medication_name)
        home_page.wait_for_loader()

        action_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1
        )
        dosage_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2
        )
        frequency_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST3
        )
        details_index = build_tab.get_random_index_from_list(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST2
        )
        side_effects_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST4
        )

        action_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1, action_index
        )
        dosage_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2, dosage_index
        )
        frequency_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST3, frequency_index
        )
        details_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST2, details_index
        )
        side_effects_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST4, side_effects_index
        )

        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1, action_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2, dosage_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST3, frequency_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST2, details_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST4, side_effects_index
        )

        medications_free_text_value = f'{generate_random_alphanumeric_string(20)}.'
        build_tab.add_text_in_free_text_box(2, medications_free_text_value)
        build_tab.collapse_blocks_by_text('Medications')

        # Select treatment block data
        build_tab.expand_blocks_by_text('Treatments')
        treatment_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1
        )
        treatment_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1, treatment_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1, treatment_index
        )

        treatment_input_value = generate_random_alphanumeric_string()
        treatments_free_text_value = f'{generate_random_alphanumeric_string(20)}.'
        self.enter_text_at(treatment_input_value, build_tab.TEXT_INPUT1)
        build_tab.add_text_in_free_text_box(3, treatments_free_text_value)
        build_tab.collapse_blocks_by_text('Treatments')

        # Select tests block data
        build_tab.expand_blocks_by_text('Tests')
        labs_multi_index = build_tab.get_random_index_from_list(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1
        )
        labs_single_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1
        )
        imaging_part1_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2
        )
        imaging_part2_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST3
        )

        labs_multi_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1, labs_multi_index
        )
        labs_single_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1, labs_single_index
        )
        imaging_part1_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2, imaging_part1_index
        )
        imaging_part2_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST3, imaging_part2_index
        )

        build_tab.click_list_elements_by_index(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1, labs_multi_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1, labs_single_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2, imaging_part1_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST3, imaging_part2_index
        )

        imaging_input_value = generate_random_alphanumeric_string()
        tests_free_text_value = f'{generate_random_alphanumeric_string(20)}.'
        self.enter_text_at(imaging_input_value, build_tab.TEXT_INPUT1)
        build_tab.add_text_in_free_text_box(4, tests_free_text_value)
        build_tab.collapse_blocks_by_text('Tests')

        # Select follow-up block data
        build_tab.expand_blocks_by_text('Follow Up')
        referral_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1
        )
        follow_up_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2
        )

        referral_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1, referral_index
        )
        follow_up_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2, follow_up_index
        )

        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1, referral_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2, follow_up_index
        )

        referral_input_value = generate_random_alphanumeric_string()
        follow_up_input_value = str(random.randrange(100))
        follow_up_free_text_value = f'{generate_random_alphanumeric_string(20)}.'

        self.enter_text_at(referral_input_value, build_tab.TEXT_INPUT1)
        self.enter_text_at(follow_up_input_value, build_tab.TEXT_INPUT2)
        build_tab.add_text_in_free_text_box(5, follow_up_free_text_value)
        build_tab.collapse_blocks_by_text('Follow Up')

        # Select other block data
        build_tab.expand_blocks_by_text('Other')
        time_spent_index = build_tab.get_random_index_from_list(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1
        )
        time_spent_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1, time_spent_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1, time_spent_index
        )

        time_spent_input_value = str(random.randrange(100))
        other_free_text_value = f'{generate_random_alphanumeric_string(20)}.'
        self.enter_text_at(time_spent_input_value, build_tab.NUMBER_INPUT1)
        build_tab.add_text_in_free_text_box(6, other_free_text_value)
        build_tab.collapse_blocks_by_text('Other')

        return {
            'assessment_block': {
                'status_descriptor': status_descriptor,
                'progression_descriptor': progression_descriptor,
                'assessment_free_text_value': assessment_free_text_value,
            },
            'medications_block': {
                'medication_name': medication_name,
                'action_descriptor': action_descriptor,
                'dosage_descriptor': dosage_descriptor,
                'frequency_descriptor': frequency_descriptor,
                'details_descriptor': details_descriptor,
                'side_effects_descriptor': side_effects_descriptor,
                'medications_free_text_value': medications_free_text_value,
            },
            'treatments_block': {
                'treatments_input_value': treatment_input_value,
                'treatments_descriptor': treatment_descriptor,
                'treatments_free_text_value': treatments_free_text_value,
            },
            'tests_block': {
                'labs_multi_descriptor': labs_multi_descriptor,
                'labs_single_descriptor': labs_single_descriptor,
                'imaging_input_value': imaging_input_value,
                'imaging_part1_descriptor': imaging_part1_descriptor,
                'imaging_part2_descriptor': imaging_part2_descriptor,
                'tests_free_text_value': tests_free_text_value,
            },
            'follow_up_block': {
                'referral_input_value': referral_input_value,
                'referral_descriptor': referral_descriptor,
                'follow_up_input_value': follow_up_input_value,
                'follow_up_descriptor': follow_up_descriptor,
                'follow_up_free_text_value': follow_up_free_text_value,
            },
            'other_block': {
                'time_spent_input_value': time_spent_input_value,
                'time_spent_descriptor': time_spent_descriptor,
                'other_free_text_value': other_free_text_value,
            },
        }
