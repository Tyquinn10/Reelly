from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

from pages.base_page import Page


class RegistrationPage(Page):
    FULL_NAME = (By.CSS_SELECTOR, '#Full-Name')
    PHONE = (By.CSS_SELECTOR, '#phone2')
    EMAIL = (By.CSS_SELECTOR, '#Email-3')
    PASSWORD = (By.CSS_SELECTOR, '#field')
    COMPANY = (By.CSS_SELECTOR, '#Company-website')

    def open_registration_page(self):
        self.open_url('https://soft.reelly.io/sign-up')

    def test_information(self):
        self.input("joe", *self.FULL_NAME)
        self.input("3475553458", *self.PHONE)
        self.input("Rabbit@gmail.com", *self.EMAIL)
        self.input("Trunks88", *self.PASSWORD)
        self.input("Test", *self.COMPANY)

    def verify_information(self):
        self.wait_for_element_appear(*self.FULL_NAME)
        self.wait_for_element_appear(*self.PHONE)
        self.wait_for_element_appear(*self.EMAIL)
        self.wait_for_element_appear(*self.PASSWORD)
        self.wait_for_element_appear(*self.COMPANY)

        # expected_name_text = "joe"
        # actual_name_text = self.find_element(*self.FULL_NAME)
        # assert expected_name_text in actual_name_text, f'Expected {expected_name_text} is not present in actual {actual_name_text}'

        # expected_phone_text = "3475553458"
        # actual_phone_text = self.find_element(*self.PHONE).text
        # assert expected_phone_text in actual_phone_text, f'Expected {expected_phone_text} is not present in actual {actual_phone_text}'
        #
        # expected_email_text = "Rabbit@gmail.com"
        # actual_email_text = self.find_element(*self.EMAIL).text
        # assert expected_email_text in actual_email_text, f'Expected {expected_email_text} is not present in actual {actual_email_text}'
        #
        # expected_password_text = "Trunks88"
        # actual_password_text = self.find_element(*self.PASSWORD).text
        # assert expected_password_text in actual_password_text, f'Expected {expected_password_text} is not present in actual {actual_password_text}'
        #
        # expected_company_text = "Test"
        # actual_company_text = self.find_element(*self.COMPANY).text
        # assert expected_company_text in actual_company_text, f'Expected {expected_company_text} is not present in actual {actual_company_text}'






