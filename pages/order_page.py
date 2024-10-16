# pages/order_page.py
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
import allure


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on 'Лента заказов'")
    def open_order_feed(self):
        self.find_until_all_elements_located(OrderPageLocators.NAVIGATE)
        self.click_element_if_visible(OrderPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Click on first order in 'Лента заказов'")
    def click_order_in_list(self):
        self.click_element_compatible(OrderPageLocators.ORDER_IN_LIST)

    @allure.step("Check if modal window with order info is open")
    def is_order_info_displayed(self) -> bool:
        modal = self.driver.find_element(*OrderPageLocators.ORDER_INFO)
        return modal.is_displayed()  # Проверка, что модалка отображается

    @allure.step("Get last order number")
    def get_last_order_number(self):
        try:
            self.wait_for_element_is_clickable(OrderPageLocators.LAST_ORDER_NUMBER, 20)
            order_text = self.get_text(OrderPageLocators.LAST_ORDER_NUMBER)
            last_order_number = order_text[2:]
            return last_order_number
        except TimeoutException:
            order_text = self.get_text(OrderPageLocators.LAST_ORDER_NUMBER)
            last_order_number = order_text[2:]
            return last_order_number
        except Exception as e:
            # Обработка других исключений
            print(f"An unexpected error occurred: {e}")
            return None

    @allure.step("Get number of total orders")
    def get_total_orders(self):
        element = OrderPageLocators.TOTAL_ORDERS
        self.wait_for_element_is_clickable(element, 20)
        return int(self.get_text(element))

    @allure.step("Get number of orders today")
    def get_today_total_orders(self):
        element = OrderPageLocators.TODAY_TOTAL_ORDERS
        self.wait_for_element_is_clickable(element, 20)
        return int(self.get_text(element))

    @allure.step("Get number of order in progress")
    def get_order_in_progress(self):
        order_text = self.get_text(OrderPageLocators.LAST_ORDER_NUMBER)
        return order_text[2:]
