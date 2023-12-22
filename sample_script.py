from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# checks every 100ms for element presence
# put in the code once
# if fails, we see NoSuchElementException
driver.implicitly_wait(5)

driver.wait = WebDriverWait(driver, 10)



# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('pokemon')

# wait for 4 sec
# sleep(4)

# defined in the code, where we use
# checks for EC every 500ms
# fails with TimeoutException
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Search btn not clickable')
driver.find_element(By.NAME, 'btnK').click()

# verify search results
# assert 'pokemon' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
# print('Test Passed')
driver.wait.until(EC.url_contains('pokemon'), message='Word pokemon not in URL')

driver.quit()
