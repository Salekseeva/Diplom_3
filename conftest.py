# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def browser(request):
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

    # Настраиваем неявное ожидание для всех страниц
    driver.implicitly_wait(10)
    # Возвращаем объект WebDriver в тест
    yield driver
    # Закрываем браузер после завершения теста
    driver.quit()

# Параметризация тестов для двух браузеров: Chrome и Firefox
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g.chrome or firefox")

#@pytest.fixture
#def get_browser(request):
#    return request.config.getoption("--browser")
