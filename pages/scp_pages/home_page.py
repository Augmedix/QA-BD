"""
Locators & methods for HomePage.
"""
import json
import random
import re
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import pages
from pages.base_page import BasePage
# from pages.note_builder.notewriter_page import NotewriterPage
# from pages.note_builder.organize_tab import OrganizeTab
from pages.scp_pages.pause_activity_modal import PauseActivityModal
from pages.scp_pages.note_builder.organize_tab import OrganizeTab
from utils.helper import find_minimum_time, get_current_time_stamp
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """
<<<<<<< HEAD
    This is the page where logged-in user is landed on.
    """
    # pylint: disable=too-many-arguments

    HAMBURGER_MENU_WINDOW = (By.ID, 'ajs-header-dropdown-menu')
    HAMBURGER_MENU_ICON_LOCATOR = (By.CSS_SELECTOR, '#ajs-header-title span')
    HAMBURGER_MENU_ITEMS_LOCATOR = (By.CSS_SELECTOR, '#ajs-header-dropdown-menu a')
    NOTEWRITER_PRIMARY = (By.CSS_SELECTOR, 'section.notewriter__primary')
    NOTEWRITER_SECONDARY = (By.CSS_SELECTOR, '#ajs-notewriter section.notewriter__secondary')

    SIGNOUT_LINK = (By.ID, 'ajs-header-scribe-signout')
    PROVIDER_DROPDOWN = (By.ID, 'ajs-header-provider-list')
    CONNECT_BTN = (By.ID, 'ajs-header-provider-connect-cta')
    CONNECTING_BTN = (By.XPATH, '//button[text()="Connecting ..."]')
    PAUSE_BTN_LOCATOR = (By.XPATH, '//button[text()="Pause"]')
    CONTINUE_BTN_LOCATOR = (By.XPATH, '//button[text()="Continue"]')
    ROLE_SELECTION_WINDOW = (
        By.CSS_SELECTOR, 'kendo-dialog[ng-reflect-title="What is your role today?"],kendo-dialog-titlebar')
    ADD_PATIENT_BTN = (By.ID, 'ajs-visit-list-add-new-patient-cta')
    LOADER = (By.CSS_SELECTOR, 'aside.loading.is--active .loading__content__text')
    NOTE_WRITER_NAME = (By.CSS_SELECTOR, 'span[id^="ajs-notewriter-note-name-"]')
    TAB_HEADER_LIST = (By.CSS_SELECTOR, 'app-nb-main-nav li')

    DISABLED_MESSAGE_ICON = (By.CSS_SELECTOR, '.message__icon')

    NOTE_CREATION_ERROR_MSG = (By.CSS_SELECTOR, '.alert.alert-danger.ng-star-inserted')
    UNSAVED_NOTE_ICON = (By.CSS_SELECTOR, '.notewriter__primary__list__item.active .oi-media-record')

    NOTE_STATUS_REMINDER_WINDOW = (By.CSS_SELECTOR, 'kendo-dialog div[role="dialog"]')
    NOTE_STATUS_REMINDER_DISCONNECT_BTN = (By.XPATH, '//kendo-dialog-actions//button[normalize-space()="Disconnect"]')
    NOTE_STATUS_REMINDER_UPDATE_BTN = (By.XPATH, '//kendo-dialog-actions//button[normalize-space()="Update statuses"]')

    DAILY_SCRIBE_LOG_WINDOW = (By.ID, 'ajs-sdl-reminder-modal')
    DAILY_SCRIBE_LOG_DO_THIS_LATER_BTN = (By.ID, 'ajs-sdl-reminder-modal-do-this-later')
    DAILY_SCRIBE_LOG_COMPLETE_LOG_BTN = (By.ID, 'ajs-sdl-reminder-modal-complete-log')
    DISCONNECT_BUTTON_LOCATOR = (By.ID, 'ajs-header-disconnect-from-provider')

    REFRESH_NOTE_LIST = (By.ID, 'ajs-visit-list-reload-cta')
    FILTER_NOTE = (By.ID, 'ajs-notewriter-filter-cta')
    ALL_PATIENT_FILTER = (By.ID, 'ajs-notewriter-filter-all-patient-cta')
    FIRST_NOTE = (By.ID, 'ajs-notewriter-note-id-0')
    SECOND_NOTE = (By.ID, 'ajs-notewriter-note-id-1')
    THIRD_NOTE_LOCATOR = (By.ID, 'ajs-notewriter-note-id-2')
    SCHEDULE_NOTE_LOCATOR = (By.CSS_SELECTOR, '.ico--lock')
    FIRST_SCHEDULE_LOCATOR = (By.XPATH, '//*[@id="ajs-notewriter-note-id-0"]//span[contains(@class,"ico--lock")]')

    SCP_CURRENT_TIMEZONE = (By.ID, 'ajs-timezone-multi-label-scibe')
    SCP_CURRENT_TIMEZONE_PROVIDER = (By.ID, 'ajs-timezone-multi-label-provider')
    SCP_CURRENT_SELECTED_CALENDER = (By.CSS_SELECTOR, 'div#ajs-notewriter-date-selection input')
    SCRIBE_NAME = (By.ID, 'ajs-header-scribe-info-name')
    SCRIBE_ROLE_INFO = (By.ID, 'ajs-header-scribe-info-dropdown-label')
    CONNECTED_SCRIBE_INFO_BODY = (By.ID, 'ajs-header-scribe-info-dropdown-body')

    HELP_DROPDOWN_ICON_LOCATOR = (By.ID, 'ajs-header-help-dropdown-label')
    HELP_MENU_BODY_LOCATOR = (By.ID, 'ajs-header-help-dropdown-body')
    HELP_MENU_ITEMS_LOCATOR = (By.CSS_SELECTOR, '#ajs-header-help-dropdown-body a')

    SETTINGS_DROPDOWN_ICON_LOCATOR = (By.ID, 'ajs-header-settings-dropdown-label')
    SETTINGS_MENU_BODY_LOCATOR = (By.ID, 'ajs-header-settings-dropdown-body')
    SETTING_MENU_ITEMS_LOCATOR = (By.CSS_SELECTOR, '#ajs-header-settings-dropdown-body a')
    NOTEWRITTER_MENU = (By.ID, 'ajs-notewriter-action-dropdown-cta')
    PUSH_CURRENT_NOTE = (By.ID, 'ajs-notewriter-action-push-note-cta')
    CONFIRM_PUSH_NOTE_MODAL = (By.XPATH, '//kendo-window[@ng-reflect-title="Push note"]')
    CONFIRM_PUSH_NOTE_MODAL_YES_BUTTON = (By.ID, 'ajs-push-note-yes')
    NBROOT_LOCATOR = (By.CSS_SELECTOR, 'app-nb-main section.nbroot')
    IS_EDITED_LOCATOR = (By.CSS_SELECTOR, 'span[class$="is--edited"]')

    # Selected note locator
    selected_note = 'li[id^="ajs-notewriter-note-id-"][class*="active"]:not([class*="d-none"])'
    SELECTED_NOTE = (By.CSS_SELECTOR, selected_note)
    SELECTED_NOTE_IS_EDITED = (By.CSS_SELECTOR, f'{selected_note} span[class$="is--edited"]')
    SELECTED_NOTE_IS_OUTDATED = (By.CSS_SELECTOR, f'{selected_note} span[class$="is--outdated"]')

    NOTE_START_TIME = (By.CSS_SELECTOR, f'{selected_note}  span[data-service-start-time]')

    SELECTED_NOTE_VISIT_TIME = (By.CSS_SELECTOR, f'{selected_note} span[id^="ajs-notewriter-start-end-"]')
    SELECTED_PATIENT_NAME = (By.CSS_SELECTOR, f'{selected_note} span[id^="ajs-notewriter-note-name-"]')
    SELECTED_NOTE_STATUS_TITLE = (
        By.CSS_SELECTOR,
        f'{selected_note} app-visit-list-item-action-dropdown span[title]'
    )
    SELECTED_NOTE_VISIT_DURATION_TIMER_TEXT = (
        By.CSS_SELECTOR,
        f'{selected_note} span[class="visit__list__item__timer__wrapper visit__list__item__action__due_time"]'
    )
    SELECTED_NOTE_PROGRESSBAR_LABEL = (By.CSS_SELECTOR, '.notewriter__primary__progress__primary__label')
    SELECTED_NOTE_PROGRESSBAR_NUMBER = (By.CSS_SELECTOR, '.notewriter__primary__progress__secondary__label')
    SELECTED_NOTE_PROGRESS = (By.CSS_SELECTOR, '.bg-success')

    # All note list locator
    ALL_VISIBLE_NOTE = (
        By.CSS_SELECTOR,
        'li[id^="ajs-notewriter-note-id-"]:not([class*="d-none"])'
    )
    ALL_VISIBLE_PATIENT_NAME = (
        By.CSS_SELECTOR,
        'li[id^="ajs-notewriter-note-id-"]:not([class*="d-none"]) '
        'span[id^="ajs-notewriter-note-name-"]'
    )

    ALL_NOTE_LOCATOR = (By.CSS_SELECTOR, 'li[id^="ajs-notewriter-note-id-"]')
    ALL_NOTE_VISIT_TIME = (By.CSS_SELECTOR, 'span[id^="ajs-notewriter-start-end-"]')
    ALL_NOTE_PATIENT_NAME = (By.CSS_SELECTOR, 'span[id^="ajs-notewriter-note-name-"]')
    ALL_NOTE_STATUS_TITLE = (By.CSS_SELECTOR, 'app-nw-visit-list-action-dropdown span[data-tooltip-right]')
    ALL_NOTE_VISIT_DURATION_TIMER = (By.CLASS_NAME, 'notewriter__primary__list__item__timer__wrapper')
    ALL_NOTE_VISIT_DURATION_TIMER_TEXT = (By.CLASS_NAME, 'notewriter__primary__list__item__timer__text')

    NOTE_ELLIPSE_ICON_LIST = (By.CSS_SELECTOR, 'app-nw-visit-list-action-dropdown')
    NOTE_DELETE_OPTION = (By.XPATH, '//li[contains(text(),"Delete")]')
    CONFIRM_DELETE_LOCATOR = (By.ID, 'ajs-notewriter-delete-note-confirm-yes')
    ACTIVE_NOTE_STATUS_LIST = (By.CSS_SELECTOR, 'app-nw-visit-list-action-dropdown ul li[class*="--active"]')

    MISSED_STATUS_REASON_INPUT = (By.ID, 'statusFormInputReason')
    MISSED_STATUS_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'app-nw-status-action-form button[type="submit"]')
    MISSED_STATUS_MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, 'button.nbmodal__content__close')

    # Note writer text area
    NOTE_WRITER_TEXT_EDITOR_LOCATOR = (By.ID, 'richtexteditor')

    # Locators for Confirmation window of Review Tab
    CONFIRM_REVIEW_TAB_LOCATOR = (By.XPATH, '//button[contains(text(), "Yes")]')

    PROVIDER_OFFLIE_TEXT = (By.CSS_SELECTOR, '.livestream__message__content__header')
    DISABLED_STREAM_SELECTION_DROPDOWN = (By.XPATH, '//div[@id="ajs-header-connection-status-dropdown" and'
                                                    ' contains(@class, "is--disabled")]/div[@id='
                                                    '"ajs-header-connection-status-dropdown-label"]/span')
    NOTIFICATION_TOGGLE = (By.CSS_SELECTOR, '.header__notification__toggle')
    NOTIFICATION_MSG_LOCATOR = (By.CSS_SELECTOR, '.header__notification__text')
    NOTIFICATION_CLEAR_ALL_BTN_LOCATOR = (By.CSS_SELECTOR, '.header__notification__dropdown__list.show'
                                                           ' .header__notification__dropdown__clear span')
    VOLUME_BUTTON = (By.ID, 'ajs-header-volume-area')

    FIRST_SCHEDULE_FROM_LIST = (By.XPATH, '(//*[@id="ajs-header-provider-list"]/'
                                          'optgroup[@label="Schedules"]/option)[1]')
    NOT_CONNECTED_TO_PROVIDER_TEXT = (By.CSS_SELECTOR, '.livestream__message__content__header')

    MODAL_WINDOW_LOCATOR = (By.TAG_NAME, 'kendo-dialog')
    CONNECTED_WITH_PROVIDER_INFO = (By.ID, 'ajs-header-scribe-connected-with')
    CONNECTED_PROVIDER_NAME_LOCATOR = (By.ID, 'ajs-header-connected-provider-name')

    DASHBOARD_MSG_LOCATOR = (By.CSS_SELECTOR, '#ajs-dashboard-alert div')

    # Scribe roles modal
    SCRIBE_ROLES_DESC_HEADER_LIST = (By.XPATH, '//h6[@class="scribe__connect__list__item__hl"]')
    SCRIBE_ROLES_DESC_LIST = (By.XPATH, '//*[@id="ajs-scribe-connect-list"]//p')
    SCRIBE_ROLES_MODAL_CROSS_ICON = (By.CSS_SELECTOR, '.k-button')
    SCRIBE_ROLES_BUTTON_LIST = (By.XPATH, '//*[@id="ajs-scribe-connect-list"]//button')
    PRIMARY_SCRIBE_BUTTON = (By.XPATH, '(//*[@id="ajs-scribe-connect-list"]//button)[1]')
    PRIMARY_VIEW_ONLY_BUTTON = (By.XPATH, '(//*[@id="ajs-scribe-connect-list"]//button)[2]')

    IMPORT_NOTE = (By.ID, 'ajs-notewriter-open-import-note-role-cta')

    # Help & support
    HELP_AND_SUPPORT_BUTTON = (By.ID, 'ajs-header-help-dropdown')

    CHAT_BOX_FRAME_LOCATOR = (By.CSS_SELECTOR, 'iframe[title="Opens a widget where you can chat to one of our agents"]')
    CHAT_BOX_CONTAINER_LOCATOR = (By.CSS_SELECTOR, '[data-testid="chat-badge"]')
    CHAT_BOX_MINIMIZE_ICON_LOCATOR = (By.CSS_SELECTOR, 'svg[data-testid="Icon--dash"]')

    ALERT_WINDOW_LOCATOR = (By.CSS_SELECTOR, 'div[id*="ajs-provider-toast-"]')
    ALERT_CLOSE_BTN_LOCATOR = (By.CSS_SELECTOR, 'div[id*="ajs-provider-toast-"] button[class="close"]')
    ALERT_TEXT_LOCATOR = (By.XPATH, '(//div[contains(@id, "ajs-provider-toast-")]//span)[1]')

    # Streaming
    CURRENT_STREAMING_OPTION = (By.ID, 'ajs-header-connection-status-dropdown')
    VIDEO_ICON = (By.XPATH, '//*[@id="ajs-header-connection-status-dropdown-label"]/span/span[@class="oi oi-video"]')
    BATTERY_HEALTH = (By.ID, 'ajs-livestream-provider-battery-health')
    LIVESTREAM_VIDEO_SECTION = (By.ID, 'ajs-livestream')
    VOLUME_HEADER = (By.CLASS_NAME, 'header__volume__text')
    VOLUME_AMPLIFY_SWITCH = (By.ID, 'ajs-header-volume-amplify-switch-input')
    VOLUME_AMPLIFY_SWITCH_SPAN = (By.CSS_SELECTOR, '.switch__slider')
    VOLUME_SLIDER = (By.ID, 'ajs-header-volume-amplify-level')
    STREAMING_OPTIONS_DROPDOWN = (By.XPATH, '//*[@id="ajs-header-connection-status-dropdown"]/'
                                            'div[@class="dropdown-menu dropdown-menu-right show"]')
    NO_STREAMING_OPTION = (By.ID, 'ajs-header-connection-status-item-no-streaming')
    AUDIO_STREAMING_OPTION = (By.ID, 'ajs-header-connection-status-item-audio-streaming')
    AUDIO_VIDEO_STREAMING_OPTION = (By.ID, 'ajs-header-connection-status-item-av-streaming')
    VIDEO_ONLY_STREAMING_OPTION = (By.ID, 'ajs-header-connection-status-item-video-streaming')
    NO_STREAMING_ICON = (By.XPATH, '//*[@id="ajs-header-connection-status-item-no-streaming"]/'
                                   'span[@class="oi oi-circle-x"]')
    AUDIO_STREAMING_ICON = (By.XPATH, '//*[@id="ajs-header-connection-status-item-audio-streaming"]/'
                                      'span[@class="k-icon k-i-volume-up"]')
    AUDIO_VIDEO_STREAMING_ICON = (By.XPATH, '//*[@id="ajs-header-connection-status-item-av-streaming"]/'
                                            'span[@class="oi oi-video"]')
    VIDEO_ONLY_STREAMING_ICON = (By.XPATH, '//*[@id="ajs-header-connection-status-item-video-streaming"]/'
                                           'span[@class="oi oi-video"]')
    A_V_CURRENT_STREAMING_VIDEO_ICON = (By.XPATH, '//*[@id="ajs-header-connection-status-dropdown-label"]/span/'
                                                  'span[@class="oi oi-video"]')
    VIDEO_ONLY_CURRENT_STREAMING_VIDEO_ICON = A_V_CURRENT_STREAMING_VIDEO_ICON
    NO_STREAMING_CURRENT_STREAMING_ICON = (By.XPATH, '//*[@id="ajs-header-connection-status-dropdown-label"]/span'
                                                     '/span[@class="oi oi-circle-x"]')
    AUDIO_CURRENT_STREAMING_ICON = (By.XPATH, '//*[@id="ajs-header-connection-status-dropdown-label"]/span/'
                                              'span[@class="k-icon k-i-volume-up"]')
    STREAMING_VIDEO = (By.ID, 'streaming-video')
    LIVESTREAM_MESSAGE_CONTENT_PARENT = (By.CSS_SELECTOR, '.livestream__message__content')
    LIVESTREAM_MESSAGE_CONTENT = (By.CSS_SELECTOR, '.livestream__message__content__header')
    LIVESTREAM_MUTE_ICON = (By.CSS_SELECTOR, '.livestream__mute__icon')
    LIVESTREAM_ICONS = (By.CSS_SELECTOR, '.livestream__online__icon')
    RESET_STREAMING = (By.ID, 'ajs-header-help-dropdown-menu-reset')
    LOG_PROVIDER_OUT_OF_GLASS = (By.ID, 'ajs-header-help-dropdown-menu-logout-provider')
    RESET_STREAMING_MODAL_TITLE = (By.CSS_SELECTOR, '.k-dialog-title')
    RESET_STREAMING_MODAL_CLOSE_BUTTON = (By.ID, 'ajs-header-close-av-reset-modal')
    RESET_STREAMING_MODAL_RESTART_BUTTON = (By.ID, 'ajs-header-restart-av-reset-cta')
    RESET_STREAMING_MODAL_BODY_TEXT = (By.CSS_SELECTOR, '.k-dialog-content')
    LOG_PROVIDER_OUT_OF_GLASS_MODAL_TITLE = RESET_STREAMING_MODAL_TITLE
    LOG_PROVIDER_OUT_OF_GLASS_MODAL_BODY_TEXT = RESET_STREAMING_MODAL_BODY_TEXT
    LOG_PROVIDER_OUT_OF_GLASS_MODAL_CLOSE_BUTTON = (By.ID, 'ajs-header-provider-logout-force-close')
    LOG_PROVIDER_OUT_OF_GLASS_MODAL_LOGOUT_BUTTON = (By.ID, 'ajs-header-provider-logout-force-yes')
    NETWORK_DISCONNECTION_ERROR_MSG_LOCATOR = (By.XPATH, '//*[text()="Connection Lost. Trying to reconnect to your'
                                                         ' internet. Please wait 120 seconds..."]')
    NETWORK_RECONNECTION_ERROR_MSG_LOCATOR = (By.XPATH, '//*[text()="You are reconnected to internet"]')

    DASHBOARD_MSG = 'Connect to a provider to see patients for the day'
    NETWORK_DISCONNECTION_MSG = 'Connection Lost. Trying to reconnect to your internet. Please wait 120 seconds...'
    NETWORK_RECONNECTION_MSG = 'You are reconnected to internet'
    LIVE_MESSAGE_TEXTAREA = (By.ID, 'ajs-quick-message-body-text')
    LOGIN_BTN = (By.ID, 'ajs-login-submit-btn')

    def pause_work(self):
        if not self.is_work_paused():
            self.click_and_wait(self.PAUSE_BTN_LOCATOR)
            self.wait_for_visibility_of(PauseActivityModal.SCREENSAVER_LOCATOR)
            print('Activity paused...')

    def select_provider_from_dropdown(self,provider_email):
        return (By.CSS_SELECTOR,"option[value*='" + provider_email + "']")

    def continue_working(self):
        if self.is_work_paused():
            self.click_and_wait(self.CONTINUE_BTN_LOCATOR)
            self.wait_for_visibility_of(self.PAUSE_BTN_LOCATOR)
            self.wait_for_loader()
            print('Continue working...')

    def is_work_paused(self):
        continue_button = self.get_total_count(self.CONTINUE_BTN_LOCATOR) == 1
        screensaver_appeared = PauseActivityModal(self.driver).is_screensaver_appeared()
        return continue_button and screensaver_appeared

    # def open_role_selection_window_for(self, provider_name):
    #     """
    #     Opens the role selection window for the specified provider.

    #     :param provider_name: name of the provider the window should be opened for.
    #     :return: returns nothing
    #     """
    #     self.select_by_visible_text(self.PROVIDER_DROPDOWN, provider_name)
    #     self.click_and_wait_for_target(self.CONNECT_BTN, self.ROLE_SELECTION_WINDOW)
    #     self.wait_for_visibility_of_text(self.ROLE_SELECTION_WINDOW, 'What is your role today?')
    #     print(f'Role selection window opened for provider: {provider_name}...')

    def open_role_selection_window_for(self, provider_email):
        """
        Opens the role selection window for the specified provider.

        :param provider_name: name of the provider the window should be opened for.
        :return: returns nothing
        """
        self.wait_for_existence_of(self.select_provider_from_dropdown(provider_email),60)
        # self.wait_for_existence_of((By.CSS_SELECTOR,"option[value*='" + provider_email + "']"),60)
        # self.click_and_wait((By.CSS_SELECTOR,"option[value*='" + provider_email + "']"),1)
        self.click_and_wait(self.select_provider_from_dropdown(provider_email),1)
    
        self.wait_for_loader(2)

        # self.select_by_visible_text(self.PROVIDER_DROPDOWN, provider_name)
        self.click_and_wait_for_target(self.CONNECT_BTN, self.ROLE_SELECTION_WINDOW)
        self.wait_for_visibility_of_text(self.ROLE_SELECTION_WINDOW, 'What is your role today?')
        print(f'Role selection window opened for provider: {provider_email}...')

    def close_role_selection_window(self):
        if self.is_element_visible(self.SCRIBE_ROLES_MODAL_CROSS_ICON, 5):
            self.click_and_wait(self.SCRIBE_ROLES_MODAL_CROSS_ICON, 5)
            self.wait_for_invisibility_of(self.SCRIBE_ROLES_MODAL_CROSS_ICON, 5)
            print('Role selection window closed for provider')

    # def connect_to_provider(self, provider_name, role='Primary scribe'):
    #     """
    #     Connects to a specified provider in a specific role provided.
    #     :param provider_name: name of the provider the window should be opened for.
    #     :param role: the role to be selected.
    #     :return:
    #     """
    #     if self.is_provider_connected():
    #         print('Scribe is already connected to provider...')
    #     else:
    #         self.open_role_selection_window_for(provider_name)
    #         xpath_for_role = (By.XPATH, f'//button[text()="{role}"]')
    #         self.click_and_wait(xpath_for_role, 5)
    #         self.wait_for_element_to_clickable(self.DISCONNECT_BUTTON_LOCATOR)
    #         self.wait_for_loader()
    #         print(f'Scribe connected to provider {provider_name} as {role}.')

    def connect_to_provider(self, provider_email, role ='Primary scribe', wait_for_loader_after_connect: bool = True):
        """
        Connects to a specified provider in a specific role provided.
        :param provider_name: name of the provider the window should be opened for.
        :param role: the role to be selected.
        :return:
        """
        if self.is_provider_connected():
            print('Scribe is already connected to provider...')
        else:
            self.open_role_selection_window_for(provider_email)
            xpath_for_role = (By.XPATH, f'//button[text()="{role}"]')
            self.click_and_wait(xpath_for_role)
            if wait_for_loader_after_connect:
                self.wait_for_element_to_clickable(self.DISCONNECT_BUTTON_LOCATOR)
                self.wait_for_loader()
            print(f'Scribe connected to provider {provider_email} as {role}.')

    def is_provider_connected(self):
        if self.get_total_count(self.DISCONNECT_BUTTON_LOCATOR) == 1:
            return True
        return False

    def disconnect_from_provider(self):
        if self.is_provider_connected():
            self.wait_for_element_to_clickable(self.DISCONNECT_BUTTON_LOCATOR, 20)
            self.click_and_wait(self.DISCONNECT_BUTTON_LOCATOR, 1)

            if self.is_element_visible(self.NOTE_STATUS_REMINDER_WINDOW, 5):
                self.wait_for_element_to_clickable(self.NOTE_STATUS_REMINDER_DISCONNECT_BTN)
                self.click_and_wait(self.NOTE_STATUS_REMINDER_DISCONNECT_BTN)

            # self.wait_for_visibility_of_text(self.NOT_CONNECTED_TO_PROVIDER_TEXT, 'Not connected to provider', 10)
            self.wait_for_element_to_clickable(self.CONNECT_BTN)
            print('Scribe is disconnected from provider')
        else:
            print('Scribe is not connected to provider')

    def disconnect_and_connect_to_provider(self, provider_name, role='Primary scribe'):
        self.disconnect_from_provider()
        time.sleep(5)  # wait for webRTC disposed
        self.connect_to_provider(provider_name, role)

    def get_all_provider_id_from_provider_dropdown(self):
        all_provider_id = []
        provider_select = Select(self.get_element(self.PROVIDER_DROPDOWN))
        for option in provider_select.options:
            option_value = json.loads(option.get_attribute('value'))
            all_provider_id.append(option_value['doctorId'])
        return all_provider_id

    def get_connected_provider_name(self):
        return self.get_element(self.CONNECTED_WITH_PROVIDER_INFO).text

    def get_scribe_name_and_role_info(self):
        scribe_name = self.get_element(self.SCRIBE_NAME).text
        scribe_role_info = self.get_element(self.SCRIBE_ROLE_INFO).text
        return [scribe_name, scribe_role_info]

    def get_selected_note_name(self):
        return self.get_text_by_locator(self.SELECTED_PATIENT_NAME)

    def clear_all_notification(self):
        self.click_and_wait_for_target(self.NOTIFICATION_TOGGLE, self.NOTIFICATION_CLEAR_ALL_BTN_LOCATOR)
        self.click_and_wait(self.NOTIFICATION_CLEAR_ALL_BTN_LOCATOR)
        self.wait_for_invisibility_of(self.NOTIFICATION_CLEAR_ALL_BTN_LOCATOR)

    def open_notification_window(self):
        if 'is--disabled' in self.get_attribute(self.NOTIFICATION_TOGGLE, 'class'):
            print('Notification is disable')
        else:
            self.click_and_wait(self.NOTIFICATION_TOGGLE)
            self.wait_for_visibility_of(self.NOTIFICATION_CLEAR_ALL_BTN_LOCATOR)
            print('Notification window opened')

    def get_all_notification(self):
        return self.get_list_of_text_from_locator(self.NOTIFICATION_MSG_LOCATOR)

    def add_patient(self, wait_for_loader=True):
        """
        Add a patients.
        :return: expected_visit_time
        """
        self.wait_for_loader()
        self.wait_for_element_to_clickable(self.ADD_PATIENT_BTN)
        expected_added_time = self.get_scp_provider_current_time()
        self.wait_and_click(self.ADD_PATIENT_BTN,1)
        if wait_for_loader:
            self.wait_for_loader()
        return expected_added_time

    def create_patient(self, patient_name=f'Patient_{get_current_time_stamp()}', gender='male',
                       age='18', visit_type='new', start_time=None, service_type='In-person',
                       visit_type_complaint=pytest.configs.get_config('visit_complaint_name'),
                       complaint_acute='', complaint_chronic=''):

        self.add_patient()
        organize_tab = OrganizeTab(self.driver)
        organize_tab.set_organize_tab_value(
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

        self.switch_to_tab('Build')
        self.switch_to_tab('Review')

    def start_visit_duration_timer(self, note_index):
        if not self.is_visit_duration_timer_running(note_index):
            self.get_elements(self.ALL_NOTE_VISIT_DURATION_TIMER)[note_index].click()
            print(f'Visit duration timer of note-{note_index} has started')
        else:
            print(f'Visit duration timer of note-{note_index} is already running')

    def stop_visit_duration_timer(self, note_index):
        if self.is_visit_duration_timer_running(note_index):
            self.get_elements(self.ALL_NOTE_VISIT_DURATION_TIMER)[note_index].click()
            print(f'Visit duration timer of note-{note_index} has stopped')
        else:
            print(f'Visit duration timer of note-{note_index} is already running')

    def is_visit_duration_timer_running(self, note_index):
        timer_element = self.get_elements(self.ALL_NOTE_VISIT_DURATION_TIMER)[note_index]
        return 'active' in self.get_attribute_from_element(timer_element, 'class')

    def get_visit_duration_by_note_index(self, note_index):
        timer_text_element = self.get_elements(self.ALL_NOTE_VISIT_DURATION_TIMER_TEXT)[note_index]
        note_visit_duration_text = self.get_text_by_element(timer_text_element)
        return int(re.sub(r'\D+', '', note_visit_duration_text))

    def get_scp_provider_current_time(self):
        current_time, am_pm, _ = self.get_text_by_locator(self.SCP_CURRENT_TIMEZONE_PROVIDER).split()
        return f'{current_time} {am_pm}'

    def get_scp_provider_time_zone(self):
        """
            expected output: provider timezone, such as: PST, CST, MT etc
        """
        scp_provider_time = self.get_text_by_locator(self.SCP_CURRENT_TIMEZONE_PROVIDER)
        return scp_provider_time.split()[-1]

    def get_selected_date(self):
        return self.get_attribute(self.SCP_CURRENT_SELECTED_CALENDER, 'value')

    def get_scribe_name(self):
        return self.get_text_by_locator(self.SCRIBE_NAME)

    def get_scribe_connected_role(self):
        return self.get_text_by_locator(self.SCRIBE_ROLE_INFO).split(',')[0]

    def get_first_added_note_visit_time(self):
        """
            This method return first added note visit time from all existing note in a day
        """
        all_visit_time = self.get_list_of_text_from_locator(self.ALL_NOTE_VISIT_TIME)
        return find_minimum_time(all_visit_time)

    def get_note_element(self, index=0):
        return self.get_elements(self.ALL_NOTE_LOCATOR)[index]

    def get_patient_info(self, selected=False, by_index=False, index=0):
        """
            This method return patient information
            if selected is True, then selected note information will be return
            if by_index is True, then note information will be return by any given index. 0 is default index value
        """
        note_id, visit_time, visit_duration, patient_name, note_status = '', '', '', '', ''
        if selected:
            note_id = self.get_selected_note_id()
            visit_time = self.get_text_by_locator(self.SELECTED_NOTE_VISIT_TIME)
            patient_name = self.get_text_by_locator(self.SELECTED_PATIENT_NAME)
            note_status = self.get_attribute(self.SELECTED_NOTE_STATUS_TITLE, 'title')

            # note_visit_duration_text = self.get_text_by_locator(self.SELECTED_NOTE_VISIT_DURATION_TIMER_TEXT)
            # visit_duration = int(re.sub(r'\D+', '', note_visit_duration_text))

        elif by_index:
            note_id = self.get_note_id_from_element(self.get_elements(self.ALL_NOTE_LOCATOR)[index])
            visit_time = self.get_text_by_element(self.get_elements(self.ALL_NOTE_VISIT_TIME)[index])
            patient_name = self.get_text_by_element(self.get_elements(self.ALL_NOTE_PATIENT_NAME)[index])
            note_status = self.get_note_status_title_by_index(index)
            # visit_duration = self.get_visit_duration_by_note_index(index)

        patient_info = {
            'note-id': note_id,
            'visit-time': visit_time,
            # 'visit-duration': visit_duration,
            'patient-name': patient_name,
            'note-status': note_status
        }
        return patient_info

    def delete_patient(self, note_id):
        target_note = f'li[data-note-id="{note_id}"]'
        note_delete_option = (By.CSS_SELECTOR, f'{target_note} app-nw-visit-list-action-dropdown ul li:last-child')

        self.expand_note_status_dropdown(by_id=True, note_id=note_id)
        self.click_and_wait_for_target(note_delete_option, self.CONFIRM_DELETE_LOCATOR)
        deletion_time = self.get_scp_provider_current_time()
        self.click_and_wait(self.CONFIRM_DELETE_LOCATOR)
        self.wait_for_loader()
        return deletion_time

    def delete_all_patient_one_by_one(self):
        """
        Delete all notes one by one from left side panel.
        """
        note_action_dropdown_elements = self.get_elements(self.NOTE_ELLIPSE_ICON_LIST)

        if len(note_action_dropdown_elements) > 0:
            for _ in note_action_dropdown_elements:
                total_patient_count = self.get_total_note_count()
                self.click_and_wait_for_target(self.NOTE_ELLIPSE_ICON_LIST, self.NOTE_DELETE_OPTION)
                self.click_and_wait_for_target(self.NOTE_DELETE_OPTION, self.CONFIRM_DELETE_LOCATOR)
                self.click_and_wait_for_invisibility(self.CONFIRM_DELETE_LOCATOR)
                self.wait_for_element_count_to_be(self.NOTE_ELLIPSE_ICON_LIST, total_patient_count - 1)
                self.wait_for_loader()
            print(f'Total of {len(note_action_dropdown_elements)} notes deleted...')
        else:
            print('No notes to delete...')

    def get_note_id_from_locator(self, note_locator):
        return self.get_attribute(note_locator, 'data-note-id')

    def get_note_id_from_element(self, note_element):
        return self.get_attribute_from_element(note_element, 'data-note-id')

    def get_selected_note_id(self):
        return self.get_note_id_from_locator(self.SELECTED_NOTE)

    def get_selected_note_index(self):
        all_note_class = self.get_list_of_attributes_from_locator(self.ALL_NOTE_LOCATOR, 'class')
        for index, class_value in enumerate(all_note_class):
            if 'active' in class_value:
                return index
        return None

    def get_note_id_by_patient_name(self, target_patient_name):
        self.refresh_visit_list()
        for index, note in enumerate(self.get_elements(self.ALL_NOTE_LOCATOR)):
            patient_name_element = self.get_elements(self.ALL_NOTE_PATIENT_NAME)[index]
            # patient_name = self.get_text_by_element(patient_name_element)
            patient_name = self.get_attribute_from_element(patient_name_element, "title")
            if patient_name == target_patient_name:
                return self.get_note_id_from_element(note)
        return None

    def get_total_note_count(self):
        return self.get_total_count(self.ALL_NOTE_LOCATOR)

    def get_all_note_id(self):
        all_note = self.get_elements(self.ALL_NOTE_LOCATOR)
        return [self.get_note_id_from_element(note) for note in all_note]

    def get_all_visible_note_id(self):
        """
           This method return a list which contains all visible note id.
           When the unfinished patient option is selected from the filter,
           scheduled & complete notes for RT and only complete notes for NRT are visible
           and the rest of the notes become invisible.
        """
        all_visible_note = self.get_elements(self.ALL_VISIBLE_NOTE)
        return [self.get_note_id_from_element(note) for note in all_visible_note]

    def get_all_patient_name(self):
        return self.get_list_of_text_from_locator(self.ALL_NOTE_PATIENT_NAME)

    def get_all_visible_patient_name(self):
        return self.get_list_of_text_from_locator(self.ALL_VISIBLE_PATIENT_NAME)

    def get_note_status_title_by_id(self, note_id):
        note_status_title_locator = (
            f'li[data-note-id="{note_id}"] '
            f'app-nw-visit-list-action-dropdown span[data-tooltip-right]'
        )
        return self.get_attribute((By.CSS_SELECTOR, note_status_title_locator), 'data-tooltip-right')

    def get_note_status_title_by_index(self, note_index):
        note_status_title_element = self.get_elements(self.ALL_NOTE_STATUS_TITLE)[note_index]
        return self.get_attribute_from_element(note_status_title_element, 'data-tooltip-right')

    def get_active_note_status_by_id(self, note_id):
        active_status_locator = (
            f'li[data-note-id="{note_id}"] '
            f'app-nw-visit-list-action-dropdown li[class*="--active"]'
        )
        return self.get_text_by_locator((By.CSS_SELECTOR, active_status_locator))

    def get_active_note_status_by_index(self, note_index):
        active_status_element = self.get_elements(self.ACTIVE_NOTE_STATUS_LIST)[note_index]
        return self.get_text_by_element(active_status_element)

    def change_note_status_by_id(self, note_id, status, missed_reason=None):
        """
            This method change note status by that note id
            status expected value: Scheduled, Denied, Cancellation
        """
        self.wait_for_loader()
        self.expand_note_status_dropdown(by_id=True, note_id=note_id)
        self.click_and_wait((By.XPATH, f'//li[@data-note-id="{note_id}"]//li[text()="{status}"]'))
        if status == 'Missed':
            self.select_by_visible_text(self.MISSED_STATUS_REASON_INPUT, missed_reason)
            self.click_and_wait(self.MISSED_STATUS_SUBMIT_BUTTON)
        self.wait_for_loader()
        print(f'"{status}" status selected!')

    def change_note_status_by_index(self, note_index, status, missed_reason=None):
        """
            This method change note status by that note index, index start with 0
            status expected value: Scheduled, Denied, Cancellation, No visit, Skipped, Duplicate
        """
        self.wait_for_loader()
        self.expand_note_status_dropdown(by_index=True, note_index=note_index)
        self.click_and_wait((By.XPATH, f'(//li[text()="{status}"])[{note_index + 1}]'), 2)
        if status == 'Missed':
            self.select_by_visible_text(self.MISSED_STATUS_REASON_INPUT, missed_reason)
            self.click_and_wait(self.MISSED_STATUS_SUBMIT_BUTTON)
        self.wait_for_loader()
        print(f'"{status}" status selected!')

    def expand_note_status_dropdown(self, by_id=False, by_index=False, note_id=None, note_index=None):
        action_dropdown, dropdown_body = '', ''
        if by_id:
            action_dropdown = (By.CSS_SELECTOR, f'li[data-note-id="{note_id}"] app-nw-visit-list-action-dropdown')
            dropdown_body = (By.CSS_SELECTOR, f'li[data-note-id="{note_id}"] app-nw-visit-list-action-dropdown ul')
        elif by_index:
            action_dropdown = (By.XPATH, f'(//app-nw-visit-list-action-dropdown)[{note_index + 1}]')
            dropdown_body = (By.XPATH, f'(//app-nw-visit-list-action-dropdown//ul)[{note_index + 1}]')

        if self.is_element_visible(dropdown_body, 2):
            print('Note status dropdown is already opened')
        else:
            self.click_and_wait(action_dropdown, 2)
            self.wait_for_visibility_of(dropdown_body)


    def navigate_to_review_of_existing_note(self, patient_name=f'Patient_{get_current_time_stamp()}', gender='male',
                                            age='18', visit_type='new', start_time=None, service_type='In-person',
                                            visit_type_complaint=pytest.configs.get_config('visit_complaint_name'),
                                            complaint_acute='', complaint_chronic=''):

        organize_tab = OrganizeTab(self.driver)
        organize_tab.set_organize_tab_value(
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
        self.switch_to_tab('Build')
        self.switch_to_tab('Review')

    def perform_logout(self):
        """
        Logs out a user from SCP.

        :return: None
        """
        if self.get_total_count(self.SIGNOUT_LINK) == 1:
            self.click_and_wait(self.SIGNOUT_LINK)

            if self.is_element_visible(self.NOTE_STATUS_REMINDER_WINDOW, 5):
                self.wait_for_element_to_clickable(self.NOTE_STATUS_REMINDER_DISCONNECT_BTN)
                self.click_and_wait(self.NOTE_STATUS_REMINDER_DISCONNECT_BTN)

            self.wait_for_existence_of(self.LOGIN_BTN)
            print('Logout performed successfully...\n')
        else:
            print('User is not logged in')

    def click_on_tab(self, tab_name):
        """
        Click on one of the specified tabs.

        :param tab_name: tab name to switch to i.e.- Build, Organize etc.
        :return: None
        """
        tab_locator_str = f'//span[text()="{tab_name.lower()}"]/parent::li'
        self.wait_for_loader()
        try:
            self.click_and_wait((By.XPATH, tab_locator_str))
        except StaleElementReferenceException:
            self.click_and_wait((By.XPATH, tab_locator_str))

    def switch_to_tab(self, tab_name):
        """
        Click on one of the specified tabs & wait until the desired tab is fully loaded.

        :param tab_name: tab name to switch to i.e.- Build, Organize etc.
        :return: None
        """
        self.click_on_tab(tab_name)
        if tab_name == 'Review':
            self.click_and_wait_for_target(self.CONFIRM_REVIEW_TAB_LOCATOR,
                                           NotewriterPage.NOTEWRITER_EDITOR_LOCATOR)
        self.wait_for_loader()
        print(f'Switched to {tab_name.upper()} tab successfully.')

    def is_tab_selected(self, tab_name):
        """
        Checks for whether specified tab is selected or not.
        :param tab_name: tab name to be checked for.
        :return: True/False based on whether the tab is selected or not.
        """
        tabs = self.get_elements(self.TAB_HEADER_LIST)
        for tab in tabs:
            if self.get_text_by_element(tab).lower() == tab_name.lower():
                return 'active' in self.get_attribute_from_element(tab, 'class')
        return False

    def wait_for_s2t_notes_to_be_visible(self):
        try:
            self.wait_for_visibility_of(self.FIRST_NOTE, 5)
            return True
        except Exception:
            print('Note is not present for today\'s service day')
            return False

    def wait_for_loader(self, max_wait_time_for_visibility=5, max_wait_time_for_invisibility=120):
        if self.is_element_visible(self.LOADER, max_wait_time_for_visibility):
            self.wait_for_invisibility_of(self.LOADER, max_wait_time_for_invisibility)

        if self.is_element_visible(self.LOADER, 2):
            self.wait_for_invisibility_of(self.LOADER, max_wait_time_for_invisibility)

    def create_new_note(self):

        self.add_patient()
        # self.wait_for_visibility_of(self.Noteid)

    def switch_note(self):
        self.get_element(self.SECOND_NOTE).click()
        self.get_element(self.FIRST_NOTE).click()

    def expand_setting_menu(self):
        if self.get_attribute(self.SETTINGS_MENU_BODY_LOCATOR, 'class').endswith('show'):
            print('Settings menu already expanded...')
        else:
            self.click_and_wait(self.SETTINGS_DROPDOWN_ICON_LOCATOR)
            print('Settings menu is expanded...')

    def open_window_for_setting_menu(self, menu_item):
        """
        Opens window for setting menu items.

        :param menu_item: name of the text expander. Possible values: Edit templates, Edit auto corrections,
        Edit Dictionary
        :return:
        """
        if self.get_total_count(self.MODAL_WINDOW_LOCATOR) == 0:
            self.expand_setting_menu()
            xpath_string = f'//*[text()="{menu_item}"]'
            menu_item_locator = (By.XPATH, xpath_string)
            window_title = menu_item.replace('Edit', '').strip()
            window_locator_string = f'[ng-reflect-title="{window_title}" i]'
            window_locator = (By.CSS_SELECTOR, f'{window_locator_string}, kendo-dialog-titlebar')
            self.click_and_wait_for_target(menu_item_locator, window_locator)
            self.wait_for_loader()
            print(f'Window opened for "{menu_item}"...')
        else:
            print('Text expander already opened...')

    def get_setting_menu_items(self):
        return self.get_list_of_text_from_locator(self.SETTING_MENU_ITEMS_LOCATOR)

    def get_setting_menu_item_text(self, item_index):
        menu_item_list = self.get_setting_menu_items()
        return menu_item_list[item_index]

    def is_hamburger_menu_open(self):
        return self.get_attribute(self.HAMBURGER_MENU_WINDOW, 'class').endswith('show')

    def open_hamburger_menu_item(self, menu_item_name):
        """
        Clicks on a hamburger menu item.

        :param menu_item_name: menu item name to click on.
        """
        if not self.is_hamburger_menu_open():
            self.click_and_wait(self.HAMBURGER_MENU_ICON_LOCATOR, 1)

        for menu_item in self.get_elements(self.HAMBURGER_MENU_ITEMS_LOCATOR):
            if menu_item.text.strip() == menu_item_name:
                menu_item.click()
                break

    def goto_notebuilder(self):
        self.open_hamburger_menu_item('Notebuilder')
        self.wait_for_loader()
        print('Notebuilder page loaded...')

    def goto_notes_for_grading_page(self):
        self.open_hamburger_menu_item('Notes for grading')
        self.wait_for_loader()
        print('Notes for grading page loaded...')

    def goto_feedback_all_page(self):
        self.open_hamburger_menu_item('Feedback (All)')
        self.wait_for_loader()
        print('Feedback (All) page loaded...')

    def expand_help_and_support_menu(self):
        if self.get_attribute(self.HELP_MENU_BODY_LOCATOR, 'class').endswith('show'):
            print('Help and support menu already expanded...')
        else:
            self.click_and_wait(self.HELP_DROPDOWN_ICON_LOCATOR)
            print('Help and support menu is expanded...')

    def open_window_for_help_and_support(self, menu_item):
        """
            Opens window for help_and_support menu items.
            param menu_item: Possible values: Keyboard shortcuts, Recover note history, Recover deleted patient
        """
        if self.get_total_count(self.MODAL_WINDOW_LOCATOR) == 0:
            self.expand_help_and_support_menu()
            xpath_string = f'//*[text()="{menu_item}"]'
            menu_item_locator = (By.XPATH, xpath_string)
            self.click_and_wait(menu_item_locator, 5)
            print(f'Window opened for "{menu_item}"...')
        else:
            print('Help and support already opened...')

    def get_help_and_support_item_text(self, item_index):
        menu_item_list = self.get_list_of_text_from_locator(self.HELP_MENU_ITEMS_LOCATOR)
        return menu_item_list[item_index]

    def save_note(self):
        """
            This method perform ctrl+s keyboard action
            return True if loader is visible else return false
        """
        actions = ActionChains(self.driver)
        # actions.key_down(Keys.CONTROL).send_keys('s').key_up(Keys.CONTROL).perform()
        actions.send_keys(Keys.ENTER).perform()
        is_loader_visible = self.is_element_visible(self.LOADER, 3)
        time.sleep(5)

        if self.get_total_count(self.SELECTED_NOTE_IS_EDITED) == 0:
            print('Note saved!')
        else:
            print('Note is not saved!')

        return is_loader_visible

    def select_note_by_id(self, note_id, wait_after_select=True):
        for single_note in self.get_elements(self.ALL_NOTE_LOCATOR):
            if note_id == self.get_note_id_from_element(single_note):
                if self.is_note_selected(note_element=single_note):
                    print(f'Note(id-{note_id}) is already selected')
                else:
                    self.scroll_into_view_by_element(single_note)
                    time.sleep(1)
                    self.click_and_wait_by_element(single_note)
                    if wait_after_select:
                        self.wait_for_loader()
                    print(f'Note(id-{note_id}) has been selected')
                break

    def select_note_by_index(self, index):
        target_note = self.get_elements(self.ALL_NOTE_LOCATOR)[index]
        if self.is_note_selected(note_element=target_note):
            print(f'Note-{index} is already selected')
        else:
            self.scroll_into_view_by_element(target_note)
            self.click_and_wait_by_element(target_note)
            self.wait_for_loader()
            print(f'Note-{index} has been selected')

    def select_note_by_name(self, patient_name):
        note_locator = (By.XPATH, f'//span[normalize-space()="{patient_name}"]//ancestor::li[@data-note-id]')
        note_element = self.get_element(note_locator)
        if self.is_note_selected(note_element=note_element):
            print(f'Note(patient-name:{patient_name}) is already selected')
        else:
            self.scroll_into_view_by_element(note_element)
            self.click_and_wait_by_element(note_element)
            self.wait_for_loader()
            print(f'Note(patient-name:{patient_name}) has been selected')

    def is_note_selected(self, note_index=None, patient_name=None, note_id=None, note_element=None):
        target_note_element = ''
        if note_index is not None:
            target_note_element = self.get_elements(self.ALL_NOTE_LOCATOR)[note_index]
        elif patient_name is not None:
            note_locator = (By.XPATH, f'//span[normalize-space()="{patient_name}"]//ancestor::li[@data-note-id]')
            target_note_element = self.get_element(note_locator)
        elif note_id is not None:
            note_locator = (By.CSS_SELECTOR, f'li[data-note-id="{note_id}"]')
            target_note_element = self.get_element(note_locator)
        elif note_element is not None:
            target_note_element = note_element
        return 'active' in self.get_attribute_from_element(target_note_element, 'class')

    def minimize_zendesk_chatbox(self):
        self.wait_for_loader(5, 30)
        try:
            self.wait_for_visibility_of(HomePage.CHAT_BOX_FRAME_LOCATOR, 60)
            self.change_frame(HomePage.CHAT_BOX_FRAME_LOCATOR)
            if self.get_total_count(HomePage.CHAT_BOX_CONTAINER_LOCATOR) > 0:
                self.click_and_wait(HomePage.CHAT_BOX_MINIMIZE_ICON_LOCATOR, 2)
                print('Zendesk chatbox minimized...')
            else:
                print('Zendesk chatbox already minimized...')
            self.driver.switch_to.default_content()
        except TimeoutException:
            print('No chatbox present...')

    def is_alert_message_visible(self):
        return self.is_element_visible(self.ALERT_WINDOW_LOCATOR, 10)

    def get_alert_message_text(self):
        return self.get_text_by_locator(self.ALERT_TEXT_LOCATOR)

    def wait_until_alert_remove(self):
        if self.is_alert_message_visible():
            self.wait_for_invisibility_of(self.ALERT_WINDOW_LOCATOR)

    def close_alert_warning(self):
        total_alert_count = self.get_total_count(self.ALERT_WINDOW_LOCATOR)
        while total_alert_count > 0:
            self.click_and_wait(self.ALERT_CLOSE_BTN_LOCATOR, 5)
            total_alert_count = self.get_total_count(self.ALERT_WINDOW_LOCATOR)
        print('Alert window colsed!')

    def get_current_note_progress_value(self):
        return self.get_text_by_locator(self.SELECTED_NOTE_PROGRESSBAR_LABEL)

    def get_current_note_progress_number(self):
        return self.get_text_by_locator(self.SELECTED_NOTE_PROGRESSBAR_NUMBER)

    def is_live_message_textarea_focused(self):
        textarea_element = self.get_element(self.LIVE_MESSAGE_TEXTAREA)
        return textarea_element == self.driver.switch_to.active_element

    def is_selected_note_outdated(self):
        return self.get_total_count(self.SELECTED_NOTE_IS_OUTDATED) == 1

    def is_nb_disable_hover_and_dimmed(self):
        nbroot_class_value = self.get_attribute(self.NBROOT_LOCATOR, 'class')
        return 'is--disable-hover is--dimmed' in nbroot_class_value
    
    def refresh_visit_list(self):
        self.click_and_wait(self.REFRESH_NOTE_LIST,1)
        self.wait_for_loader(2,30)

    def handle_alert(self,wait=10):
        WebDriverWait(self.driver, wait).until(EC.alert_is_present())
        print('Alert found')
        alert = self.driver.switch_to.alert
        alert.accept()
        print('Alert accepted')
