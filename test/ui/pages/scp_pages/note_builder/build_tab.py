"""Page object for Build Tab"""
import random
import re
import time

import pytest
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.scp_pages.home_page import HomePage
from pages.scp_pages.note_builder.build.pe_tab import PeTab
from pages.scp_pages.note_builder.organize_tab import OrganizeTab
from pages.scp_pages.test_Input_data import user_input_data


class BuildTab(BasePage):
    """Page object for Build Tab"""
    SUB_TAB_LIST = (By.CSS_SELECTOR, 'app-nb-builder-nav li')
    BLOCK_GROUPS_LOCATOR = (By.CSS_SELECTOR, 'section.nbblock__container app-nb-group')
    COMPLAINT_SECTIONS = (
        By.XPATH,
        '//app-nb-group//section[not(contains(@class, "nbblock--child"))]',
    )
    COMPLAINT_BLOCK_NAME = (
        By.XPATH,
        '//app-nb-group//section[not(contains(@class, "nbblock--child"))]'
        '//div[@class="nbblock__primary"]//div[@class="nbblock__item__header__hl"]',
    )

    CANVAS_NOTE_LOCATOR = (
        By.CSS_SELECTOR,
        'app-nb-canvas-note .nbcanvas-accordion__item__body app-nb-text-editor div',
    )

    SELECTED_COMPLAINT = (
        By.CSS_SELECTOR,
        'app-nb-complaint-selection li.nbtag__item--primary',
    )

    # Restructured
    NOTES = (By.XPATH, '(//div[contains(@class,"nbcanvas-sentence")])[3]')
    HPI_BUILD_DEFAULT_TEXT = (
        By.XPATH,
        '(//div[@class="nbcanvas-sentence" and @contenteditable])[1]',
    )
    VISIT_LIST = (By.XPATH, '//app-nb-multi-select//li/span')
    DESCRIPTION_LIST = (By.XPATH, '//app-nb-pos-neg//li/span')
    PRIMARY_VISIT_TYPE_HPI_VISIT = (By.XPATH, '(//app-nb-text-editor)[3]')
    PRIMARY_VISIT_TYPE_HPI_DESCRIPTION = (By.XPATH, '(//app-nb-text-editor)[4]')
    PRIMARY_VISIT_TYPE_HPI_MEDICATION = (By.XPATH, '(//app-nb-text-editor)[5]')
    PRIMARY_VISIT_TYPE_HPI_FAMILY_HISTORY = (By.XPATH, '(//app-nb-text-editor)[6]')
    PRIMARY_VISIT_TYPE_HPI_PAST_MEDICAL_HISTORY = (
        By.XPATH,
        '(//app-nb-text-editor)[7]',
    )
    ACUTE_COMPLAINT_TIMING_HPI = (By.XPATH, '(//app-nb-text-editor)[8]')
    ACUTE_COMPLAINT_TIMING_TIMING_HPI = (By.XPATH, '(//app-nb-text-editor)[9]')
    ACUTE_COMPLAINT_TIMING_PROGRESSION_HPI = (By.XPATH, '(//app-nb-text-editor)[10]')
    ACUTE_COMPLAINT_TIMING_EPISODE_HPI = (By.XPATH, '(//app-nb-text-editor)[11]')
    ACUTE_COMPLAINT_TIMING_EPISODE_DURATION_HPI = (
        By.XPATH,
        '(//app-nb-text-editor)[12]',
    )
    ACUTE_COMPLAINT_TIMING_FACTORS_AGGRAVATING_HPI = (
        By.XPATH,
        '(//app-nb-text-editor)[18]',
    )
    ACUTE_COMPLAINT_TIMING_FACTORS_ALLEVIATING_HPI = (
        By.XPATH,
        '(//app-nb-text-editor)[19]',
    )
    SORE_THROAT_TITLE = (By.XPATH, '//div[@data-tooltip-bottom-left="sore throat"]')
    ONSET_INPUT = (By.CSS_SELECTOR, 'app-nb-number > input')
    ONSET_LIST = (By.XPATH, '(//app-nb-single-select)[1]//li//span')
    PROGRESSION_LIST = (By.XPATH, '(//app-nb-single-select)[2]//li//span')
    FREQUENCY_LIST = (By.XPATH, '(//app-nb-single-select)[1]//li//span')
    RELIEF_LIST = (By.XPATH, '(//app-nb-single-select)[2]//li//span')
    COMPLIANCE_LIST = (By.XPATH, '(//app-nb-single-select)[3]//li//span')
    REFILS_LIST = (By.XPATH, '(//app-nb-single-select)[5]//li//span')
    FAMILY_HISTORY_LIST = (By.XPATH, '(//app-nb-multi-select)[2]//li//span')
    FAMILY_HISTORY_LIST_VISIT = (By.XPATH, '(//app-nb-multi-select)[1]//li//span')
    TIMING_LIST = (By.XPATH, '(//app-nb-single-select)[1]//li//span')
    TIMING_TIMING_LIST = (By.XPATH, '(//app-nb-multi-select)[1]//li//span')
    TIMING_PROGRESSION_LIST = (By.XPATH, '(//app-nb-single-select)[2]//li//span')
    CURRENT_MEDICATION_INPUT = (By.XPATH, '//app-nb-block-remote-header-input//input')
    DOSAGE_INPUT = (By.XPATH, '(//app-nb-text)[1]//input')
    DIAGNOSED_IN_YEAR = (By.XPATH, '(//app-nb-text)[1]//input')
    SIDE_EFFECT_INPUT = (By.XPATH, '(//app-nb-text)[2]//input')
    FAMILY_HISTORY_INPUT = (By.XPATH, '(//app-nb-block-remote-header-input//input)[1]')
    PAST_MEDICAL_HISTORY_INPUT = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[2]',
    )
    FAMILY_HISTORY_SEARCH_ITEM = (
        By.XPATH,
        '//app-nb-block-remote-header-input//li[@data-item]'
        '/div[text()="streptococcal pharyngitis"]',
    )
    FAMILY_HISTORY_SEARCH_ITEM2 = (
        By.XPATH,
        '//app-nb-block-remote-header-input//li[@data-item]'
        '/div[text()="skin cancer"]',
    )
    PAST_MEDICAL_HISTORY_SEARCH_ITEM = (
        By.XPATH,
        '//app-nb-block-remote-header-input//li[@data-item]'
        '/div[text()="acute bronchitis due to streptococcus"]',
    )
    SURGICAL_HISTORY_SEARCH_ITEM = (
        By.XPATH,
        '//app-nb-block-remote-header-input//li[@data-item]/div[text()="arthrodesis"]',
    )
    SIDE_EFFECT_NO = (By.XPATH, '(//app-nb-single-select)[4]//li//span')
    SIDE_EFFECT_RELIEF_LIST = (By.XPATH, '(//app-nb-single-select)[5]//li//span')
    ACUTE_COMPLAINT_TIMEING_EPISODE_LIST = (
        By.XPATH,
        '(//app-nb-single-select)[3]//li//span',
    )
    ACUTE_COMPLAINT_TIMEING_DURATION_LIST = (
        By.XPATH,
        '(//app-nb-single-select)[4]//li//span',
    )
    ACUTE_COMPLAINT_SYMTOMP_LIST = (By.XPATH, '//app-nb-pos-neg//li/span')
    ACUTE_COMPLAINT_TREATMENT_LIFESTYLE_LIST = (By.XPATH, '//app-nb-pos-neg//li/span')
    ACUTE_COMPLAINT_TIMEING_DURATION_SEARCH = (
        By.XPATH,
        '(//app-nb-block-header-input//input)[5]',
    )
    ACUTE_COMPLAINT_FACTORS_AGGRAVATING_SEARCH = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[1]',
    )
    ACUTE_COMPLAINT_FACTORS_ALLEVIATING_SEARCH = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[2]',
    )
    ACUTE_COMPLAINT_SYMTOMP_SEARCH = (
        By.XPATH,
        '//app-nb-block-remote-header-input//input',
    )
    ASPIRIN_MEDICATION_FROM_SEARCH = (
        By.XPATH,
        '//app-nb-block-remote-header-input//li[@data-item]/div[text()= "aspirin"]',
    )
    ACUTE_COMPLAINT_SYMTOMP_ONSET_SEARCH = (
        By.XPATH,
        '(//app-nb-block-header-input//input)[1]',
    )
    ACUTE_COMPLAINT_SYMTOMP_PROGRESSION_SEARCH = (
        By.XPATH,
        '(//app-nb-block-header-input//input)[2]',
    )
    ACUTE_COMPLAINT_MEDICATION_INPUT = (
        By.XPATH,
        '//app-nb-block-remote-header-input//input',
    )
    ASPIRIN_MEDICATION_SELECTED = (
        By.XPATH,
        '//app-nb-multi-select//li/span[text()="aspirin"]',
    )
    ACUTE_COMPLAINT_VISIT_TYPE_TEMPLATE = (
        By.XPATH,
        '//app-nb-complaint-selection/ul/li[1]',
    )
    VISIT_COMPLAINT_SECTION = (
        By.XPATH,
        '//app-nb-complaint-selection//li/div[contains(text(), "TA VISIT(BD)")]',
    )
    ACUTE_COMPLAINT_SECTION = (
        By.XPATH,
        '//app-nb-complaint-selection//li/div[contains(text(), "TA ACUTE(BD)")]',
    )
    CHRONIC_COMPLAINT_SECTION = (
        By.XPATH,
        '//app-nb-complaint-selection//li/div[contains(text(), "TA CHRONIC(BD)")]',
    )
    TIMING_ONSET_INPUT = (By.XPATH, '(//app-nb-descriptor//input)[1]')
    TIMING_EPISODE_INPUT = (By.XPATH, '(//app-nb-descriptor//input)[2]')
    TIMING_EPISODE_DURATION_INPUT = (By.XPATH, '(//app-nb-descriptor//input)[3]')
    FACTORS_DETAILS_INPUT = (By.XPATH, '//app-nb-text//input')
    ACUTE_COMPLAINT_FACTORS_AGGRAVATING = (
        By.XPATH,
        '(//app-nb-pos-neg//li/span[text()="eating"])[1]',
    )
    ACUTE_COMPLAINT_FACTORS_ALLEVIATING = (
        By.XPATH,
        '(//app-nb-pos-neg//li/span[text()="anorexia"])[1]',
    )
    HPI_SECTION_TEXT = (By.XPATH, '(//div[@class="nbcanvas-sentence__list"])[2]')
    AP_CANVAS_SECTION_TEXT = (By.XPATH, '(//div[@class="nbcanvas-sentence__list"])[5]')
    HPI_VISIT_CANVAS_TEXT = (
        By.XPATH,
        '(((//div[@class="nbcanvas-sentence__list"])[2]//h5)'
        '[2]/following::div[@class="nbcanvas-sentence__list__item ng-star-inserted"]'
        '//div[@class="nbcanvas-sentence" and text()])',
    )
    HPI_SECTION_VISIT_TEXT = (
        By.XPATH,
        '(((//div[@class="nbcanvas-sentence__list"])[2]//h5)[2]'
        '/following::div[@class="nbcanvas-sentence__list__item ng-star-inserted"]'
        '//div[@class="nbcanvas-sentence" and text()])[last()]',
    )
    HPI_SECTION_CHRONIC_TEXT = (
        By.XPATH,
        '(((//div[@class="nbcanvas-sentence__list"])[2]//h5)[4]'
        '/following::div[@class="nbcanvas-sentence__list__item ng-star-inserted"]'
        '//div[@class="nbcanvas-sentence" and text()])[last()]',
    )
    HPI_SECTION_ACUTE_TEXT = (
        By.XPATH,
        '(((//div[@class="nbcanvas-sentence__list"])[2]//h5)[3]'
        '/following::div[@class="nbcanvas-sentence__list__item ng-star-inserted"]'
        '//div[@class="nbcanvas-sentence" and text()])[last()-1]',
    )
    ACUTE_COMPLAINT_MULTI_SELECT_LIST = (By.XPATH, '//app-nb-multi-select//li/span')
    ACUTE_COMPLAINT_MULTI_SELECT_ONE_LIST = (
        By.XPATH,
        '(//app-nb-multi-select)[1]//li/span',
    )
    ACUTE_COMPLAINT_MULTI_SELECT_TWO_LIST = (
        By.XPATH,
        '(//app-nb-multi-select)[2]//li/span',
    )
    ACUTE_COMPLAINT_MULTI_SELECT_THREE_LIST = (
        By.XPATH,
        '(//app-nb-multi-select)[3]//li/span',
    )
    ACUTE_COMPLAINT_SINGLE_SELECT_LIST = (By.XPATH, '//app-nb-single-select//li/span')
    ACUTE_COMPLAINT_SINGLE_SELECT_ONE_LIST = (
        By.XPATH,
        '(//app-nb-single-select)[1]//li/span',
    )
    ACUTE_COMPLAINT_SINGLE_SEARCH = (
        By.XPATH,
        '//app-nb-block-remote-header-input//input',
    )
    ACUTE_COMPLAINT_TREATMENT_PROCEDURE = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[1]',
    )
    ACUTE_COMPLAINT_LIFESTYLE_TREATMENT = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[2]',
    )
    ACUTE_COMPLAINT_TREATMENT_RELIEF = (
        By.XPATH,
        '(//app-nb-single-select)[1]//li//span',
    )
    ACUTE_COMPLAINT_TREATMENT_DETAILS = (By.XPATH, '//app-nb-text//input')
    ACUTE_COMPLAINT_TESTS_CBC = (By.XPATH, '(//app-nb-multi-select//li/span)[1]')
    ACUTE_COMPLAINT_TESTS_US_ABDOMEN = (
        By.XPATH,
        '((//app-nb-multi-select)[2]//li/span)[1]',
    )
    ACUTE_COMPLAINT_TESTS_US_ENDOSCOPY = (
        By.XPATH,
        '((//app-nb-multi-select)[3]//li/span)[1]',
    )
    ACUTE_COMPLAINT_ONSET_SEARCH = (By.XPATH, '(//app-nb-block-header-input//input)[1]')
    ACUTE_COMPLAINT_TIMING_SEARCH = (
        By.XPATH,
        '(//app-nb-block-header-input//input)[2]',
    )
    ACUTE_COMPLAINT_PROGRESSION_SEARCH = (
        By.XPATH,
        '(//app-nb-block-header-input//input)[3]',
    )
    ACUTE_COMPLAINT_EPISODE_COUNT_SEARCH = (
        By.XPATH,
        '(//app-nb-block-header-input//input)[4]',
    )
    ACUTE_COMPLAINT_LOCATION_SEARCH = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[1]',
    )
    ACUTE_COMPLAINT_RADIATION_SEARCH = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[2]',
    )
    ACUTE_COMPLAINT_DISCHARGE_SEARCH = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[3]',
    )
    ACUTE_COMPLAINT_QUALITY_SEARCH = (
        By.XPATH,
        '(//app-nb-block-header-input//input)[1]',
    )
    ACUTE_COMPLAINT_SEVERITY_SEARCH = (
        By.XPATH,
        '(//app-nb-block-header-input//input)[2]',
    )
    ACUTE_COMPLAINT_TESTS_RECENT_LABS_SEARCH = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[1]',
    )
    ACUTE_COMPLAINT_TESTS_RECENT_IMAGING_SEARCH = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[2]',
    )
    ACUTE_COMPLAINT_TESTS_RECENT_DIAGNOSTIC_SEARCH = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[3]',
    )
    ACUTE_COMPLAINT_DESCRIPTION_DETAILS_LIST = (
        By.XPATH,
        '(//app-nb-single-select)[2]//li/span',
    )
    TEXT_INPUT_ONE = (By.XPATH, '(//app-nb-text//input)[1]')
    TEXT_INPUT_TWO = (By.XPATH, '(//app-nb-text//input)[2]')
    DATE_PICKER = (By.XPATH, '//app-nb-date//input')
    ACUTE_COMPLAINT_POS_NEG_SELECT_LIST = (By.XPATH, '//app-nb-pos-neg//li/span')
    ACUTE_COMPLAINT_POS_NEG_SELECT_ONE_LIST = (
        By.XPATH,
        '(//app-nb-pos-neg)[1]//li/span',
    )
    ACUTE_COMPLAINT_POS_NEG_SELECT_TWO_LIST = (
        By.XPATH,
        '(//app-nb-pos-neg)[2]//li/span',
    )
    ACUTE_COMPLAINT_POS_NEG_SELECT_THREE_LIST = (
        By.XPATH,
        '(//app-nb-pos-neg)[3]//li/span',
    )
    CHRONIC_COMPLAINT_LIFESTYLE_TREATMENT_INPUT = (By.XPATH, '//app-nb-text/input')
    OPTION_PICKER = (By.XPATH, '//app-nb-range//select/option[text()="5 "]')
    TIME_PICKER = (By.XPATH, '//app-nb-time//input')
    SINGLE_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-header-input)[1]//input')
    SECOND_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-header-input)[2]//input')
    THIRD_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-header-input)[3]//input')
    FOURTH_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-header-input)[4]//input')
    FIFTH_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-header-input)[5]//input')
    SIX_SEARCH_INPUT = (By.XPATH, '(//app-nb-block-header-input)[6]//input')
    SEARCH_THREE = (By.XPATH, '(//app-nb-block-remote-header-input//input)[3]')
    SECTION_SEARCH_INPUT_ONE = (
        By.XPATH,
        '(//app-nb-block-remote-header-input//input)[1]',
    )
    PRESET_INPUT_BOX = (By.XPATH, '//div[@class=\'nbselect__field__header\']/input')
    PRESET_SAVE_AS_NEW = (
        By.XPATH,
        '//li[contains(@class,\'nbselect__list__item\') and text()=\'Save as new\']',
    )
    PRESET_SAVE = (
        By.XPATH,
        '//li[contains(@class,\'nbselect__list__item\') and text()=\'Save\']',
    )
    SAVE_PRESET_MODAL_INPUT = (By.ID, 'save-preset-modal-input')
    SAVE_PRESET_MODAL_YES_BUTTON = (
        By.XPATH,
        '//button[contains(@class, \'nbmodal__action__cta\') and text() = ' '\'Yes\']',
    )
    PRESET_LIST_ITEMS = (
        By.XPATH,
        '//div[@class="nbselect__field__body"]'
        '//li[not(contains(@class, "nbselect__list__item--hr"))]',
    )
    BLOCKS_SECTION_HEADERS = (
        By.XPATH,
        "//app-nb-group/section//div[@class='nbblock__item__header__hl']",
    )
    PE_BLOCKS_SECTION_HEADERS = (
        By.XPATH,
        "//app-nb-group/section//div[@class='nbblock__item__header__hl']",
    )
    SELECTED_BLOCKS_TEXT = (
        By.XPATH,
        '//app-nb-group/section//span[@data-ui-nb-preview-text] | '
        '//div[@class="nbblock__item__list__item__input"]',
    )
    PE_SELECTED_BLOCKS_TEXT = (
        By.XPATH,
        '//app-nb-pe-group/section//span[@data-ui-nb-preview-text] | '
        '//div[@class="nbblock__item__list__item__input"]',
    )
    PRESET_CLEAR_ICON = (By.CSS_SELECTOR, '.nbselect_action_item .nbicon__trash')
    PRESET_CLEAR_MODAL_YES_BUTTON = (By.CSS_SELECTOR, '.nbmodal__action__cta--primary')
    PRESET_CLEAR_MODAL_NO_BUTTON = (By.XPATH, '//button[text()="Cancel"]')
    PRESET_CLEAR_ALL_INPUT_TEXT = (By.CSS_SELECTOR, '.nbmodal__content__title')
    PRESET_CLEAR_BODY_TEXT = (By.CSS_SELECTOR, '.nbmodal__content__body')
    PRESET_CLEAR_CROSS_BUTTON = (By.CSS_SELECTOR, '.nbmodal__content__close')

    COMPLAINT_ADD_BUTTON = (By.CSS_SELECTOR, '.nbtag__item__add')
    BUILD_COMPLAINT_SEARCH_INPUT = (By.CSS_SELECTOR, '.nbmodal__field__input')
    FIRST_SEARCHED_COMPLAINT = (By.XPATH, "//li[@data-item='nb-dropdown-item-0']")
    TOTAL_COMPLAINT = (By.XPATH, "//ul[contains(@class,'nbtag--edit-enabled')]/li/div")
    CURRENT_SELECTED_COMPLAINT = (By.CSS_SELECTOR, '.nbtag__item--primary > div')
    FREE_TEXT_BOX = (By.CLASS_NAME, 'nbblock__item__list__item__input')
    DELETE_PRESET_BUTTON = (By.CSS_SELECTOR, '.delete__preset__btn')
    DELETE_PRESET_MODAL_YES_BUTTON = (
        By.XPATH,
        '//button[@class="nbmodal__action__cta nbmodal__action__cta--primary"]',
    )
    GOOGLE_INPUT_FIELD = (By.NAME, 'q')

    HPI_SYMPTOMS_CONDITIONAL_BLOCK_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-hpi//app-nb-group[3]//section | //app-nb-hpi//app-nb-group[4]//section',
    )
    HPI_CHRONIC_SYMPTOMS_CONDITIONAL_BLOCK_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-hpi//app-nb-group[4]//section | //app-nb-hpi//app-nb-group[5]//section',
    )
    HPI_ACUTE_SYMPTOMS_CONDITIONAL_BLOCK_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-hpi//app-nb-group[8]//section',
    )
    HPI_MEDICATION_CONDITIONAL_BLOCK_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-hpi//app-nb-group[6]//section | //app-nb-hpi//app-nb-group[7]//section',
    )
    HPI_FAMILY_HISTORY_CONDITIONAL_BLOCK_TEXT_LOCATOR = (
        By.XPATH,
        "//app-nb-hpi//app-nb-group//section[not(contains(@class, 'nbblock--collapsed')) or contains(@class, 'nbblock--child')]",
    )
    HPI_CONDITIONAL_BLOCK_LOCATOR = (
        By.XPATH,
        "//app-nb-hpi//app-nb-group//section[not(contains(@class, 'nbblock--collapsed')) or contains(@class, 'nbblock--child')]",
    )
    HPI_PAST_MEDICAL_HISTORY_CONDITIONAL_BLOCK_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-hpi//app-nb-group[9]//section | //app-nb-hpi//app-nb-group[10]//section '
        '| //app-nb-hpi//app-nb-group[11]//section',
    )
    HPI_RECENT_LABS_CONDITIONAL_BLOCK_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-hpi//app-nb-group[8]//section | //app-nb-hpi//app-nb-group[9]//section',
    )
    HPI_LOCATION_CONDITIONAL_BLOCK_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-hpi//app-nb-group[3]//section',
    )
    HPI_FACTORS_CONDITIONAL_BLOCK_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-hpi//app-nb-group[5]//section',
    )
    HPI_TREATMENTS_CONDITIONAL_BLOCK_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-hpi//app-nb-group[11]//section',
    )
    HPI_TREATMENTS_LIFESTYLE_CONDITIONAL_BLOCK_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-hpi//app-nb-group[11]//section | //app-nb-hpi//app-nb-group[12]//section',
    )
    HPI_TESTS_CONDITIONAL_BLOCK_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-hpi//app-nb-group[15]//section',
    )
    HPI_NUMBER_INPUT_LOCATOR = (By.XPATH, '//app-nb-number/input')
    HPI_TEXT_INPUT_LOCATOR = (By.XPATH, '//app-nb-text/input')
    HPI_DATE_PICKER_LIST_LOCATOR = (By.XPATH, '//app-nb-date/input')
    COMPLAINT_NUMBER_LIST_LOCATOR = (By.XPATH, '//app-nb-complaint-selection//sub')
    AP_MEDICATION_CONDITIONAL_BLOCK_LIST_LOCATOR = (
        By.XPATH,
        '//app-nb-ap//app-nb-group[3]//section | //app-nb-ap//app-nb-group[4]//section',
    )
    AP_TREATMENTS_LIFESTYLE_TREATMENTS_CONDITIONAL_BLOCK_LIST_LOCATOR = (
        By.XPATH,
        '//app-nb-ap//app-nb-group[7]//section | //app-nb-ap//app-nb-group[8]//section',
    )
    AP_TREATMENTS_PROCEDURE_CONDITIONAL_BLOCK_LIST_LOCATOR = (
        By.XPATH,
        '//app-nb-ap//app-nb-group[7]//section | //app-nb-ap//app-nb-group[8]//section',
    )
    AP_TESTS_CONDITIONAL_BLOCK_LIST_LOCATOR = (
        By.XPATH,
        '//app-nb-ap//app-nb-group[12]//section | //app-nb-ap//app-nb-group[15]//section',
    )
    HPI_CHILD_CONDITIONAL_BLOCKS_LOCATOR = (By.CSS_SELECTOR, '.nbblock--child')

    # CANVAS
    CANVAS_MAIN_LOCATOR = (
        By.XPATH,
        '//app-nb-canvas-header//div[@class="nbcanvas-header"]//div',
    )
    CANVAS_SECTION_NOTE_LOCATOR = (
        By.XPATH,
        '//app-nb-canvas//app-nb-canvas-note/div[1]/div',
    )
    CANVAS_HPI_LOCATOR = (By.XPATH, '//app-nb-canvas//app-nb-canvas-hpi/div[1]/div')
    CANVAS_ROS_LOCATOR = (By.XPATH, '//app-nb-canvas//app-nb-canvas-ros/div[1]/div')
    CANVAS_ROS_FREE_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-canvas//app-nb-canvas-ros/div[1]/div[2]',
    )
    CANVAS_PE_LOCATOR = (By.XPATH, '//app-nb-canvas//app-nb-canvas-pe/div[1]/div')
    CANVAS_AP_LOCATOR = (By.XPATH, '//app-nb-canvas//app-nb-canvas-ap/div[1]/div')

    CANVAS_HPI_H5_LOCATOR = (By.XPATH, '//app-nb-canvas//app-nb-canvas-hpi//h5')
    CANVAS_AP_H5_LOCATOR = (By.XPATH, '//app-nb-canvas//app-nb-canvas-ap//h5')
    CANVAS_PE_H5_LOCATOR = (By.XPATH, '//app-nb-canvas//app-nb-canvas-pe//h5')

    WHOLE_HPI_CANVAS = (By.XPATH, '//app-nb-canvas-hpi')

    HPI_CANVAS_FREE_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-canvas-hpi//app-nb-text-editor'
        '//div[@class="nbcanvas-sentence nbcanvas-sentence--secondary"]',
    )
    AP_CANVAS_FREE_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-canvas-ap//app-nb-text-editor'
        '//div[@class="nbcanvas-sentence nbcanvas-sentence--secondary"]',
    )
    PE_CANVAS_FREE_TEXT_LOCATOR = (
        By.XPATH,
        '//app-nb-canvas-pe//app-nb-text-editor'
        '//div[@class="nbcanvas-sentence nbcanvas-sentence--secondary"]',
    )

    ADDED_COMPLAINT_LIST = (
        By.XPATH,
        '//app-nb-complaint-selection//div[@class="nbtag__item__text"]',
    )
    ADDED_OTHER_COMPLAINT_LIST_WHICH_ARE_NOT_CURRENTLY_SELECTED = (
        By.XPATH,
        '//app-nb-complaint-selection//li[not(contains(@class, "nbtag__item--primary"))]/div',
    )
    COMPLAINT_EDIT_INPUT_FIELD = (By.CSS_SELECTOR, '.nbtag__item__input__field')
    CONFIRM_COMPLAINT_DELETE_MODAL_YES_BUTTON = (
        By.CSS_SELECTOR,
        '.nbmodal__action__cta--primary',
    )

    BLOCK_FOCUS_LOCATOR_H1 = (
        By.XPATH,
        '//div[contains(@class,"is--focused")]//div[@class="nbblock__item__header__hl"]',
    )
    BLOCK_FOCUS_LOCATOR = (By.XPATH, '//div[contains(@class,"is--focused")]')

    SEARCH_COMPLAINT_ROW_LIST = (By.XPATH, '//app-nb-complaint-selector//li')
    SEARCH_COMPLAINT_NAME_LIST = (
        By.CSS_SELECTOR,
        'app-nb-complaint-selector li div.nbdropdown__item__primary'
    )
    SEARCH_COMPLAINT_TYPE_LIST = (
        By.CSS_SELECTOR,
        'app-nb-complaint-selector li div.nbdropdown__item__secondary span:nth-child(1)'
    )
    SEARCH_COMPLAINT_SPECIALTY_LIST = (
        By.CSS_SELECTOR,
        'app-nb-complaint-selector li div.nbdropdown__item__secondary span:nth-child(2)'
    )
    SEARCH_COMPLAINTS_MODAL_TITLE_LOCATOR = (
        By.CSS_SELECTOR,
        '.nbmodal__content__title',
    )
    SEARCH_COMPLAINT_MODAL_CONTENTS_LOCATOR = (
        By.XPATH,
        "//div[contains(@class, 'nbdropdown__item') "
        "and not(contains(@class , 'nbdropdown__item--paginator'))]",
    )
    SEARCH_COMPLAINT_MODAL_NEXT_LOCATOR = (
        By.XPATH,
        "//li[contains(@class , 'nbdropdown__item--paginator')]"
        "//span[contains(text(), 'Next')]",
    )
    SEARCH_COMPLAINT_MODAL_PREVIOUS_LOCATOR = (
        By.XPATH,
        "//li[contains(@class , 'nbdropdown__item--paginator')]"
        "//span[contains(text(), 'Previous')]",
    )
    SEARCH_COMPLAINT_CLOSE_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        '.nbmodal__content__close',
    )
    COMPLAINT_PRESET_SELECTION = (By.TAG_NAME, 'app-nb-complaint-preset')

    # Custom complaint locator
    POS_NEG_DESCRIPTOR1 = (By.XPATH, '(//app-nb-pos-neg//li/span)[1]')
    DESCRIPTOR_SEARCH_RESULT = (By.CSS_SELECTOR, 'app-nb-block-header-input li')

    SEARCH_INPUT1 = (
        By.XPATH,
        '(//div[@class="nbblock__item__header__body__input"]/input)[1]',
    )
    SEARCH_INPUT2 = (
        By.XPATH,
        '(//div[@class="nbblock__item__header__body__input"]/input)[2]',
    )
    SEARCH_INPUT3 = (
        By.XPATH,
        '(//div[@class="nbblock__item__header__body__input"]/input)[3]',
    )
    SEARCH_INPUT4 = (
        By.XPATH,
        '(//div[@class="nbblock__item__header__body__input"]/input)[4]',
    )
    SEARCH_INPUT5 = (
        By.XPATH,
        '(//div[@class="nbblock__item__header__body__input"]/input)[5]',
    )
    SEARCH_INPUT6 = (
        By.XPATH,
        '(//div[@class="nbblock__item__header__body__input"]/input)[6]',
    )
    SEARCH_INPUT7 = (
        By.XPATH,
        '(//div[@class="nbblock__item__header__body__input"]/input)[7]',
    )
    SEARCH_INPUT8 = (
        By.XPATH,
        '(//div[@class="nbblock__item__header__body__input"]/input)[8]',
    )

    SINGLE_SELECT_DESCRIPTOR_LIST1 = (By.XPATH, '(//app-nb-single-select)[1]//li//span')
    SINGLE_SELECT_DESCRIPTOR_LIST2 = (By.XPATH, '(//app-nb-single-select)[2]//li//span')
    SINGLE_SELECT_DESCRIPTOR_LIST3 = (By.XPATH, '(//app-nb-single-select)[3]//li//span')
    SINGLE_SELECT_DESCRIPTOR_LIST4 = (By.XPATH, '(//app-nb-single-select)[4]//li//span')
    SINGLE_SELECT_DESCRIPTOR_LIST5 = (By.XPATH, '(//app-nb-single-select)[5]//li//span')
    SINGLE_SELECT_DESCRIPTOR_LIST6 = (By.XPATH, '(//app-nb-single-select)[6]//li//span')
    SINGLE_SELECT_DESCRIPTOR_LIST7 = (By.XPATH, '(//app-nb-single-select)[7]//li//span')
    MULTI_SELECT_DESCRIPTOR_LIST1 = (By.XPATH, '(//app-nb-multi-select)[1]//li//span')
    MULTI_SELECT_DESCRIPTOR_LIST2 = (By.XPATH, '(//app-nb-multi-select)[2]//li//span')

    TEXT_INPUT1 = (By.XPATH, '(//app-nb-text//input[@type="text"])[1]')
    TEXT_INPUT2 = (By.XPATH, '(//app-nb-text//input[@type="text"])[2]')
    DATE_INPUT1 = (By.XPATH, '(//app-nb-date//input[@type="date"])[1]')
    NUMBER_INPUT1 = (By.XPATH, '(//app-nb-number//input)[1]')

    BUILD_FREE_TEXT_INPUT1 = (
        By.XPATH,
        '(//div[@class="nbblock__item__list__item__input"])[1]',
    )
    BUILD_FREE_TEXT_INPUT2 = (
        By.XPATH,
        '(//div[@class="nbblock__item__list__item__input"])[2]',
    )
    BUILD_FREE_TEXT_INPUT3 = (
        By.XPATH,
        '(//div[@class="nbblock__item__list__item__input"])[3]',
    )
    BUILD_FREE_TEXT_INPUT4 = (
        By.XPATH,
        '(//div[@class="nbblock__item__list__item__input"])[4]',
    )
    BUILD_FREE_TEXT_INPUT5 = (
        By.XPATH,
        '(//div[@class="nbblock__item__list__item__input"])[5]',
    )
    BUILD_FREE_TEXT_INPUT6 = (
        By.XPATH,
        '(//div[@class="nbblock__item__list__item__input"])[6]',
    )

    MULTI_SELECT_ACTIVE_DESCRIPTOR_LIST = (
        By.CSS_SELECTOR,
        'app-nb-multi-select li[class*="active"] span'
    )


    def is_descriptor_selected(self, descriptor_name):
        descriptor_parent_locator = (
            By.XPATH,
            f'//app-nb-descriptor//li/span[normalize-space()="{descriptor_name}"]/parent::li',
        )
        return 'nbtag__item--active' in self.get_attribute(
            descriptor_parent_locator, 'class'
        )

    def get_random_index_from_list(self, descriptor_list_locator):
        total_count = self.get_total_count(descriptor_list_locator)
        if total_count < 1:
            raise IndexError('Not enough data.')
        return random.randrange(total_count)

    def get_class_attribute_from_block_list_elements_by_index(
        self, list_locator, index
    ):
        target_element = self.get_elements(list_locator)[index].find_element(
            By.XPATH, './parent::li[1]'
        )
        return target_element.get_attribute('class')

    def get_text_from_elements_by_index(self, list_locator, index):
        return self.get_text_by_element(self.get_elements(list_locator)[index])

    def click_list_elements_by_index(self, list_locator, index, wait=0):
        target_element = self.get_elements(list_locator)[index]
        self.scroll_into_view_by_element(target_element)
        self.click_and_wait_by_element(target_element, wait)

    def retry_find_class_attribute(self, list_locator, element_index, attempt=5):
        for _ in range(attempt):
            try:
                return self.get_class_attribute_from_block_list_elements_by_index(
                    list_locator, element_index
                )
            except StaleElementReferenceException:
                print('Exception in retry find element')

        # If attempts are exhausted
        return None

    def retry_get_text_from_list_by_index(self, list_locator, element_index, attempt=5):
        for _ in range(attempt):
            try:
                return self.get_text_from_elements_by_index(list_locator, element_index)
            except StaleElementReferenceException:
                print('Exception in retry get text')

        # If attempts are exhausted
        return None

    def retry_get_text(self, locator, attempt=5):
        for _ in range(attempt):
            try:
                return self.get_element(locator, 3).text.strip()
            except StaleElementReferenceException:
                print('Exception in retry get text')

        # If attempts are exhausted
        return None

    def retry_get_element_from_elements(self, list_locator, element_index, attempt=5):
        for _ in range(attempt):
            try:
                target_element = self.get_elements(list_locator)[element_index].find_element(
                    By.XPATH, './parent::li[1]'
                )
                return target_element
            except StaleElementReferenceException:
                print('Exception in retry find element')

        # If attempts are exhausted
        return None

    def retry_get_blocks_section_headers(self, attempt=5):
        for _ in range(attempt):
            try:
                elements = self.get_elements(self.BLOCKS_SECTION_HEADERS)
                return self.get_list_of_text_from_elements(elements)
            except StaleElementReferenceException:
                print('Exception in retry getting list of text')

        # If attempts are exhausted
        return None

    def retry_click(self, list_locator, element_index, wait=0, attempt=5):
        for _ in range(attempt):
            try:
                self.click_list_elements_by_index(list_locator, element_index, wait)
                break
            except StaleElementReferenceException:
                print('Exception in retry click element')


    def retry_click_by_single_locator(self, locator, attempt=5):
        for _ in range(attempt):
            try:
                self.get_element(locator, 5).click()
                break
            except:
                print('Exception in retry click element')


    def expand_blocks_by_text(self, text):
        block_header_locator = (
            By.XPATH,
            f'//app-nb-group//section//div[@class="nbblock__item__header__hl" and text()=" {text} "]'
        )
        parent_locator = (
            By.XPATH,
            f'//app-nb-group//section//div[@class="nbblock__item__header__hl" and text()=" {text} "]'
            f'/parent::*/parent::*/parent::*/parent::*'
        )
        block_header_element = self.get_element(block_header_locator, 10)
        if 'nbblock--collapsed' in self.get_attribute(parent_locator, 'class'):
            block_header_element.click()
            print(f'"{text}" block expaned.')
        else:
            print(f'"{text}" block already expanded.')

    def collapse_blocks_by_text(self, text):
        block_header_locator = (
            By.XPATH,
            f"//app-nb-group//section//div[@class='nbblock__item__header__hl' "
            f"and text()=' {text} ']",
        )
        parent_locator = (
            By.XPATH,
            f"//app-nb-group//section//div[@class='nbblock__item__header__hl' "
            f"and text()=' {text} ']"
            f"/parent::*/parent::*/parent::*/parent::*",
        )
        block_header_element = self.get_element(block_header_locator, 10)
        if 'nbblock--collapsed' not in self.get_attribute(parent_locator, 'class'):
            block_header_element.click()
            print('block collapsed.')
        else:
            print('block already collapsed.')

    def get_block_attribute_by_text(self, text):
        parent_locator = (
            By.XPATH,
            f"//app-nb-group//section//div[@class='nbblock__item__header__hl' "
            f"and text()=' {text} ']"
            f"/parent::*/parent::*/parent::*/parent::*",
        )

        return self.get_attribute(parent_locator, 'class')

    def get_selected_complaint(self):
        return self.get_text_by_locator(self.SELECTED_COMPLAINT)

    def is_block_expand(self, block_name):
        element_locator = (
            By.XPATH,
            f'//app-nb-group//section[not(contains(@class, "nbblock--child"))]'
            f'//div[@class="nbblock__primary"]'
            f'//div[@class="nbblock__item__header__hl" and normalize-space()="{block_name}"]'
            f'//ancestor::app-nb-group/section',
        )
        return 'nbblock--collapsed' not in self.get_attribute(element_locator, 'class')

    def is_descriptor_group_selected(self, block_name, descriptor_group_index):
        """
        descriptor_group_index start from 1
        """
        element_locator = (
            By.XPATH,
            f'(//app-nb-group//section[not(contains(@class, "nbblock--child"))]//div[@class="nbblock__primary"]'
            f'//div[@class="nbblock__item__header__hl" and normalize-space()="{block_name}"]'
            f'//ancestor::app-nb-group//app-nb-block-item/div)[{descriptor_group_index}]',
        )
        return 'is--focused' in self.get_attribute(element_locator, 'class')

    def search_and_select(self, search_locator, search_item):
        max_49_char_of_search_item = search_item[:49]
        self.enter_text_at(max_49_char_of_search_item, search_locator, 1)
        drop_down_element = (By.XPATH,
                             f'//li[contains(@class,"nbdropdown__item") and normalize-space()="{search_item}"] | '
                             f'//li[contains(@class,"nbdropdown__item")]/div[text()="{search_item}"] | '
                             f'//li[contains(@class,"nbdropdown__item") and contains(text(),"+ Add new")]')
        self.retry_click_by_single_locator(drop_down_element)

    def insert_text_in_search_field(self, search_field_locator, text):
        self.enter_text_at(text, search_field_locator, 1)

    def get_text_from_search_field(self, search_field_locator):
        return self.get_text_by_locator(search_field_locator)

    def paste_text_in_search_field(self, search_field_locator):
        # create action chain object
        self.click_and_wait(search_field_locator, 1)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(
            Keys.CONTROL
        ).perform()

    def click_on_subtab(self, subtab_name):
        """
        Clicks on sub tab under Build tab i.e.: HPI, ROS etc.
        :param subtab_name: name of the sub tab
        """
        sub_tab_locator_str = f'//span[text()="{subtab_name}"]/parent::li'
        self.click_and_wait((By.XPATH, sub_tab_locator_str), 2)

    def switch_to_subtab(self, subtab_name):
        self.click_on_subtab(subtab_name)
        HomePage(self.driver).wait_for_loader()
        print(f'Switched to {subtab_name.upper()} successfully.')

    def is_subtab_selected(self, subtab_name):
        home_page = HomePage(self.driver)
        home_page.wait_for_loader()
        sub_tabs = self.get_elements(self.SUB_TAB_LIST)
        return next(
            (
                'active' in self.get_attribute_from_element(sub_tab, 'class')
                for sub_tab in sub_tabs
                if self.get_text_by_element(sub_tab) == subtab_name
            ),
            False,
        )

    def get_text_from_free_text_box(self, block_no, canvas=False, pe_free_text=False):
        free_text_locator = self.get_appropriate_free_text_locator(
            block_no, canvas, pe_free_text
        )
        self.click_and_wait(self.CANVAS_NOTE_LOCATOR, 1)
        return self.get_text_by_locator(free_text_locator)

    def add_text_in_free_text_box(
        self, block_no, text, clear_existing=True, canvas=False, pe_free_text=False
    ):
        free_text_locator = self.get_appropriate_free_text_locator(
            block_no, canvas, pe_free_text
        )
        self.click_and_wait(self.NOTES, 1)
        self.enter_text_at(text, free_text_locator, clear_existing, 1)
        self.click_and_wait(self.NOTES, 1)

    def delete_text_in_free_text_box(
        self,
        block_no,
        canvas=False,
        pe_free_text=False,
        verify_hpi_canvas=False,
        verify_ap_canvas=False,
        verify_pe_canvas=False,
    ):
        self.click_and_wait(self.NOTES, 1)
        free_text_locator = self.get_appropriate_free_text_locator(
            block_no, canvas, pe_free_text
        )
        self.click_and_wait(free_text_locator, 1)
        self.clear_field_by_keyboard(
            free_text_locator, verify_hpi_canvas, verify_ap_canvas, verify_pe_canvas
        )

    def copy_text_from_free_text_box(self, block_no, canvas=False, pe_free_text=False):
        # create action chain object
        action = ActionChains(self.driver)
        free_text_locator = self.get_appropriate_free_text_locator(
            block_no, canvas, pe_free_text
        )
        self.click_and_wait(self.NOTES, 1)
        self.press_ctrl_and_a(free_text_locator)
        action.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()
        self.click_and_wait(self.NOTES, 1)

    def copy_text_from_locator(self, locator):
        # create action chain object
        action = ActionChains(self.driver)
        self.press_ctrl_and_a(locator)
        action.key_down(Keys.CONTROL).send_keys('C').key_up(Keys.CONTROL).perform()

    def paste_text_in_currently_focused_canvas_area(self):
        # self.Press_Ctrl_And_V(locator)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(
            Keys.CONTROL
        ).perform()

    def paste_text_in_free_text_box(self, block_no, canvas=False, pe_free_text=False):
        free_text_locator = self.get_appropriate_free_text_locator(
            block_no, canvas, pe_free_text
        )
        if '--focused' in self.get_attribute(free_text_locator, 'class') or canvas or pe_free_text:
            self.paste_text_in_input_field_by_locator(free_text_locator)
        else:
            self.paste_text_in_input_field_by_locator(free_text_locator)
            print('Canvas free text is not focused!')

    def cut_text_from_free_text_box(self, block_no, canvas=False, pe_free_text=False):
        free_text_locator = self.get_appropriate_free_text_locator(
            block_no, canvas, pe_free_text
        )
        self.click_and_wait(self.NOTES, 1)
        self.press_ctrl_and_a(free_text_locator)
        # create action chain object
        action = ActionChains(self.driver)
        # perform the operation
        action.key_down(Keys.CONTROL).send_keys('X').key_up(Keys.CONTROL).perform()
        self.click_and_wait(self.NOTES, 1)

    def remove_character_from_free_text_field(
        self, number_of_character, block_no, canvas=False, pe_free_text=False
    ):
        free_text_locator = self.get_appropriate_free_text_locator(
            block_no, canvas, pe_free_text
        )
        for _ in range(number_of_character):
            self.click_and_wait(self.NOTES, 1)
            self.get_element(free_text_locator).send_keys(Keys.END)
            self.click_and_wait(self.NOTES, 1)
            self.get_element(free_text_locator).send_keys(Keys.BACKSPACE)
            self.click_and_wait(self.NOTES, 1)

    def remove_character_from_textbox(self, locator, number_of_character):
        for _ in range(number_of_character):
            self.get_element(locator).send_keys(Keys.END)
            self.get_element(locator).send_keys(Keys.BACKSPACE)
            # self.click_and_wait(self.notes, 1)

    def clear_field_by_keyboard(
        self,
        locator,
        verify_hpi_canvas=False,
        verify_ap_canvas=False,
        verify_pe_canvas=False,
    ):
        canvas_locator = ''
        self.click_and_wait(self.CANVAS_NOTE_LOCATOR, 1)
        try:
            value = self.get_attribute(locator, 'value')
            input_value_length = len(value)
            text_or_value = value
            text_length = 0
        except AttributeError:
            input_value_length = 0
            text_or_value = self.get_text_by_locator(locator)
            text_length = len(text_or_value)
        self.get_element(locator).send_keys(Keys.END)
        action = ActionChains(self.driver)
        increament = 1
        if verify_hpi_canvas:
            canvas_locator = self.HPI_SECTION_TEXT
        if verify_ap_canvas:
            canvas_locator = self.AP_CANVAS_SECTION_TEXT

        if verify_pe_canvas:
            canvas_locator = PeTab.PE_CANVAS_SECTION
        for _ in range(text_length or input_value_length):
            text_without_removed_character = ''
            action.key_down(Keys.BACKSPACE).key_up(Keys.CONTROL).perform()
            time.sleep(0.1)
            if verify_hpi_canvas or verify_ap_canvas or verify_pe_canvas:
                for idx in range(len(text_or_value) - increament):
                    text_without_removed_character = (
                        text_without_removed_character + text_or_value[idx]
                    )
                text_without_removed_character = text_without_removed_character.strip()
                time.sleep(1)
                self.wait_for_visibility_of_text(
                    canvas_locator, text_without_removed_character, 5
                )
                increament += 1

    def get_canvas_free_text_locator(self, block_no):
        free_text_locator = ''
        if block_no == 1:
            free_text_locator = self.CANVAS_NOTE_LOCATOR
        elif block_no == 2:
            free_text_locator = self.HPI_CANVAS_FREE_TEXT_LOCATOR
        elif block_no == 3:
            free_text_locator = self.CANVAS_ROS_FREE_TEXT_LOCATOR
        elif block_no == 4:
            free_text_locator = self.PE_CANVAS_FREE_TEXT_LOCATOR
        elif block_no == 5:
            free_text_locator = self.AP_CANVAS_FREE_TEXT_LOCATOR
        return free_text_locator

    def paste_using_keyboard_shortcut_in_canvas_note(self):
        self.paste_text_in_free_text_box(1, canvas=True)

    def paste_using_keyboard_shortcut_in_hpi_canvas(self):
        self.paste_text_in_free_text_box(2, canvas=True)

    def paste_using_keyboard_shortcut_in_ros_canvas(self):
        self.paste_text_in_free_text_box(3, canvas=True)

    def paste_using_keyboard_shortcut_in_pe_canvas(self):
        self.paste_text_in_free_text_box(4, canvas=True)

    def paste_using_keyboard_shortcut_in_ap_canvas(self):
        self.paste_text_in_free_text_box(5, canvas=True)

    def get_canvas_note_text(self):
        return self.get_text_by_locator(self.CANVAS_NOTE_LOCATOR)

    def get_added_complaint_list_of_text(self):
        return self.get_list_of_text_from_locator(self.ADDED_COMPLAINT_LIST)

    def get_added_complaint_name_list(self):
        for _ in range(5):
            try:
                complaint_text_list = self.get_list_of_text_from_locator(self.ADDED_COMPLAINT_LIST)
                return [re.sub(r'\n\d+', '', complaint_text) for complaint_text in complaint_text_list]
            except StaleElementReferenceException:
                print('StaleElementReferenceException in getting complaint elements')
        return None

    def get_total_added_complaint_count(self):
        for _ in range(5):
            try:
                return self.get_total_count(self.ADDED_COMPLAINT_LIST)
            except StaleElementReferenceException:
                print('StaleElementReferenceException in getting complaint elements')
        return None

    def get_total_block_groups_count(self):
        return self.get_total_count(self.BLOCK_GROUPS_LOCATOR)

    def is_block_groups_visible(self):
        return self.is_element_visible(self.BLOCK_GROUPS_LOCATOR, 10)

    def select_complaint_by_index(self, index):
        for _ in range(5):
            try:
                complaint_elements = self.get_elements(self.ADDED_COMPLAINT_LIST)
                self.click_and_wait_by_element(complaint_elements[index])
                HomePage(self.driver).wait_for_loader()
                break
            except StaleElementReferenceException:
                print('Exception in getting complaint elements')

    def select_complaint_by_name(self, complaint_name):
        for _ in range(5):
            try:
                for element in self.get_elements(self.ADDED_COMPLAINT_LIST):
                    if complaint_name in self.get_text_by_element(element):
                        self.click_and_wait_by_element(element)
                        break
                HomePage(self.driver).wait_for_loader()
                break
            except StaleElementReferenceException:
                print('Exception in getting complaint elements')

    def is_complaint_selected(self, index):
        for _ in range(5):
            try:
                complaint_parent_element = (
                    self.get_elements(self.ADDED_COMPLAINT_LIST)[index]
                    .find_element(By.XPATH, './parent::li')
                )
                class_value = self.get_attribute_from_element(complaint_parent_element, 'class')
                return 'nbtag__item--primary' in class_value
            except StaleElementReferenceException:
                print('StaleElementReferenceException in getting complaint elements')
        return None

    def hovar_to_complaint_no(self, complaint_no_element):
        self.hover_element(complaint_no_element)

    def get_complaint_name_from_edit_input(self):
        return self.get_text_by_locator(self.COMPLAINT_EDIT_INPUT_FIELD).strip()

    def get_complaint_name_from_edit_input_field_count(self):
        return self.get_total_count(self.COMPLAINT_EDIT_INPUT_FIELD)

    def delete_complaint_by_name(self, name):
        result = False
        try:
            total_complaint_no_list = self.get_elements(
                self.COMPLAINT_NUMBER_LIST_LOCATOR
            )
            for complaint_no in total_complaint_no_list:
                self.hovar_to_complaint_no(complaint_no)
                time.sleep(1)
                edit_button = complaint_no.find_element(
                    By.XPATH, './/following::button[1]'
                )
                self.is_element_visible(edit_button, 10)
                self.hover_and_click_by_element(edit_button)
                if name == self.get_complaint_name_from_edit_input():
                    delete_button = complaint_no.find_element(
                        By.XPATH, './/following::button[2]'
                    )
                    assert self.text_to_be_present_in_web_element(
                        delete_button, 'delete', 2
                    ), 'Delete not presentt'
                    delete_button.click()
                    self.click_on_confirm_delete_complaint_modal_yes_button()
                    result = True
                    break
        except AssertionError as error:
            print(error.args[0] if error.args else 'error')

        return result

    def click_on_complaints_edit_button(self, complaint_number_list):
        total_complaint_no_list = self.get_elements(complaint_number_list)
        complaint_names_in_edit_input = []
        input_field_count = 0
        for complaint_no in total_complaint_no_list:
            self.hovar_to_complaint_no(complaint_no)
            time.sleep(1)
            edit_button = complaint_no.find_element(By.XPATH, './/following::button[1]')
            self.hover_and_click_by_element(edit_button)
            complaint_names_in_edit_input.append(
                self.get_complaint_name_from_edit_input()
            )
            input_field_count = self.get_complaint_name_from_edit_input_field_count()
        complaint_names_in_edit_input.append(input_field_count)
        return complaint_names_in_edit_input

    def click_on_complaints_edit_button_by_name(self, name):
        total_complaint_no_list = self.get_elements(self.COMPLAINT_NUMBER_LIST_LOCATOR)
        for idx, complaint_no in enumerate(total_complaint_no_list):
            print(self.get_elements(self.ADDED_COMPLAINT_LIST)[idx].text)
            if name in self.get_elements(self.ADDED_COMPLAINT_LIST)[idx].text:
                self.hovar_to_complaint_no(complaint_no)
                time.sleep(1)
                edit_button = complaint_no.find_element(
                    By.XPATH, './/following::button[1]'
                )
                self.hover_and_click_by_element(edit_button)

    def click_on_confirm_delete_complaint_modal_yes_button(self):
        self.click_and_wait_for_invisibility(
            self.CONFIRM_COMPLAINT_DELETE_MODAL_YES_BUTTON
        )

    def edit_complaint_from_initial_name(self, initial_name):
        self.click_on_complaints_edit_button_by_name(initial_name)
        self.remove_character_from_complaint_edit_input_field(2)

    def remove_character_from_complaint_edit_input_field(self, number):
        for _ in range(number):
            self.get_element(BuildTab.COMPLAINT_EDIT_INPUT_FIELD).send_keys(Keys.END)
            self.get_element(BuildTab.COMPLAINT_EDIT_INPUT_FIELD).send_keys(
                Keys.BACKSPACE
            )

    def insert_text_in_complaint_edit_input_field(self, text, clear_existing=False):
        self.enter_text_at(
            text, BuildTab.COMPLAINT_EDIT_INPUT_FIELD, clear_existing=clear_existing
        )

    def get_appropriate_free_text_locator(self, block_no, canvas, pe_free_text=False):
        if canvas:
            return self.get_canvas_free_text_locator(block_no)
        return (
            (
                By.XPATH,
                f"(//app-nb-pe-block-free-text)[{block_no}]//div[@class='nbblock__item__list__item__input']",
            )
            if pe_free_text
            else (
                By.XPATH,
                f"(//app-nb-group-block-free-text)[{block_no}]//div[@class='nbblock__item__list__item__input']",
            )
        )

    @staticmethod
    def process_list_for_notewritter_verification(notewriterr_list):
        for idx, list_element in enumerate(notewriterr_list):
            text = list_element.replace('\n', '')
            text = text.strip()
            notewriterr_list[idx] = text
        return notewriterr_list

    def insert_enter_key_in_free_text(self, block_no, canvas=False):
        free_text_element = self.get_element(
            self.get_appropriate_free_text_locator(block_no, canvas=canvas), 5
        )
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(free_text_element).click().perform()
        action_chains.send_keys(Keys.END).perform()
        action_chains.send_keys(Keys.ENTER).perform()

    def insert_ctrl_enter_key_in_canvas_and_write_text_in_line(
        self, text, new_line_text
    ):
        canvas_text_element = self.get_element_by_text(text)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(canvas_text_element).click().perform()
        action_chains.send_keys(Keys.END).perform()
        action_chains.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(
            Keys.CONTROL
        ).perform()
        action_chains.send_keys(new_line_text).perform()

    def insert_enter_key_in_canvas_text_and_paste_text(self, text):
        canvas_text_element = self.get_element_by_text(text)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(canvas_text_element).click().perform()
        action_chains.send_keys(Keys.END).perform()
        action_chains.send_keys(Keys.ENTER).perform()
        time.sleep(1)
        action_chains.key_down(Keys.CONTROL).send_keys('v').key_up(
            Keys.CONTROL
        ).perform()

    def insert_text_in_notebuilder_input_text_field(self, text):
        self.enter_text_at(text, self.HPI_TEXT_INPUT_LOCATOR, 1)

    def insert_number_in_notebuilder_input_number_field(self, text):
        self.enter_text_at(text, self.HPI_NUMBER_INPUT_LOCATOR, 1)

    def get_text_from_notebuilder_input_text_field(self):
        return self.get_text_by_locator(self.HPI_TEXT_INPUT_LOCATOR)

    def get_number_from_notebuilder_input_number_field(self):
        return self.get_text_by_locator(self.HPI_NUMBER_INPUT_LOCATOR)

    def delete_number_from_notebuilder_input_number_field(self):
        self.clear_field_by_keyboard(self.HPI_NUMBER_INPUT_LOCATOR)

    def delete_text_from_notebuilder_input_text_field(self):
        self.clear_field_by_keyboard(self.HPI_TEXT_INPUT_LOCATOR)

    def check_text_is_present_in_hpi_canvas(self, text):
        return self.wait_for_visibility_of_text(self.HPI_SECTION_TEXT, text, 5)

    def check_text_is_not_present_in_hpi_canvas(self, text):
        return self.wait_for_invisibility_of_text(self.HPI_SECTION_TEXT, text, 5)

    def check_text_is_present_in_ap_canvas(self, text):
        return self.wait_for_visibility_of_text(self.AP_CANVAS_SECTION_TEXT, text, 5)

    def check_text_is_not_present_in_ap_canvas(self, text):
        return self.wait_for_invisibility_of_text(PeTab.PE_CANVAS_SECTION, text, 5)

    def check_text_is_present_in_pe_canvas(self, text):
        return self.wait_for_visibility_of_text(PeTab.PE_CANVAS_SECTION, text, 5)

    def check_text_is_not_present_in_pe_canvas(self, text):
        return self.wait_for_invisibility_of_text(PeTab.PE_CANVAS_SECTION, text, 5)

    def get_text_from_hpi_canvas(self):
        return self.get_text_by_locator(self.HPI_SECTION_TEXT)

    def get_text_from_ap_canvas(self):
        return self.get_text_by_locator(self.AP_CANVAS_SECTION_TEXT)

    def get_text_from_pe_canvas(self):
        return self.get_text_by_locator(PeTab.PE_CANVAS_SECTION)

    def get_current_focused_block_class(self):
        return self.get_attribute(self.BLOCK_FOCUS_LOCATOR, 'class')

    def get_current_focused_block_names(self):
        return self.get_list_of_text_from_locator(self.BLOCK_FOCUS_LOCATOR_H1)

    def get_search_complaint_modal_title(self):
        return self.get_text_by_locator(self.SEARCH_COMPLAINTS_MODAL_TITLE_LOCATOR)

    def open_search_complaint_modal(self):
        self.click_and_wait_for_target(
            self.COMPLAINT_ADD_BUTTON, self.SEARCH_COMPLAINT_MODAL_CONTENTS_LOCATOR
        )

    def get_current_contents_from_search_complaints_modal(self):
        return self.get_list_of_text_from_locator(
            self.SEARCH_COMPLAINT_MODAL_CONTENTS_LOCATOR
        )

    def click_on_next_link_from_search_complaint_modal(self):
        self.click_and_wait(self.SEARCH_COMPLAINT_MODAL_NEXT_LOCATOR)

    def click_on_previous_link_from_search_complaint_modal(self):
        self.click_and_wait(self.SEARCH_COMPLAINT_MODAL_PREVIOUS_LOCATOR)

    def close_search_complaint_modal(self):
        self.click_and_wait(self.SEARCH_COMPLAINT_CLOSE_BUTTON_LOCATOR, 2)

    def get_saved_preset_list_items(self):
        self.open_preset_list()
        return self.get_list_of_text_from_elements(
            self.get_elements(self.PRESET_LIST_ITEMS)
        )

    def enter_text_in_search_complaint_modal_input(self, text):
        self.enter_text_at(text, self.BUILD_COMPLAINT_SEARCH_INPUT, 1)

    def get_text_from_search_complaint_modal_input(self):
        return self.get_attribute(self.BUILD_COMPLAINT_SEARCH_INPUT, 'value')

    def clear_preset(self):
        self.click_and_wait_for_target(
            self.PRESET_CLEAR_ICON, self.PRESET_CLEAR_MODAL_YES_BUTTON
        )
        self.click_and_wait(self.PRESET_CLEAR_MODAL_YES_BUTTON, 1)

    def select_preset(self, name):
        self.open_preset_list()
        self.select_item_from_selection_list(self.PRESET_LIST_ITEMS, name)

    def save_preset(self, name):
        self.select_preset(name)

    def open_preset_list(self):
        if self.is_element_visible(self.PRESET_LIST_ITEMS, 5):
            print('Preset list already opened')
        else:
            self.click_and_wait(self.PRESET_INPUT_BOX, 5)

    def delete_preset(self):
        self.click_and_wait_for_target(
            self.DELETE_PRESET_BUTTON, self.DELETE_PRESET_MODAL_YES_BUTTON
        )
        time.sleep(2)
        self.click_and_wait(self.DELETE_PRESET_MODAL_YES_BUTTON)

    def get_selected_text_from_descriptor_block_elements(self):
        selected_blocks_body_text_when_saved = []
        for _ in range(5):
            try:
                selected_blocks_body_text_when_saved = (
                    self.get_list_of_text_from_elements(
                        self.get_elements(self.SELECTED_BLOCKS_TEXT)
                    )
                )
                break
            except StaleElementReferenceException:
                print('exception')
        return selected_blocks_body_text_when_saved

    def add_existing_complaint(self, target_complaint_name, complaint_type, specialty='PRIMARY'):
        self.click_and_wait_for_target(self.COMPLAINT_ADD_BUTTON, self.BUILD_COMPLAINT_SEARCH_INPUT)
        homepage = HomePage(self.driver)
        homepage.wait_for_loader()
        self.enter_text_at(target_complaint_name, self.BUILD_COMPLAINT_SEARCH_INPUT, 1)
        homepage.wait_for_loader()

        for index, complaint_name_element in enumerate(self.get_elements(self.SEARCH_COMPLAINT_NAME_LIST)):
            if (
                target_complaint_name == self.get_text_by_element(complaint_name_element) and
                complaint_type == self.get_elements(self.SEARCH_COMPLAINT_TYPE_LIST)[index].text and
                specialty == self.get_elements(self.SEARCH_COMPLAINT_SPECIALTY_LIST)[index].text
            ):
                self.click_and_wait_by_element(complaint_name_element)
                break

        self.wait_for_invisibility_of(self.BUILD_COMPLAINT_SEARCH_INPUT)
        homepage.wait_for_loader()
        print(f'{target_complaint_name} comaplint added from Build tab.')

    def add_custom_complaint(self, complaint_name, complaint_type='visit'):
        complaint_text = ''
        self.click_and_wait_for_target(self.COMPLAINT_ADD_BUTTON, self.BUILD_COMPLAINT_SEARCH_INPUT)
        homepage = HomePage(self.driver)
        homepage.wait_for_loader()
        self.enter_text_at(complaint_name, self.BUILD_COMPLAINT_SEARCH_INPUT, 1)
        homepage.wait_for_loader()

        complaint_list = self.get_list_of_text_from_locator(self.SEARCH_COMPLAINT_ROW_LIST)
        for search_complaints in self.get_elements(self.SEARCH_COMPLAINT_ROW_LIST):
            if (
                complaint_name in search_complaints.text
                and f'Add new {complaint_type}' in search_complaints.text
            ):
                complaint_text = search_complaints.text.strip()
                break

        self.select_item_from_selection_list(self.SEARCH_COMPLAINT_ROW_LIST, complaint_text)
        homepage.wait_for_loader()
        return complaint_list

    def prepare_preset_data_hpi_visit(self):
        self.expand_blocks_by_text('Visit')
        accompanied_by_item_index = self.get_random_index_from_list(self.VISIT_LIST)
        self.retry_click(self.VISIT_LIST, accompanied_by_item_index)

        self.add_text_in_free_text_box(1, 'test free text visit accompanied by')

        self.expand_blocks_by_text('Description')

        description_item_index = self.get_random_index_from_list(self.DESCRIPTION_LIST)
        self.retry_click(self.DESCRIPTION_LIST, description_item_index)

        self.insert_number_in_notebuilder_input_number_field('3')

        description_onset_item_index = self.get_random_index_from_list(self.ONSET_LIST)
        self.retry_click(self.ONSET_LIST, description_onset_item_index)

        description_progression_item_index = self.get_random_index_from_list(
            self.PROGRESSION_LIST
        )
        self.retry_click(self.PROGRESSION_LIST, description_progression_item_index)

        self.add_text_in_free_text_box(2, 'test free text description by')

        self.expand_blocks_by_text('Medications')

        self.search_and_select(self.SEARCH_INPUT1, 'aspirin')

        self.insert_text_in_notebuilder_input_text_field('15')

        medications_frequency_item_index = self.get_random_index_from_list(
            self.FREQUENCY_LIST
        )
        self.retry_click(self.FREQUENCY_LIST, medications_frequency_item_index)

        medications_relief_item_index = self.get_random_index_from_list(
            self.RELIEF_LIST
        )
        self.retry_click(self.RELIEF_LIST, medications_relief_item_index)

        medications_compliance_item_index = self.get_random_index_from_list(
            self.COMPLIANCE_LIST
        )
        self.retry_click(self.COMPLIANCE_LIST, medications_compliance_item_index)

        medications_refils_item_index = self.get_random_index_from_list(
            self.REFILS_LIST
        )
        self.retry_click(self.REFILS_LIST, medications_refils_item_index)

        self.add_text_in_free_text_box(3, 'test free text medication')

        self.expand_blocks_by_text('History')

        self.search_and_select(self.SEARCH_INPUT1, 'streptococcal pharyngitis')

        # self.search_and_select(self.SEARCH_INPUT2, 'acute bronchitis due to streptococcus')

        self.add_text_in_free_text_box(4, 'test free text history')
        self.collapse_blocks_by_text('History')

    def add_patient_and_navigate_to_build(self):
        data = user_input_data()
        home_page = HomePage(self.driver)
        organize_tab = OrganizeTab(self.driver)
        home_page.add_patient()
        organize_tab.set_organize_tab_value(
            patient_name=data.patient_first_name,
            gender=data.gender,
            age=data.age,
            visit_type=data.type[0],
            start_time=data.start_time,
            service_type=data.service_type[0],
            complaint_visit=pytest.configs.get_config('visit_complaint_name')
        )
        home_page.switch_to_tab('Build')
        home_page.wait_for_loader()

    def preset_visibility_common_steps(self, section):
        self.add_patient_and_navigate_to_build()
        if section == 'AP':
            self.switch_to_subtab('A/P')

        if section == 'PE':
            self.switch_to_subtab('PE')

        self.open_preset_list()

    def is_complaint_preset_selection_visible(self):
        return (
            self.is_element_visible(self.COMPLAINT_PRESET_SELECTION, 5)
            and self.get_total_count(self.COMPLAINT_PRESET_SELECTION) == 1
        )

    def collapse_all_block(self):
        block_header_locator = (
            By.XPATH,
            '//section/app-nb-group/section/div[1]/div/div[1]/div',
        )

        for _ in self.get_elements(block_header_locator):
            parent_locator = (
                By.XPATH,
                '//section/app-nb-group/section/div[1]/div/div[1]/div/parent::*/parent::*/parent::*/parent::*',
            )
            block_header_element = self.get_element(block_header_locator, 10)
            if 'nbblock--collapsed' not in self.get_attribute(parent_locator, 'class'):
                block_header_element.click()
                print('block collapsed.')
            else:
                print('block already collapsed.')

    def wait_until_attribute_contains_by_list_locator(self, list_locator, element_index, attribute,
                                                      attribute_value, timeout=10):
        for _ in range(5):
            try:
                target_element = (
                    self.get_elements(list_locator)[element_index]
                    .find_element(By.XPATH, './parent::li[1]')
                )
                self.wait_for_expected_condition(
                    lambda driver: attribute_value in target_element.get_attribute(attribute),
                    max_wait=timeout
                )
                break
            except TimeoutException:
                print(f"Timed out waiting for class value '{attribute_value}'")
            except StaleElementReferenceException:
                print('Exception in getting class element')

    def wait_until_attribute_not_contains_by_list_locator(self, list_locator, element_index, attribute,
                                                          attribute_value, timeout=10):
        for _ in range(5):
            try:
                target_element = (
                    self.get_elements(list_locator)[element_index]
                    .find_element(By.XPATH, './parent::li[1]')
                )
                self.wait_for_expected_condition(
                    lambda driver: attribute_value not in target_element.get_attribute(attribute),
                    max_wait=timeout
                )
                break
            except TimeoutException:
                print(f"Timed out waiting for class value '{attribute_value}'")
            except StaleElementReferenceException:
                print('Exception in getting class element')
