from data.data import Data
from pages.appointment_screen_page import AppointmentScreenPage
from pages.base_page import BasePage
from pages.problems_screen_page import ProblemsScreenPage

data = Data()


# pylint: disable-all
class AppSyncPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.appointment_screen = AppointmentScreenPage(self.driver)
        self.problems_screen = ProblemsScreenPage(self.driver)

    def modify_problem_page_content(self):
        self.problems_screen.add_problem_in_empty_state(data.CHRONIC_PROBLEM_NAME, 'CHRONIC')
        self.problems_screen.click_on_add_block_button(data.CHRONIC_PROBLEM_NAME, self.problems_screen.ADD_SYMPTOMS_BUTTON)
        self.problems_screen.add_descriptor(data.CHRONIC_HPI_SYMPTOMS_NAME)
        self.problems_screen.click_on_add_block_button(data.CHRONIC_PROBLEM_NAME, self.problems_screen.ADD_CURRENT_MEDICATION_BUTTON)
        self.problems_screen.add_descriptor(data.CHRONIC_HPI_CURRENT_MEDICATION_NAME)
        self.problems_screen.click_on_add_block_button(data.CHRONIC_PROBLEM_NAME, self.problems_screen.ADD_LIFESTYLE_TREATMENTS_BUTTON)
        self.problems_screen.add_descriptor(data.CHRONIC_HPI_LIFESTYLE_TREATMENT_NAME)
        self.wait_and_click(self.problems_screen.BACK_SCHEDULE_BUTTON, 5)





