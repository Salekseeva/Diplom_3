# pages/recovery_page.py
from pages.base_page import BasePage
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators
import time


class RecoveryPage(BasePage):
    def enter_email(self, email):
        self.enter_text(RecoveryPasswordPageLocators.EMAIL_FIELD, email)

    def click_recover_button(self):
        self.click_element(RecoveryPasswordPageLocators.RECOVER_BUTTON)
        time.sleep(1)  # Для стабильности интерфейса

#    def wait_for_show_password_element(self):
#        self.wait_and_find_element(RecoveryPasswordPageLocators.SHOW_PASSWORD_ELEMENT)

    def enter_password(self, password):
        self.enter_text(RecoveryPasswordPageLocators.PASSWORD_FIELD, password)

    def click_show_password(self):
        # Найти элемент и прокрутить до него
        self.click_element(RecoveryPasswordPageLocators.SHOW_PASSWORD_ELEMENT)
        time.sleep(1)  # Для обновления интерфейса

    def is_password_visible(self):
        # Проверяем, что тип поля пароля изменился на 'text'
        password_field = self.wait_for_element(RecoveryPasswordPageLocators.PASSWORD_FIELD)
        return password_field.get_attribute("type") == "text"

    def is_password_active(self):
        # Проверяем, что у поля пароля появился класс 'input_status_active'
        class_attribute = self.get_attribute(RecoveryPasswordPageLocators.ACTIVE_PASSWORD_CLASS, "class")
        return "input_status_active" in class_attribute
