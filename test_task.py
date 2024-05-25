from base.base_test import BaseTest


class TestTask(BaseTest):

    def test_task(self):

        """Zaloguj się jako bank"""
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_bank_manager_login_button()
        self.bank_manager_page.is_opened()

        """Dodaj klienta"""
        self.bank_manager_page.click_add_customer_button()
        self.bank_manager_page.enter_first_name(self.data.FIRST_NAME)
        self.bank_manager_page.enter_last_name(self.data.LAST_NAME)
        self.bank_manager_page.enter_post_code(self.data.POST_CODE)
        self.bank_manager_page.click_submit_button()
        self.bank_manager_page.alert_action()

        """Przejdź do otwarcia konta"""
        self.bank_manager_page.click_open_account_button()

        """ Wybierz dodanego klienta i otwórz jego konto w dowolnej walucie"""
        self.bank_manager_page.click_select_user_dropdown()
        self.bank_manager_page.select_user_action(f"{self.data.FIRST_NAME} {self.data.LAST_NAME}")
        self.bank_manager_page.select_users_currency()
        self.bank_manager_page.click_submit_button()
        self.bank_manager_page.alert_action()

        """Wróć na stronę główną"""
        self.home_page.click_home_button()

        """Zaloguj się jako nowo dodany klient"""
        self.home_page.click_customer_login_button()
        self.customer_page.is_opened()
        self.customer_page.select_user_action("Salazar Slytherin")
        self.customer_page.click_submit_button()

        """Dodaj kilka transakcji wpłat"""
        self.customer_page.click_deposit_button()
        self.customer_page.enter_amount('100')
        self.customer_page.click_submit_button()

        self.customer_page.enter_amount('200')
        self.customer_page.click_submit_button()

        """Dodaj kilka transakcji wypłat"""
        self.customer_page.click_withdraw_button()
        self.customer_page.enter_amount('1')
        self.customer_page.click_submit_button()

        self.customer_page.enter_amount('2')
        self.customer_page.click_submit_button()

        """Przejdź na stronę spisu transakcji"""
        self.customer_page.click_transaction_button()
