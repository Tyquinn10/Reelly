from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import given, when, then
from time import sleep


FULL_NAME = (By.CSS_SELECTOR, '#Full-Name')
PHONE = (By.CSS_SELECTOR, '#phone2')
EMAIL = (By.CSS_SELECTOR, '#Email-3')
PASSWORD = (By.CSS_SELECTOR, '#field')
COMPANY = (By.CSS_SELECTOR, '#Company-website')


@given('Open the registration page')
def open_registration_page(context):
    context.app.registration_page.open_registration()


@then('Enter some test information in the input fields')
def test_information(context, name, phone, email, password, company):
    context.driver.find_element(*FULL_NAME).send_keys(name)
    context.driver.find_element(*PHONE).send_keys(phone)
    context.driver.find_element(*EMAIL).send_keys(email)
    context.driver.find_element(*PASSWORD).send_keys(password)
    context.driver.find_element(*COMPANY).send_keys(company)


@then('Verify the right information is present')
def verify_information(context):
    expected_information = ['name', 'phone', 'email', 'password', 'company']
    actual_information = []

    assert expected_information == actual_information, f'Expected {expected_information} did not match actual {actual_information}'

