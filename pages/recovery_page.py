import allure
from pages.base_page import BasePage
from locators.recovery_page_locators import RecoveryPageLocators
from helpers.urls import FORGOT_PASSWORD_URL, RESET_PASSWORD_URL
from selenium.webdriver.support.ui import WebDriverWait


class RecoveryPage(BasePage):

    @allure.step("Открыть страницу восстановления пароля")
    def open(self):
        self.driver.get(FORGOT_PASSWORD_URL)


    @allure.step("Проверить, что открыта страница восстановления пароля")
    def is_opened(self):
        return FORGOT_PASSWORD_URL in self.driver.current_url


    @allure.step("Дождаться перехода на страницу сброса пароля")
    def wait_reset_page(self):
        WebDriverWait(self.driver, 10).until(lambda d: RESET_PASSWORD_URL in d.current_url)


    @allure.step("Проверить, что открыт экран сброса пароля")
    def is_reset_opened(self):
        return RESET_PASSWORD_URL in self.driver.current_url


    @allure.step("Ввести email для восстановления пароля")
    def fill_email(self, email):
        self.fill(RecoveryPageLocators.EMAIL_INPUT, email)


    @allure.step("Кликнуть в кнопку 'Восстановить'")
    def click_recover_button(self):
        self.click(RecoveryPageLocators.RECOVER_BUTTON)


    @allure.step("Кликнуть в кнопку 'Показать пароль'")
    def click_show_password(self):
        self.click(RecoveryPageLocators.SHOW_PASSWORD)
    

    @allure.step("Проверить отображение поля пароля")
    def get_password_container(self):
        return self.find(RecoveryPageLocators.PASSWORD_CONTAINER)