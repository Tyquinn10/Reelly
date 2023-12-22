from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class RegistrationPage(Page):

    def open_registration(self):
        self.open_url('https://soft.reelly.io/sign-up')

