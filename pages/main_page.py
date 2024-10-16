# pages/main_page.py
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    def open_main_page(self, url):
        """Открыть главную страницу."""
        self.driver.get(url)

    @allure.step("Click on 'Лента заказов'")
    def click_order_feed_button(self):
        """Клик по кнопке 'Лента заказов'."""
        self.wait_for_modal_overlay_to_disappear()
        self.click_element_compatible(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Click on an ingredient")
    def click_ingredient_details(self):
        """Клик по ингредиенту на странице."""
        self.click_element_compatible(MainPageLocators.INGREDIENT)

    @allure.step("Check if ingredient modal is open")
    def is_ingredient_modal_open(self):
        """Проверяет, открылось ли модальное окно с деталями ингредиента."""
        modal_class = self.get_element_attribute(MainPageLocators.INGREDIENT_DETAILS, 'class')
        return 'modal_opened' in modal_class

    @allure.step("Click close button on ingredient modal")
    def close_ingredient_details(self):
        """Закрывает модальное окно с деталями ингредиента."""
        self.click_element_compatible(MainPageLocators.DETAILS_CLOSE)

    @allure.step("Add ingredient to order")
    def add_ingredient_to_order(self):
        """Добавить ингредиент в заказ."""
        self.drag_and_drop(MainPageLocators.INGREDIENT_BUN, MainPageLocators.CREATE_BURGER)

    @allure.step("Click on 'Place Order' button")
    def place_order(self):
        """Клик по кнопке 'Оформить заказ'."""
        self.click_element_if_clickable(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Check if order is in progress")
    def is_order_in_progress(self):
        """Проверить, что заказ в процессе оформления."""
        return self.wait_for_element_is_clickable(MainPageLocators.ORDER_IN_PROGRESS, 20)

    def wait_for_modal_overlay_to_disappear(self):
        self.find_element_not_visibility(MainPageLocators.MODAL_OVERLAY_ELEMENT, 20)
