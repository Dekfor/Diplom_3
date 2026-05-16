from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR = (By.XPATH, "//a[@href='/']")
    FEED = (By.XPATH, "//a[@href='/feed']")
    ACCOUNT = (By.XPATH, "//a[@href='/account']")

    LOGIN_BUTTON = (By.XPATH, "//button[contains(.,'Войти')]")
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")

    INGREDIENT = (By.XPATH, "(//a[contains(@class,'BurgerIngredient_ingredient')])[1]")
    
    MODAL = (By.XPATH, "//div[contains(@class,'Modal_modal__contentBox')]")
    MODAL_CLOSE = (By.CSS_SELECTOR, "button[class*='Modal_modal__close']")

    ORDER_MODAL_NUMBER = (By.XPATH, "//h2[contains(@class,'Modal_modal__title')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    COUNTER = (By.XPATH, "//p[contains(@class,'counter_counter')]")

    DROP_ZONE = (By.XPATH, "//section//div[contains(@class,'constructor-element_pos_top')]/ancestor::section")


