from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ..base.base_class import Base

class Calatog_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #Locators at catalog page
    treats_for_dogs = "//a[contains(@href, 'lakomstva') and @class='dark_link']"


    def get_treats_for_dogs(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.for_dogs))

    def click_treats_for_dogs(self):
        self.get_treats_for_dogs().click()