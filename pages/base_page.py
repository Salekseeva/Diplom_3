# pages/base_page.py
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def find_element_clickable(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator),
                                                         message=f"Can't find element by locator {locator}")

    def find_element_visibility(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                                         message=f'Cant find element by locator {locator}')

    def find_element_not_visibility(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator),
                                                         message=f'Cant find element by locator {locator}')

    def wait_for_element_is_clickable(self, locator, timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_element_with_wait(self, locator):
        self.find_element_visibility(locator, 20)
        return self.find_element_with_wait(locator)

    def click_element_compatible(self, locator):
        """Выполняет клик в зависимости от браузера:
        - Использует стандартный клик для Chrome.
        - Использует JavaScript клик для Firefox."""
        browser_name = self.driver.capabilities['browserName'].lower()
        if 'chrome' in browser_name:
            self.click_element_if_visible(locator)
        elif 'firefox' in browser_name:
            self.click_element_if_clickable(locator)
        else:
            self.click_element_if_visible(locator)

    def click_element_if_visible(self, locator):
        element = self.find_element_visibility(locator, 20)
        element.click()

    def click_element_if_clickable(self, locator):
        click_element = self.find_element_visibility(locator, 20)
        self.driver.execute_script("arguments[0].click();", click_element)

    def set_text(self, locator, text):
        element = self.find_element_visibility(locator, 10)
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element_visibility(locator, 20)
        return element.text

    def drag_and_drop(self, source_locator, target_locator):
        """Перетаскивание элемента с одного места на другое."""
        source_element = self.find_element_clickable(source_locator)
        target_element = self.find_element_clickable(target_locator)

        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(source_element, target_element).perform()

    def get_attribute(self, locator, attribute):
        element = self.find_element_clickable(locator, 20)
        return element.get_attribute(attribute)

    def get_element_attribute(self, locator, attribute):
        element = self.find_element_clickable(locator, 20)
        return element.get_attribute(attribute)

    def find_until_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(locator))

    def wait_for_modal_overlay_to_disappear(self):
        self.find_element_not_visibility(MainPageLocators.MODAL_OVERLAY_ELEMENT, 30)

    def open_url(self, url):
        self.driver.get(url)
