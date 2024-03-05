from selenium.webdriver.common.by import By

from PageObjectLesson.PageObject.BasePage import BasePage


class CatalogPage(BasePage):
    PRODUCT_CARD = By.XPATH, "//div[@class='catalogCard']"

    def click_product_card(self):
        self.click(self.PRODUCT_CARD)


