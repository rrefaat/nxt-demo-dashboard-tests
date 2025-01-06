import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.new_event_page import EventPage
from utils.config import Resources
from tests.test_base import BaseTest


@pytest.mark.usefixtures("setup")
class TestScenarios(BaseTest):

    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
    
        # Perform login steps
        login_page.enter_username(Resources.USERNAME)
        login_page.enter_password(Resources.PASSWORD)
        login_page.click_login()
        login_page.click_skip()
        # Verify successful login by checking the title
        dashboard_page.verify_title("Events")

    def test_invalid_username_or_password(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("invalid_user")
        login_page.enter_password("invalid_pass")
        login_page.click_login()
    
        banner_msg, detail_msg = login_page.get_error_message()

        # Validate both messages
        assert banner_msg == "Invalid username or password", "Banner error message mismatch!"
        assert detail_msg == "Invalid login information, please check and try again.", "Detail error message mismatch!"
    
    def test_add_new_trip_event(self):
        dashboard_page = DashboardPage(self.driver)
        new_event_page = EventPage(self.driver)
        login_page = LoginPage(self.driver)
        login_page.login()
        dashboard_page.click_add_event()
        new_event_page.click_start_from_scratch()
        new_event_page.enter_event_details("TestEvent","01/10/2025","01/15/2025","09:00","12:00")

    def test_validate_edit_event_page(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        login_page.login()
        dashboard_page.validate_edit_page()

    def test_validate_view_event_page(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)
        login_page.login()
        dashboard_page.validate_event_page()