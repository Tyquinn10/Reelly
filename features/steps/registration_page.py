from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import given, when, then
from time import sleep


@given('Open the registration page')
def open_registration_page(context):
    context.app.registration_page.open_registration_page()


@then('Enter some test information in the input fields')
def test_information(context):
    context.app.registration_page.test_information()


@then('Verify the right information is present')
def verify_information(context):
    context.app.registration_page.verify_information()