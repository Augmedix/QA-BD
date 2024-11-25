"""
Contains locators & methods for NOTEWRITER page.
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pages
from pages.base_page import BasePage
import pages.scp_pages
from pages.scp_pages.home_page import HomePage
import pages.scp_pages.home_page
import pages.scp_pages.login_page
# from pages.text_expanders.macro_usage_page import MacroUsagePage


class NotewriterPage(BasePage):
    """
    Contains locators & methods for Review tab/NOTEWRITER'S.
    """
    NOTEWRITER_SECONDARY_HEADER = (By.CSS_SELECTOR, '.notewriter__secondary__header ')
    NOTEWRITER_SECONDARY_SUBHEADER = (By.CSS_SELECTOR, '.notewriter__secondary__subheader ')

    START_TIME_LOCATOR = (By.ID, 'ajs-notewriter-field-start-time')
    NOTE_NAME_FIELD_LOCATOR = (By.CSS_SELECTOR, 'input[placeholder="Name"]')
    NOTE_HEADER_LIST_LOCATOR = (By.CSS_SELECTOR, 'ul[class="tab__header__list"]'
                                                 ' li:not([class^="tab__header__list__button"])')
    NOTEWRITER_EDITOR_LOCATOR = (By.ID, 'richtexteditor')
    NOTEWRITER_ACTION_ICON_LOCATOR = (By.ID, 'notewriterAction')
    PUSH_CURRENT_NOTE_TO_ACTIVE_TRAINEES_LOCATOR = (By.ID, 'ajs-notewriter-action-push-note-cta')
    DELETE_ALL_PATIENT_LOCATOR = (By.ID, 'ajs-notewriter-action-delete-all-patients')

    DELETE_ALL_PATIENT_CHECKBOX_LOCATOR = (By.ID, 'ajs-notewriter-delete-all-note-confirm-checkbox')
    CONFIRM_DELETE_BTN_LOCATOR = (By.ID, 'ajs-notewriter-delete-all-note-confirm-yes')
    CANCEL_DELETE_BTN_LOCATOR = (By.ID, 'ajs-notewriter-delete-all-note-confirm-cancel')

    PUSH_NOTE_CONFIRMATION_WINDOW_LOCATOR = (By.CSS_SELECTOR, 'app-push-note kendo-window')
    PUSH_NOTE_CONFIRMATION_WINDOW_HEADER_LOCATOR = (By.CSS_SELECTOR, 'kendo-window-titlebar div')
    PUSH_NOTE_CONFIRMATION_WINDOW_BODY_LOCATOR = (By.CSS_SELECTOR, 'kendo-window-titlebar ~ div p')
    PUSH_NOTE_CONFIRMATION_WINDOW_CLOSE_ICON_LOCATOR = (By.CSS_SELECTOR, '#ajs-push-note-close span')
    PUSH_NOTE_YES_BTN_LOCATOR = (By.ID, 'ajs-push-note-yes')
    PUSH_NOTE_NO_BTN_LOCATOR = (By.ID, 'ajs-push-note-cancel')

    MISSPELLED_WORD_LIST_LOCATOR = (By.CLASS_NAME, 'nanospell-typo')
    CONTEXT_MENU_FRAME_LOCATOR = (By.CLASS_NAME, 'cke_panel_frame')
    ADD_TO_PERSONAL_DICTIONARY_LOCATOR = (By.CSS_SELECTOR, '[title="Context Menu Options"] '
                                                           '[title="Add To Personal Dictionary"]')

    #   Locators related to Templates
    TEMPLATE_MENU_LOCATOR = (By.ID, 'ajs-notewriter-template-dropdown')
    TEMPLATE_DROPDOWN_BODY = (By.ID, 'ajs-notewriter-template-dropdown-body')
    TEMPLATES_LIST_LOCATOR = (By.CSS_SELECTOR, '#ajs-notewriter-template-dropdown-body a')
    MOVE_NOTES_AND_USE_TEMPLATE_BTN_LOCATOR = (By.XPATH, '//button[contains(text(), "Move notes and use template")]')
    CANCEL_TEMPLATE_REPLACEMENT_BTN_LOCATOR = (By.XPATH, '//button[contains(text(), "Cancel")]')

    PATIENT_LIST_LOCATOR = (By.CSS_SELECTOR, '#ajs-notewriter-note-list li[id^="ajs-notewriter-note-id-"]')
    PATIENT_NAME_LOCATOR = (By.CLASS_NAME, 'notewriter__primary__list__item__text')

    TOOLBAR_ITEMS_LOCATOR = (By.CSS_SELECTOR, '#richtexteditor-toolbar a[title]')
    COMPLETE_BTN_LOCATOR = (By.XPATH, '//button[normalize-space(text())="Complete"]')
    # UPLOAD_BTN_LOCATOR = (By.XPATH, '//section[@class="notewriter__secondary__header"]//button[text()="Upload"]')
    UPLOAD_BTN_LOCATOR = (By.XPATH,'//button[normalize-space(text())="Upload"]')
    UPLOADED_BTN_LOCATOR = (By.XPATH,'//button[normalize-space(text())="Uploaded"]')
    COMPLETE_CONFIRMATION_MODAL_LOCATOR = (By.XPATH,'//div[contains(text(),"Complete Note")]')
    UPLOAD_CONFIRMATION_MODAL_LOCATOR = (By.XPATH,'//span[contains(text(),"Upload Note")]')
    COMPLETE_CONFIRM_BTN_LOCATOR = (By.XPATH,'//button[normalize-space(text())="Done"]')
    UPLOAD_CONFIRM_BTN_LOCATOR = (By.XPATH,'//button[@data-dialog-action-text="Upload"]')
    COMPLETE_BTN_SUCCESS_LOCATOR = (By.XPATH, '//button[@class="btn btn-sm btn-success" and text()="Complete"]')
    UPLOAD_BTN_SUCCESS_LOCATOR = (By.XPATH, '//button[@class="btn btn-sm btn-success" and text()="Upload"]')

    MISSPELLED_WORK_MARKER_LOCATOR = (By.CSS_SELECTOR, 'span[data-cke-bogus]')

    TOOLBAR_ITEMS_TITLE_LIST = [
                'Undo (Ctrl+Z)', 'Redo (Ctrl+Y)', 'Bold (Ctrl+B)', 'Italic (Ctrl+I)',
                'Underline (Ctrl+U)', 'Insert/Remove Numbered List (Ctrl+2)',
                'Insert/Remove Bulleted List (Ctrl+1)', 'Remove Format (Ctrl+¿)',
            ]

    NOTEWRITER_START_TIME = (By.ID, 'ajs-notewriter-field-start-time')
    NOTEWRITER_NAME_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Name"]')
    NOTEWRITER_NOTE_ID_BTN = (By.CSS_SELECTOR, 'input[title="Note ID"]')

    MACRO_WINDOW = (By.CSS_SELECTOR, 'app-macro div[role="dialog"]')
    MACRO_CROSS_ICON = (By.CSS_SELECTOR, 'app-macro button[aria-label="Close"]')

    BOLD_BUTTON = (By.XPATH, '(//span[@class="cke_toolgroup"]//a)[3]')
    ITALIC_BUTTON = (By.XPATH, '(//span[@class="cke_toolgroup"]//a)[4]')
    UNDERLINE_BUTTON = (By.XPATH, '(//span[@class="cke_toolgroup"]//a)[5]')
    NUMBERED_LIST_BUTTON = (By.XPATH, '(//span[@class="cke_toolgroup"]//a)[6]')
    BULLETED_LIST_BUTTON = (By.XPATH, '(//span[@class="cke_toolgroup"]//a)[7]')

    BOLD_ALL_TEXT = (By.XPATH, '//div[@id="richtexteditor"]/strong')
    UNDERLINE_ALL_TEXT = (By.XPATH, '//div[@id="richtexteditor"]/u')
    ITALIC_ALL_TEXT = (By.XPATH, '//div[@id="richtexteditor"]/em')
    BULLETED_LIST_ALL_TEXT = (By.XPATH, '//div[@id="richtexteditor"]/ul')
    NUMBERED_LIST_ALL_TEXT = (By.XPATH, '//div[@id="richtexteditor"]/ol')
    RE_EVALUATION_HEADER_LOCATOR = (By.XPATH,'//div[contains(text(),"Re-evaluation")]')
    FIRST_RE_EVAL_TEXT_LOCATOR = (By.XPATH,'//app-canvas-progress/div/div[2]/div[1]//div[1]/app-canvas-sentence/div')
    SECOND_RE_EVAL_TEXT_LOCATOR = (By.XPATH,'//app-canvas-progress/div/div[2]/div[1]/div[2]/app-canvas-sentence/div')
    THIRD_RE_EVAL_TEXT_LOCATOR = (By.XPATH,'//app-canvas-progress/div/div[2]/div[1]/div[3]/app-canvas-sentence/div')

    ALERT_MSG_LOCATOR = (By.CSS_SELECTOR, '#ajs-provider-toast-0 span')

    PUSH_NOTE_CONFIRMATION_WINDOW_HEADER_TXT = 'Push note'
    PUSH_NOTE_CONFIRMATION_WINDOW_BODY_TXT = 'Are you sure this note is finalized and ready to be sent to all trainees?'

    PUSH_NOTE_CONFIRMATION_WINDOW_NO_BTN_COLOR = '#f8f9fa'
    PUSH_NOTE_CONFIRMATION_WINDOW_YES_BTN_COLOR = '#dc3545'

    NOTIFICATION_MSG_FOR_ALL_PATIENT_DELETION = 'All patients deleted successfully'

    def goto_start(self):
        """
        Press the HOME key.
        """
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).key_down(Keys.HOME).key_up(
            Keys.CONTROL).key_up(Keys.HOME).perform()

    def goto_end(self):
        """
        Press the END key.
        """
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL).key_down(Keys.END).key_up(
            Keys.CONTROL).key_up(Keys.END).perform()

    def goto_next_character(self):
        """
        Press the RIGHT ARROW key.
        """
        actions = ActionChains(self.driver)
        actions.key_down(Keys.ARROW_RIGHT).key_up(Keys.ARROW_RIGHT).perform()

    def goto_previous_character(self):
        """
        Press the LEFT ARROW key.
        """
        actions = ActionChains(self.driver)
        actions.key_down(Keys.ARROW_LEFT).key_up(Keys.ARROW_LEFT).perform()

    def select_text_from_start_to_end_of_line(self):
        """
        Press the SHIFT + HOME key.
        """
        actions = ActionChains(self.driver)
        actions.key_down(Keys.LEFT_SHIFT).key_down(Keys.END).\
            key_up(Keys.LEFT_SHIFT).key_up(Keys.END).perform()

    def select_text_from_end_to_start_of_line(self):
        """
        Press the SHIFT + HOME ARROW key.
        """
        actions = ActionChains(self.driver)
        actions.key_down(Keys.LEFT_SHIFT).key_down(Keys.HOME).\
            key_up(Keys.LEFT_SHIFT).key_up(Keys.HOME).perform()

    def open_macro_window(self):
        """
        Opens the macro usage window.
        """
        self.get_element(self.NOTEWRITER_EDITOR_LOCATOR).send_keys(' .')

    def use_macro(self, macro_name=None):
        """
        Enters macro content by opening macro window.
        :param macro_name:
        :return:
        """
        # macro_usage_page = MacroUsagePage(self.driver)
        self.open_macro_window()
        # macro_usage_page.select_macro(macro_name)
        print(f'Macro "{macro_name}" is selected...')

    def use_autocorrection(self, target_locator=NOTEWRITER_EDITOR_LOCATOR, autocorrection_name=None):
        """
        Enters autocorrection content by shortcut.
        :param autocorrection_name - the autocorrection to use in notewriter/notebuilder
        :param target_locator - locator to find the target web element
        """
        self.enter_text_at(f'{autocorrection_name} ', target_locator, False, 1)
        print(f'Autocorrection "{autocorrection_name}" is selected...')

    def get_notewriter_text(self):
        return self.get_text_by_locator(self.NOTEWRITER_EDITOR_LOCATOR)

    def get_notewriter_start_time(self):
        return self.get_attribute(self.NOTEWRITER_START_TIME, 'value')

    def get_notewriter_patient_name(self):
        return self.get_attribute(self.NOTEWRITER_NAME_INPUT, 'value')

    def get_notewriter_note_id(self):
        return self.get_attribute(self.NOTEWRITER_NOTE_ID_BTN, 'value')

    def select_tempate(self, template_name):
        """
        Selects templates from notewriter page.
        :param template_name: name of the template to select.
        """
        self.click_and_wait(self.TEMPLATE_MENU_LOCATOR)
        template_list = self.get_elements(self.TEMPLATES_LIST_LOCATOR)
        for template in template_list:
            if template.text.strip() == template_name:
                template.click()
                self.wait_for_visibility_of(self.MOVE_NOTES_AND_USE_TEMPLATE_BTN_LOCATOR)
                self.click_and_wait(self.MOVE_NOTES_AND_USE_TEMPLATE_BTN_LOCATOR)
                print(f'Tempalte "{template_name}" has been selected...')
                break
        else:
            print(f'No such template called "{template_name}"...')

    def is_template_dropdown_open(self):
        return self.is_element_visible(self.TEMPLATE_DROPDOWN_BODY, 5)

    def open_notewriter_action_menu(self):
        self.click_and_wait_for_target(self.NOTEWRITER_ACTION_ICON_LOCATOR,
                                       self.PUSH_CURRENT_NOTE_TO_ACTIVE_TRAINEES_LOCATOR)

    def push_note_to_active_trainees(self):
        """
        Push notes to active trainees.
        """
        self.open_notewriter_action_menu()
        self.click_and_wait_for_target(self.PUSH_CURRENT_NOTE_TO_ACTIVE_TRAINEES_LOCATOR,
                                       self.PUSH_NOTE_YES_BTN_LOCATOR)
        self.click_and_wait(self.PUSH_NOTE_YES_BTN_LOCATOR, 2)
        self.wait_for_element_count_to_be(self.PUSH_NOTE_YES_BTN_LOCATOR, 0)
        print('Push current note completed...')

    def delete_all_notes(self):
        """
        Deletes all notes from notewriter.
        """
        home_page = pages.scp_pages.home_page.HomePage(self.driver)
        home_page.wait_for_loader()
        self.click_and_wait_for_target(self.NOTEWRITER_ACTION_ICON_LOCATOR, self.DELETE_ALL_PATIENT_LOCATOR)
        self.click_and_wait_for_target(self.DELETE_ALL_PATIENT_LOCATOR, self.CONFIRM_DELETE_BTN_LOCATOR)
        self.click_and_wait(self.DELETE_ALL_PATIENT_CHECKBOX_LOCATOR)
        self.click_and_wait(self.CONFIRM_DELETE_BTN_LOCATOR)
        self.wait_for_element_count_to_be(self.PATIENT_LIST_LOCATOR, 0)
        print('All notes deleted...')

    def close_delete_all_notes_window(self):
        self.click_and_wait(self.CANCEL_DELETE_BTN_LOCATOR)
        self.wait_for_invisibility_of(self.CANCEL_DELETE_BTN_LOCATOR)

    def is_delete_all_notes_window_open(self):
        return self.get_total_count(self.CANCEL_DELETE_BTN_LOCATOR) == 1

    def add_to_personal_dictionary(self, word_to_add):
        """
        Used to add unknown word to personal dictionary.

        :param word_to_add: word to add in the personal dictionary.
        :return: None
        """
        misspelled_words = self.get_elements(self.MISSPELLED_WORD_LIST_LOCATOR)
        for misspelled_word in misspelled_words:
            if misspelled_word.text.strip() == word_to_add:
                self.perform_right_click_on(misspelled_word)
                self.change_frame(self.CONTEXT_MENU_FRAME_LOCATOR)
                self.click_and_wait(self.ADD_TO_PERSONAL_DICTIONARY_LOCATOR, 1)
                self.driver.switch_to.default_content()
                print(f'Word {word_to_add} is added to personal dictionary...')
                break
        else:
            print(f'No such word {word_to_add} to add to dictionary...')

    def complete_note(self, note_id):
        # complete_status_icon_locator = (By.XPATH, f'//*[contains(text(), "{note_name}")]/ancestor::li/descendant::'
        #                                           f'div[@class="notewriter__primary__list__item__secondary__block"]'
        #                                           f'//*[@data-tooltip-right="Complete"]')
        self.home_page = pages.scp_pages.home_page.HomePage(self.driver)
        self.home_page.continue_working()
        self.home_page.refresh_visit_list()
        self.home_page.select_note_by_id(note_id)
        try:
            self.click_and_wait_for_target(self.COMPLETE_BTN_LOCATOR, self.COMPLETE_CONFIRMATION_MODAL_LOCATOR)
        except:
            self.home_page.refresh_visit_list()
            self.home_page.select_note_by_id(note_id)
            self.click_and_wait_for_target(self.COMPLETE_BTN_LOCATOR, self.COMPLETE_CONFIRMATION_MODAL_LOCATOR)
        self.click_and_wait(self.COMPLETE_CONFIRM_BTN_LOCATOR,3)
        self.home_page.wait_for_loader()
        print(f'Note status for {note_id} is changed to Complete...')

    def upload_note(self, note_id):
        # uploaded_status_icon_locator = (By.XPATH, f'//*[contains(text(), "{note_name}")]/ancestor::li/descendant::'
        #                                           f'div[@class="notewriter__primary__list__item__secondary__block"]'
        #                                           f'//*[@data-tooltip-right="Uploaded"]')
        self.home_page = pages.scp_pages.home_page.HomePage(self.driver)
        # self.home_page.continue_working()
        # self.home_page.refresh_visit_list()
        self.complete_note(note_id)
        # self.home_page.disconnect_from_provider()
        # self.home_page.connect_to_provider(provider_email)     
        # self.home_page.refresh_visit_list()
        # self.home_page.select_note_by_id(note_id)
        try:
            self.wait_for_visibility_of(self.UPLOAD_BTN_LOCATOR)
            self.click_and_wait_for_target(self.UPLOAD_BTN_LOCATOR, self.UPLOAD_CONFIRMATION_MODAL_LOCATOR)
        except:
            self.home_page.refresh_visit_list()
            self.home_page.select_note_by_id(note_id)
            self.click_and_wait_for_target(self.UPLOAD_BTN_LOCATOR, self.UPLOAD_CONFIRMATION_MODAL_LOCATOR)
        self.click_and_wait(self.UPLOAD_CONFIRM_BTN_LOCATOR,3)
        self.home_page.wait_for_loader()
        print(f'Note status for {note_id} is changed to Uploaded...')

    def get_note_status(self, note_name):
        xpath_string = (f'//*[contains(text(), "{note_name}")]/parent::*/parent::*/following-sibling::div'
                        f'//app-nw-visit-list-action-dropdown//span[@data-tooltip-right]')
        return self.get_attribute((By.XPATH, xpath_string), 'data-tooltip-right')
    def get_note_status_dropdown_text(self, note_id, max_wait=30):
        self.home_page = HomePage(self.driver)
        self.home_page.refresh_visit_list()
        note_status_button_xpath_string = (f"//li[@data-note-id='{note_id}']//app-visit-list-item-action-dropdown/div/span/span")
        note_status_xpath_string = (f"//li[@data-note-id='{note_id}']//li[@class='mini__dropdown__list__item mini__dropdown__delete__item ng-star-inserted']")
        self.click_and_wait((By.XPATH, note_status_button_xpath_string),1)
        return self.get_text_by_locator((By.XPATH, note_status_xpath_string),max_wait)
    # //li[@data-note-id='5e324bb9-916c-4bce-a42b-6501eb41b3eb']//li[@class='mini__dropdown__list__item mini__dropdown__delete__item ng-star-inserted']
    
    # //*[@id="ajs-notewriter-note-name-5e324bb9-916c-4bce-a42b-6501eb41b3eb"]/text()

    def get_note_creation_time(self, note_name):
        xpath_string = f'//*[contains(text(), "{note_name}")]/parent::*/parent::*//' \
                       f'span[@ui_test_id="patient_info_span"]'
        return self.get_text_by_locator((By.XPATH, xpath_string))

    def send_text_to_notewriter(self, text):
        self.goto_end()
        self.enter_text_at(text, self.NOTEWRITER_EDITOR_LOCATOR, False, 1)

    def click_on_complete_button(self):
        self.click_and_wait(self.COMPLETE_BTN_LOCATOR)
        pages.scp_pages.home_page.HomePage(self.driver).wait_for_loader()
        print('Note status is changed to Complete...')

    def click_on_upload_button(self, complete_before=False):
        home_page = pages.scp_pages.home_page.HomePage(self.driver)
        if complete_before:
            selected_note_id = home_page.get_selected_note_id()
            self.click_on_complete_button()
            home_page.select_note_by_id(selected_note_id)

        self.click_and_wait(self.UPLOAD_BTN_LOCATOR)
        home_page.wait_for_loader()
        print('Note status is changed to Uploaded...')

    def get_complete_btn_background_color(self):
        return self.get_css_value(self.COMPLETE_BTN_LOCATOR, 'background-color')

    def get_upload_btn_background_color(self):
        return self.get_css_value(self.UPLOAD_BTN_LOCATOR, 'background-color')

    def use_macro_by_shortcut(self):
        actions = ActionChains(self.driver)
        actions.send_keys(' .').perform()

    def is_macro_window_open(self):
        return self.get_total_count(self.MACRO_WINDOW) == 1

    def close_macro_window(self):
        self.click_and_wait(self.MACRO_CROSS_ICON)
        self.wait_for_invisibility_of(self.MACRO_WINDOW)

    def is_text_blod(self):
        is_text_bold = self.get_total_count(self.BOLD_ALL_TEXT) == 1
        is_bold_button_on = self.get_attribute(self.BOLD_BUTTON, 'class').endswith('button_on')
        return is_text_bold and is_bold_button_on

    def is_text_underline(self):
        is_text_underline = self.get_total_count(self.UNDERLINE_ALL_TEXT) == 1
        is_underline_button_on = self.get_attribute(self.UNDERLINE_BUTTON, 'class').endswith('button_on')
        return is_text_underline and is_underline_button_on

    def is_text_italic(self):
        is_text_italic = self.get_total_count(self.ITALIC_ALL_TEXT) == 1
        is_italic_button_on = self.get_attribute(self.ITALIC_BUTTON, 'class').endswith('button_on')
        return is_text_italic and is_italic_button_on

    def is_text_bulleted_list(self):
        is_text_bulleted_list = self.get_total_count(self.BULLETED_LIST_ALL_TEXT) == 1
        is_bulleted_list_button_on = self.get_attribute(self.BULLETED_LIST_BUTTON, 'class').endswith('button_on')
        return is_text_bulleted_list and is_bulleted_list_button_on

    def is_text_numbered_list(self):
        is_text_numbered_list = self.get_total_count(self.NUMBERED_LIST_ALL_TEXT) == 1
        is_numbered_list_button_on = self.get_attribute(self.NUMBERED_LIST_BUTTON, 'class').endswith('button_on')
        return is_text_numbered_list and is_numbered_list_button_on

    def is_notewriter_section_disabled(self):
        is_secondary_header_disabled = 'is--disabled' in self.get_attribute(self.NOTEWRITER_SECONDARY_HEADER, 'class')
        is_secondary_subheader_disabled = 'is--disabled' in self.get_attribute(self.NOTEWRITER_SECONDARY_SUBHEADER,
                                                                               'class')
        is_richtexteditor_editable = 'false' == self.get_attribute(self.NOTEWRITER_EDITOR_LOCATOR, 'contenteditable')
        return is_secondary_header_disabled and is_secondary_subheader_disabled and is_richtexteditor_editable
