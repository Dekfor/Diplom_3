import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from helpers.urls import BASE_URL

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(BASE_URL)

    @allure.step("Переключиться на конструктор бургеров")
    def open_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR)

    @allure.step("Проверить, что открыт конструктор")
    def is_constructor_active(self):
        return self.driver.current_url.rstrip("/") == BASE_URL.rstrip("/")    

    @allure.step("Открыть 'Ленту заказов'")
    def open_feed(self):
        self.click(MainPageLocators.FEED)

    @allure.step("Открыть 'Личный кабинет'")
    def open_account(self):
        self.click(MainPageLocators.ACCOUNT)

    @allure.step("Кликнуть на ингредиент")
    def click_ingredient(self):
        ingredient = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.INGREDIENT))
        self.driver.execute_script("arguments[0].click();", ingredient)

    @allure.step("Перетащить ингредиент в конструктор")
    def drag_ingredient(self, locator):
        ingredient = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

        target = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.DROP_ZONE))

        ActionChains(self.driver) \
            .click_and_hold(ingredient) \
            .move_to_element(target) \
            .release() \
            .perform()
        
    @allure.step("Проверить открытие модалки ингредиента")
    def is_modal_open(self):
        return (len(self.driver.find_elements(*MainPageLocators.MODAL)) > 0 and self.driver.find_element(*MainPageLocators.MODAL).is_displayed())

    @allure.step("Закрыть модалку")
    def close_modal(self):
        close_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE))
        self.driver.execute_script("arguments[0].click();", close_btn)

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.MODAL))

    @allure.step("Дождаться изменения счетчика ингредиентов")
    def wait_counter_change(self, old_value):
        WebDriverWait(self.driver, 10).until(lambda d: int(d.find_element(*MainPageLocators.COUNTER).text) > old_value)

    @allure.step("Получить значение счетчика ингредиентов")
    def get_counter_value(self):
        counter = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.COUNTER))
        return int(counter.text)

    @allure.step("Авторизоваться на сайте")
    def login(self, email, password):
        self.click(MainPageLocators.LOGIN_BUTTON)

        email_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)

        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)

        self.click(MainPageLocators.LOGIN_SUBMIT_BUTTON)

    @allure.step("Создать заказ")
    def create_order(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Дождаться появления номера заказа")
    def wait_order_number_ready(self):
        WebDriverWait(self.driver, 20).until(
            lambda d: (
                (el := d.find_element(*MainPageLocators.ORDER_MODAL_NUMBER))
                and el.text.strip().isdigit()
                and el.text.strip() != "9999"
            )
        )

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        return self.driver.find_element(*MainPageLocators.ORDER_MODAL_NUMBER).text

        