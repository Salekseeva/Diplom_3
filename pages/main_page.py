# from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import time
import allure


class MainPage(BasePage):
    def open_main_page(self, url):
        """Открыть главную страницу."""
        self.browser.get(url)

    @allure.step("Click on 'Конструктор'")
    def click_constructor_button(self):
        """Клик по кнопке 'Конструктор'."""
#        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click_element_with_js(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Click on 'Лента заказов'")
    def click_order_feed_button(self):
        """Клик по кнопке 'Лента заказов'."""
        self.click_element_with_js(MainPageLocators.ORDER_FEED_BUTTON)
#        self.click_element_with_js(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Click on an ingredient")
    def click_ingredient_details(self):
        """Клик по ингредиенту на странице."""
        time.sleep(1)
        self.click_element(MainPageLocators.INGREDIENT)

    @allure.step("Check if ingredient modal is open")
    def is_ingredient_modal_open(self):
        """Проверяет, открылось ли модальное окно с деталями ингредиента."""
        modal_class = self.get_element_attribute(MainPageLocators.INGREDIENT_DETAILS, 'class')
        return 'modal_opened' in modal_class

    @allure.step("Click close button on ingredient modal")
    def close_ingredient_details(self):
        """Закрывает модальное окно с деталями ингредиента."""
        self.click_element(MainPageLocators.DETAILS_CLOSE)

#    @allure.step("Drag an ingredient to the burger creation area")
#    def drag_ingredient_to_burger(self):
#        """Перетаскивает ингредиент в область создания бургера."""
#        ingredient = self.find_element(MainPageLocators.INGREDIENT_BUN)
#        burger_area = self.find_element(MainPageLocators.CREATE_BURGER)
#        self.drag_and_drop(ingredient, burger_area)

    def add_ingredient_to_order(self):
        """Добавить ингредиент в заказ."""
        self.drag_and_drop(MainPageLocators.INGREDIENT_BUN, MainPageLocators.CREATE_BURGER)

    @allure.step("Click on 'Place Order' button")
    def place_order(self):
        """Клик по кнопке 'Оформить заказ'."""
        self.click_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Check if order is in progress")
#    def is_order_in_progress(self):
#        """Проверяет, отображается ли элемент, показывающий, что заказ в процессе оформления."""
#        return self.is_element_visible(MainPageLocators.ORDER_IN_PROGRESS)
    def is_order_in_progress(self):
        """Проверить, что заказ в процессе оформления."""
        return self.wait_for_element(MainPageLocators.ORDER_IN_PROGRESS)
