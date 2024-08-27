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
