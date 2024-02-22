from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestFirstSelenium:
    def test_first_selenium(self, chrome_browser):
        chrome_browser.get('https://staging.12stz.dev/catalog/new/womencollection')

        logotype_locator = By.XPATH, "//a[@class='HeaderLogotype HeaderLogotype--theme-main']"
        logotype = chrome_browser.find_element(logotype_locator[0], logotype_locator[1])
        logotype.click()

        search_field_locator = By.XPATH, "//input[@class='SearchField__input']"
        search_field = chrome_browser.find_element(search_field_locator[0], search_field_locator[1])
        search_field.send_keys("Кофта")

        sleep(5)

    def test_waiting(self, chrome_browser):
        chrome_browser.get('https://staging.12stz.dev/catalog/new/womencollection')
        logotype_locator = By.XPATH, "//a[@class='HeaderLogotype HeaderLogotype--theme-main']"

        # element = chrome_browser.find_element(logotype_locator[0], logotype_locator[1])

        element = WebDriverWait(driver=chrome_browser, timeout=20).until(EC.element_to_be_clickable(logotype_locator))
        element.click()

    def test_action_chains(self, chrome_browser):
        chrome_browser.get('https://staging.12stz.dev/catalog/new/womencollection')

        logotype_locator = By.XPATH, "//a[@class='HeaderLogotype HeaderLogotype--theme-main']"
        element = WebDriverWait(driver=chrome_browser, timeout=20).until(EC.element_to_be_clickable(logotype_locator))

        ActionChains(chrome_browser).move_to_element(element).pause(5).click_and_hold(element).click().perform()
