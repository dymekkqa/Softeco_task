import pytest
from pages.home_page import HomePage
from pages.bank_manager_page import BankManagerPage
from pages.customer_page import CustomerPage
from config.data import Data


class BaseTest:
    home_page: HomePage
    bank_manager_page: BankManagerPage
    customer_page: CustomerPage
    data: Data

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.home_page = HomePage(driver)
        request.cls.customer_page = CustomerPage(driver)
        request.cls.bank_manager_page = BankManagerPage(driver)
