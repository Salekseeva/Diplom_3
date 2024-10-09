# locators/profile_page_locators.py
from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')
    ORDER_HISTORY_LINK = (By.XPATH, '//a[text()="История заказов"]')
    EXIT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
