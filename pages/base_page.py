from selenium import webdriver

class BasePage:
    """
    Contains methods common to all pages
    """

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)
    
    def click(self, locator):
        self.driver.find_element(*locator).click()

    def set_value(self, locator, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text
    
    def get_title(self):
        return self.driver.title