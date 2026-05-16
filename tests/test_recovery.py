import allure
from pages.recovery_page import RecoveryPage
from helpers.data import get_test_email
from helpers.urls import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait


class TestRecovery:

    @allure.title("Переход на страницу восстановления пароля")
    def test_open_recovery_page(self, driver):
        page = RecoveryPage(driver)
        page.open()

        assert (BASE_URL + "/forgot-password") in driver.current_url


    @allure.title("Ввод email и восстановление пароля")
    def test_recover_password(self, driver):
        page = RecoveryPage(driver)
        page.open()

        page.fill_email(get_test_email())
        page.click_recover_button()

        WebDriverWait(driver, 10).until(lambda d: "/reset-password" in d.current_url)

        assert (BASE_URL + "/reset-password") in driver.current_url


    @allure.title("Клик по 'показать пароль' активирует поле")
    def test_show_password_active(self, driver):
        page = RecoveryPage(driver)
        page.open()

        page.fill_email(get_test_email())
        page.click_recover_button()

        WebDriverWait(driver, 10).until(lambda d: "/reset-password" in d.current_url)

        password_container = page.get_password_container()

        initial_class = password_container.get_attribute("class")

        page.click_show_password()

        WebDriverWait(driver, 5).until(lambda d: "input_status_active" in password_container.get_attribute("class"))

        updated_class = password_container.get_attribute("class")

        assert "input_type_text" in updated_class
        assert "input_status_active" in updated_class
        assert initial_class != updated_class