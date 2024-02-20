import pytest
from selenium import webdriver


@pytest.fixture
def chrome_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    # options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    # driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
