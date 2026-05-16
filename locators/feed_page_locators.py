from selenium.webdriver.common.by import By


class FeedPageLocators:

    FEED_LINK = (By.XPATH, "//a[@href='/feed']")
    ORDERS = (By.XPATH, "//li[contains(@class,'OrderHistory_listItem')]")
    ORDER_LINK = (By.CSS_SELECTOR, "a.OrderHistory_link__1iNby")

    ORDER_MODAL = (By.XPATH, "//div[contains(@class,'Modal_modal__container')]")

    TOTAL_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")

    LOADER = (By.CSS_SELECTOR, '.Modal_modal__loading__3534A')
    EMPTY_STATE = (By.XPATH, "//*[contains(text(),'Все текущие заказы готовы')]")
    IN_PROGRESS = (By.CSS_SELECTOR,".OrderFeed_orderListReady__1YFem li")