from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ..base.base_class import Base

class Treats_page(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators at catalog page
    min_price_filter = "//input[@id='NEXT_SMART_FILTER_P1_MIN']"
    max_price_filter = "//input[@id='NEXT_SMART_FILTER_P1_MAX']"
    feed_line = "(//div[contains(@class, 'bx_filter_parameters_box_title')])[5]"
    age_of_dogs = "(//div[contains(@class, 'bx_filter_parameters_box_title')])[6]"
    size_of_dog = "(//div[contains(@class, 'bx_filter_parameters_box_title')])[8]"
    filter_breeds = "//span[contains(text(), 'Все породы')]"
    filter_ages = "//span[contains(text(), 'Для всех возрастов')]"
    premium_feed = "//span[contains(text(), 'Премиум')]"
    super_premium_feed = "//span[contains(text(), 'Супер-премиум')]"
    country_filter = "(//div[contains(@class, 'bx_filter_parameters_box_title')])[11]"
    canada_country = "//span[contains(text(), 'Канада')]"
    china_country = "//span[contains(text(), 'Китай')]"
    russia_country = "//span[contains(text(), 'Россия')]"
    japan_country = "//span[contains(text(), 'Японий')]"
    show_button = "//input[@id='set_filter']"
    sausages_img = "//img[@title='Колбаски']"