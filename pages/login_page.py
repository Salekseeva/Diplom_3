# pages/login_page.py
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
import allure


class LoginPage(BasePage):

    def navigate_to_login_page(self, url):
        self.open_url(url)

    def click_forgot_password(self):
        self.wait_for_element_is_clickable(LoginPageLocators.FORGOT_PASSWORD_LINK, 20)
        self.click_element_compatible(LoginPageLocators.FORGOT_PASSWORD_LINK)

    def enter_email(self, email):
        email_field = self.wait_for_element_is_clickable(LoginPageLocators.EMAIL_FIELD, 10)
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.wait_for_element_is_clickable(LoginPageLocators.PASSWORD_FIELD, 10)
        password_field.clear()
        password_field.send_keys(password)

    def submit_login(self):
        self.wait_for_element_is_clickable(LoginPageLocators.LOGIN_SUBMIT_BUTTON, 20)
        self.click_element_compatible(LoginPageLocators.LOGIN_SUBMIT_BUTTON)

    def login(self, email, password):
        """Логин пользователя."""
        self.enter_email(email)
        self.enter_password(password)
        self.submit_login()

    @allure.step("Click on 'Конструктор'")
    def click_constructor_button(self):
        """Клик по кнопке 'Конструктор'."""
        self.click_element_compatible(LoginPageLocators.CONSTRUCTOR_BUTTON)
