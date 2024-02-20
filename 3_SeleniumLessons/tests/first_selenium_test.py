import time

from selenium.webdriver.common.by import By


class TestFirstSelenium:
    def test_first_selenium(self, chrome_browser):
        chrome_browser.get('https://staging.12stz.dev/catalog/new/womencollection')

        logotype_locator = By.XPATH, "//a[@class='HeaderLogotype HeaderLogotype--theme-main']"
        logotype = chrome_browser.find_element(logotype_locator[0], logotype_locator[1])
        logotype.click()

        search_field_locator = By.XPATH, "//input[@class='SearchField__input']"
        search_field = chrome_browser.find_element(search_field_locator[0], search_field_locator[1])
        search_field.send_keys("Кофта")

        time.sleep(5)

