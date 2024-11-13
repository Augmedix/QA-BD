"""
Used to set up test configurations and store/modify the testcases that are used
by test functions/methods.
"""

import datetime
import glob
import importlib
import json
import os
import re
import shutil
import sys

import allure
import pytest
from _pytest.mark import Mark, MarkDecorator
from allure_commons.types import AttachmentType
from appium import webdriver as appium_driver
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
from jproperties import Properties
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from utils.app_constants import AppConstant
from utils.config_parser import ConfigParser
# from utils.google_drive_manager import GoogleDriveManager
from appium.options.ios import XCUITestOptions
# from utils.lambdatest_manager import LambdaManager


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

    set_skipped_test(config)

    configs = ConfigParser()

    if env is None or env == 'dev':
        configs.add_file(AppConstant.DEV_CONFIG)
        pytest.conf = AppConstant.DEV_CONFIG
        pytest.env = env
    elif env in ('stage', 'staging'):
        configs.add_file(AppConstant.STAGING_CONFIG)
        pytest.conf = AppConstant.STAGING_CONFIG
        pytest.env = 'staging'
    elif env in ('prod', 'production', 'live'):
        configs.add_file(AppConstant.PRODUCTION_CONFIG)
        pytest.conf = AppConstant.PRODUCTION_CONFIG
        pytest.env = 'prod'
    else:
        sys.exit('Invalid option. Please provide either of the following values: dev, staging, production...')

    if device_name == 'ios_device':
        configs.add_file(AppConstant.IOS_REAL_DEVICE_CONFIG)
        pytest.conf = AppConstant.IOS_REAL_DEVICE_CONFIG
        pytest.device = device_name
    elif device_name == "ios_simulator" or device_name == 'ios_emulator':
        configs.add_file(AppConstant.IOS_SIMULATOR_CONFIG)
        pytest.conf = AppConstant.IOS_SIMULATOR_CONFIG
        pytest.device = device_name

    configs.add_file(AppConstant.SYSTEM_CONFIG)
    configs.add_file(AppConstant.ALLURE_ENV_FILE)
    configs.add_file(AppConstant.LAMBDATEST_CONFIG)
    configs.add_file(AppConstant.JIRA_CONFIG)
    configs.add_file(AppConstant.DATA_CONFIG)

    if config.getoption('--default-dataset') == 'yes':
        configs.add_file(AppConstant.USER_DATA_CONFIG)
    # else:
    #     configs.add_file(AppConstant.USER_DATA_CONFIG_OPTIONAL)

    pytest.marker = marker
    configs.load_configs()

    if url is not None:
        configs.set_config('url', url)

    browser_version = config.getoption('--browser-version') or configs.get_config('browser_version')

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
    pytest.browser_version = browser_version
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
    pytest.unmark = Unmarker()


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


@pytest.fixture(scope='class', autouse=True)
def init_device(request):
    if 'no_auto' in request.keywords:
        yield
        return
    driver = get_requested_browser(pytest.browser)
    driver.get(pytest.url)
    request.cls.driver = driver
    browser_version = driver.capabilities['browserVersion']
    os.environ['browser_version'] = browser_version

    # _appium_driver = get_selected_device()
    # request.cls.appium_driver = _appium_driver
    yield driver
    driver.quit()
    # _appium_driver.quit()



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
# def delete_lambdatest_apps():
#     lambdatest_manager = LambdaManager()
#     lambdatest_manager.delete_apps()


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


def get_requested_browser(requested_browser_name='chrome'):
    driver = None
    if requested_browser_name == 'chrome':
        if pytest.enable_jenkins == 'yes':
            selenium_grid = pytest.configs.get_config('selenium_grid_url')
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('headless')
            chrome_options.add_argument('--incognito')
            chrome_options.add_argument('--use-fake-device-for-media-stream')
            chrome_options.add_argument('--use-fake-ui-for-media-stream')
            chrome_options.add_argument('window-size=1920x1080')
            desired_capabilities = DesiredCapabilities.CHROME
            desired_capabilities['loggingPrefs'] = {'browser': 'ALL'}
            desired_capabilities.update(chrome_options.to_capabilities())
            driver = webdriver.Remote(
                command_executor=selenium_grid,
                options=desired_capabilities,
            )
        elif pytest.enable_jenkins == 'no':
            # pylint: disable=import-error
            from selenium.webdriver.chrome.service import Service
            from webdriver_manager.chrome import ChromeDriverManager

            # pylint: enable=import-error
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--use-fake-device-for-media-stream')
            chrome_options.add_argument('--use-fake-ui-for-media-stream')
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        else:
            print('Invalid flag value provided for --enable-jenkins.')

    elif requested_browser_name == 'debugging':
        # pylint: disable=import-error
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager

        # pylint: enable=import-error
        options = Options()
        options.add_experimental_option('debuggerAddress', 'localhost:9222')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    else:
        print('Invalid browser type. Please try with Chrome or Firefox.')
        sys.exit()

    driver.maximize_window()

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


def get_modules_and_packages(test_root_dir='testcases'):
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