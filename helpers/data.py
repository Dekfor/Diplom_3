import pytest

def get_test_email():
    return "test@test.com"

def skip_if_firefox(driver):
    if driver.capabilities['browserName'] == 'firefox':
        pytest.skip("Drag and drop не работает в Firefox")