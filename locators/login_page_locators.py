# locators/login_page_locators.py
from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, '//input[@name="Пароль"]')
    LOGIN_SUBMIT_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//a[text()="Восстановить пароль"]')
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')
