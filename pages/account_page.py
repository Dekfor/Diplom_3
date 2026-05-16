import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from helpers.urls import BASE_URL, ACCOUNT_URL, ORDER_HISTORY, LOGIN_URL
from selenium.webdriver.support.ui import WebDriverWait

class AccountPage(BasePage):

    @allure.step("Открыть личный кабинет")
    def open(self):
        self.driver.get(BASE_URL)
        self.click(AccountPageLocators.PERSONAL_ACCOUNT)
        WebDriverWait(self.driver, 10).until(lambda d: "/account" in d.current_url)
    
    @allure.step("Проверить, что открыт личный кабинет")
    def is_opened(self):
        return ACCOUNT_URL in self.driver.current_url

    @allure.step("Открыть историю заказа")
    def open_history(self):
        self.click(AccountPageLocators.HISTORY)
        WebDriverWait(self.driver, 10).until(lambda d: "/order-history" in d.current_url)

    @allure.step("Проверить, что открыта история заказов")
    def is_history_opened(self):
        return ORDER_HISTORY in self.driver.current_url

    @allure.step("Выйти из аккаунта")
    def exit(self):
        self.click(AccountPageLocators.EXIT)
        WebDriverWait(self.driver, 10).until(lambda d: "/login" in d.current_url)

    @allure.step("Проверить, что открыта страница авторизации")
    def is_login_opened(self):
        return LOGIN_URL in self.driver.current_url