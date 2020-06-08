from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium.controls.link import Link
from webium.driver import get_driver
from webium import BasePage, Find, Finds

class MekariPage(BasePage):
	url = 'https://mekari.com'

	buttonPelajariMekari = Find(by=By.XPATH, value="//a[contains(text(),'Pelajari Tentang Mekari')]")

class AssertPage()
if __name__ == '__main__':
	home_page = MekariPage()
	home_page.open()
	home_page.buttonPelajariMekari.click()
	print('Tested')
	get_driver().quit()
