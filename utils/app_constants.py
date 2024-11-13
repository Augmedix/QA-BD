"""
Provides paths for various resource under resource folder.
"""
from os.path import dirname, join


class AppConstant:
    """
    Used for storing constants.
    """
    PROJECT_ROOT = dirname(dirname(__file__))
    RESOURCE_FOLDER = join(PROJECT_ROOT, 'resources')
    RECORDING_FOLDER = join(RESOURCE_FOLDER, 'recordings')
    TEST_DATA_FOLDER = join(RESOURCE_FOLDER, 'test_data')
    TEST_STEPS_FOLDER = join(RESOURCE_FOLDER, 'test_steps')
    DEFAULT_CONFIGS_FOLDER = join(RESOURCE_FOLDER, 'default_configs')
    SYSTEM_CONFIG = join(RESOURCE_FOLDER, 'system.properties')
    DEV_CONFIG = join(RESOURCE_FOLDER, 'dev.properties')
    STAGING_CONFIG = join(RESOURCE_FOLDER, 'staging.properties')
    PRODUCTION_CONFIG = join(RESOURCE_FOLDER, 'production.properties')
    DR_CONFIG = join(RESOURCE_FOLDER, 'dr.properties')
    DATA_CONFIG = join(RESOURCE_FOLDER, 'data.properties')
    USER_DATA_CONFIG = join(RESOURCE_FOLDER, 'user_data.properties')
    PAGE_OBJECTS_CONFIG_FILE = join(RESOURCE_FOLDER, 'page_objects.properties')
    SKIPPED_TESTCASES_FILE = join(RESOURCE_FOLDER, 'skipped_testcases.properties')
    XFAILED_TESTCASES_FILE = join(RESOURCE_FOLDER, 'xfailed_testcases.properties')
    ALLURE_ENV_FILE = join(RESOURCE_FOLDER, 'environment.properties')
    CLIENT_CONFIG_FILE = join(RESOURCE_FOLDER, 'credentials/client_secrets.json')
    DOCKER_COMPOSE_FILE = join(RESOURCE_FOLDER, 'docker-compose.yml')
    DOCKER_COMPOSE_TEMPLATE_FILE = join(RESOURCE_FOLDER, 'docker-compose-template.yml')
    GOOGLE_CREDENTIAL_FILE = join(RESOURCE_FOLDER, 'credentials/google_saved_credentials.txt')
    LAMBDATEST_CONFIG = join(RESOURCE_FOLDER, 'lambdatest.properties')
    JIRA_CONFIG = join(RESOURCE_FOLDER, 'jira.properties')
    API_REQUEST_DATA_FOLDER = join(RESOURCE_FOLDER, 'api_request_data')
    APK_FOLDER = join(RESOURCE_FOLDER, 'apk')
    IOS_CAPABILITIES_CONFIGS = join(RESOURCE_FOLDER, 'device_capabilities/ios_capabilities.json')
    IOS_REAL_DEVICE_CONFIG = join(RESOURCE_FOLDER, 'ios_real_device.properties')
    IOS_SIMULATOR_CONFIG = join(RESOURCE_FOLDER, 'ios_simulator.properties')