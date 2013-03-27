from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get("http://tripsta.de/hotels")

inputElement = driver.find_element_by_id("destinationInput")
inputElement.send_keys("Berlin, Deutschland")

inputElement = driver.find_element_by_id("checkin")
inputElement.clear()
inputElement.send_keys( "27.08.2013")
# print dir(inputElement)
# driver.quit()

inputElement = driver.find_element_by_id("checkout")
inputElement.clear()
inputElement.send_keys("31.08.2013")

inputElement = driver.find_element_by_id("Room-0-AdultsNum")
inputElement.send_keys("2")

inputElement.submit()

try:	
	WebDriverWait(driver, 3).until(EC.title_contains("Suchergebnisse - Hotel"))
except:
	driver.quit()
	assert 0, 'Hotel Results never loaded'

try:
	total_price = driver.find_element_by_css_selector("span.total-price")
except NoSuchElementException:
	driver.quit()
	assert 0, 'No element with price'

# kensigton_link.click()
# try:
# 	WebDriverWait(driver, 3).until(EC.title_contains("Kensington"))
# except NoSuchElementException:
# 	driver.quit()
# 	assert 0, 'Domesday Book not found In Kensington'

# body = driver.find_element_by_id("bodyContent")
# assert 'Domesday Books' in body.text

driver.quit()
print "OK"

