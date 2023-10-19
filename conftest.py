from selenium import webdriver
import pytest
from utilities.test_data import LoginTestData


@pytest.fixture(params=['chrome', 'edge'])
def initialize_driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'edge':
        driver = webdriver.Edge()
    request.cls.driver = driver
    driver.get(LoginTestData.url)
    driver.maximize_window()
    yield
    driver.close()