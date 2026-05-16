from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_overlay_disappear(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")))
        except TimeoutException:
            pass

    def find(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait_overlay_disappear()

        element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator))

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)

        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def fill(self, locator, value):
        element = self.find(locator)
        element.clear()
        element.send_keys(value)
