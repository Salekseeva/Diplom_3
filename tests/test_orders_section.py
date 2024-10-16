# tests/test_orders_section.py
import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from test_data import INGREDIENTS


@allure.feature("Order Feed")
@pytest.mark.usefixtures("register_and_login_user", "create_order")
class TestOrderFeed:

    @allure.story("Order details modal opens when clicking on an order")
    def test_order_modal_opens_on_click(self, driver, register_and_login_user):
        """Проверка, что открывается всплывающее окно с деталями заказа"""
        main_page = MainPage(driver)
        main_page.click_order_feed_button()

        order_page = OrderPage(driver)
        order_page.click_order_in_list()  # Клик на заказ из списка
        assert order_page.is_order_info_displayed(), "Модальное окно с деталями заказа не открылось"

    @allure.story("Last order appears in the feed")
    def test_last_order_appears_in_feed(self, driver, register_and_login_user, create_order):
        """Проверка, что заказ пользователя отображается в ленте заказов"""

        # Создание заказа
        order_number = create_order(INGREDIENTS)

        main_page = MainPage(driver)
        main_page.click_order_feed_button()

        order_page = OrderPage(driver)
        last_order = order_page.get_last_order_number()
        assert str(order_number) in last_order, f"Ожидался заказ с номером {order_number}, но найден {last_order}"

    @allure.story("Total orders count increases after new order")
    def test_total_orders_count_increases(self, driver, register_and_login_user, create_order):
        """Проверка, что счётчик 'Выполнено за всё время' увеличивается после нового заказа"""
        main_page = MainPage(driver)
        main_page.click_order_feed_button()

        order_page = OrderPage(driver)
        total_orders_before = order_page.get_total_orders()

        # Создание нового заказа
        create_order(INGREDIENTS)

        total_orders_after = order_page.get_total_orders()
        assert total_orders_after > total_orders_before, "Счётчик 'Выполнено за всё время' не увеличился"

    @allure.story("Today's orders count increases after new order")
    def test_today_orders_count_increases(self, driver, register_and_login_user, create_order):
        """Проверка, что счётчик 'Выполнено за сегодня' увеличивается после нового заказа"""
        main_page = MainPage(driver)
        main_page.click_order_feed_button()

        order_page = OrderPage(driver)
        today_orders_before = order_page.get_today_total_orders()

        # Создание нового заказа
        create_order(INGREDIENTS)

        today_orders_after = order_page.get_today_total_orders()
        assert today_orders_after > today_orders_before, "Счётчик 'Выполнено за сегодня' не увеличился"

    @allure.story("Order number appears in 'In Progress' section after creation")
    def test_order_in_progress_after_creation(self, driver, register_and_login_user, create_order):
        """Проверка, что номер заказа появляется в разделе 'В работе'"""
        # Создание заказа
        order_number = create_order(INGREDIENTS)

        main_page = MainPage(driver)
        main_page.click_order_feed_button()

        order_page = OrderPage(driver)
        order_in_progress = order_page.get_order_in_progress()
        assert str(order_in_progress) == str(order_number), \
            f"Ожидался заказ с номером {order_number}, но найден {order_in_progress}"
