from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    PAGE_URL = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'

    HOME_BUTTON = ("xpath", '//button[@ng-click="home()"]')
    BANK_MANAGER_LOGIN_BUTTON = ("xpath", '//button[@ng-click="manager()"]')
    CUSTOMER_LOGIN_BUTTON = ("xpath", '//button[@ng-click="customer()"]')

    def click_home_button(self):
        self.wait.until(EC.visibility_of_element_located(self.HOME_BUTTON),
                        message="Button 'HOME_BUTTON' is not found")
        button = self.wait.until((EC.element_to_be_clickable(self.HOME_BUTTON)),
                                 message="Button 'HOME_BUTTON' is not clickable")
        button.click()

    def click_bank_manager_login_button(self):
        self.wait.until(EC.visibility_of_element_located(self.BANK_MANAGER_LOGIN_BUTTON),
                        message="Button 'BANK_MANAGER_LOGIN_BUTTON' is not found")
        button = self.wait.until((EC.element_to_be_clickable(self.BANK_MANAGER_LOGIN_BUTTON)),
                                 message="Button 'BANK_MANAGER_LOGIN_BUTTON' is not clickable")
        button.click()

    def click_customer_login_button(self):
        self.wait.until(EC.visibility_of_element_located(self.CUSTOMER_LOGIN_BUTTON),
                        message="Button 'CUSTOMER_LOGIN_BUTTON' is not found")
        button = self.wait.until((EC.element_to_be_clickable(self.CUSTOMER_LOGIN_BUTTON)),
                                 message="Button 'CUSTOMER_LOGIN_BUTTON' is not clickable")
        button.click()
