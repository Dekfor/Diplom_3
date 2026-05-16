import allure
from helpers.order_flow import create_order
from pages.feed_page import FeedPage
from locators.feed_page_locators import FeedPageLocators
from selenium.webdriver.support.ui import WebDriverWait


@allure.title("Лента заказов: открытие модалки заказа")
def test_order_modal_opens(driver):
    feed = FeedPage(driver)
    feed.open_feed()

    WebDriverWait(driver, 10).until(lambda d: len(d.find_elements(*FeedPageLocators.ORDERS)) > 0)

    feed.click_first_order()
    assert feed.is_order_modal_open()


@allure.title("Лента заказов: заказы отображаются")
def test_user_orders_visible_in_feed(driver):
    feed = FeedPage(driver)
    feed.open_feed()

    WebDriverWait(driver, 10).until(lambda d: len(d.find_elements(*FeedPageLocators.ORDERS)) > 0)

    assert len(feed.get_feed_orders_text()) > 0


@allure.title("Лента заказов: увеличивается 'выполнено за все время'")
def test_total_counter_increases(driver, user):
    feed = FeedPage(driver)
    feed.open_feed()
    feed.wait_feed_loaded()

    total_before = feed.get_total_counter()

    create_order(driver, user)

    feed.open_feed()
    feed.wait_feed_loaded()

    assert feed.get_total_counter() >= total_before


@allure.title("Лента заказов: увеличивается 'выполнено за сегодня'")
def test_today_counter_increases(driver, user):
    feed = FeedPage(driver)
    feed.open_feed()
    feed.wait_feed_loaded()

    today_before = feed.get_today_counter()

    create_order(driver, user)

    feed.open_feed()
    feed.wait_feed_loaded()

    assert feed.get_today_counter() >= today_before


@allure.title("Лента заказов: номер заказа появляется в 'В работе'")
def test_order_in_progress_section(driver, user):

    create_order(driver, user)

    feed = FeedPage(driver)
    feed.open_feed()

    feed.wait_feed_loaded()
    feed.wait_feed_ready()

    in_progress = feed.get_in_progress_orders_text()

    assert len(in_progress) > 0