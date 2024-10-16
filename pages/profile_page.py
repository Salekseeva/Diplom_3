# pages/profile_page.py
from selenium.common import ElementClickInterceptedException, TimeoutException

from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from locators.main_page_locators import MainPageLocators


class ProfilePage(BasePage):
    def open_profile(self):
        try:
            self.find_element_not_visibility(MainPageLocators.MODAL_OVERLAY_ELEMENT, 20)
        except TimeoutException:
            print("Модальное окно не исчезло в течение ожидаемого времени")

        try:
            self.find_element_not_visibility(MainPageLocators.MODAL_OVERLAY_ELEMENT, 20)
            self.wait_for_element_is_clickable(ProfilePageLocators.PROFILE_BUTTON, 20)
            self.click_element_if_visible(ProfilePageLocators.PROFILE_BUTTON)
        except ElementClickInterceptedException:
            print("Элемент не кликабельный, так как что-то его перекрывает")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def go_to_order_history(self):
        self.wait_for_element_is_clickable(ProfilePageLocators.ORDER_HISTORY_LINK, 20)
        self.click_element_compatible(ProfilePageLocators.ORDER_HISTORY_LINK)

    def is_order_history_active(self):
        element = self.wait_for_element_is_clickable(ProfilePageLocators.ORDER_HISTORY_LINK)
        return "Account_link_active__2opc9" in element.get_attribute("class")

    def logout(self):
        self.click_element_compatible(ProfilePageLocators.EXIT_BUTTON)
        self.wait_for_element_is_clickable(ProfilePageLocators.EMAIL_FIELD, 20)
