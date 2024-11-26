"""
Used to set up test configurations and store/modify the testcases that are used
by test functions/methods.
"""

import datetime
import glob
import logging
import importlib
import json
import os
import re
import shutil
import sys
import requests
from requests.auth import HTTPBasicAuth
import allure
import pytest
from _pytest.mark import Mark, MarkDecorator
from allure_commons.types import AttachmentType
from appium import webdriver as appium_driver
from appium.options.ios import XCUITestOptions
from cryptography.fernet import Fernet, InvalidToken
from jproperties import Properties
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.common.exceptions import WebDriverException
import time
from test.ui.utils.app_constants import AppConstant
from test.ui.utils.config_parser import ConfigParser
from test.ui.utils.google_drive_manager import GoogleDriveManager
from test.ui.utils.lambdatest_manager import LambdaManager
from appium.webdriver.common.appiumby import AppiumBy
from test.ui.utils.helper import get_formatted_date_str, generate_random_string


class Unmarker:
    """
    Return MarkDecorator object.
    """
    def __getattr__(self, item):
        # Return a marker remover
        if item[0] == '_':
            raise AttributeError('Marker name must NOT start with underscore')
        return MarkDecorator(Mark(f'unmark:{item}', args=(), kwargs={}))


class Fauxcals:
    """
    SHould work with the eval() as the set of 'locals'. Will return
    true for any item keyword that begins with unmark. This should only work for
    marks set by 'unmarker', because you can't do `@pytest.mark.namewith:colon`.
    """
    def __init__(self, keywords):
        self.keys = [key.split(':')[1] for key in keywords if 'unmark:' in key]

    def __getitem__(self, item):
        return item in self.keys


@pytest.hookimpl(trylast=True)
def pytest_configure(config):   # pylint: disable=too-many-locals, too-many-statements
    env = config.getoption('--env').lower()
    url = config.getoption('--url')
    browser = config.getoption('--browser')
    marker = config.getoption('-m')
    platform_name = config.getoption('--platform-name')
    device_name = config.getoption('--device-name')
    device_os_version = config.getoption('--device-os-version')
    alluredir = config.getoption('--alluredir') or 'TestResults/allure-reports'
    #browser_version = config.getoption("browser_version")


    set_skipped_test(config)

    configs = ConfigParser()

    if env is None or env == 'dev':
        configs.add_file(AppConstant.DEV_CONFIG)
        pytest.conf = AppConstant.DEV_CONFIG
        pytest.env = env
        pytest.bundle_id_env = env
    elif env in ('stage', 'staging'):
        configs.add_file(AppConstant.STAGING_CONFIG)
        pytest.conf = AppConstant.STAGING_CONFIG
        pytest.env = 'staging'
        pytest.bundle_id_env = pytest.env
    elif env in ('prod', 'production', 'live'):
        configs.add_file(AppConstant.PRODUCTION_CONFIG)
        pytest.conf = AppConstant.PRODUCTION_CONFIG
        pytest.env = 'prod'
        pytest.bundle_id_env = 'ed'
    else:
        sys.exit('Invalid option. Please provide either of the following values:'
                 ' dev, staging, production...')

    if device_name == 'ios_device':
        configs.add_file(AppConstant.IOS_REAL_DEVICE_CONFIG)
        pytest.conf = AppConstant.IOS_REAL_DEVICE_CONFIG
        pytest.device = device_name
    elif device_name == "ios_simulator" or device_name == 'ios_emulator':
        configs.add_file(AppConstant.IOS_SIMULATOR_CONFIG)
        pytest.conf = AppConstant.IOS_SIMULATOR_CONFIG
        pytest.device = device_name

    configs.add_file(AppConstant.SYSTEM_CONFIG)
    configs.add_file(AppConstant.TESTRAIL_CONFIG)
    configs.add_file(AppConstant.ALLURE_ENV_FILE)
    configs.add_file(AppConstant.LAMBDATEST_CONFIG)
    configs.add_file(AppConstant.JIRA_CONFIG)
    configs.add_file(AppConstant.DATA_CONFIG)
    configs.add_file(AppConstant.JENKINS_CONFIG)

    pytest.marker = marker
    configs.load_configs()

    if url is not None:
        configs.set_config('url', url)

    # browser_version = config.getoption('--browser-version') or configs.get_config('browser_version')
    
    #   Load & set environment variables
    env_var_prefix = configs.get_config('environment_variable_prefix')

    env_vars = os.environ
    secret_key = os.environ.get('SECRET_KEY')
    cipher = Fernet(secret_key)

    for key, value in env_vars.items():
        if key.startswith(env_var_prefix):
            truncated_key = key.replace(env_var_prefix, '').lower()
            try:
                decrypted_value = cipher.decrypt(str.encode(value)).decode()
                configs.set_config(truncated_key, decrypted_value)
            except InvalidToken:
                print(f'Key {key} is encrypted with invalid token.')

    # Other settings is cached here
    pytest.configs = configs
    pytest.browser = browser
    pytest.platform_name = platform_name
    pytest.device_name = device_name
    pytest.device_os_version = device_os_version
    pytest.url = configs.get_config('url')
    pytest.report_title = config.getoption('--report-title')
    pytest.run_skipped = config.getoption('--run-skipped')
    pytest.enable_jenkins = config.getoption('--enable-jenkins')
    pytest.apk_version = config.getoption('--apk-version')
    pytest.check_complaints = config.getoption('--check-complaints')
    pytest.run_locally = config.getoption('--run-locally')
    pytest.reset_complaint_and_elements = config.getoption('--reset-complaints-elements')
    pytest.alluredir = alluredir
    pytest.admin_url = pytest.configs.get_config('admin_base_url')
    pytest.unmark = Unmarker()
    pytest.browser_version = config.getoption("browser_version")


def pytest_collection_modifyitems(config, items):   # pylint: disable=too-many-locals
    """
    Modifies the collected test cases by adding skip marker. Test case lists are read from
    'skipped_testcases.properties' file under 'resources' folder. Test cases are listed as key
    & associated comments are placed as the value of that particular test case.
    """
    skipped_list = re.split(r'\s+', config.getoption('--skip-list'))

    with open(AppConstant.SKIPPED_TESTCASES_FILE, 'rb') as skipped_tcs_file, \
            open(AppConstant.XFAILED_TESTCASES_FILE, 'rb') as xfailed_tcs_file:

        skipped_config = Properties()
        xfailed_config = Properties()

        skipped_config.load(skipped_tcs_file)
        xfailed_config.load(xfailed_tcs_file)

        skipped_tcs = get_dict_from_loaded_config(skipped_config)
        xfailed_tcs = get_dict_from_loaded_config(xfailed_config)

        ignoring_item_set = set()

    matchexpr = config.option.markexpr

    remaining = []
    deselected = []

    for item in items:
        test_module, _, _ = item.nodeid.split('::')
        test_module_name = test_module.split('/')[-1]
        if test_module_name in skipped_list:
            ignoring_item_set.add(test_module)

            config.__dict__['option'].ignore = list(ignoring_item_set)

        if pytest.run_skipped == 'no':
            add_marker_to_test(item, skipped_tcs, 'skip')
        add_marker_to_test(item, xfailed_tcs, 'xfail')

        # modifying DOCSTRING for each of the test cases in a module/suite.
        test_module_name = '/'.join(item.nodeid.split('::')[0].split('.')[0].split('/')[1:])
        try:
            with open(f'{AppConstant.TEST_STEPS_FOLDER}/{test_module_name}.json',
                      encoding='utf-8') as step_file:
                test_steps_in_json_file = json.load(step_file)

            test_case_steps = test_steps_in_json_file.get(item.obj.__name__, '')
            if isinstance(test_case_steps, list):
                test_case_steps = '\n'.join(test_case_steps)

            setattr(item.obj.__func__, '__doc__', test_case_steps)
        except FileNotFoundError:
            print(f'No such file: {test_module_name}.json.')

        if matchexpr:
            if eval(matchexpr, {}, Fauxcals(item.keywords)):    # pylint: disable=eval-used
                print(f'Deselecting {item!r} (mark removed by @pytest.unmark)')
                deselected.append(item)
                continue
        remaining.append(item)

    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = remaining


def pytest_sessionfinish(session):
    failed_test_list = []
    for item in session.items:
        if hasattr(item, 'rep_call') and item.rep_call.outcome == 'failed':
            failed_test_list.append(item.nodeid.split('::')[0])

    if failed_test_list:
        last_failed_testcases_file = f'{AppConstant.RESOURCE_FOLDER}/' \
                                     f'scp_failed_test_{pytest.marker.upper()}.properties'
        with open(last_failed_testcases_file, 'w', encoding='utf-8'):
            failed_tests_as_arguments = ' '.join(set(failed_test_list))
            configs = ConfigParser()
            configs.update_config('env', pytest.env, config_path=last_failed_testcases_file)
            configs.update_config('url', pytest.url, config_path=last_failed_testcases_file)
            configs.update_config('testtype', pytest.marker,
                                  config_path=last_failed_testcases_file)
            configs.update_config('run_skipped', pytest.run_skipped,
                                  config_path=last_failed_testcases_file)
            configs.update_config('failed_tcs', failed_tests_as_arguments,
                                  config_path=last_failed_testcases_file)


def get_scp_driver():
    """
    Initialize driver & yield it to currently running test suite. If any suite uses @pytest.mark.no_auto
    mark then no driver will be returned.
    """
    # if 'no_auto' in request.keywords:
    #     yield
    #     return
    try:
        print(f'Enable Jenkins: {pytest.enable_jenkins}')
        # Initialize the browser driver
        scp_driver = get_requested_browser(pytest.browser)
        
        # Check if WebDriver was successfully created
        if scp_driver is None:
            raise WebDriverException("Failed to create WebDriver instance.")
        
        # Open the URL in the browser
        scp_driver.get(pytest.url)
        print("URL opened: ", pytest.url)
        
        # Check if the driver has a valid session ID (indicating the browser is open)
        if not scp_driver.session_id:
            raise WebDriverException("Chrome browser session failed to start.")
        
        # Log the browser version
        browser_version = scp_driver.capabilities.get('browserVersion')
        os.environ['browser_version'] = browser_version
        print(f'Browser opened, version: {browser_version}')
        scp_driver.save_screenshot("headless_view.png")
        print(scp_driver.page_source)
        return scp_driver
    
    except WebDriverException as e:
        print(f"Error opening Chrome Driver: {str(e)}")
        return None

@pytest.fixture(scope='class', autouse=True)
def init_device(request):
    if 'no_auto' in request.keywords:
        yield
        return

    _appium_driver = get_selected_device()
    
    request.cls.appium_driver =_appium_driver
    print(f"Appium driver initialized for {request.cls.__name__}")
    yield _appium_driver


@pytest.fixture(scope='class', autouse=True)
def init_page_objects(request, init_device):    # pylint: disable=unused-argument, too-many-locals, redefined-outer-name
    with open(AppConstant.PAGE_OBJECTS_CONFIG_FILE, 'r', encoding='utf-8') as file:
        module_info_list = file.readlines()
        for module_info in module_info_list:
            if '#' not in module_info and module_info != '':
                object_name, fully_qualified_module_name = module_info.split('=')
                module_name = fully_qualified_module_name.split('.')[-1].replace('\n', '')
                package_name = '.'.join(['pages'] + fully_qualified_module_name.split('.')[:-1])

                module = importlib.import_module(f'.{module_name}', package=package_name)
                class_name = ''.join(map(lambda item: item.title().strip(),
                                         fully_qualified_module_name.split('.')[-1].split('_')))
                current_fully_qualified_test_module = '.'.join(
                    str(request.cls).replace('<class \'', '').split('.')[:-1])
                current_test_module = current_fully_qualified_test_module\
                    .rsplit('.', maxsplit=1)[-1]
                current_test_package = '.'.join(current_fully_qualified_test_module
                                                .rsplit('.', maxsplit=1)[:-1])
                current_test_class = request.cls.__name__
                current_object = getattr(importlib.import_module(f'.{current_test_module}',
                                                                 package=current_test_package), current_test_class)
                try:
                    page_object = getattr(module, class_name)(request.cls.appium_driver)
                    setattr(current_object, object_name, page_object)
                except AttributeError as attribute_error:
                    print(f'Attribute \'{attribute_error.name}\' not found for {attribute_error.obj.__name__}.')


@pytest.fixture(scope='class', name='marker', autouse=True)
def get_marker(request):
    """
    Used to indentify testing type from test cases.
    """

    request.cls.is_regression = pytest.marker == 'regression'


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, 'result', rep)


@pytest.fixture(scope='function', autouse=True)
def failed_page(request):

    yield

    feature_type = request.node.result.when
    feature_outcome = request.node.result.outcome
    if feature_outcome == 'failed':
        allure.attach(request.cls.appium_driver.get_screenshot_as_png(),
                      name=f'Screenshot for failed {"TESTCASE" if feature_type == "call" else feature_type.upper()}',
                      attachment_type=AttachmentType.JPG)

        console_log = ''
        for entry in request.cls.appium_driver.get_log('server'):
            console_log = f'console_log\n{entry}'
        allure.attach(console_log, name='Console Log', attachment_type=AttachmentType.TEXT, extension='.txt')


@pytest.fixture(scope='session', autouse=True)
def update_allure_environment_configs():
    """
    Provides environment specific information if the tests are run on Jenkins.
    """
    yield
    env_configs = ConfigParser()
    env_configs.update_config('Browser', pytest.browser.title(), AppConstant.ALLURE_ENV_FILE)
    env_configs.update_config('BrowserVersion',
                              str(os.environ.get('browser_version')), AppConstant.ALLURE_ENV_FILE)
    env_configs.update_config('Env', pytest.env.title(), AppConstant.ALLURE_ENV_FILE)
    env_configs.update_config('TestType', pytest.marker.title(), AppConstant.ALLURE_ENV_FILE)
    env_configs.update_config('reportName', 'Augmedix TestReport', AppConstant.ALLURE_ENV_FILE)

    shutil.copy2(AppConstant.ALLURE_ENV_FILE, pytest.alluredir)


# @pytest.fixture(scope='session', autouse=True)
def delete_lambdatest_apps():
    lambdatest_manager = LambdaManager()
    lambdatest_manager.delete_apps()


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='dev', help='env: dev, staging, prod/live or dr')
    parser.addoption('--url', action='store',
                     help='url: dev, staging, production or dr url. If it is provided this value will '
                          'override the value provided by config file.')
    parser.addoption('--browser-version', action='store',
                     help='browser-version: 116/117/118/119/120. Used for selecting '
                          'chrome browser version to execute test cases.')
    parser.addoption('--testrail-report', action='store', default='off',
                     help='testrail-status: on/off. Used for updating status on TestRail.')
    parser.addoption('--browser', action='store', default='chrome',
                     help='browser: chrome/firefox/headless-chrome. Used for browser selection,')
    parser.addoption('--repeat', action='store', type=int, default=1, help='Run eah test specified number of times.')
    parser.addoption('--report-title', action='store', default='ScribePortal Automation Report')
    parser.addoption('--run-skipped', action='store', default='no',
                     help='Enable skipped test cases.')
    parser.addoption('--enable-jenkins', action='store', default='no',
                     help='Enable running from local machine/Jenkins.'
                          ' --enable-jenkins=no by default.')
    parser.addoption('--skip-list', action='store', default='', help='Path to module/package to skip.')
    parser.addoption('--check-complaints', action='store', default='no',
                     help='Check complaints data before execute tests')
    parser.addoption('--run-locally', action='store', default='no',
                     help='Running code locally using either simulator or lambda-test real device.'
                          ' If \'no\' is selected then test will be run on simulator.')
    parser.addoption('--platform-name', action='store', default='iOS', help='Device Type i.e.: Android/iOS.')
    parser.addoption('--device-name', action='store', default='ios_device',
                     help='Device to use for running LiveApp tests.')
    parser.addoption('--device-os-version', action='store', default='12',
                     help='OS version of the device to use for running LiveApp tests.')
    parser.addoption('--reset-complaints-elements', action='store', default='no',
                     help='Deletes existing complaints & elements & creates new complaints with elements')
    parser.addoption('--apk-version', action='store', default='',
                     help='Desired apk version to be downloaded')
    parser.addoption('--device_version', action='store', default='', help='Desired apk version to be downloaded')
    parser.addoption('--default-dataset', action='store', default='yes', help='Select user dataset to test with.')


def get_next_ipa_folder_from_gd(env_dict, value_iterator, key_iterator, gdm):
    while len(env_dict) == 0:
        try:
            # Get the next value from the iterators
            version_folder_id = next(value_iterator)
            apk_version_in_gd = next(key_iterator)

            # Retrieve list of files by the folder ID
            env_dict = gdm.get_list_of_files_by_id(version_folder_id)

            return version_folder_id, apk_version_in_gd, env_dict
        except StopIteration:
            # If either iterator is exhausted, return None or handle the end of the iteration gracefully
            print("No more items to iterate.")
            return None, None, None


def get_requested_browser(requested_browser_name='chrome'):
    # Initialize driver as None
    driver = None

    if requested_browser_name == 'chrome':
        # Running in Jenkins with Selenium Grid
        if pytest.enable_jenkins == 'yes':
            selenium_grid = pytest.configs.get_config('selenium_grid_url')
            
            # Setup Chrome options for headless and other configurations
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('headless')
            chrome_options.add_argument('--incognito')
            chrome_options.add_argument('--use-fake-device-for-media-stream')
            chrome_options.add_argument('--use-fake-ui-for-media-stream')
            chrome_options.add_argument('window-size=1920x1080')
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-save-password-bubble")
            
            desired_capabilities = DesiredCapabilities.CHROME
            desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
            desired_capabilities.update(chrome_options.to_capabilities())
            driver = webdriver.Remote(
                command_executor=selenium_grid,
                #options=chrome_options,
                desired_capabilities=desired_capabilities,
            )
            
        # Running locally, without Jenkins
        elif pytest.enable_jenkins == 'no':

            # Setup local Chrome options
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--use-fake-device-for-media-stream')
            chrome_options.add_argument('--use-fake-ui-for-media-stream')
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-save-password-bubble")
            
            # Initialize local Chrome WebDriver
            driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), 
                options=chrome_options
            )
            
        else:
            raise ValueError('Invalid flag value provided for --enable-jenkins.')

    # Debugging browser session with an existing Chrome instance
    elif requested_browser_name == 'debugging':
        options = Options()
        options.add_experimental_option('debuggerAddress', 'localhost:9222')

        # Attach to existing Chrome debugging session
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    else:
        raise ValueError('Invalid browser type. Please try with Chrome or debugging.')

    # Maximize the window after driver initialization
    if driver:
        driver.maximize_window()

    return driver





def get_selected_device(apk_type='go', change_device_time=False, auto_accept_alert=False):   # pylint: disable=too-many-statements, too-many-locals
    """
    Get the appropriate mobile webdriver based on the input params
    :param apk_type: apk type of the device ('RT' or 'NRT')
    :return: mobile webdriver instance
    """
    with open(AppConstant.IOS_CAPABILITIES_CONFIGS, encoding='utf-8') as ios_caps:
        DRIVER_CONFIGS = json.load(ios_caps)['capabilities']
        LAMBDATEST_CONFIGS = DRIVER_CONFIGS['lambdatest_caps']['lt:options']
        if auto_accept_alert:
            LAMBDATEST_CONFIGS['autoAcceptAlerts'] = True

        if change_device_time:
            LAMBDATEST_CONFIGS['timezone'] = 'UTC+10:00'

        else:
            LAMBDATEST_CONFIGS['timezone'] = 'UTC-04:00'

    expected_app_id_key = f'apk_id_{apk_type}_{pytest.env}'
    app_id = pytest.configs.get_config(expected_app_id_key)

    if pytest.enable_jenkins == 'yes' or pytest.run_locally == 'yes':

        gdm = GoogleDriveManager()
        lambdatest = LambdaManager()

        if pytest.env == 'staging':
            pytest.file_env = 'Stag'
        elif pytest.env == 'dev':
            pytest.file_env = 'Dev'
        elif pytest.env == 'prod':
            pytest.file_env = 'Prod'

        if pytest.apk_version == '':
            all_folder_under_root = gdm.get_list_of_files_by_name(pytest.configs.get_config(f'app_root_folder_{apk_type}'))

            value_iterator = iter(all_folder_under_root.values())
            key_iterator = iter(all_folder_under_root.keys())
            version_folder_id = next(value_iterator)   # Latest version in GD
            apk_version_in_gd = next(key_iterator)
            print(version_folder_id, apk_version_in_gd)

            env_dict = gdm.get_list_of_files_by_id(version_folder_id)
            if len(env_dict) == 0:
                version_folder_id, apk_version_in_gd, env_dict = get_next_ipa_folder_from_gd(env_dict,
                                                                                         value_iterator,
                                                                                         key_iterator,gdm)
                print(f"Latest version with build present in the folder is being used: {version_folder_id} : {apk_version_in_gd}")

            print(env_dict)

            file_id = gdm.get_latest_zip_file_id(version_folder_id, pytest.file_env)

            print(file_id)
        else:
            try:
                all_folder_under_root = gdm.get_list_of_files_by_name(pytest.configs.get_config(f'app_root_folder_{apk_type}'))
                # print(all_folder_under_root)
                version_folder_id = all_folder_under_root[pytest.apk_version]
            except KeyError:
                all_folder_under_root = gdm.get_list_of_files_by_name(pytest.configs.get_config(f'app_root_folder_old_{apk_type}'))
                # print(all_folder_under_root)
                version_folder_id = all_folder_under_root[pytest.apk_version]
            apk_version_in_gd = pytest.apk_version
            print(version_folder_id, apk_version_in_gd)

            env_dict = gdm.get_list_of_files_by_id(version_folder_id)
            print(env_dict)
            file_id = gdm.get_latest_zip_file_id(version_folder_id, pytest.file_env)
            print(file_id)

        expected_apk_name = f'GO_Automation_{apk_type}_{pytest.env}_{apk_version_in_gd}'
        destination_folder = f'{AppConstant.APK_FOLDER}'
        apk_download_destination_folder = f'{AppConstant.APK_FOLDER}/{apk_type}'
        extracted_folder_path = os.path.join(destination_folder, 'extracted')

        lamdatest_app_id = f'lt://{lambdatest.get_apk_info(expected_apk_name)}'
        if not app_id == lamdatest_app_id:
            app_id = lamdatest_app_id

        print(f'app_id = {app_id}')

        apk_modified_date_time_str_in_gd = gdm.get_latest_zip_file_modified_date(version_folder_id,pytest.file_env)
        apk_modified_date_time_str_in_lambdatest = lambdatest.get_apk_info(expected_apk_name, 'updated_at')

        if apk_modified_date_time_str_in_lambdatest:

            date_format = '%Y-%m-%dT%H:%M:%S.%f%z'
            apk_modified_date_time_in_gd = datetime.datetime.strptime(apk_modified_date_time_str_in_gd, date_format)
            apk_modified_date_time_in_lambdatest = datetime.datetime.strptime(apk_modified_date_time_str_in_lambdatest, date_format)

            if apk_modified_date_time_in_gd > apk_modified_date_time_in_lambdatest:
                print('\nLambdatest has older apk. Uploading latest apk from Google Drive...\n')
                try:
                    os.makedirs(destination_folder, exist_ok=True)
                    os.makedirs(extracted_folder_path, exist_ok=True)
                    gdm.download_and_extract_zip_file(file_id, extracted_folder_path)
                finally:
                    pass
                    # shutil.rmtree(extracted_folder_path, ignore_errors=True)

                ipa_file_name = gdm.get_the_latest_ipa_file_name_from_apk_folder(f'{AppConstant.APK_FOLDER}/extracted')
                ipa_file_path = f'{AppConstant.APK_FOLDER}/extracted/{ipa_file_name}'
                app_id = f'lt://{lambdatest.get_app_id_after_uploading_apk(app_name=expected_apk_name, apk_file_path=ipa_file_path)}'
                os.remove(ipa_file_path)
            else:
                print('\nLambdatest has the latest apk. Continuing with existing one...\n')
                print('\nChecking for validity of the latest saved APP_ID.\n')
                if not lambdatest.check_app_id_exist(app_id):
                    try:
                        os.makedirs(destination_folder, exist_ok=True)
                        os.makedirs(extracted_folder_path, exist_ok=True)
                        gdm.download_and_extract_zip_file(file_id, extracted_folder_path)
                    finally:
                        pass
                        # shutil.rmtree(extracted_folder_path, ignore_errors=True)

                    ipa_file_name = gdm.get_the_latest_ipa_file_name_from_apk_folder(f'{AppConstant.APK_FOLDER}/extracted/')
                    ipa_file_path = f'{AppConstant.APK_FOLDER}/extracted/{ipa_file_name}'
                    app_id = f'lt://{lambdatest.get_app_id_after_uploading_apk(app_name=expected_apk_name, apk_file_path=ipa_file_path)}'
                    os.remove(ipa_file_path)
        else:
            try:
                os.makedirs(destination_folder, exist_ok=True)
                os.makedirs(extracted_folder_path, exist_ok=True)
                gdm.download_and_extract_zip_file(file_id, extracted_folder_path)
                gdm.download_ipa_file(extracted_folder_path, apk_download_destination_folder, f'{pytest.env}.ipa')
            finally:
                pass
                # shutil.rmtree(extracted_folder_path, ignore_errors=True)

            ipa_file_name = gdm.get_the_latest_ipa_file_name_from_apk_folder(f'{AppConstant.APK_FOLDER}/extracted')
            ipa_file_path = f'{AppConstant.APK_FOLDER}/extracted/{ipa_file_name}'
            app_id = f'lt://{lambdatest.get_app_id_after_uploading_apk(app_name=expected_apk_name, apk_file_path=ipa_file_path)}'
            os.remove(ipa_file_path)

        LAMBDATEST_CONFIGS['app'] = app_id
        print(LAMBDATEST_CONFIGS)
        data_props = ConfigParser()
        data_props.add_file(AppConstant.LAMBDATEST_CONFIG)
        data_props.load_configs()
        data_props.update_config(expected_app_id_key, app_id, AppConstant.LAMBDATEST_CONFIG)

        selected_capabilities = LAMBDATEST_CONFIGS
        user_name = pytest.configs.get_config('lambdatest_username')
        access_key = pytest.configs.get_config('lambdatest_access_key')
        url = f"https://{user_name}:{access_key}@mobile-hub.lambdatest.com/wd/hub"
    else:
        # file path for local .app file
        path = f'{AppConstant.APK_FOLDER}/{apk_type}/{pytest.env}.app'
        DRIVER_CONFIGS['local_caps']['app'] = path
        DRIVER_CONFIGS['local_caps']['udid'] = pytest.configs.get_config('udid')

        selected_capabilities = DRIVER_CONFIGS['local_caps']
        url = "http://localhost:4723"

    # pytest.configs.set_config('app_id', DRIVER_CONFIGS['local_caps']['bundleId'])
    options = XCUITestOptions()
    options.load_capabilities(selected_capabilities)
    driver = appium_driver.Remote(command_executor=url, options=options)
    return driver


def get_dict_from_loaded_config(testcases_config=None):
    testcase_dict = {}
    for __item in testcases_config.items():
        key = __item[0]
        value = __item[1].data
        testcase_dict[key] = value

    return testcase_dict


def add_marker_to_test(item, marker_info_dict, marker_type='skip'):
    collected_class_name = item.nodeid.split('::')[1]

    if collected_class_name in marker_info_dict:
        expected_marker = prepare_marker(marker_info_dict, collected_class_name, marker_type)
        item.add_marker(expected_marker)
    elif item.name in marker_info_dict:
        expected_marker = prepare_marker(marker_info_dict, item.name, marker_type)
        item.add_marker(expected_marker)


def prepare_marker(marker_info_dict, tc_or_suite_name, marker_type='skip'):
    unwanted_tc_info_list = marker_info_dict[tc_or_suite_name].split('|')

    if len(unwanted_tc_info_list) == 1:
        skip_marker = pytest.mark.skip(reason=unwanted_tc_info_list[0])
        xfail_marker = pytest.mark.xfail(reason=unwanted_tc_info_list[0])
    else:
        skip_marker = pytest.mark.skipif(pytest.env in unwanted_tc_info_list[0].split(','),
                                         reason=unwanted_tc_info_list[1])
        xfail_marker = pytest.mark.xfail(pytest.env in unwanted_tc_info_list[0].split(','),
                                         reason=unwanted_tc_info_list[1])

    if marker_type == 'skip':
        return skip_marker

    return xfail_marker


def get_modules_and_packages(test_root_dir='.'):
    package_or_modules = []

    for item in glob.iglob(test_root_dir + '**/*.py', recursive=True):
        package_or_modules.append(item)

    return package_or_modules

def set_skipped_test(config):
    skipped_list = re.split(r'\s+', config.getoption('--skip-list'))
    package_or_modueles = get_modules_and_packages()

    items_to_be_skipped = [package_or_module for package_or_module in package_or_modueles
                           if any(package_or_module.endswith(skipped_item)
                                  for skipped_item in skipped_list)]

    if config.__dict__['option'].ignore:
        config.__dict__['option'].ignore.extend(items_to_be_skipped)
    else:
        config.__dict__['option'].ignore = items_to_be_skipped





# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def trigger_ehr_patient_creation_jenkins_job(provider_npi: str, first_name_length: int = 4, last_name_length: int = 4,
                                             chief_complaint: str = 'Pain', room_number: str = '1001',
                                             DOB: str = '2000-01-01', gender: str = 'M',
                                             appointment_date_offset: int = 0, timeout: int = 30):
    """
    Triggers the Jenkins job that creates an EHR appointment for the provider.
    """
    # Jenkins server details
    jenkins_url = pytest.configs.get_config('ehr_patient_creation_jenkins_url')
    jenkins_user = pytest.configs.get_config('jenkins_user')
    jenkins_api_token = pytest.configs.get_config('jenkins_token')

    first_name = generate_random_string(first_name_length)
    last_name = generate_random_string(last_name_length)

    job_parameters = {
        'ENV': 'STAGE',
        'CLOUD_PLATFORM': 'GCP',
        'PARAM_NPI': provider_npi,
        'PARAM_APP_DATE': get_formatted_date_str(appointment_date_offset, '%Y-%m-%d'),
        'PARAM_APP_TIME': '15:00:00',
        'PARAM_VISIT_REASON': chief_complaint,
        'PARAM_FN': first_name,
        'PARAM_LN': last_name,
        'PARAM_BIRTHDATE': DOB,
        'PARAM_SEX': gender,
        'PARAM_ROOM': room_number
    }

    try:
        logging.info("Triggering Jenkins job...")
        response = requests.post(
            jenkins_url,
            auth=HTTPBasicAuth(jenkins_user, jenkins_api_token),
            params=job_parameters,
            timeout=timeout,  # Specify a timeout to avoid hanging
            verify=False  # Consider making SSL verification configurable
        )

        if response.status_code in [200, 201]:
            logging.info("Jenkins job triggered successfully.")
            queue_url = response.headers.get('Location')
            build_number = get_jenkins_build_number(queue_url, jenkins_user, jenkins_api_token, timeout)

            if build_number:
                job_name = "custom_hca_note_creation"  
                check_jenkins_job_status(
                    pytest.configs.get_config('ehr_patient_creation_jenkins_base_url'),
                    job_name, build_number, jenkins_user, jenkins_api_token, timeout
                )

                patient_name = f'{first_name} {last_name}'
                patient_locator = (AppiumBy.ACCESSIBILITY_ID, patient_name)
                return patient_name, patient_locator
            else:
                logging.error("Failed to retrieve the build number.")
        else:
            logging.error("Failed to trigger Jenkins job. Status code: %d", response.status_code)
            logging.debug("Response content: %s", response.text)

    except requests.exceptions.RequestException as e:
        logging.error("Request error occurred: %s", e)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)

def get_jenkins_build_number(queue_url, user, token, timeout=30):
    """Checks the Jenkins queue until the job starts and retrieves the build number."""
    try:
        while True:
            queue_response = requests.get(queue_url + '/api/json', auth=HTTPBasicAuth(user, token), verify=False, timeout=timeout)
            if queue_response.status_code == 200:
                queue_info = queue_response.json()
                if 'executable' in queue_info:
                    build_number = queue_info['executable']['number']
                    logging.info("Job has started with build number: %d", build_number)
                    return build_number
                else:
                    logging.info("Job is still in queue...")
                    time.sleep(10)
            else:
                logging.error("Error retrieving queue status: %s", queue_response.text)
                break
    except requests.exceptions.RequestException as e:
        logging.error("Request error while getting build number: %s", e)
    except Exception as e:
        logging.error("Unexpected error occurred: %s", e)

def check_jenkins_job_status(base_url, job_name, build_number, user, token, timeout=30):
    """Checks the status of the Jenkins job until completion."""
    try:
        build_url = f"{base_url}/job/{job_name}/{build_number}/api/json"
        while True:
            response = requests.get(build_url, auth=HTTPBasicAuth(user, token), verify=False, timeout=timeout)
            if response.status_code == 200:
                build_info = response.json()
                if build_info['result'] is not None:
                    if build_info['result'] == "SUCCESS":
                        logging.info("Jenkins job completed successfully.")
                        return True
                    else:
                        logging.error("Jenkins job failed with result: %s", build_info['result'])
                        return False
                else:
                    logging.info("Jenkins job is still running...")
                    time.sleep(10)
            else:
                logging.error("Error checking job status: %s", response.text)
                break
    except requests.exceptions.RequestException as e:
        logging.error("Request error while checking job status: %s", e)
    except Exception as e:
        logging.error("Unexpected error occurred: %s", e)



