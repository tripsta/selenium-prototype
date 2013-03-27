from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://en.wikipedia.org")

inputElement = driver.find_element_by_id("searchInput")

inputElement.send_keys("aston martin")

inputElement.submit()

try:	
	WebDriverWait(driver, 3).until(EC.title_contains("Aston Martin"))
except:
	driver.quit()
	assert 0, 'title does not contain: Aston Martin'

try:
	kensigton_link = driver.find_element_by_link_text("Kensington")
except NoSuchElementException:
	driver.quit()
	assert 0, 'No link with Kensington'

kensigton_link.click()
try:
	WebDriverWait(driver, 3).until(EC.title_contains("Kensington"))
except NoSuchElementException:
	driver.quit()
	assert 0, 'Domesday Book not found In Kensington'

body = driver.find_element_by_id("bodyContent")
assert 'Domesday Book' in body.text

driver.quit()
print "OK"

