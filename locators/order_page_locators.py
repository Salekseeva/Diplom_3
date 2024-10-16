# locators/order_page_locators.py
from selenium.webdriver.common.by import By


class OrderPageLocators:
    ORDER_IN_LIST = (By.XPATH, '//a[contains(@class, "OrderHistory_link")]')
    ORDER_INFO = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]')
    LAST_ORDER_NUMBER = (By.XPATH, '//li[contains(@class, "OrderHistory_list")]//p[contains(@class, "type_digits")]')
    TOTAL_ORDERS = (By.XPATH, '//p[contains(text(), "все время")]/following-sibling::p')
    TODAY_TOTAL_ORDERS = (By.XPATH, '//p[contains(text(), "сегодня")]/following-sibling::p')
    ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, "orderListReady") and contains(@class, "orderList")]/li')
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]')
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDERS_AT_FEED = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text "
                                "text_type_digits-default']")
    NAVIGATE = (By.XPATH, '//*[@id="root"]/div/header/nav')
