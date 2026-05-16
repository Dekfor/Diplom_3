from selenium.webdriver.common.by import By


class AccountPageLocators:

    PERSONAL_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")
    HISTORY = (By.XPATH, "//a[@href='/account/order-history']")
    EXIT = (By.XPATH, "//button[contains(text(),'Выход')]")

    