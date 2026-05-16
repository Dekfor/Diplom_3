import allure
from helpers.order_flow import login
from pages.account_page import AccountPage


class TestAccount:

    @allure.title("Переход в личный кабинет")
    def test_open_account(self, driver, user):

        login(driver, user)

        page = AccountPage(driver)
        page.open()

        assert page.is_opened()


    @allure.title("Переход в историю заказов")
    def test_open_history(self, driver, user):

        login(driver, user)

        page = AccountPage(driver)
        page.open()
        page.open_history()

        assert page.is_history_opened()


    @allure.title("Выход из аккаунта")
    def test_logout(self, driver, user):

        login(driver, user)

        page = AccountPage(driver)
        page.open()
        page.exit()

        assert page.is_login_opened()