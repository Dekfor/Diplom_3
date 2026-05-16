from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.feed_page_locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    def open_feed(self):
        self.click(FeedPageLocators.FEED_LINK)

    def wait_feed_loaded(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(FeedPageLocators.TOTAL_COUNTER))

    def click_first_order(self):
        first_order = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(FeedPageLocators.ORDER_LINK))
        first_order.click()

    def is_order_modal_open(self):
        return len(self.driver.find_elements(*FeedPageLocators.ORDER_MODAL)) > 0

    def get_feed_orders_text(self):
        return [o.text for o in self.driver.find_elements(*FeedPageLocators.ORDERS)]

    def get_total_counter(self):
        return int(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(FeedPageLocators.TOTAL_COUNTER)).text.strip())

    def get_today_counter(self):
        return int(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(FeedPageLocators.TODAY_COUNTER)).text.strip())

    def get_in_progress_orders_text(self):
        elements = self.driver.find_elements(*FeedPageLocators.IN_PROGRESS)
        texts = []
        for el in elements:
            txt = el.text.strip()
            if txt and txt.isdigit():
                texts.append(txt)

        return texts

    def wait_order_in_progress(self, order_number):
        expected = str(int(order_number))

        def _check(driver):
            texts = [
                el.text.strip()
                for el in driver.find_elements(*FeedPageLocators.IN_PROGRESS)
            ]

            return expected in texts

        WebDriverWait(self.driver, 60, poll_frequency=0.5).until(_check)

    def wait_loader_disappear(self):
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element_located(FeedPageLocators.LOADER))

    def wait_feed_ready(self):
        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located(FeedPageLocators.LOADER))

        WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located(FeedPageLocators.EMPTY_STATE))
        