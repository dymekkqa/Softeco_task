import time
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class CustomerPage(BasePage):
    PAGE_URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    LOGIN_BUTTON = ("xpath", '//button[@type="submit"]')
    SELECT_USER_DROPDOWN = ("id", 'userSelect')
    DEPOSIT_BUTTON = ("xpath", '//button[@ng-click="deposit()"]')
    WITHDRAW_BUTTON = ("xpath", '//button[@ng-click="withdrawl()"]')
    TRANSACTION_BUTTON = ("xpath", '//button[@ng-click="transactions()"]')
    AMOUNT_INPUT = ("xpath", '//input[@type="number"]')

    def click_submit_button(self):
        self.wait.until(EC.presence_of_element_located(self.LOGIN_BUTTON))
        self.wait.until(EC.visibility_of_element_located(self.LOGIN_BUTTON),
                        message="Button 'LOGIN_BUTTON' is not found")
        button = self.wait.until((EC.element_to_be_clickable(self.LOGIN_BUTTON)),
                                 message="Button 'LOGIN_BUTTON' is not clickable")
        button.click()

    def select_user_action(self, value):
        self.wait.until(EC.visibility_of_element_located(self.SELECT_USER_DROPDOWN),
                        message="Button 'SELECT_USER_DROPDOWN' is not found")
        select_customer = Select(self.driver.find_element(By.ID, 'userSelect'))
        select_customer.select_by_visible_text(value)

    def enter_amount(self, amount):
        button = self.wait.until((EC.element_to_be_clickable(self.AMOUNT_INPUT)),
                                 message="Button 'SELECT_USER_DROPDOWN' is not clickable")
        button.click()
        time.sleep(0.5)
        self.wait.until(EC.visibility_of_element_located(self.AMOUNT_INPUT),
                        message="Input 'AMOUNT_INPUT' is not found")
        self.wait.until(EC.element_to_be_clickable(self.AMOUNT_INPUT)).send_keys(amount)
        self.wait.until(EC.text_to_be_present_in_element_value(self.AMOUNT_INPUT, amount))

    def click_deposit_button(self):
        self.wait.until(EC.visibility_of_element_located(self.DEPOSIT_BUTTON),
                        message="Button 'DEPOSIT_BUTTON' is not found")
        button = self.wait.until((EC.element_to_be_clickable(self.DEPOSIT_BUTTON)),
                                 message="Button 'DEPOSIT_BUTTON' is not clickable")
        button.click()

    def click_withdraw_button(self):
        self.wait.until(EC.visibility_of_element_located(self.WITHDRAW_BUTTON),
                        message="Button 'WITHDRAW_BUTTON' is not found")
        button = self.wait.until((EC.element_to_be_clickable(self.WITHDRAW_BUTTON)),
                                 message="Button 'WITHDRAW_BUTTON' is not clickable")
        button.click()

    def click_transaction_button(self):
        time.sleep(0.3)
        self.wait.until(EC.visibility_of_element_located(self.TRANSACTION_BUTTON),
                        message="Button 'TRANSACTION_BUTTON' is not found")
        button = self.wait.until((EC.element_to_be_clickable(self.TRANSACTION_BUTTON)),
                                 message="Button 'TRANSACTION_BUTTON' is not clickable")
        button.click()
