import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from helpers.order_flow import create_order
from helpers.data import skip_if_firefox

class TestMain:

    @allure.title("Переход в конструктор")
    def test_constructor(self, driver):
        page = MainPage(driver)
        page.open()

        page.open_constructor()

        assert page.is_constructor_active()


    @allure.title("Лента заказов")
    def test_feed(self, driver):
        page = MainPage(driver)
        page.open()

        page.open_feed()

        assert "feed" in driver.current_url


    @allure.title("Открытие модалки ингредиента")
    def test_open_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.open()

        page.click_ingredient()

        assert page.is_modal_open()


    @allure.title("Закрытие модалки ингредиента")
    def test_close_modal(self, driver):
        page = MainPage(driver)
        page.open()

        page.click_ingredient()
        page.close_modal()

        assert not page.is_modal_open()


    @allure.title("Добавление ингредиента увеличивает счетчик")
    def test_counter_increase(self, driver):

        skip_if_firefox(driver)

        page = MainPage(driver)
        page.open()

        before = page.get_counter_value()
        page.drag_ingredient(MainPageLocators.INGREDIENT)
        page.wait_counter_change(before)
        after = page.get_counter_value()

        assert after >= before + 1


    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_create_order(self, driver, user):

        order_number = create_order(driver, user)

        assert order_number.isdigit()