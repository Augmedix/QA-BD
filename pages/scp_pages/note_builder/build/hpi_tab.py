"""Page object for HPI"""
import random

import pytest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.note_builder.build_tab import BuildTab
from utils.conversion_utility import convert_rgba_to_hex
from utils.helper import generate_random_alphanumeric_string


class HpiTab(BasePage):
    """Page object for HPI"""
    COMPLAINTS = (By.CSS_SELECTOR, '#nb-formbuilder-hpi-complaint span.label--warning')
    ADD_BTN = (By.CSS_SELECTOR, '#nb-formbuilder-hpi-complaint li:last-child')
    COMPLAINTS_SEQUENCE_NUMBER = (By.CSS_SELECTOR, 'small.label__info')
    ELEMENT_BLOCK = (By.CSS_SELECTOR, '#nb-hpi-block-container .builder__content')
    ELEMENT_BLOCK_HEADER = (By.CLASS_NAME, 'builder__content__header--heading')

    def get_complaints_list(self):
        complaints = self.get_elements(self.COMPLAINTS)

        complaint_texts = []
        for complaint in complaints:
            complaint_text = self.get_text_by_element(complaint)
            child_text = complaint.find_element(By.XPATH, './*').text
            last_match_index = complaint_text.rfind(child_text)
            complaint_texts.append(complaint_text[:last_match_index].strip())
        return complaint_texts

    def verify_all_complaints_have_yellow_border(self):
        complaint_list = self.get_elements(HpiTab.COMPLAINTS)
        for complaint in complaint_list:
            complaint_border_color = convert_rgba_to_hex(
                self.get_css_value_from_element(complaint, 'border-color')
            )
            if complaint_border_color != '#ffc107':
                return False
        return True

    def verify_complaints_sequence_number_exists_as_expected(self):
        sequence_number_list = self.get_list_of_text_from_locator(
            self.COMPLAINTS_SEQUENCE_NUMBER
        )
        for sequence_position, sequence in enumerate(sequence_number_list, start=1):
            print(f'{type(sequence)} <=> {type(sequence_position)} *****')
            if int(sequence_position) != int(sequence):
                return False
        return True

    def get_block_headers(self):
        print(self.get_elements(self.ELEMENT_BLOCK_HEADER))
        return self.get_list_of_text_from_locator(self.ELEMENT_BLOCK_HEADER)

    def verify_only_first_block_is_expanded(self):
        element_blocks = self.get_elements(self.ELEMENT_BLOCK)
        is_first_block_expanded = '--expanded' in self.get_attribute_from_element(
            element_blocks.pop(0), 'class'
        )
        assert is_first_block_expanded, 'First block should be expanded by default.'
        is_all_remaining_block_collapsed = not any(
            self.get_attribute_from_element(element_block, 'class').endswith(
                '--expanded'
            )
            for element_block in element_blocks
        )
        assert (
            is_all_remaining_block_collapsed
        ), 'All the blocks should be collapsed except the first one.'

    def select_random_value_of_hpi_visit_complaint(self):
        home_page = HomePage(self.driver)
        build_tab = BuildTab(self.driver)

        # Select visit type complaint for automation in HPI tab
        build_tab.select_complaint_by_name(pytest.configs.get_config('visit_complaint_name'))

        # Select visit block data
        build_tab.expand_blocks_by_text('Visit')
        accompanied_by_index = build_tab.get_random_index_from_list(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1
        )
        accompanied_by_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1, accompanied_by_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1, accompanied_by_index
        )

        visit_free_text_value = f'{generate_random_alphanumeric_string(20)}.'
        build_tab.add_text_in_free_text_box(1, visit_free_text_value)
        build_tab.collapse_blocks_by_text('Visit')

        # Select description block data
        build_tab.expand_blocks_by_text('Description')
        symptoms_name = generate_random_alphanumeric_string()
        build_tab.search_and_select(build_tab.SEARCH_INPUT1, symptoms_name)
        home_page.wait_for_loader()

        onset_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1
        )
        progression_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2
        )
        onset_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1, onset_index
        )
        progression_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2, progression_index
        )

        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1, onset_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2, progression_index
        )

        onset_input_value = str(random.randrange(1, 100))
        description_free_text_value = f'{generate_random_alphanumeric_string(20)}.'
        self.enter_text_at(onset_input_value, build_tab.NUMBER_INPUT1)
        build_tab.add_text_in_free_text_box(2, description_free_text_value)
        build_tab.collapse_blocks_by_text('Description')

        # Select medications block data
        build_tab.expand_blocks_by_text('Medications')
        medication_name = generate_random_alphanumeric_string()
        build_tab.search_and_select(build_tab.SEARCH_INPUT1, medication_name)
        home_page.wait_for_loader()

        frequency_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1
        )
        relief_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2
        )
        compliance_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST3
        )
        side_effects_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST4
        )
        refills_index = build_tab.get_random_index_from_list(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST5
        )

        frequency_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1, frequency_index
        )
        relief_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2, relief_index
        )
        compliance_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST3, compliance_index
        )
        side_effects_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST4, side_effects_index
        )
        refills_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST5, refills_index
        )

        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST1, frequency_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST2, relief_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST3, compliance_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST4, side_effects_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.SINGLE_SELECT_DESCRIPTOR_LIST5, refills_index
        )

        dosage_input_value = generate_random_alphanumeric_string()
        side_effects__input_value = generate_random_alphanumeric_string()
        medications_free_text_value = f'{generate_random_alphanumeric_string(20)}.'

        self.enter_text_at(dosage_input_value, build_tab.TEXT_INPUT1)
        self.enter_text_at(side_effects__input_value, build_tab.TEXT_INPUT2)
        build_tab.add_text_in_free_text_box(3, medications_free_text_value)
        build_tab.collapse_blocks_by_text('Medications')

        # Select history block data
        build_tab.expand_blocks_by_text('History')
        family_history = generate_random_alphanumeric_string()
        build_tab.search_and_select(build_tab.SEARCH_INPUT1, family_history)
        home_page.wait_for_loader()

        family_history_index = build_tab.get_random_index_from_list(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1
        )
        family_member_descriptor = build_tab.get_text_from_elements_by_index(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1, family_history_index
        )
        build_tab.click_list_elements_by_index(
            build_tab.MULTI_SELECT_DESCRIPTOR_LIST1, family_history_index
        )

        past_medical_history = generate_random_alphanumeric_string()
        build_tab.search_and_select(build_tab.SEARCH_INPUT2, past_medical_history)
        home_page.wait_for_loader()

        diagnosed_input_value = generate_random_alphanumeric_string()
        history_free_text_value = f'{generate_random_alphanumeric_string(20)}.'
        self.enter_text_at(diagnosed_input_value, build_tab.TEXT_INPUT1)
        build_tab.add_text_in_free_text_box(4, history_free_text_value)
        build_tab.collapse_blocks_by_text('History')

        return {
            'visit_block': {
                'accompanied_by_descriptor': accompanied_by_descriptor,
                'visit_free_text_value': visit_free_text_value,
            },
            'description_block': {
                'symptoms_name': symptoms_name,
                'onset_input_value': onset_input_value,
                'onset_descriptor': onset_descriptor,
                'progression_descriptor': progression_descriptor,
                'description_free_text_value': description_free_text_value,
            },
            'medications_block': {
                'medication_name': medication_name,
                'dosage_input_value': dosage_input_value,
                'frequency_descriptor': frequency_descriptor,
                'relief_descriptor': relief_descriptor,
                'compliance_descriptor': compliance_descriptor,
                'side_effects_input_value': side_effects__input_value,
                'side_effects_descriptor': side_effects_descriptor,
                'refills_descriptor': refills_descriptor,
                'medications_free_text_value': medications_free_text_value,
            },
            'history_block': {
                'family_history': family_history,
                'family_member_descriptor': family_member_descriptor,
                'past_medical_history': past_medical_history,
                'diagnosed_input_value': diagnosed_input_value,
                'history_free_text_value': history_free_text_value,
            },
        }
