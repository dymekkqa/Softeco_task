import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope='function', autouse=True)
def driver(request):
    options = ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    request.cls.driver = driver
    yield driver

