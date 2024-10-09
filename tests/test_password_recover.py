# tests/test_password_recovery.py
import pytest
from pages.login_page import LoginPage
from pages.recovery_page import RecoveryPage
from utils.generators import generate_random_email, generate_random_password
from test_data import LOGIN_URL


@pytest.mark.usefixtures("browser")
class TestPasswordRecovery:

    def test_password_recovery(self, browser):
        login_page = LoginPage(browser)
        recovery_page = RecoveryPage(browser)

        # Открыть страницу входа
        login_page.navigate_to_login_page(LOGIN_URL)
        # Нажать на ссылку "Восстановить пароль"
        login_page.click_forgot_password()

        # Генерация случайного email
        random_email = generate_random_email()
        # Ввод email для восстановления
        recovery_page.enter_email(random_email)
        # Нажать кнопку "Восстановить"
        recovery_page.click_recover_button()

        # Ожидание появления элемента для показа пароля
#        recovery_page.wait_for_show_password_element()

        # Генерация случайного пароля
        random_password = generate_random_password(8)
        # Ввод сгенерированного пароля в поле
        recovery_page.enter_password(random_password)

        # Нажать на кнопку отображения пароля
        recovery_page.click_show_password()

        # Проверка, что тип поля пароля изменился на 'text'
        assert recovery_page.is_password_visible(), "Пароль не отображается текстом."

        # Проверка, что к полю пароля добавился класс 'input_status_active'
        assert recovery_page.is_password_active(), "К полю пароля не добавлен класс активности."
