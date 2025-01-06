from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Open URL
    def open_url(self, url):
        self.driver.get(url)


    # Generalized Wait for Element
    def wait_for_element(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException as e:
            raise Exception(f"Element not found: {locator}, Error: {str(e)}")

    # Click Element
    def click(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.click()

    # Enter Text into a Field
    def enter_text(self, locator, text, timeout=10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    # Check Visibility of Element
    def is_element_visible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    # Verify Page Title
    def verify_title(self, expected_title, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.title_contains(expected_title)
            )
            return True
        except TimeoutException:
            return False

    # Error Handling
    def check_for_errors(self):
        errors = self.driver.find_elements(By.XPATH, "//*[contains(text(),'Error')]")
        if errors:
            error_messages = [error.text for error in errors]
            raise Exception(f"Errors Found: {error_messages}")
        
    def verify_page_title(self, expected_title):
        # Verify the page title
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//h2[contains(@class,'truncate')]"),expected_title))
