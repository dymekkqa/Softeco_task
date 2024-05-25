from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class BankManagerPage(BasePage):
    PAGE_URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'

    ADD_CUSTOMER_BUTTON = ("xpath", '//button[@ng-click="addCust()"]')
    OPEN_ACCOUNT_BUTTON = ("xpath", '//button[@ng-click="openAccount()"]')
    SHOW_CUSTOMERS_BUTTON = ("xpath", '//button[@ng-click="showCust()"]')
    FIRST_NAME_INPUT = ('xpath', '//input[@ng-model="fName"]')
    LAST_NAME_INPUT = ('xpath', '//input[@ng-model="lName"]')
    POST_CODE_INPUT = ("xpath", '//input[@ng-model="postCd"]')
    SUBMIT_BUTTON = ("xpath", '//button[@type="submit"]')
    SELECT_USER_DROPDOWN = ("id", 'userSelect')

    def click_add_customer_button(self):
        self.wait.until(EC.visibility_of_element_located(self.ADD_CUSTOMER_BUTTON),
                        message="Button 'ADD_CUSTOMER_BUTTON' is not found")
        button = self.wait.until((EC.element_to_be_clickable(self.ADD_CUSTOMER_BUTTON)),
                                 message="Button 'ADD_CUSTOMER_BUTTON' is not clickable")
        button.click()

    def click_open_account_button(self):
        self.wait.until(EC.visibility_of_element_located(self.OPEN_ACCOUNT_BUTTON),
                        message="Button 'OPEN_ACCOUNT_BUTTON' is not found")
        button = self.wait.until((EC.element_to_be_clickable(self.OPEN_ACCOUNT_BUTTON)),
                                 message="Button 'OPEN_ACCOUNT_BUTTON' is not clickable")
        button.click()

    def click_show_customers_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SHOW_CUSTOMERS_BUTTON),
                        message="Button 'SHOW_CUSTOMERS_BUTTON' is not found")
        button = self.wait.until((EC.element_to_be_clickable(self.SHOW_CUSTOMERS_BUTTON)),
                                 message="Button 'SHOW_CUSTOMERS_BUTTON' is not clickable")
        button.click()

    def enter_first_name(self, first_name):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT),
                        message="Input 'FIRST_NAME_INPUT' not found")
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_INPUT)).send_keys(first_name)
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_INPUT, first_name))

    def enter_last_name(self, last_name):
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_INPUT), message="Input 'LAST_NAME_INPUT' is not "
                                                                                        "found")
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_INPUT)).send_keys(last_name)
        self.wait.until(EC.text_to_be_present_in_element_value(self.LAST_NAME_INPUT, last_name))

    def enter_post_code(self, POST_CODE):
        self.wait.until(EC.visibility_of_element_located(self.POST_CODE_INPUT), message="input 'POST_CODE_INPUT' is not "
                                                                                        "found")
        self.wait.until(EC.element_to_be_clickable(self.POST_CODE_INPUT)).send_keys(POST_CODE)
        self.wait.until(EC.text_to_be_present_in_element_value(self.POST_CODE_INPUT, POST_CODE))

    def click_submit_button(self):
        self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BUTTON),
                        message="Button 'SUBMIT_BUTTON' is not found")
        button = self.wait.until((EC.element_to_be_clickable(self.SUBMIT_BUTTON)),
                                 message="Button 'SUBMIT_BUTTON' is not clickable")
        button.click()

    def alert_action(self):
        alert = self.wait.until(EC.alert_is_present(), message="Alert is not present")
        self.driver.switch_to.alert
        alert.accept()

    def click_select_user_dropdown(self):
        self.wait.until(EC.visibility_of_element_located(self.SELECT_USER_DROPDOWN),
                        message="Button 'SELECT_USER_DROPDOWN' is not found")
        button = self.wait.until((EC.element_to_be_clickable(self.SELECT_USER_DROPDOWN)),
                                 message="Button 'SELECT_USER_DROPDOWN' is not clickable")
        button.click()

    def select_user_action(self, value):
        self.wait.until(EC.visibility_of_element_located(self.SELECT_USER_DROPDOWN),
                        message="Button 'SELECT_USER_DROPDOWN' is not found")
        select_customer = Select(self.driver.find_element(By.ID, 'userSelect'))
        select_customer.select_by_visible_text(value)

    def select_users_currency(self):
        select_currency = Select(self.driver.find_element(By.ID, 'currency'))
        select_currency.select_by_visible_text('Dollar')

