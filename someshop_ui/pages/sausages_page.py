from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ..base.base_class import Base

class Sausages_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #Locators at sausages page
    max_price_filter = "//input[@id='NEXT_SMART_FILTER_P1_MAX']"
    age_of_dogs = "(//div[contains(@class, 'bx_filter_parameters_box_title')])[6]"
    brands = "(//div[contains(@class, 'bx_filter_parameters_box_title')])[4]"
    villages_treats = "//span[contains(@title, 'ДЕРЕВЕНСКИЕ ЛАКОМСТВА')]"
    clan_classic = "//span[contains(@title, 'CLAN CLASSIC')]"
    stuzzy_friends = "//span[contains(@title, 'STUZZY FRIENDS')]"
    show_button = "//input[@id='set_filter']"
    sorted_by = "(//div[contains(@class, 'dropdown-select__title')])"
    available_sort = "(//a[contains(@class, 'CATALOG_AVAILABLE')])"
    pet_goods = "//div[contains(@class, 'item_block')]"
    cart_icon = "//span[contains(@class, 'dark_link')]/span[@class='count']"

    def get_max_price_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.max_price_filter))

    def get_age_of_dogs(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.age_of_dogs))

    def get_brands(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.brands))

    def get_villages_treats(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.villages_treats))

    def get_clan_classic(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.clan_classic))

    def get_stuzzy_friends(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.stuzzy_friends))

    def get_show_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.show_button))

    def get_sorted_by(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.sorted_by))

    def get_available_sort(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.available_sort))

    def get_pet_goods(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.pet_goods))

    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.cart_icon))