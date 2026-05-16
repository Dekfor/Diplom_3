import pytest
from selenium import webdriver
from helpers.urls import BASE_URL
from helpers.user import create_user, delete_user


class WebDriverFactory:

    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == "chrome":
            return webdriver.Chrome()
        elif browser_name == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError(f"Browser {browser_name} is not supported")


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):

    driver = WebDriverFactory.get_webdriver(request.param)
    driver.get(BASE_URL)

    yield driver
    driver.quit()

@pytest.fixture
def user():
    payload, token = create_user()
    yield payload

    delete_user(token)