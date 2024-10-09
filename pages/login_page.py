# pages/login_page.py
# from selenium.common import TimeoutException
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import time
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    def navigate_to_login_page(self, url):
        self.open_page(url)

    def click_forgot_password(self):
        time.sleep(1)
        self.click_element(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def enter_email(self, email):
        email_field = self.wait_for_element(LoginPageLocators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.wait_for_element(LoginPageLocators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)
        time.sleep(1)

    def submit_login(self):
        self.click_element(LoginPageLocators.LOGIN_SUBMIT_BUTTON)

    def login(self, email, password):
        """Логин пользователя."""
        self.enter_email(email)
        self.enter_password(password)
        self.submit_login()
