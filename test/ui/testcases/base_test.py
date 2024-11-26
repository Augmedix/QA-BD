import pytest
from test.ui.pages.home_screen_page import HomeScreenPage


@pytest.mark.usefixtures('init_device')
class BaseTest:
    """
    Base class for all test classes.
    """

    scp_driver = None  # Class attribute
    browser_driver = None
    data = None
    configs = pytest.configs
    auto_accept_alert = False

    

    @pytest.fixture(scope='class', autouse=True)
    def teardown(self):
        """
        Common teardown method for all test classes.
        """
        yield  # This will pause the execution here and allow cleanup code to be executed afterward

        try:
            self.home_screen_page.logout_from_app()
        except Exception as e:
            print(f"An error occurred during app logout: {e}")
        finally:
            self.appium_driver.quit()

        if self.scp_driver:
            print('\nBrowser driver available, quiting')
            #Sign out of SCP which was logged in from previous test case
            try:
                self.scp_home_page.perform_logout()
            except Exception as e:
                print(f"An error occurred during SCP logout: {e}")
            finally:
                self.scp_driver.quit()

        if self.browser_driver:
            print('\nBrowser driver available, quiting')
            #Sign out of SCP which was logged in from previous test case
            try:
                self.browser_driver.perform_logout()
            except Exception as e:
                print(f"An error occurred during SCP logout: {e}")
            finally:
                self.browser_driver.quit()
        print('Teardown performed!')

