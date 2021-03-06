from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webium.controls.link import Link
from webium.driver import get_driver
from webium import BasePage, Find, Finds

class MekariHomePage(BasePage):
	url = 'https://mekari.com'

	button = Find(by=By.XPATH, value="//a[contains(text(),'Pelajari Tentang Mekari')]")

if __name__ == '__main__':
	home_page = MekariHomePage()
	home_page.open()
	home_page.button.click()
	print('Tested')
	get_driver().quit()
