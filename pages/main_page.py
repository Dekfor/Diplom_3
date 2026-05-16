from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from helpers.urls import BASE_URL

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    def open(self):
        self.driver.get(BASE_URL)

    def open_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR)

    def is_constructor_active(self):
        return self.driver.current_url.rstrip("/") == BASE_URL.rstrip("/")    

    def open_feed(self):
        self.click(MainPageLocators.FEED)

    def open_account(self):
        self.click(MainPageLocators.ACCOUNT)

    def click_ingredient(self):
        ingredient = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.INGREDIENT))
        self.driver.execute_script("arguments[0].click();", ingredient)

    def drag_ingredient(self, locator):
        ingredient = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

        target = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.DROP_ZONE))

        ActionChains(self.driver) \
            .click_and_hold(ingredient) \
            .move_to_element(target) \
            .release() \
            .perform()
        
    def is_modal_open(self):
        return (len(self.driver.find_elements(*MainPageLocators.MODAL)) > 0 and self.driver.find_element(*MainPageLocators.MODAL).is_displayed())
    
    def wait_order_modal(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(MainPageLocators.MODAL))

    def close_modal(self):
        close_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE))
        self.driver.execute_script("arguments[0].click();", close_btn)

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.MODAL))

    def get_counter_value(self):
        counter = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.COUNTER))
        return int(counter.text)

    def wait_counter_change(self, old_value):
        WebDriverWait(self.driver, 10).until(lambda d: int(d.find_element(*MainPageLocators.COUNTER).text) > old_value)

    def login(self, email, password):
        self.click(MainPageLocators.LOGIN_BUTTON)

        email_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.EMAIL_INPUT))
        email_input.clear()
        email_input.send_keys(email)

        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(MainPageLocators.PASSWORD_INPUT))
        password_input.clear()
        password_input.send_keys(password)

        self.click(MainPageLocators.LOGIN_SUBMIT_BUTTON)

    def create_order(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    def wait_order_number_ready(self):
        WebDriverWait(self.driver, 20).until(
            lambda d: (
                (el := d.find_element(*MainPageLocators.ORDER_MODAL_NUMBER))
                and el.text.strip().isdigit()
                and el.text.strip() != "9999"
            )
        )

    def get_order_number(self):
        return self.driver.find_element(*MainPageLocators.ORDER_MODAL_NUMBER).text

    def close_order_modal(self):
        close_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.MODAL_CLOSE))
        self.driver.execute_script("arguments[0].click();", close_btn)

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.MODAL))
        