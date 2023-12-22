from pages.base_page import Page
from pages.registration_page import RegistrationPage


class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.registration_page = RegistrationPage(driver)
