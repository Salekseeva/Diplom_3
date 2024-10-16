# locators/main_page_locators.py
from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]')
    ORDER_FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]')
    INGREDIENT = (By.XPATH, '//a[contains(@class, "BurgerIngredient_ingredient")]')
    INGREDIENT_DETAILS = (By.XPATH, '//section//h2[text()="Детали ингредиента"]/ancestor::section')
    DETAILS_CLOSE = (By.XPATH, '//button[contains(@class, "close_modified")]')
    INGREDIENT_BUN = (By.XPATH, '//img[@alt="Флюоресцентная булка R2-D3"]')
    CREATE_BURGER = (By.XPATH, '//span[contains(text(), "Перетяните булочку")]')
    PLACE_ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]')
    ORDER_IN_PROGRESS = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]')
    # Элемент, перекрывающий всю страницу и иногда не дающий нажать на кнопку
    MODAL_OVERLAY_ELEMENT = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]")
