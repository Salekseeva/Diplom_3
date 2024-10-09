# tests/test_profile.py
import pytest
import allure
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.api_client import APIClient
from utils.generators import generate_random_email, generate_random_password
from test_data import LOGIN_URL
import time


@allure.feature("Profile Test")
@pytest.mark.usefixtures("browser")
class TestProfile:

    @allure.title("Login, navigate to profile and verify actions")
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

    @allure.title("Login, navigate to profile and verify actions")
    @allure.step("Test Profile Navigation and Logout")
    def test_profile_navigation_and_logout(self, browser):
        login_page = LoginPage(browser)
        profile_page = ProfilePage(browser)

        with allure.step("Open login page"):
            login_page.navigate_to_login_page(LOGIN_URL)

        with allure.step("Login with valid credentials"):
            login_page.login(self.email, self.password)

        with allure.step("Wait for the main page to load"):
            time.sleep(2)  # Небольшая пауза для загрузки страницы

        with allure.step("Click on 'Личный Кабинет'"):
            profile_page.open_profile()

        with allure.step("Navigate to 'История заказов'"):
            profile_page.go_to_order_history()
            assert profile_page.is_order_history_active(), "Order history link is not active."

        with allure.step("Logout from the account"):
            profile_page.logout()
            assert browser.current_url == LOGIN_URL, "Did not navigate back to login page after logout."
