# pages/order_page.py
from selenium.webdriver.common.by import By
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_order_feed(self):
        self.click_element(OrderPageLocators.ORDER_FEED_BUTTON)

    def click_order_in_list(self):
        self.click_element(OrderPageLocators.ORDER_IN_LIST)

    def get_last_order_number(self):
        return self.get_text(OrderPageLocators.LAST_ORDER_NUMBER)

    def get_total_orders(self):
        return int(self.get_text(OrderPageLocators.TOTAL_ORDERS))

    def get_today_total_orders(self):
        return int(self.get_text(OrderPageLocators.TODAY_TOTAL_ORDERS))

    def get_order_in_progress(self):
        return self.get_text(OrderPageLocators.ORDER_IN_PROGRESS)

    def is_order_info_displayed(self) -> bool:
        """
        Проверяет, открыто ли модальное окно с информацией о заказе.
        """
        modal = self.browser.find_element(*OrderPageLocators.ORDER_INFO)
        return modal.is_displayed()  # Проверка, что модалка отображается

    def click_on_order(self, order_number: int):
        """
        Кликает на заказ с указанным номером.
        """
        order_element = self.browser.find_element(By.XPATH, f"//div[contains(text(), '{order_number}')]")
        order_element.click()

    def get_text(self, locator) -> str:
        """
        Получает текст элемента, указанный локатором.
        """
        element = self.browser.find_element(*locator)
        return element.text
