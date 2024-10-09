# pages/base_page.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    def enter_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def drag_and_drop(self, source_locator, target_locator):
        """Перетаскивание элемента с одного места на другое."""
        source_element = self.wait_for_element(source_locator)
        target_element = self.wait_for_element(target_locator)

        action_chains = ActionChains(self.browser)
        action_chains.drag_and_drop(source_element, target_element).perform()

    def get_attribute(self, locator, attribute):
        element = self.wait_for_element(locator)
        return element.get_attribute(attribute)

    # Метод для нахождения элемента
    def find_element(self, locator):
        return self.browser.find_element(*locator)

    # Метод для получения атрибута элемента
    def get_element_attribute(self, locator, attribute):
        element = self.find_element(locator)
        return element.get_attribute(attribute)

        # Метод для клика по элементу с использованием JavaScript
    def click_element_with_js(self, locator):
        element = self.find_element(locator)
        self.browser.execute_script("arguments[0].click();", element)

    def open_page(self, url):
        self.browser.get(url)
#        self.driver.get(url)
