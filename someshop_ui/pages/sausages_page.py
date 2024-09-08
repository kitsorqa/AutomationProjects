from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ..base.base_class import Base

class SausagesPage(Base):
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
    cart_icon_count = "//span[contains(@class, 'dark_link')]/span[@class='count']"
    all_products = "//div[contains(@class, 'display_list')]"
    view_by_list = "//i[@title='списком']"
    to_basket = "//span[contains(@class, 'to-cart')]"

    def get_max_price_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.max_price_filter)))

    def get_age_of_dogs(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.age_of_dogs)))

    def get_brands(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.brands)))

    def get_villages_treats(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.villages_treats)))

    def get_clan_classic(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.clan_classic)))

    def get_stuzzy_friends(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.stuzzy_friends)))

    def get_show_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.show_button)))

    def get_sorted_by(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.sorted_by)))

    def get_available_sort(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.available_sort)))

    def get_pet_goods(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.pet_goods)))

    def get_cart_icon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.cart_icon)))

    def get_all_products_of_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.all_products)))

    def get_view_by_list(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.view_by_list)))

    def get_to_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.to_basket)))

    def get_cart_count(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.cart_icon_count)))

    def input_max_price_filter(self):
        self.get_max_price_filter().click()

    def send_max_price(self, value):
        self.get_max_price_filter().send_keys(value)

    def press_dogs_age(self):
        self.get_age_of_dogs().click()

    def click_into_brands(self):
        self.get_brands().click()

    def click_villages_treats(self):
        self.get_villages_treats().click()

    def press_clan_classic(self):
        self.get_clan_classic().click()

    def press_stuzzy_friends(self):
        self.get_stuzzy_friends().click()

    def choose_sausages_brands(self):
        self.click_into_brands()
        self.press_stuzzy_friends()
        self.press_clan_classic()
        self.click_villages_treats()

    def press_show_button(self):
        self.get_show_button().click()

    def press_sorted_by(self):
        self.get_sorted_by().click()

    def press_available_sort(self):
        self.get_available_sort().click()

    def press_pet_goods(self):
        self.get_pet_goods().click()

    def press_cart_icon(self):
        self.get_cart_icon().click()

    def press_view_by_list(self):
        self.get_view_by_list().click()

    def press_to_basket(self):
        self.get_to_basket().click()



    def filters_work(self):
        self.send_max_price(999)
        self.press_dogs_age()
        self.choose_sausages_brands()
        self.press_view_by_list()

    def buy_3_products(self):
        self.get_to_basket().click()
        self.get_to_basket().click()
        self.get_to_basket().click()
        self.assert_count_of_locator(3, int(self.get_cart_count().text))