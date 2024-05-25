from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30, poll_frequency=1)

    def open(self):
        self.driver.get(self.PAGE_URL)

    def is_opened(self):
        current_url = self.driver.current_url
        self.wait.until((EC.url_to_be(self.PAGE_URL)), message=f"Actual page is {current_url}, "
                                                                   f"Expected page is  {self.PAGE_URL}")
