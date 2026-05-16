import allure
from pages.recovery_page import RecoveryPage
from helpers.data import get_test_email


class TestRecovery:

    @allure.title("Переход на страницу восстановления пароля")
    def test_open_recovery_page(self, driver):
        page = RecoveryPage(driver)
        page.open()

        assert page.is_opened()


    @allure.title("Ввод email и восстановление пароля")
    def test_recover_password(self, driver):
        page = RecoveryPage(driver)
        page.open()

        page.fill_email(get_test_email())
        page.click_recover_button()

        page.wait_reset_page()

        assert page.is_reset_opened()


    @allure.title("Клик по 'показать пароль' активирует поле")
    def test_show_password_active(self, driver):
        page = RecoveryPage(driver)
        page.open()

        page.fill_email(get_test_email())
        page.click_recover_button()

        page.wait_reset_page()

        page.click_show_password()
        
        classes = page.get_password_container().get_attribute("class")

        assert "input_status_active" in classes