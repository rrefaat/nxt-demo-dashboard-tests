from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.config import Resources

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGO = (By.XPATH, "//img[@class='mt-5']")
    SKIP_BUTTON = (By.XPATH, "//button[contains(text(), 'Skip (only for testing)')]")
    ERROR_BANNER = (By.XPATH, "//div[contains(@role, 'status')]")
    ERROR_MESSAGE = (By.XPATH, "//*[@class= 'Text_root__M6tno']")

    # Methods
    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.USERNAME_FIELD))
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def get_error_message(self):
        # Wait for the error banner
        banner_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ERROR_BANNER)).text

        # Wait for the detailed error message below the password field
        message_text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text

        # Return both error messages
        return banner_text, message_text

    def click_skip(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SKIP_BUTTON)).click()

    
    def login(self):
        self.enter_username(Resources.USERNAME)
        self.enter_password(Resources.PASSWORD)
        self.click_login()
        self.click_skip()

    