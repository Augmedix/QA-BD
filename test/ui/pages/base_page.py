import time

import pytest
from appium import webdriver as appium_webdriver
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import Select, WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
import time



def wait_for(max_wait=15):
    time.sleep(max_wait)


class ElementAttributeToBe:
    def __init__(self, locator, attribute, expected_attribute_value):
        self.locator = locator
        self.attribute = attribute
        self.attribute_value = expected_attribute_value

    def __call__(self, driver, *args, **kwargs):
        expected_element = driver.find_element(*self.locator)
        attribute_value = expected_element.get_attribute(self.attribute)
        return self.attribute_value == attribute_value


class ElementCountToBeEqual:
    def __init__(self, locator, expected_count):
        self.locator = locator
        self.expected_count = expected_count

    def __call__(self, driver, *args, **kwargs):
        elements = driver.find_elements(*self.locator)
        element_count = len(elements)
        return element_count == self.expected_count


class ElementCountToBeEqualOrGrater:
    def __init__(self, locator, expected_count):
        self.locator = locator
        self.expected_count = expected_count

    def __call__(self, driver, *args, **kwargs):
        elements = driver.find_elements(*self.locator)
        element_count = len(elements)
        return element_count >= self.expected_count


class BasePage:

    def __init__(self, driver):
        self.driver = driver if driver is not None else appium_webdriver.Remote()
        self.wait = WebDriverWait(self.driver, 10)

        """with open(f'{AppConstant.RESOURCE_FOLDER}/page_objects.properties', 'r') as file:
            module_info_list = file.readlines()
            for module_info in module_info_list:
                if '#' not in module_info:
                    object_name, module_name = module_info.split('=')
                    module = importlib.import_module('pages.' + module_name.replace('\n', ''))
                    class_name = ''.join(map(lambda item: item.title().strip(), module_name.split('.')[-1].split('_')))
                    page_object = getattr(module, class_name)(driver)
                    setattr(self, object_name, page_object)"""

    def get_element(self, by_locator, max_wait=30):
        self.wait_for_existence_of(by_locator, max_wait)
        return self.driver.find_element(*by_locator)

    def get_elements(self, by_locator):
        return self.driver.find_elements(*by_locator)


    # def get_element_above_of(self, reference_locator, target_locator):
    #     """
    #     :param reference_locator: this is the reference locator against which we need to find element above
    #     :param target_locator: the locator by which we need to find element above the reference locator
    #     :return: returns an element above the reference locator
    #     """
    #     reference_element = self.get_element(reference_locator)
    #     return self.driver.find_element(locate_with(target_locator).above(reference_element))
    #
    # def get_element_below_of(self, reference_locator, target_locator):
    #     """
    #     :param reference_locator: this is the reference locator against which we need to find element below
    #     :param target_locator: the locator by which we need to find element below the reference locator
    #     :return: returns an element below the reference locator
    #     """
    #     reference_element = self.get_element(reference_locator)
    #     return self.driver.find_element(locate_with(*target_locator).below(reference_element))
    #
    # def get_element_to_left_of(self, reference_locator, target_locator):
    #     """
    #     :param reference_locator: this is the reference locator against which we need to find element to the left
    #     :param target_locator: the locator by which we need to find element to the left of the reference locator
    #     :return: returns an element which is to the left of the reference locator
    #     """
    #     reference_element = self.get_element(reference_locator)
    #     return self.driver.find_element(locate_with(target_locator).to_left_of(reference_element))
    #
    # def get_element_to_right_of(self, reference_locator, target_locator):
    #     """
    #     :param reference_locator: this is the reference locator against which we need to find element to the right
    #     :param target_locator: the locator by which we need to find element to the right of the reference locator
    #     :return: returns an element which is to the right of the reference locator
    #     """
    #     reference_element = self.get_element(reference_locator)
    #     return self.driver.find_element(locate_with(target_locator).to_right_of(reference_element))

    def get_parent_of(self, child_locator):
        element = self.get_element(child_locator)
        return element.find_element(By.XPATH, '..')

    def get_attribute(self, locator, attribute):
        return self.get_element(locator).get_attribute(attribute).strip()

    def get_attribute_from_element(self, element, attribute):
        return element.get_attribute(attribute).strip()

    def get_list_of_text_from_locator(self, by_locator):
        elements = self.get_elements(by_locator)
        list_of_texts = list(
            map(lambda element: element.text.strip(), elements))
        return list_of_texts

    def get_list_of_text_from_elements(self, elements):
        """
        :param elements: list of elements from which text will be extracted
        :return: returns a list of texts/strings extracted from elements provided
        """
        list_of_texts = list(
            map(lambda element: element.text.strip(), elements))
        return list_of_texts

    def get_total_count(self, by_locator, wait:bool = False):
        """
        :param by_locator: the locator for which total items to be counted/found
        :return: return the total number of elements found for that specific locator
        """
        if wait:
            self.wait_for_visibility_of(by_locator,30)
        return len(self.get_elements(by_locator))
    
    def scroll_into_view(self, locator):
        element = self.get_element(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    def scroll_into_view_by_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView();', element)
    
    def click_and_wait_by_element(self, element, wait_time=0, max_wait_for_clickable=5):
        """
        Click on provided element & wait for a specified amount of time.
        :param element: element for which element to be clicked
        :param wait_time: wait after click on the element. wait time is in second
        :param max_wait_for_clickable: maximum waiting time for element to clickable
        :return: returns nothing
        """
        self.wait_for_element_to_clickable(element, max_wait=max_wait_for_clickable)
        element.click()
        time.sleep(wait_time)

    def get_text_by_locator(self, locator, max_wait: int = 5):
        """
        :param locator: the locator for which text is to be extracted
        :return: returns a trimmed/stripped string for element located by provided locator
        """
        return self.get_element(locator, max_wait).text.strip()

    def get_text_by_element(self, element):
        """
        Returns string from element provided.
        :param element: element for which text is to be extracted
        :return: returns stripped text/string from element provided
        """
        return element.text.strip()

    def get_list_of_texts_for_element(self, locator):
        """
        Get texts for all elements found by specified locator.
        :param locator: the locator for which text list to be extracted.
        :return: list of text.
        """
        return [item.text.strip() for item in self.get_elements(locator)]

    def get_css_value(self, locator, css_property):
        """
        Get css value for a css property i.e.: color, background-color, padding etc.
        :param locator: locator by which element's css property to be extracted
        :param css_property: the css property for which value to be extracted
        :return: returns css property value after stripping it off.
        """
        expected_element = self.get_element(locator)
        return expected_element.value_of_css_property(css_property).strip()

    def get_css_value_from_element(self, expected_element, css_property):
        """
        Get css value for a css property i.e.: color, background-color, padding etc.
        :param expected_element: element for which element's css property to be extracted
        :param css_property: the css property for which value to be extracted
        :return: returns css property value after stripping it off.
        """
        return expected_element.value_of_css_property(css_property).strip()

    def get_value_by_locator(self, locator):
        """
        :param locator: the locator for which text is to be extracted
        :return: returns a trimmed/stripped string for element located by provided locator
        """
        return self.get_element(locator).value
    
    def click_and_wait(self, by_locator, max_wait=0):
        """
        Clicks an element for provided locator & wait for a specified amount of time.
        :param by_locator: locator for which element to be clicked
        :param max_wait: maximum waiting time before throwing ELEMENT NOT FOUND EXCEPTION
        :return: returns nothing
        """
        self.get_element(by_locator).click()
        wait_for(max_wait)
    
    def click_on_last_element_and_wait(self, by_locator, max_wait = 0):
        """
        Clicks last element for provided locator & wait for a specified amount of time.
        :param by_locator: locator for which last element to be clicked
        :param max_wait: maximum waiting time before throwing ELEMENT NOT FOUND EXCEPTION
        :return: returns nothing
        """
        self.get_last_element(by_locator).click()
        wait_for(max_wait)

    def click_on_first_element_and_wait(self, by_locator, max_wait = 0):
        """
        Clicks last element for provided locator & wait for a specified amount of time.
        :param by_locator: locator for which last element to be clicked
        :param max_wait: maximum waiting time before throwing ELEMENT NOT FOUND EXCEPTION
        :return: returns nothing
        """
        self.get_first_element(by_locator).click()
        wait_for(max_wait)

    def wait_and_click(self, by_locator, max_wait=10):
        """
        Wait for a specified amount of time to clickable the provided locator and then click
        :param by_locator: locator for which element to be clicked
        :param max_wait: maximum waiting time before throwing ELEMENT NOT FOUND EXCEPTION
        :return: returns nothing
        """
        self.wait_for_visibility_of(by_locator, max_wait)
        self.wait_for_element_to_clickable(by_locator, max_wait)
        self.get_element(by_locator).click()

    def click_and_wait_for_target(self, by_locator, target_locator=None):
        """
        Clicks an element for provided locator & wait for a specific element located by target locator.
        :param by_locator: locator for which element to be clicked
        :param target_locator: the locator for which to wait for before throwing ELEMENT NOT FOUND EXCEPTION
        :return: returns nothing
        """
        self.click_and_wait(by_locator)
        self.wait_for_existence_of(target_locator) if target_locator is not None else None

    def click_and_wait_for_visibility(self, by_locator, target_locator=None, max_wait=5):
        """
        Clicks an element for provided locator & wait for a specific element located by target locator.
        :param by_locator: locator for which element to be clicked
        :param target_locator: the locator for which to wait for visibility before throwing ELEMENT NOT FOUND EXCEPTION
        :return: returns nothing
        """
        self.click_and_wait(by_locator)
        self.wait_for_visibility_of(target_locator, max_wait) if target_locator is not None else None

    def click_and_wait_for_invisibility(self, by_locator, max_wait=5):
        self.click_and_wait(by_locator)
        self.wait_for_invisibility_of(by_locator, max_wait)

    def enter_text_at(self, target_locator, text='',  clear_existing=True, max_wait=5):
        """
        Enter text into specific element located by a target locator. If clear_existing=True then existing text
        will be cleared out & new text is entered. Otherwise, new text is entered at the end of existing text.
        :param text: text to be entered
        :param target_locator: locator for which text to be entered
        :param clear_existing: if set to True existing content/data is cleared before entering new data.
        :param max_wait: maximum waiting time before throwing ELEMENT NOT FOUND EXCEPTION
        :return: returns nothing
        """
        self.wait_for_visibility_of(target_locator, max_wait)
        element = self.get_element(target_locator)
        
        if clear_existing:
            element.clear()
        # else:
        #     actions = ActionChains(self.driver)
        #     actions.key_down(Keys.LEFT_CONTROL).key_down(Keys.END) \
        #         .key_up(Keys.LEFT_CONTROL).key_up(Keys.END).perform()
        element.send_keys(text)

    def clear_texts(self, target_locator, max_wait=5):
        self.wait_for_visibility_of(target_locator, max_wait)
        element = self.get_first_element(target_locator)
        element.click()
        element.clear()


    def enter_text_at_first_locator(self, target_locator, text='',  clear_existing=True, max_wait=5):
        """
        Enter text into specific last element located by a target locator. If clear_existing=True then existing text
        will be cleared out & new text is entered. Otherwise, new text is entered at the end of existing text.
        :param text: text to be entered
        :param target_locator: locator for which text to be entered
        :param clear_existing: if set to True existing content/data is cleared before entering new data.
        :param max_wait: maximum waiting time before throwing ELEMENT NOT FOUND EXCEPTION
        :return: returns nothing
        """
        self.wait_for_visibility_of(target_locator, max_wait)
        element = self.get_first_element(target_locator)
        
        if clear_existing:
            element.clear()
        # else:
        #     actions = ActionChains(self.driver)
        #     actions.key_down(Keys.LEFT_CONTROL).key_down(Keys.END) \
        #         .key_up(Keys.LEFT_CONTROL).key_up(Keys.END).perform()
        element.send_keys(text)
    
    def enter_text_at_last_locator(self, target_locator, text='',  clear_existing=True, max_wait=5):
        """
        Enter text into specific last element located by a target locator. If clear_existing=True then existing text
        will be cleared out & new text is entered. Otherwise, new text is entered at the end of existing text.
        :param text: text to be entered
        :param target_locator: locator for which text to be entered
        :param clear_existing: if set to True existing content/data is cleared before entering new data.
        :param max_wait: maximum waiting time before throwing ELEMENT NOT FOUND EXCEPTION
        :return: returns nothing
        """
        self.wait_for_existence_of(target_locator, max_wait)
        element = self.get_last_element(target_locator)
        
        if clear_existing:
            element.clear()
        # else:
        #     actions = ActionChains(self.driver)
        #     actions.key_down(Keys.LEFT_CONTROL).key_down(Keys.END) \
        #         .key_up(Keys.LEFT_CONTROL).key_up(Keys.END).perform()
        element.send_keys(text)

    def enter_text_at_element(self, element, text='',  clear_existing=True):
        """
        Enter text into specific provided element. If clear_existing=True then existing text
        will be cleared out & new text is entered. Otherwise, new text is entered at the end of existing text.
        :param text: text to be entered
        :param element: element for which text to be entered
        :param clear_existing: if set to True existing content/data is cleared before entering new data.
        :param max_wait: maximum waiting time before throwing ELEMENT NOT FOUND EXCEPTION
        :return: returns nothing
        """
        
        if clear_existing:
            element.clear()
        # else:
        #     actions = ActionChains(self.driver)
        #     actions.key_down(Keys.LEFT_CONTROL).key_down(Keys.END) \
        #         .key_up(Keys.LEFT_CONTROL).key_up(Keys.END).perform()
        element.send_keys(text)


    def select_by_visible_text(self, locator, text_to_select):
        """
        Select item from a dropdown menu by visible text.
        :param locator: dropdown locator to which specific item to be selected
        :param text_to_select: text to be selected
        :return: returns nothing
        """
        if not text_to_select or text_to_select != '':
            select = Select(self.get_element(locator))
            select.select_by_visible_text(text_to_select)
        else:
            print(f'No selectable item found: {text_to_select}')

    def select_by_value(self, locator, value_to_select):
        """
        Select item from a dropdown menu by visible text.
        :param locator: dropdown locator to which specific item to be selected
        :param value_to_select: value to be selected
        :return: returns nothing
        """
        if not value_to_select or value_to_select != '':
            select = Select(self.get_element(locator))
            select.select_by_value(value_to_select)
        else:
            print(f'No selectable item found: {value_to_select}')

    def get_selected_text_from_dropdown(self, locator):
        """
        Returns the text for first selected option.
        :param locator: locator of the Select element.
        :return: returns text for first selected option.
        """
        select = Select(self.get_element(locator))
        return select.first_selected_option.text

    def get_mobile_element(self, driver, locator):
        return driver.find_element(by=locator['by'],value=locator['value'])


    def get_all_options_from_dropdown(self, locator):
        """
        Returns all visible texts as list from a dropdown specified by a locator.
        :param locator: locator for the dropdown.
        :return: a list of text for all options in the dropdown.
        """
        select = Select(self.get_element(locator))
        all_options_as_text = [option.text.strip() for option in select.options]
        return all_options_as_text

    def wait_for_expected_condition(self, condition, max_wait=5, poll_frequency=0.5):
        """
        Wait for specified time until provided CONDITION is met.
        :param condition: condition for which we must wait until specified amount of time
        :param max_wait: maximum time to wait for the CONDITION to be satisfied
        :return: nothing
        """
        wait = WebDriverWait(self.driver, max_wait, poll_frequency)
        wait.until(condition)

    def wait_for_existence_of(self, locator, max_wait=5):
        self.wait_for_expected_condition(
            EC.presence_of_element_located(locator), max_wait)

    def wait_for_existence_of_all(self, locator, max_wait=5):
        self.wait_for_expected_condition(
            EC.presence_of_all_elements_located(locator), max_wait)

    def wait_for_visibility_of(self, locator, max_wait=5, poll_frequency=0.5):
        """
        Wait for the visibility of an element located by specified locator until maximum time expire
        :param locator: the locator for which we need to wait
        :param max_wait: the time we need to wait for until the element is visible for the locator
        :return:
        """
        self.wait_for_expected_condition(
            EC.visibility_of_element_located(locator), max_wait, poll_frequency)

    def wait_for_visibility_and_invisibility_of(self, locator, max_wait=5):
        """
        Wait for the visibility and invisibility of an element located by specified locator until maximum time expire
        :param locator: the locator for which we need to wait
        :param max_wait: the time we need to wait for until the element is visible and invisible for the locator
        :return:
        """
        try:
            self.wait_for_expected_condition(
                EC.visibility_of_element_located(locator), max_wait)
        except:
            print("Element did not appear")
        try:
            self.wait_for_expected_condition(EC.invisibility_of_element_located(locator), max_wait)
        except:
            print("Element did not disappear")

    def wait_for_visibility_with_selector_type(self, selector_type, locator_text, max_wait=5):
        wait = WebDriverWait(self.driver, max_wait)
        if selector_type == By.ID:
            wait.until(EC.visibility_of_element_located((By.ID, locator_text)))
        elif selector_type == By.CSS_SELECTOR:
            wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, locator_text)))
        elif selector_type == By.XPATH:
            wait.until(EC.visibility_of_element_located(
                (By.XPATH, locator_text)))
        elif selector_type == By.LINK_TEXT:
            wait.until(EC.visibility_of_element_located(
                (By.LINK_TEXT, locator_text)))
        else:
            raise Exception('No such type found!')

    def wait_for_invisibility_of(self, locator, max_wait=5):
        """
        Wait for the invisibility of an element located by specified locator until maximum time expire
        :param locator: the locator for which we need to wait
        :param max_wait: the time we need to wait for until the element is invisible for the locator
        :return: returns nothing
        """
        self.wait_for_expected_condition(
            EC.invisibility_of_element_located(locator), max_wait)

    def wait_for_visibility_of_text(self, locator, text, max_wait=5):
        self.wait_for_expected_condition(
            EC.text_to_be_present_in_element(locator, text), max_wait)
        return True

    def wait_for_invisibility_of_text(self, locator, text, max_wait=5):
        self.text_to_be_not_present_in_locator(locator, text, max_wait)

    def text_to_be_not_present_in_locator(self, locator, text, second):
        """ An expectation for checking if the given text is present in the
        specified element.
        locator, text
        """
        for _ in range(second):
            try:
                if text not in self.get_text_by_locator(locator):
                    return True
            except Exception as e:
                print('An exception occurred:', e)
            time.sleep(1)
        return False

    def text_to_be_present_in_web_element(self, element, text_, second):
        """ An expectation for checking if the given text is present in the
        specified element.
        locator, text
        """
        result = False
        for x in range(0, second):
            try:
                element_text = element.text
                print(element_text)
                result = text_ in element_text
                if result:
                    break
            except StaleElementReferenceException:
                print('not present yet')

            time.sleep(1)

        return result

    def wait_for_element_to_clickable(self, locator, max_wait=5):
        self.wait_for_expected_condition(
            EC.element_to_be_clickable(locator), max_wait)

    def wait_for_element_count_to_be(self, locator, expected_count, max_wait=5):
        expected_condition = ElementCountToBeEqual(locator, expected_count)
        self.wait_for_expected_condition(expected_condition, max_wait)

    def wait_for_element_count_to_be_equal_or_greater(self, locator, expected_count, max_wait=5):
        expected_condition = ElementCountToBeEqualOrGrater(locator, expected_count)
        self.wait_for_expected_condition(expected_condition, max_wait)

    def wait_for_attribute_to_be(self, locator, attribute, attribute_value, max_wait=5):
        condition = ElementAttributeToBe(locator, attribute, attribute_value)
        self.wait_for_expected_condition(condition, max_wait)

    def is_displayed(self, locator):
        return self.get_element(locator).is_displayed()

    def is_element_visible(self, locator, wait_time=5, poll_frequency=0.5):
        """
        Checks for an element for its visibility & return True if it's visible.
        :param locator: locator for the element to wait for visibility.
        :param wait_time: maximum wait time for the element's visibility.
        :return: True/False
        """
        try:
            self.wait_for_visibility_of(locator, wait_time, poll_frequency)
        except TimeoutException as toe:
            return False
        return True

    def is_text_proper(self, locator, expected_text):
        actual_text = self.get_text_by_locator(locator, 5)
        print(actual_text)
        return actual_text == expected_text
      
    def is_element_enable(self, locator, wait_time=20):
        """
        Checks for an element for its enable state & return True if it's enable.
        :param locator: locator for the element.
        :param wait_time: maximum wait time for the element's existence.
        :return: True/False
        """

        try:
            return self.get_element(locator, wait_time).is_enabled()
        except TimeoutException as toe:
            return False
    def is_text_proper(self, locator, expected_text):
        actual_text = self.get_text_by_locator(locator, 5)
        print(actual_text)
        return actual_text == expected_text

    def is_element_selected(self, locator, wait_time=3):
        """
        Checks for an element for its selected state & return True if it's enable.
        :param locator: locator for the element.
        :param wait_time: maximum wait time for the element's existence.
        :return: True/False
        """

        try:
            value = self.get_element(locator, wait_time).get_attribute("value")
            if value == '1':
                return True
            else:
                return False
        except (TimeoutException, AttributeError)as toe:
            print("Element or Attribute value not found")
            return False

    def select_item_from_selection_list(self, locator, expected_item):
        selection_items = self.get_elements(locator)
        for item in selection_items:
            if self.get_text_by_element(item) == expected_item:
                item.click()
                print(f'Selection item {expected_item.upper()} selected.')
                break

    def get_pseudo_element_property_value(self, locator, expected_pseudo_element, expected_pseudo_property):
        js_script = f"return window.getComputedStyle(document.querySelector('{locator}'),':{expected_pseudo_element}').getPropertyValue('{expected_pseudo_property}')"
        return self.driver.execute_script(js_script)

    def get_js_executed_result(self, element_identifier, type):
        js_script = f"return document.querySelector('{element_identifier}').{type};"
        return self.driver.execute_script(js_script)

    def scroll_into_view(self, locator):
        element = self.get_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait_for_visibility_of(locator, 5)
        print('Element should be in view')

    def scroll_into_view_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def drag_item_by_offset(self, source_locator, x_offset, y_offset):
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(self.get_element(source_locator), x_offset, y_offset).perform()
        time.sleep(1)

    def click_element_by_offset(self, locator, x_offset, y_offset):
        element = self.get_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element, x_offset, y_offset).click().perform()

    def use_keyboard_shortcut(self, key):
        actions = ActionChains(self.driver)
        actions.key_down(Keys.LEFT_CONTROL).key_down(Keys.LEFT_ALT) \
            .send_keys(key).key_up(Keys.LEFT_CONTROL).key_up(Keys.LEFT_ALT).perform()

    def perform_double_click_on(self, locator):
        actions = ActionChains(self.driver)
        actions.double_click(self.get_element(locator)).perform()

    def perform_right_click_on(self, element):
        """
        Performs a right click/context click on a desired element by its locator.
        :param element: locator of the desired element.
        :return: None
        """
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()

    def close_current_window(self):
        self.driver.close()
        print('Focused window closed...')

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def switch_to_window(self, window_identifier=1):
        """
        Switches to window by its position or window handle. First window position is 1, second window position is 2 etc.
        :param window_identifier: position of the window or window handle
        """
        if type(window_identifier) == int:
            self.driver.switch_to.window(self.driver.window_handles[window_identifier - 1])
        elif type(window_identifier) == str:
            self.driver.switch_to.window(window_identifier)
        else:
            print('Invalid window type provided...')

    def scroll_to_element(self, element):
        self.driver.execute_script('mobile: scroll', {'direction': 'down', "element": element, "toVisible": True})

    def scroll_to_locator(self, locator):
        element = self.get_element(locator)
        self.scroll_to_element(element)

    def is_visible(self, element):
        element = self.wait.until(EC.visibility_of(element))
        return bool(element)

    def get_last_element(self, by_locator):
        elements = self.get_elements(by_locator)
        # print(elements)
        if len(elements) > 0:
            return elements[-1]
        
    def get_first_element(self, by_locator):
        elements = self.get_elements(by_locator)
        if len(elements) > 0:
            return elements[0]

    def scroll_to(self, by_origin, by_destination):
        self.driver.scroll(self.driver.find_element(*by_origin), self.driver.find_element(*by_destination))

    def swipe_to(self, start_x, start_y, end_x, end_y):
        self.driver.swipe(start_x, start_y,end_x, end_y)

    def swipe_down(self):
        screen_dimensions = self.driver.get_window_size()
        self.swipe_to(screen_dimensions["width"] * 0.5, screen_dimensions["height"] * 0.6, screen_dimensions["width"] * 0.5, screen_dimensions["height"] * 0.5)

    def swipe_up(self):
        screen_dimensions = self.driver.get_window_size()
        self.swipe_to(screen_dimensions["width"] * 0.5, screen_dimensions["height"] * 0.6, screen_dimensions["width"] * 0.5, screen_dimensions["height"] * 0.7)

    def swipe_on_element(self, by_locator, direction):
        element = self.get_element(by_locator)
        self.driver.execute_script("mobile: swipe", {"direction": direction, "element": element})
    
    def swipe_on_last_element(self, by_locator, direction):
        element = self.get_last_element(by_locator)
        self.driver.execute_script("mobile: swipe", {"direction": direction, "element": element})

    def scroll_down(self):
        self.driver.execute_script("mobile: scroll", {"direction": "down"})

    def scroll_up(self):
        self.driver.execute_script("mobile: scroll", {"direction": "up"})

    def scroll_right(self, element):
        self.driver.execute_script("mobile: scroll", {"direction": "right", "element": element})

    def scroll_left(self, element):
        self.driver.execute_script("mobile: scroll", {"direction": "left", "element": element})

    def scroll_to_get_element(self, by_locator ):
        # screen_dimensions = self.driver.get_window_size()
        # location_x = screen_dimensions["width"] * 0.5
        # location_start_y = screen_dimensions["height"] * 0.6
        # location_end_y = screen_dimensions["height"] * 0.5
        # location_end_y_a = screen_dimensions["height"] * 0.7
        # actions = ActionChains(self.driver)
        max = 20
        while not self.is_element_visible(by_locator, 3) and max > -20:
            if max > 0:
                self.swipe_down()
                #wait_for(2)
                max -= 1
            elif max <= 0:
                self.swipe_up()
                max -= 1
                #wait_for(2)
        return self.get_element(by_locator)

    def is_clickable(self, by_locator, max_wait=5):
        try:
            self.wait_for_expected_condition(EC.element_to_be_clickable(by_locator), max_wait)
        except TimeoutException:
            return False
        return True
    
    def is_element_clickable(self, element, max_wait=5):
        try:
            WebDriverWait(self.driver, max_wait).until(lambda driver: element.is_enabled() and element.is_displayed())
        except TimeoutException:
            return False
        return True

    

    def get_child_element(self, parent_element, child_locator):
        try:
            parent_element.find_element(*child_locator)
        except:
            print("Child element is not found")
            return False
        return parent_element.find_element(*child_locator)

    def get_child_element_by_locator(self, parent_locator, child_locator):
        return self.get_child_element(self.get_element(parent_locator), child_locator)

    def wait_for_an_alert(self, max_wait=5):
       return WebDriverWait(self.driver, max_wait).until(EC.alert_is_present())

    def is_wifi_enabled(self):
        WIFI_OPTION_SETTINGS = (AppiumBy.ACCESSIBILITY_ID,'Wi-Fi')
        self.driver.activate_app('com.apple.Preferences')  # opens settings
        time.sleep(1)
        wifi_status = self.get_attribute(WIFI_OPTION_SETTINGS,'value')
        if wifi_status == 'Off':
            print("Wifi is disabled")
            return False
        else:
            print("Wifi is enabled")
            return True

    def turn_on_wifi(self,navigate_back_to_app: bool = True):
        
        if self.is_wifi_enabled() == True:
            print("Wifi already turned on!")
        else:
            self.driver.find_element("xpath",'//XCUIElementTypeCell[@name="Wi-Fi"]').click()
            try:
                self.driver.find_element("xpath",'//XCUIElementTypeCell[@name="Wi-Fi"]').click()  # click on WiFi 
            except:
                pass
            time.sleep(1)

            # driver.find_element("xpath",'//XCUIElementTypeSwitch[@name="Wi‑Fi"]').click()  # click on the WiFi switch
            self.driver.find_element("xpath",'//XCUIElementTypeSwitch').click()
            self.driver.find_element("xpath",'//XCUIElementTypeButton[@name="Settings"]').click()
            print('Wifi is now turned on!')
        if navigate_back_to_app:
            self.open_the_app()  # back to your app

    def turn_off_wifi(self,navigate_back_to_app: bool = True):

        if self.is_wifi_enabled() == False:
            print("Wifi already turned off!")
        else:
            self.driver.find_element("xpath",'//XCUIElementTypeCell[@name="Wi-Fi"]').click()
            try:
                self.driver.find_element("xpath",'//XCUIElementTypeCell[@name="Wi-Fi"]').click()  # click on WiFi 
            except:
                pass
            time.sleep(1)

            # driver.find_element("xpath",'//XCUIElementTypeSwitch[@name="Wi‑Fi"]').click()  # click on the WiFi switch
            self.driver.find_element("xpath",'//XCUIElementTypeSwitch').click()
            self.driver.find_element("xpath",'//XCUIElementTypeButton[@name="Settings"]').click()
            print('Wifi is now turned off!')
        if navigate_back_to_app:
            self.open_the_app()  # back to your app


    def change_frame(self, frame_identifier, max_wait=60):
        if isinstance(frame_identifier, int):
            self.driver.switch_to.frame(self.get_elements((By.TAG_NAME, 'iframe'))[frame_identifier])
            print(f'Frame switched by using id/index {frame_identifier}...')
        elif isinstance(frame_identifier, str):
            self.wait_for_expected_condition(EC.frame_to_be_available_and_switch_to_it((By.ID,
                                                                                        frame_identifier)), max_wait)
            print(f'Frame switched by using ID {frame_identifier}...')
        else:
            self.wait_for_expected_condition(
                EC.frame_to_be_available_and_switch_to_it(self.get_element(frame_identifier)), max_wait)
            print(f'Frame switched by using locator {frame_identifier}...')
        time.sleep(2)

    def text_to_be_present_in_locator(self, locator, text, second):
        """ An expectation for checking if the given text is present in the
        specified element.
        locator, text
        """
        result = False
        for _ in range(0, second):
            try:
                element_text = self.get_text_by_locator(locator)
                result = text in element_text
                if result:
                    break
            except:
                print('not present yet')

            time.sleep(1)

        return result
    
    def is_text_present_in_locator(self, locator, text, second):
        """ An expectation for checking if the given text is present in the
        specified element.
        locator, text
        """
        result = False
        for _ in range(0, second):
            try:
                element_text = self.get_text_by_locator(locator,0)
                result = text in element_text
                if result:
                    break
            except:
                pass
            time.sleep(1)
        return result
    
    def is_switch_button_selected(self, locator):
        return self.get_attribute(locator, 'selected')
    
    # def wake_up_screen_from_dimmed_state(self):
    #     action = ActionChains(self.driver)
    #     action.press(x=500, y=200).release().perform()
    #     time.sleep(1)
    #     print('Touch action performed, display should be undimmed')
    
    # def wake_up_screen_from_dimmed_state(self):
    #     # Initialize the ActionChains object
    #     actions = ActionChains(self.driver)

    #     # Create a pointer input instance for touch actions
    #     touch_input = PointerInput(POINTER_TOUCH, "touch")

    #     # Chain the actions to tap on the screen at the specified coordinates
    #     actions.w3c_actions = touch_input
    #     actions.w3c_actions.pointer_action.move_to_location(500, 200)
    #     actions.w3c_actions.pointer_action.pointer_down()
    #     actions.w3c_actions.pointer_action.pointer_up()
      

    #     # Perform the actions
    #     actions.perform()

    #     time.sleep(1)
    #     print('Touch action performed, display should be undimmed')

    def get_list_of_attributes_from_locator(self, by_locator, attribute):
        """
        Returns a specific attribute values for all elements found by given locator.

        Args:
            by_locator (_type_): the locator for which elements to be found.
            attribute (_type_): the attribute needs to find the value for.

        Returns:
            list: a list of values of the specified attribute.
        """
        elements = self.get_elements(by_locator)
        list_of_values = [element.get_attribute(attribute).strip() for element in elements]
        return list_of_values
    
    def open_the_app(self):
        print(f'_____________com.augmedix.Lynx.{pytest.bundle_id_env}______________')
        self.driver.activate_app(f'com.augmedix.Lynx.{pytest.bundle_id_env}')
        time.sleep(1)

    def close_the_app(self):
        self.driver.terminate_app(f'com.augmedix.Lynx.{pytest.bundle_id_env}')
        time.sleep(1)
    
    def send_app_to_background(self, time_in_seconds):
        self.driver.background_app(time_in_seconds)

    # def adjust_ios_time_picker(self, hours_order=None, hours_offset=0.7, 
    #                        minutes_order=None, minutes_offset=0.7, 
    #                        am_pm_order=None, am_pm_offset=0.7):
    #     """
    #     Adjusts the iOS time picker wheels based on the provided scrolling order and offset.

    #     :param hours_order: Scrolling direction for the hours picker ('next' or 'previous').
    #     :param hours_offset: Offset value for the hours picker scroll.
    #     :param minutes_order: Scrolling direction for the minutes picker ('next' or 'previous').
    #     :param minutes_offset: Offset value for the minutes picker scroll.
    #     :param am_pm_order: Scrolling direction for the AM/PM picker ('next' or 'previous').
    #     :param am_pm_offset: Offset value for the AM/PM picker scroll.
    #     """

    #     # Locate the picker wheels (adjust locators as needed)
    #     hours_picker = self.driver.find_element("xpath", "//XCUIElementTypePickerWheel[1]")
    #     minutes_picker = self.driver.find_element("xpath", "//XCUIElementTypePickerWheel[2]")
    #     ampm_picker = self.driver.find_element("xpath", "//XCUIElementTypePickerWheel[3]")

    #     # Adjust hours if the order is provided
    #     if hours_order:
    #         self.driver.execute_script('mobile: selectPickerWheelValue', {
    #             'element': hours_picker,
    #             'order': hours_order,
    #             'offset': hours_offset
    #         })

    #     # Adjust minutes if the order is provided
    #     if minutes_order:
    #         self.driver.execute_script('mobile: selectPickerWheelValue', {
    #             'element': minutes_picker,
    #             'order': minutes_order,
    #             'offset': minutes_offset
    #         })

    #     # Adjust AM/PM if the order is provided
    #     if am_pm_order:
    #         self.driver.execute_script('mobile: selectPickerWheelValue', {
    #             'element': ampm_picker,
    #             'order': am_pm_order,
    #             'offset': am_pm_offset
    #         })

    def adjust_ios_time_picker(self, hours_order=None, hours_offset=0.15, 
                           minutes_order=None, minutes_offset=0.15, 
                           am_pm_order=None, am_pm_offset=0.15):
        """
        Adjusts the iOS time picker wheels based on the provided scrolling order and offset.
        Increases the hour if minutes overflow past 59.

        :param hours_order: Scrolling direction for the hours picker ('next' or 'previous').
        :param hours_offset: Offset value for the hours picker scroll.
        :param minutes_order: Scrolling direction for the minutes picker ('next' or 'previous').
        :param minutes_offset: Offset value for the minutes picker scroll.
        :param am_pm_order: Scrolling direction for the AM/PM picker ('next' or 'previous').
        :param am_pm_offset: Offset value for the AM/PM picker scroll.
        """

        # Locate the picker wheels (adjust locators as needed)
        hours_picker = self.driver.find_element("xpath", "//XCUIElementTypePickerWheel[1]")
        minutes_picker = self.driver.find_element("xpath", "//XCUIElementTypePickerWheel[2]")
        ampm_picker = self.driver.find_element("xpath", "//XCUIElementTypePickerWheel[3]")

        # Helper function to get the current value of a picker wheel
        def get_picker_value(picker):
            # Extract the numeric part of the value using regular expressions
            import re
            value_text = picker.get_attribute("value")
            numeric_part = re.search(r'\d+', value_text)  # Find the first numeric part in the string
            return int(numeric_part.group()) if numeric_part else 0  # Return the numeric part or 0 if not found


        # Adjust minutes if the order is provided
        if minutes_order:
            initial_minutes_value = get_picker_value(minutes_picker)
            self.driver.execute_script('mobile: selectPickerWheelValue', {
                'element': minutes_picker,
                'order': minutes_order,
                'offset': minutes_offset
            })
            final_minutes_value = get_picker_value(minutes_picker)

            # Check if minute overflow occurred
            if minutes_order == 'next' and final_minutes_value < initial_minutes_value:
                hours_order = 'next'
            elif minutes_order == 'previous' and final_minutes_value > initial_minutes_value:
                hours_order = 'previous'

        # Adjust hours if the order is provided
        if hours_order:
            self.driver.execute_script('mobile: selectPickerWheelValue', {
                'element': hours_picker,
                'order': hours_order,
                'offset': hours_offset
            })

        # Adjust AM/PM if the order is provided
        if am_pm_order:
            self.driver.execute_script('mobile: selectPickerWheelValue', {
                'element': ampm_picker,
                'order': am_pm_order,
                'offset': am_pm_offset
            })

    # Function to check if two rectangles overlap
    def is_overlapping(self,locator_1, locator_2):
        # Locate the UI elements
        element1 = self.get_element(locator_1,10)
        element2 = self.get_element(locator_2,10)

        # Get the location and size of both elements
        try:
            location1 = element1.location
            size1 = element1.size
            location2 = element2.location
            size2 = element2.size
        except StaleElementReferenceException:
            element1 = self.get_element(locator_1,10)
            element2 = self.get_element(locator_2,10)
            location1 = element1.location
            size1 = element1.size
            location2 = element2.location
            size2 = element2.size

        # Calculate the bounding boxes of both elements
        box1 = {
            'x1': location1['x'],
            'y1': location1['y'],
            'x2': location1['x'] + size1['width'],
            'y2': location1['y'] + size1['height']
        }

        box2 = {
            'x1': location2['x'],
            'y1': location2['y'],
            'x2': location2['x'] + size2['width'],
            'y2': location2['y'] + size2['height']
        }
        # Check if one rectangle is to the left of the other
        if box1['x2'] <= box2['x1'] or box2['x2'] <= box1['x1']:
            return False

        # Check if one rectangle is above the other
        if box1['y2'] <= box2['y1'] or box2['y2'] <= box1['y1']:
            return False

        # If neither condition is met, the rectangles overlap
        return True

    def is_keyboard_open(self):
        return self.driver.is_keyboard_shown()

    def reset_app(self):
        self.close_the_app()
        self.open_the_app()
