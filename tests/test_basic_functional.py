import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.api_client import APIClient
from utils.generators import generate_random_email, generate_random_password
from test_data import LOGIN_URL, MAIN_PAGE_URL, FEED_URL
# import time


@allure.feature("Basic Functional Test")
@pytest.mark.usefixtures("browser")
class TestBasicFunctional:

    @pytest.fixture(autouse=True)
    def setup_and_teardown(self):
        # Генерация данных пользователя
        self.email = generate_random_email()
        self.password = generate_random_password()
        self.name = "TestUser"

        # Создание пользователя через API
        user_data = APIClient.create_user(self.email, self.password, self.name)
        self.token = user_data.get("accessToken")

        yield

        # Удаление пользователя после завершения теста
        if self.token:
            APIClient.delete_user(self.token)

    @allure.story("Click on Constructor")
    @allure.step("Test Constructor Navigation")
    def test_constructor_navigation(self, browser):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)

        with allure.step("Open login page"):
            login_page.open_page(LOGIN_URL)

        with allure.step("Login with valid credentials"):
            login_page.enter_email(self.email)
            login_page.enter_password(self.password)
            login_page.submit_login()

        with allure.step("Click on 'Конструктор'"):
            main_page.click_constructor_button()
            assert browser.current_url == MAIN_PAGE_URL, "Did not navigate to the constructor page."

    @allure.story("Click on Order Feed")
    @allure.step("Test Order Feed Navigation")
    def test_order_feed_navigation(self, browser):
        main_page = MainPage(browser)

        with allure.step("Open main page"):
            main_page.open_page(MAIN_PAGE_URL)

        with allure.step("Click on 'Лента заказов'"):
            main_page.click_order_feed_button()
            assert browser.current_url == FEED_URL, "Did not navigate to the order feed."

    @allure.story("Click on Ingredient and Check Modal")
    @allure.step("Test Ingredient Modal Popup")
    def test_ingredient_modal(self, browser):
        main_page = MainPage(browser)

        with allure.step("Open main page"):
            main_page.open_page(MAIN_PAGE_URL)

        with allure.step("Click on an ingredient"):
            main_page.click_ingredient_details()
            assert main_page.is_ingredient_modal_open(), "Ingredient modal did not open."

    @allure.story("Close Ingredient Modal")
    @allure.step("Test Closing Ingredient Modal")
    def test_close_ingredient_modal(self, browser):
        main_page = MainPage(browser)

        with allure.step("Open main page"):
            main_page.open_page(MAIN_PAGE_URL)

        with allure.step("Click on an ingredient"):
            main_page.click_ingredient_details()

        with allure.step("Close ingredient modal"):
            main_page.close_ingredient_details()
            assert not main_page.is_ingredient_modal_open(), "Ingredient modal did not close."

    @allure.story("Logged-in User Can Place an Order")
    @allure.step("Test Placing an Order")
    def test_place_order(self, browser):
        login_page = LoginPage(browser)
        main_page = MainPage(browser)

        with allure.step("Open login page"):
            login_page.open_page(LOGIN_URL)

        with allure.step("Login with valid credentials"):
            login_page.enter_email(self.email)
            login_page.enter_password(self.password)
            login_page.submit_login()

        with allure.step("Drag an ingredient to create a burger"):
            main_page.add_ingredient_to_order()

        with allure.step("Click 'Place Order'"):
            main_page.place_order()
            assert main_page.is_order_in_progress(), "Order did not start processing."
