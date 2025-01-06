import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from pages.page_base import BasePage


class EventPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  # Inherit from BasePage

    # Locators
    START_FROM_SCRATCH = (By.XPATH, "//div[@role='button']//p[contains(text(),'Start From Scratch')]")
    EVENT_NAME_FIELD = (By.XPATH, "(//input[@class='Input_root__fi0ZK'])[1]")
    EVENT_TYPE_LIST = (By.XPATH, "(//select[@class='Input_root__fi0ZK Input_selectInput__aHlvF'])[1]")
    EVENT_SLUG_FIELD = (By.XPATH, "(//input[@class='Input_root__fi0ZK'])[2]")
    START_DATE_FIELD = (By.XPATH, "(//input[@class='Input_root__fi0ZK'])[3]")
    END_DATE_FIELD = (By.XPATH, "(//input[@class='Input_root__fi0ZK'])[5]")
    START_TIME_FIELD = (By.XPATH, "(//input[@class='Input_root__fi0ZK'])[4]")
    END_TIME_FIELD = (By.XPATH, "(//input[@class='Input_root__fi0ZK'])[6]")
    TIMEZONE_LIST = (By.XPATH, "(//select[@class='Input_root__fi0ZK Input_selectInput__aHlvF'])[2]")
    CREATE_BUTTON = (By.XPATH, "//button[contains(text(),'Create')]")

    # Click "Start From Scratch"
    def click_start_from_scratch(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.START_FROM_SCRATCH)).click()

    # Generalized Dropdown Selection
    def select_from_dropdown(self, locator, value):
        dropdown = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)))
        dropdown.select_by_visible_text(value)

    # Set Event Details
    def enter_event_details(self, name, start_date, end_date, start_time, end_time):
        # Generate random 3-digit number for uniqueness
        random_number = str(random.randint(100, 999))
        updated_name = f"{name}_automation_{random_number}"
        self.enter_text(self.EVENT_NAME_FIELD, updated_name)

        # Select Event Type
        self.select_from_dropdown(self.EVENT_TYPE_LIST, "Incentive Trip")

        # Fill in the Event Slug
        slug = updated_name.lower().replace(" ", "-") + "-slug"
        self.enter_text(self.EVENT_SLUG_FIELD, slug)

        # Fill in Dates and Times
        self.enter_text(self.START_DATE_FIELD, start_date)
        self.enter_text(self.END_DATE_FIELD, end_date)

        # Set Time with Keys
        self.set_time(self.START_TIME_FIELD, start_time, Keys.ARROW_UP)
        self.set_time(self.END_TIME_FIELD, end_time, Keys.ARROW_DOWN)

        # Select Timezone
        self.select_from_dropdown(self.TIMEZONE_LIST, "(UTC+02:00) Cairo")
        
        # Submit Form
        self.click_create()
        
        assert self.is_event_created(updated_name), f"Event '{updated_name}' was not created!"


    # Helper Method for Time
    def set_time(self, locator, time_value, key):
        actions = ActionChains(self.driver)
        time_field = self.driver.find_element(*locator)
        actions.move_to_element(time_field).click().perform()
        time_field.send_keys(time_value, key, Keys.ENTER)

    # Click Create Button
    def click_create(self):
        create_button =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CREATE_BUTTON))
        # Focus and Click
        self.driver.execute_script("arguments[0].focus();", create_button)
        self.click(self.CREATE_BUTTON)
        self.check_for_errors()

    def is_event_created(self, event_name):
        # Wait for the success message
        success_message = (By.XPATH, "//*[contains(text(),'Event created successfully')]")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(success_message))

        # Locate the event in the table
        event_locator = (By.XPATH, f"//*[contains(text(),'{event_name}')]")
        return self.is_element_visible(event_locator, timeout=10)
