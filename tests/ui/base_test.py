"""
Used to setup device, browser, taking screenshots etc.
"""
import pytest


@pytest.mark.usefixtures('init_device', 'failed_page')
class BaseTest:
    """
    Base class for all test classes.
    """
    configs = pytest.configs