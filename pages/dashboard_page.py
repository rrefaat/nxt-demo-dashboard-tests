from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.page_base import BasePage

class DashboardPage (BasePage):
    def __init__(self, driver):
        self.driver = driver

    # Locators
    ADD_EVENT_BUTTON = (By.XPATH, "//a[@href='/events/options']")
    EDIT_EVENT_BUTTON = (By.XPATH, "(//button[@class='Button_root__0RbKd Button_ghost__tLrp+ Button_tiny__+g2s1 Button_circle__MofPb'])[2]")
    EVENT_NAME_FIELD = (By.XPATH, "(//input[@class='Input_root__fi0ZK'])[1]")
    VIEW_EVENT_BUTTON = (By.XPATH, "(//button[@class='Button_root__0RbKd Button_ghost__tLrp+ Button_tiny__+g2s1 Button_circle__MofPb'])[3]")   

    def click_add_event(self):
        self.check_for_errors()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ADD_EVENT_BUTTON))
        self.driver.find_element(*self.ADD_EVENT_BUTTON).click()

    def click_edit_event(self):
        self.click(self.EDIT_EVENT_BUTTON)

    def click_view_event(self):
        self.click(self.VIEW_EVENT_BUTTON)

    def validate_edit_page(self):
        self.click_edit_event()
        self.verify_page_title("Edit Event")
        self.check_for_errors()

    def validate_event_page(self):
        self.click_view_event()
        self.verify_page_title("Dashboard")
        self.check_for_errors()
        
        

