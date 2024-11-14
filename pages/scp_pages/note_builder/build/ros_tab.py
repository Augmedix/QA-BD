"""
Page object for ROS tab
"""
import json
import random
import time
import uuid

from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.home_page import HomePage
from utils.app_constants import AppConstant
from utils.helper import generate_random_alphanumeric_string, generate_sublist_with_same_order


class RosTab(BasePage):
    """
    Page object for ROS tab
    """
    ROS_CANVAS_SECTION_LOCATOR = (By.XPATH, '//app-nb-canvas//app-nb-canvas-ros')
    ROS_CANVAS_SENTENCE_LOCATOR = (
        By.CSS_SELECTOR, 'app-nb-canvas-ros .nbcanvas-sentence__list'
    )
    ROS_CANVAS_FIRST_SENTENCE_LOCATOR = (
        By.CSS_SELECTOR, 'app-nb-canvas-ros .nbcanvas-sentence__list__item:nth-child(1)'
    )
    ROS_BLOCK_ITEM = (By.XPATH, '//app-nb-ros//app-nb-block-item')
    ROS_BLOCK_ITEM_LAST = (By.XPATH, '//app-nb-ros//app-nb-block-item/div')
    ROS_BLOCKS_HEADER_LOCATOR = (
        By.CSS_SELECTOR, 'app-nb-ros .nbblock__primary .nbblock__item__header__hl'
    )
    STATEMENT_TEXT_INPUT_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-inline-text/input)[1]'
    )

    CONSTITUTIONAL_DESCRIPTORS_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-pos-neg)[1]//li/span'
    )
    SKIN_DESCRIPTORS_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-pos-neg)[2]//li/span'
    )
    EYES_DESCRIPTORS_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-pos-neg)[3]//li/span'
    )
    ENT_DESCRIPTORS_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-pos-neg)[4]//li/span'
    )
    CARDIOVASCULAR_DESCRIPTORS_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-pos-neg)[5]//li/span'
    )
    RESPIRATORY_DESCRIPTORS_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-pos-neg)[6]//li/span'
    )
    GASTROINTESTINAL_DESCRIPTORS_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-pos-neg)[7]//li/span'
    )
    GENITOURINARY_DESCRIPTORS_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-pos-neg)[8]//li/span'
    )
    MUSCULOSKELETAL_DESCRIPTORS_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-pos-neg)[9]//li/span'
    )
    NEUROLOGICAL_DESCRIPTORS_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-pos-neg)[10]//li/span'
    )
    PSYCHIATRIC_DESCRIPTORS_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-pos-neg)[11]//li/span'
    )
    ENDOCRINE_DESCRIPTORS_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-pos-neg)[12]//li/span'
    )

    CONSTITUTIONAL_SEARCH_INPUT_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-block-remote-header-input//input)[1]'
    )
    SKIN_SEARCH_INPUT_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-block-remote-header-input//input)[2]'
    )
    EYES_SEARCH_INPUT_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-block-remote-header-input//input)[3]'
    )
    ENT_SEARCH_INPUT_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-block-remote-header-input//input)[4]'
    )
    CARDIOVASCULAR_SEARCH_INPUT_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-block-remote-header-input//input)[5]'
    )
    RESPIRATORY_SEARCH_INPUT_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-block-remote-header-input//input)[6]'
    )
    GASTROINTESTINAL_SEARCH_INPUT_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-block-remote-header-input//input)[7]'
    )
    GENITOURINARY_SEARCH_INPUT_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-block-remote-header-input//input)[8]'
    )
    MUSCULOSKELETAL_SEARCH_INPUT_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-block-remote-header-input//input)[9]'
    )
    NEUROLOGICAL_SEARCH_INPUT_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-block-remote-header-input//input)[10]'
    )
    PSYCHIATRIC_SEARCH_INPUT_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-block-remote-header-input//input)[11]'
    )
    ENDOCRINE_SEARCH_INPUT_LOCATOR = (
        By.XPATH, '(//app-nb-ros//app-nb-block-remote-header-input//input)[12]'
    )

    NBSELECT_FIELD_LOCATOR = (By.CSS_SELECTOR, 'app-nb-ros app-nb-preset .nbselect__field')
    PRESET_TRASH_ICON_LOCATOR = (By.CSS_SELECTOR, 'app-nb-ros app-nb-preset .nbselect__action .nbicon__trash')
    PRESET_ALL_TRASH_ICON_LOCATOR = (By.CSS_SELECTOR, 'app-nb-ros app-nb-preset .nbselect__field .nbicon__trash')

    PRESET_SELECTION_INPUT_LOCATOR = (By.CSS_SELECTOR, 'app-nb-ros app-nb-preset .nbselect__field input')
    PRESET_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, 'app-nb-ros app-nb-preset ul.nbselect__list')
    ALL_PRESET_LOCATOR = (By.XPATH, '//app-nb-ros//app-nb-preset//li/span/parent::li')
    ALL_PRESET_NAME_LOCATOR = (By.XPATH, '//app-nb-ros//app-nb-preset//li//span[1]')
    SELECTED_PRESET_NAME_LOCATOR = (
        By.CSS_SELECTOR, 'app-nb-ros app-nb-preset li[class*="selected"] span:nth-child(1)'
    )
    SAVE_PRESET_LOCATOR = (By.XPATH, '//app-nb-ros//app-nb-preset//li[text()="Save"]')
    SAVE_AS_NEW_PRESET_LOCATOR = (By.XPATH, '//app-nb-ros//app-nb-preset//li[text()="Save as new"]')

    SAVE_PRESET_INPUT_LOCATOR = (By.CSS_SELECTOR, 'app-nb-ros app-nb-preset-save-modal #save-preset-modal-input')
    SAVE_PRESET_YES_BUTTON = (By.XPATH, '//app-nb-ros//app-nb-preset-save-modal//button[text()="Yes"]')
    MODAL_YES_BUTTON = (By.XPATH, '//app-nb-ros//app-nb-modal//button[text()="Yes"]')

    PRESET_INPUT_PLACEHOLDER = 'Select Preset'
    CREATE_EMPTY_PRESET_WARNING = 'Preset cannot be saved for empty selections'
    UPDATE_EMPTY_PRESET_WARNING = 'Preset could not be updated'
    ANOTHER_PRESET_WARNING = 'Another Preset cannot be applied!'


    def get_statement_input_value(self):
        return self.get_attribute(self.STATEMENT_TEXT_INPUT_LOCATOR, 'value')

    def get_ros_section_canvas_text(self):
        return self.get_text_by_locator(self.ROS_CANVAS_SENTENCE_LOCATOR)

    def get_ros_blocks_header_text(self):
        return self.get_list_of_text_from_locator(self.ROS_BLOCKS_HEADER_LOCATOR)


    def get_ros_block_descriptors(self, block_index=1):
        descriptors_locator = (By.XPATH, f'(//app-nb-ros//app-nb-pos-neg)[{block_index}]//li/span')
        return self.get_list_of_text_from_locator(descriptors_locator)

    def get_ros_block_active_descriptors(self, block_index=1, custom_symptoms=False):
        if custom_symptoms:
            descriptors_locator = (
                By.XPATH, '//app-nb-ros//app-nb-tag-list//li[contains(@class, "active")]/span'
            )
        else:
            descriptors_locator = (
                (By.XPATH, f'(//app-nb-ros//app-nb-pos-neg)[{block_index}]//li[contains(@class, "active")]/span')
            )
        return self.get_list_of_text_from_locator(descriptors_locator)

    def get_ros_block_deselected_descriptors(self, block_index=1):
        descriptors_locator = (
            (By.XPATH, f'(//app-nb-ros//app-nb-pos-neg)[{block_index}]//li[not(contains(@class, "active"))]/span')
        )
        return self.get_list_of_text_from_locator(descriptors_locator)

    def get_descriptor_selection_status(self, block_index, descriptor_name, positive_selection=False,
                                        negative_selection=False, deselection=False):
        status = False
        descriptor_class_value = self.get_attribute(
            (By.XPATH, f'(//app-nb-ros//app-nb-pos-neg)[{block_index}]'
                       f'//li/span[text()="{descriptor_name}"]/parent::li'), 'class'
        )

        if positive_selection:
            status = 'active' in descriptor_class_value and 'striked' not in descriptor_class_value
        elif negative_selection:
            status = 'active' in descriptor_class_value and 'striked' in descriptor_class_value
        elif deselection:
            status = 'active' not in descriptor_class_value and 'striked' not in descriptor_class_value

        return status

    def select_descriptor(self, block_index, descriptor_name, positive_selection=False, negative_selection=False):
        descriptor_locator = (By.XPATH, f'(//app-nb-ros//app-nb-pos-neg)[{block_index}]'
                                        f'//li/span[text()="{descriptor_name}"]/parent::li')

        if positive_selection:
            if self.get_descriptor_selection_status(block_index, descriptor_name, positive_selection=True):
                print(f'"{descriptor_name}" is already positively selected')

            elif self.get_descriptor_selection_status(block_index, descriptor_name, negative_selection=True):
                self.click_and_wait(descriptor_locator, 1)
                self.wait_until_attribute_contains(descriptor_locator, 'class', 'active')
                print(f'"{descriptor_name}" is positively selected')

            elif self.get_descriptor_selection_status(block_index, descriptor_name, deselection=True):
                self.click_and_wait(descriptor_locator, 1)
                self.click_and_wait(descriptor_locator, 1)
                self.wait_until_attribute_contains(descriptor_locator, 'class', 'active')
                print(f'"{descriptor_name}" is positively selected')

        elif negative_selection:
            if self.get_descriptor_selection_status(block_index, descriptor_name, negative_selection=True):
                print(f'"{descriptor_name}" is already negatively selected')

            elif self.get_descriptor_selection_status(block_index, descriptor_name, positive_selection=True):
                self.click_and_wait(descriptor_locator, 1)
                self.click_and_wait(descriptor_locator, 1)
                self.wait_until_attribute_contains(descriptor_locator, 'class', 'active')
                print(f'"{descriptor_name}" is negatively selected')

            elif self.get_descriptor_selection_status(block_index, descriptor_name, deselection=True):
                self.click_and_wait(descriptor_locator, 1)
                self.wait_until_attribute_contains(descriptor_locator, 'class', 'active')
                print(f'"{descriptor_name}" is negatively selected')

    def remove_all_values_of_selected_preset(self):
        # Remove statement input text value
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_element(self.STATEMENT_TEXT_INPUT_LOCATOR)).click()
        actions.key_down(Keys.LEFT_CONTROL).key_down(Keys.END)
        actions.key_up(Keys.LEFT_CONTROL).key_up(Keys.END).perform()

        for _ in range(len(self.get_statement_input_value())):
            actions.send_keys(Keys.BACKSPACE).perform()

        # Deselect all blocks descriptors
        for block_index in range(1, 13):
            for descriptor in self.get_ros_block_active_descriptors(block_index):
                descriptor_locator = (By.XPATH, f'(//app-nb-ros//app-nb-pos-neg)[{block_index}]'
                                                f'//li/span[text()="{descriptor}"]/parent::li')

                if self.get_descriptor_selection_status(block_index, descriptor, positive_selection=True):
                    self.click_and_wait(descriptor_locator, 1)
                    self.wait_until_attribute_not_contains(descriptor_locator, 'class', 'active')

                elif self.get_descriptor_selection_status(block_index, descriptor, negative_selection=True):
                    self.click_and_wait(descriptor_locator, 1)
                    self.click_and_wait(descriptor_locator, 1)
                    self.wait_until_attribute_not_contains(descriptor_locator, 'class', 'active')

    def select_random_descriptors_from_each_block(self):
        selected_descriptors_info = []
        with open(AppConstant.ROS_DATA_FILE, encoding='utf-8') as json_file:
            ros_data = json.loads(json_file.read())

        for block_index, block_header_text in enumerate(ros_data['ros_blocks_header_text'][1:-1], start=1):
            # Select positive descriptors
            positive_descriptors = generate_sublist_with_same_order(
                self.get_ros_block_deselected_descriptors(block_index), 2
            )
            for descriptor in positive_descriptors:
                self.select_descriptor(block_index, descriptor, positive_selection=True)

            # Select negative descriptors
            negative_descriptors = generate_sublist_with_same_order(
                self.get_ros_block_deselected_descriptors(block_index), 2
            )
            for descriptor in negative_descriptors:
                self.select_descriptor(block_index, descriptor, negative_selection=True)

            # Generate canvas sentence
            canvas_sentence = self.get_generated_ros_canvas_sentence(
                block_header_text, positive_descriptors, negative_descriptors
            )
            selected_descriptors_info.append([
                positive_descriptors, negative_descriptors, canvas_sentence
            ])

        selected_descriptors_info.append(self.get_ros_section_canvas_text())
        print('Selected descriptors info:', selected_descriptors_info)
        return selected_descriptors_info

    @staticmethod
    def generate_random_descriptors_from_each_block():
        # Load ROS data from JSON file
        with open(AppConstant.ROS_DATA_FILE, encoding='utf-8') as json_file:
            ros_data = json.loads(json_file.read())

        # Extract headers of ROS blocks (excluding the first and last block, which have no descriptors)
        block_headers = ros_data['ros_blocks_header_text'][1:-1]

        random_descriptors_list = []
        for block_header_text in block_headers:
            block_descriptors = ros_data[f'{block_header_text.lower()}_block']['descriptors']
            random_sublist = generate_sublist_with_same_order(block_descriptors, random.randint(1, 2))
            random_descriptors_list.append(random_sublist)

        print('Random descriptors from each ROS block:', random_descriptors_list)
        return random_descriptors_list

    def expand_preset_dropdown(self):
        if 'open' in self.get_attribute(self.NBSELECT_FIELD_LOCATOR, 'class'):
            print('Preset dropdown already expanded')
        else:
            self.click_and_wait(self.PRESET_SELECTION_INPUT_LOCATOR, 1)
            self.wait_for_visibility_of(self.PRESET_DROPDOWN_LOCATOR)
            print('Preset dropdown expanded')

    def save_as_new_preset(self, wait_for_loader=True):
        time.sleep(10)  # Wait for Note Builder auto save
        self.expand_preset_dropdown()
        self.click_and_wait(self.SAVE_AS_NEW_PRESET_LOCATOR, 1)
        self.wait_for_visibility_of(self.SAVE_PRESET_INPUT_LOCATOR)

        preset_name = str(uuid.uuid4())
        self.enter_text_at(preset_name, self.SAVE_PRESET_INPUT_LOCATOR)
        self.click_and_wait(self.SAVE_PRESET_YES_BUTTON, 1)
        self.wait_for_invisibility_of(self.SAVE_PRESET_YES_BUTTON)
        if wait_for_loader:
            HomePage(self.driver).wait_for_loader()
        return preset_name

    def save_preset(self, wait_for_loader=True):
        time.sleep(10)  # Wait for Note Builder auto save
        self.expand_preset_dropdown()
        self.click_and_wait(self.SAVE_PRESET_LOCATOR, 1)
        if wait_for_loader:
            HomePage(self.driver).wait_for_loader()

    def get_preset_info_after_creating_new_preset(self):
        preset_info = self.select_random_descriptors_from_each_block()
        preset_name = self.save_as_new_preset()
        return [preset_name, preset_info]

    def get_preset_info_after_updating_preset(self):
        statement_text = generate_random_alphanumeric_string(50)
        self.enter_text_at(statement_text, self.STATEMENT_TEXT_INPUT_LOCATOR)

        block1_descriptor = random.choice(self.get_ros_block_deselected_descriptors(1))
        self.select_descriptor(1, block1_descriptor, positive_selection=True)

        block2_descriptor = random.choice(self.get_ros_block_deselected_descriptors(2))
        self.select_descriptor(2, block2_descriptor, negative_selection=True)

        self.save_preset()

        ros_canvas_text = self.get_ros_section_canvas_text()
        return [statement_text, block1_descriptor, block2_descriptor, ros_canvas_text]

    def preset_selection_input_placeholder(self):
        return self.get_attribute(self.PRESET_SELECTION_INPUT_LOCATOR, 'placeholder')

    def get_all_preset_name(self):
        return self.get_list_of_text_from_locator(self.ALL_PRESET_NAME_LOCATOR)

    def get_selected_preset_name(self):
        return self.get_text_by_locator(self.SELECTED_PRESET_NAME_LOCATOR)

    def get_random_deselected_preset_index(self):
        all_preset_class = self.get_list_of_attributes_from_locator(self.ALL_PRESET_LOCATOR, 'class')
        filtered_indices = [index for index, item in enumerate(all_preset_class) if 'selected' not in item]
        return random.choice(filtered_indices)

    def clear_preset(self):
        self.click_and_wait_for_target(self.PRESET_TRASH_ICON_LOCATOR, self.MODAL_YES_BUTTON)
        self.click_and_wait_for_invisibility(self.MODAL_YES_BUTTON)
        HomePage(self.driver).wait_for_loader()

    def select_preset(self, preset_name=None, preset_index=0, by_name=False, by_index=False, wait_for_loader=True):
        self.expand_preset_dropdown()
        if by_name:
            all_preset_name = self.get_all_preset_name()
            if preset_name in all_preset_name:
                target_preset_index = all_preset_name.index(preset_name)
                preset_element = self.get_elements(self.ALL_PRESET_LOCATOR)[target_preset_index]
                if 'selected' in self.get_attribute_from_element(preset_element, 'class'):
                    print(f'"{preset_name}" preset already selected')
                else:
                    self.click_and_wait_by_element(preset_element, 2)
                    if wait_for_loader:
                        HomePage(self.driver).wait_for_loader()
                    print(f'"{preset_name}" preset selected')
            else:
                print(f'"{preset_name}" not found in preset dropdown')

        elif by_index:
            preset_element = self.get_elements(self.ALL_PRESET_LOCATOR)[preset_index]
            if 'selected' in self.get_attribute_from_element(preset_element, 'class'):
                print(f'Preset-{preset_index} already selected')
            else:
                self.click_and_wait_by_element(preset_element, 2)
                if wait_for_loader:
                    HomePage(self.driver).wait_for_loader()
                print(f'Preset-{preset_index} selected')

    def delete_preset(self, preset_name):
        self.expand_preset_dropdown()
        all_preset_name = self.get_all_preset_name()
        if preset_name in all_preset_name:
            preset_index = all_preset_name.index(preset_name)
            preset_element = self.get_elements(self.ALL_PRESET_LOCATOR)[preset_index]
            preset_trash_element = self.get_elements(self.PRESET_ALL_TRASH_ICON_LOCATOR)[preset_index]
            self.hover_element(preset_element)
            self.hover_and_click_by_element(preset_trash_element)
            self.wait_for_element_to_clickable(self.MODAL_YES_BUTTON)
            self.click_and_wait_for_invisibility(self.MODAL_YES_BUTTON)
            HomePage(self.driver).wait_for_loader()
            print(f'"{preset_name}" preset deleted')
        else:
            print(f'"{preset_name}" not found in preset dropdown')

    def get_block_index_after_descriptor_selection(self):
        block_index = random.randint(1, 12)
        descriptors_locator = (By.XPATH, f'(//app-nb-ros//app-nb-pos-neg)[{block_index}]//li')
        descriptor_element = random.choice(self.get_elements(descriptors_locator))
        self.click_and_wait_by_element(descriptor_element, 1)
        return block_index

    def is_block_disabled(self, block_index=0):
        block_element = self.get_elements(self.ROS_BLOCK_ITEM_LAST)[block_index]
        return 'disabled' in self.get_attribute_from_element(block_element, 'class')

    def retry_click_on_disabled_block(self, block_index):
        for _ in range(3):
            try:
                block_element = self.get_elements(self.ROS_BLOCK_ITEM)[block_index]
                self.click_and_wait_by_element(block_element, 1)
                if self.is_element_visible(self.MODAL_YES_BUTTON, 5):
                    break
            except StaleElementReferenceException:
                print(f'"StaleElementReferenceException" for block-{block_index} element, try again!')

    def re_enable_block(self, block_index=0):
        if self.is_block_disabled(block_index):
            self.retry_click_on_disabled_block(block_index)
            self.wait_for_element_to_clickable(self.MODAL_YES_BUTTON)
            self.click_and_wait_for_invisibility(self.MODAL_YES_BUTTON)
            print(f'Block-{block_index} Re-enabled')
        else:
            print(f'Block-{block_index} is already enabled')


    def search_and_select(self, search_input_locator, search_text, custom_search=False):
        home_page = HomePage(self.driver)
        self.enter_text_at(search_text, search_input_locator)
        home_page.wait_for_loader()

        if custom_search:
            dropdown_item_locator = (
                By.XPATH,
                f'//app-nb-ros//app-nb-block-remote-header-input//li/b[text()=\'"{search_text}"\']'
            )
        else:
            dropdown_item_locator = (
                By.XPATH,
                f'//app-nb-ros//app-nb-block-remote-header-input//li/div[text()="{search_text}"]'
            )

        try:
            self.click_and_wait(dropdown_item_locator, 1, 5)
        except TimeoutException as exc:
            raise TimeoutException(f'"{search_text}" is not found in search result dropdown') from exc


    def get_suggested_active_descriptors(self, block_index=1, custom_symptoms=False):
        if custom_symptoms:
            suggested_descriptors_locator = (
                By.XPATH,
                '//app-nb-ros//app-nb-tag-list'
                '//li[contains(@class, "suggested") and contains(@class, "active")]/span'
            )
        else:
            suggested_descriptors_locator = (
                By.XPATH,
                f'(//app-nb-ros//app-nb-pos-neg)[{block_index}]'
                f'//li[contains(@class, "suggested") and contains(@class, "active")]/span'
            )
        suggested_descriptors = self.get_list_of_text_from_locator(suggested_descriptors_locator)
        return suggested_descriptors


    def get_generated_ros_canvas_sentence(self, block_name, positive_descriptors=None, negative_descriptors=None):
        if negative_descriptors is not None and positive_descriptors is None:
            generated_sentence = (
                f'{block_name}: Denies {self.join_descriptors_in_canvas_sentence(negative_descriptors, "or")}.'
            )
        elif positive_descriptors is not None and negative_descriptors is None:
            generated_sentence = (
                f'{block_name}: Positive for {self.join_descriptors_in_canvas_sentence(positive_descriptors, "and")}.'
            )
        else:
            generated_sentence = (
                f'{block_name}: Positive for {self.join_descriptors_in_canvas_sentence(positive_descriptors, "and")}. '
                f'Denies {self.join_descriptors_in_canvas_sentence(negative_descriptors, "or")}.'
            )

        return generated_sentence


    @staticmethod
    def join_descriptors_in_canvas_sentence(descriptors, conjunction):
        sentence = None
        descriptors_count = len(descriptors)

        if descriptors_count == 1:
            sentence = descriptors[0]
        elif descriptors_count == 2:
            sentence = f'{descriptors[0]} {conjunction} {descriptors[1]}'
        elif descriptors_count > 2:
            sentence = f'{", ".join(descriptors[:-1])}, {conjunction} {descriptors[-1]}'

        return sentence
