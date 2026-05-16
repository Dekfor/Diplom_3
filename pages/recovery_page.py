from pages.base_page import BasePage
from locators.recovery_page_locators import RecoveryPageLocators
from helpers.urls import FORGOT_PASSWORD_URL


class RecoveryPage(BasePage):

    def open(self):
        self.driver.get(FORGOT_PASSWORD_URL)

    def click_recover_link(self):
        self.click(RecoveryPageLocators.RECOVER_LINK)

    def fill_email(self, email):
        self.fill(RecoveryPageLocators.EMAIL_INPUT, email)

    def click_recover_button(self):
        self.click(RecoveryPageLocators.RECOVER_BUTTON)

    def click_show_password(self):
        self.click(RecoveryPageLocators.SHOW_PASSWORD)
    
    def get_password_container(self):
        return self.find(RecoveryPageLocators.PASSWORD_CONTAINER)