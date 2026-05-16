from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from helpers.urls import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait

class AccountPage(BasePage):

    def open(self):
        self.driver.get(BASE_URL)
        self.click(AccountPageLocators.PERSONAL_ACCOUNT)
        WebDriverWait(self.driver, 10).until(lambda d: "/account" in d.current_url)

    def open_history(self):
        self.click(AccountPageLocators.HISTORY)
        WebDriverWait(self.driver, 10).until(lambda d: "/order-history" in d.current_url)

    def exit(self):
        self.click(AccountPageLocators.EXIT)
        WebDriverWait(self.driver, 10).until(lambda d: "/login" in d.current_url)