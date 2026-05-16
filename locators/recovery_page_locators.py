from selenium.webdriver.common.by import By


class RecoveryPageLocators:

    RECOVER_LINK = (By.XPATH, "//a[@href='/forgot-password']")

    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    
    RECOVER_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")

    SHOW_PASSWORD = (By.XPATH, "//div[contains(@class,'input__icon-action')]")

    PASSWORD_CONTAINER = (By.CSS_SELECTOR, "div.input.input_size_default")

    