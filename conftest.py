# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from test_data import LOGIN_URL
from utils.api_client import APIClient
from utils.generators import generate_random_email, generate_random_password
from utils.order_api import OrderAPI


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    browser_choice = request.param
    # Инициализация WebDriver для Chrome
    if browser_choice == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    # Инициализация WebDriver для Firefox
    elif browser_choice == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Browser '{browser_choice}' is not supported.")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.delete_all_cookies()
    driver.quit()


@pytest.fixture
def register_and_login_user(driver):
    # Создание пользователя
    email = generate_random_email()
    password = generate_random_password()
    user_data = APIClient.create_user(email, password, name="TestUser")
    token = user_data.get("accessToken")

    # Логин в браузере
    login_page = LoginPage(driver)
    login_page.open_url(LOGIN_URL)
    login_page.login(email, password)

    yield {
        "email": email,
        "password": password,
        "token": token
    }

    # Удаление пользователя после теста
    APIClient.delete_user(token)


@pytest.fixture(scope="function")
def create_order(register_and_login_user):
    order_api = OrderAPI()

    def _create_order(ingredients):
        token = register_and_login_user['token']
        order_response = order_api.create_order(token, ingredients)
        return order_response.json().get('order', {}).get('number')

    yield _create_order
