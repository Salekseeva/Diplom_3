# tests/test_profile.py
import pytest
import allure
from pages.profile_page import ProfilePage
from test_data import LOGIN_URL


@allure.feature("Profile Test")
@pytest.mark.usefixtures("driver", "register_and_login_user")
class TestProfile:
    @allure.title("Login, navigate to profile and verify actions")
    @allure.step("Test Profile Navigation and Logout")
    def test_profile_navigation_and_logout(self, driver, register_and_login_user):
        profile_page = ProfilePage(driver)

        with allure.step("Click on 'Личный Кабинет'"):
            profile_page.wait_for_modal_overlay_to_disappear()
            profile_page.open_profile()

        with allure.step("Navigate to 'История заказов'"):
            profile_page.go_to_order_history()
            assert profile_page.is_order_history_active(), "Order history link is not active."

        with allure.step("Logout from the account"):
            profile_page.logout()
            assert driver.current_url == LOGIN_URL, "Did not navigate back to login page after logout."
