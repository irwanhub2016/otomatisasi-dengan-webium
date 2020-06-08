from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium.controls.link import Link
from webium.driver import get_driver
from webium import BasePage, Find, Finds

class MekariPage(BasePage):
	url = 'https://mekari.com'

	button = Find(by=By.XPATH, value="//a[contains(text(),'Pelajari Tentang Mekari')]")

class AssertPage(WebElement):
	page_heading = Find(by=By.CLASS_NAME, value="h1.u-str-48")

if __name__ == '__main__':
	home_page = MekariPage()
	home_page.open()
	home_page.buttonPelajariMekari.click()
	result_page = AssertPage()
	print('This should be True: ' + str(result_page.is_element_present('page_heading')))
	print('Tested')
	get_driver().quit()
