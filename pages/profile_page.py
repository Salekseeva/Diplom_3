# pages/profile_page.py
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
import time


class ProfilePage(BasePage):
    def open_profile(self):
        self.click_element(ProfilePageLocators.PROFILE_BUTTON)
        time.sleep(1)

    def go_to_order_history(self):
        self.click_element(ProfilePageLocators.ORDER_HISTORY_LINK)
        time.sleep(1)

    def is_order_history_active(self):
        element = self.wait_for_element(ProfilePageLocators.ORDER_HISTORY_LINK)
        time.sleep(1)
        return "Account_link_active__2opc9" in element.get_attribute("class")

    def logout(self):
        self.click_element(ProfilePageLocators.EXIT_BUTTON)
        time.sleep(1)
