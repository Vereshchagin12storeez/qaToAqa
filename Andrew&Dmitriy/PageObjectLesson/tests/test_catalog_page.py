from PageObjectLesson.PageObject.CatalogPage import CatalogPage


def test_click_product_card(chrome_browser):
    browser = CatalogPage(chrome_browser)

    browser.go_to_catalog_page()
    old_url = browser.get_current_url()
    browser.click_product_card()
    new_url = browser.get_current_url()

    assert old_url != new_url, "Старый адрес равен новому"
