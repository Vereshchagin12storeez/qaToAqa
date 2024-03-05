from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:
    def __init__(self, browser):
        self.driver = browser

    def get_current_url(self):
        return self.driver.current_url

    def go_to_catalog_page(self):
        self.driver.get("https://staging.12stz.dev/catalog")

    def find_element(self, locator):
        return WebDriverWait(self.driver, 20, ignored_exceptions=(StaleElementReferenceException,)
                             ).until(EC.presence_of_element_located(locator),
                                     message=f"Can't find element by locator {locator}")

    def wait_element_visibility(self, locator, time):
        return WebDriverWait(self.driver, time, ignored_exceptions=(StaleElementReferenceException,)
                             ).until(EC.visibility_of_element_located(locator),
                                     message=f"Can't find element by locator {locator}")

    def wait_element_clickability(self, locator):
        return WebDriverWait(self.driver, 20, ignored_exceptions=(StaleElementReferenceException,)
                             ).until(EC.element_to_be_clickable(locator),
                                     message=f"Can't find element by locator {locator}")

    def hover_to_element(self, locator):
        element = self.wait_element_clickability(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def hover_click(self, locator):
        element = self.wait_element_clickability(locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    def click(self, locator):
        element = self.wait_element_clickability(locator)
        element.click()

