from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from support.logger import logger


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_url(self, url):
        self.driver.get(url)
        logger.info(f'Opening url {url}')

    def click(self, *locator):
        self.driver.find_element(*locator).click()
        logger.info(f'Clicking on {locator}')

    def find_element(self, *locator):
        logger.info(f'Searching for element {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f'Searching for elements {locator}')
        return self.driver.find_elements(*locator)

    def input(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_element_appear(self, *locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} not visible'
        )
        return element

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, \
            f"Expected text '{expected_text}' not in actual '{actual_text}'"

