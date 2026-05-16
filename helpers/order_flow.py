from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from helpers.data import skip_if_firefox


def login(driver, user):
    main = MainPage(driver)
    main.open()
    main.login(user['email'], user['password'])

    WebDriverWait(driver, 10).until(lambda d: "/login" not in d.current_url)

def normalize_order_number(number: str) -> str:
    return str(int(number))


def create_order(driver,user):
    #"drag and drop будет работать только в хроме,то что в мозиле он не работает - это будет ок"
    skip_if_firefox(driver)

    main = MainPage(driver)

    main.open()
    main.login(user['email'], user['password'])

    main.drag_ingredient(MainPageLocators.INGREDIENT)
    main.create_order()

    main.wait_order_number_ready()

    order_number = normalize_order_number(main.get_order_number())

    main.close_modal()

    return order_number
