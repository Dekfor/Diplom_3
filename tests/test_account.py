import allure
from helpers.order_flow import login
from helpers.urls import ACCOUNT_URL, ORDER_HISTORY
from pages.account_page import AccountPage


class TestAccount:

    @allure.title("Переход в личный кабинет")
    def test_open_account(self, driver, user):

        login(driver, user)

        page = AccountPage(driver)
        page.open()

        assert ACCOUNT_URL in driver.current_url


    @allure.title("Переход в историю заказов")
    def test_open_history(self, driver, user):

        login(driver, user)

        page = AccountPage(driver)
        page.open()
        page.open_history()

        assert ORDER_HISTORY in driver.current_url


    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, user):

        login(driver, user)

        page = AccountPage(driver)
        page.open()
        page.exit()

        assert "/login" in driver.current_url