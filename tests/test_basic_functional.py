import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from test_data import LOGIN_URL, MAIN_PAGE_URL, FEED_URL


@allure.feature("Basic Functional Test")
@pytest.mark.usefixtures("driver")
class TestBasicFunctional:
    @allure.story("Click on Constructor")
    @allure.step("Test Constructor Navigation")
    def test_constructor_navigation(self, driver):
        login_page = LoginPage(driver)
#        main_page = MainPage(driver)

        with allure.step("Open login page"):
            login_page.open_url(LOGIN_URL)

        with allure.step("Click on 'Конструктор'"):
            login_page.click_constructor_button()
            assert driver.current_url == MAIN_PAGE_URL, "Did not navigate to the constructor page."

    @allure.story("Click on Order Feed")
    @allure.step("Test Order Feed Navigation")
    def test_order_feed_navigation(self, driver):
        main_page = MainPage(driver)

        with allure.step("Open main page"):
            main_page.open_url(MAIN_PAGE_URL)

        with allure.step("Click on 'Лента заказов'"):
            main_page.click_order_feed_button()
            assert driver.current_url == FEED_URL, "Did not navigate to the order feed."

    @allure.story("Click on Ingredient and Check Modal")
    @allure.step("Test Ingredient Modal Popup")
    def test_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        with allure.step("Open main page"):
            main_page.open_url(MAIN_PAGE_URL)

        with allure.step("Click on an ingredient"):
            main_page.click_ingredient_details()
            assert main_page.is_ingredient_modal_open(), "Ingredient modal did not open."

    @allure.story("Close Ingredient Modal")
    @allure.step("Test Closing Ingredient Modal")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)

        with allure.step("Open main page"):
            main_page.open_url(MAIN_PAGE_URL)

        with allure.step("Click on an ingredient"):
            main_page.click_ingredient_details()

        with allure.step("Close ingredient modal"):
            main_page.close_ingredient_details()
            assert not main_page.is_ingredient_modal_open(), "Ingredient modal did not close."

    @pytest.mark.usefixtures("register_and_login_user")
    @allure.story("Logged-in User Can Place an Order")
    @allure.step("Test Placing an Order")
    def test_place_order(self, driver, register_and_login_user):
#        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        with allure.step("Drag an ingredient to create a burger"):
            main_page.add_ingredient_to_order()

        with allure.step("Click 'Place Order'"):
            main_page.place_order()
            assert main_page.is_order_in_progress(), "Order did not start processing."
