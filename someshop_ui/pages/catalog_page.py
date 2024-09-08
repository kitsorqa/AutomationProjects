from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from someshop_ui.base.base_class import Base


class CalatogPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators at catalog page
    treats_for_dogs = "//a[contains(@href, 'lakomstva') and @class='dark_link']"

    def get_treats_for_dogs(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.treats_for_dogs)))

    def click_treats_for_dogs(self):
        self.get_treats_for_dogs().click()
        print("Click treats catalog")

    def products_for_dogs(self):
        self.get_treats_for_dogs().is_enabled()
        self.assert_title(self.get_current_title(), 'Каталог товаров - Dogokot')
        self.click_treats_for_dogs()
        print("Open products for dog")