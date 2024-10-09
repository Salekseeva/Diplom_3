# locators/recovery_password_page_locators.py
from selenium.webdriver.common.by import By

class RecoveryPasswordPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    RECOVER_BUTTON = (By.XPATH, '//button[text()="Восстановить"]')
    PASSWORD_FIELD = (By.XPATH, '//div//label[text()="Пароль"]/following-sibling::input')
    ACTIVE_PASSWORD_CLASS = (By.XPATH, "//div[contains(@class, 'input') and ./label[text()='Пароль']]")
    SHOW_PASSWORD_ELEMENT = (By.XPATH, '//div[@class="input__icon input__icon-action"]')
