# pages/recovery_page.py
from pages.base_page import BasePage
from locators.recovery_password_page_locators import RecoveryPasswordPageLocators


class RecoveryPage(BasePage):
    def enter_email(self, email):
        self.set_text(RecoveryPasswordPageLocators.EMAIL_FIELD, email)

    def click_recover_button(self):
        self.click_element_if_clickable(RecoveryPasswordPageLocators.RECOVER_BUTTON)

    def enter_password(self, password):
        self.set_text(RecoveryPasswordPageLocators.PASSWORD_FIELD, password)

    def click_show_password(self):
        # Найти элемент и прокрутить до него
        self.click_element_if_clickable(RecoveryPasswordPageLocators.SHOW_PASSWORD_ELEMENT)

    def is_password_visible(self):
        # Проверяем, что тип поля пароля изменился на 'text'
        password_field = self.wait_for_element_is_clickable(RecoveryPasswordPageLocators.PASSWORD_FIELD, 20)
        return password_field.get_attribute("type") == "text"

    def is_password_active(self):
        # Проверяем, что у поля пароль появился класс 'input_status_active'
        class_attribute = self.get_attribute(RecoveryPasswordPageLocators.ACTIVE_PASSWORD_CLASS, "class")
        return "input_status_active" in class_attribute
