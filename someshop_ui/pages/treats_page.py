from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from someshop_ui.base.base_class import Base


class TreatsPage(Base):
    """
    Класс реализует работу в каталоге на странице лакомств, где происходит имитация того, что потенциальный покупатель
    ищет товары по фильтрам, ничего не находит и переходит в другой интересующий раздел
    """
    def __init__(self, driver):
        super().__init__(driver)
        self.url_treats_page = "https://dogokot.ru/catalog/tovary_dlya_sobak/lakomstva/"

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
    japan_country = "//span[contains(text(), 'Япония')]"
    italy_country = "//span[contains(text(), 'Италия')]"
    show_button = "//input[@id='set_filter']"
    sausages_img = "//img[@title='Колбаски']"

    def get_min_price_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.min_price_filter)))

    def get_max_price_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.max_price_filter)))

    def get_feed_line(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.feed_line)))

    def get_age_of_dogs(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.age_of_dogs)))

    def get_size_of_dog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.size_of_dog)))

    def get_filter_breeds(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.filter_breeds)))

    def get_filter_ages(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.filter_ages)))

    def get_premium_feed(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.premium_feed)))

    def get_super_premium_feed(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.super_premium_feed)))

    def get_country_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.country_filter)))

    def get_canada_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.canada_country)))

    def get_china_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.china_country)))

    def get_russia_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.russia_country)))

    def get_japan_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.japan_country)))

    def get_italy_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.italy_country)))

    def get_show_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.show_button)))

    def get_sausages_img(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.sausages_img)))

    def press_min_price_filter(self):
        self.get_min_price_filter().click()

    def input_min_price(self, value):
        self.get_min_price_filter().send_keys(value)
        print("Input min price")

    def press_max_price_filter(self):
        self.get_max_price_filter().click()

    def input_max_price(self, value):
        self.get_max_price_filter().send_keys(value)
        print("Input max price")

    def choose_feed_line(self):
        self.get_feed_line().click()
        print("Line of feed")

    def choose_dogs_age(self):
        self.get_age_of_dogs().click()
        print("Dogs age")

    def choose_dogs_size(self):
        self.get_size_of_dog().click()
        print("Dogs size")

    def choose_breeds_filter(self):
        self.get_filter_breeds().click()
        print("Breeds filter")

    def choose_filter_ages(self):
        self.get_filter_ages().click()
        print("Filter age")

    def choose_premium_feed(self):
        self.get_premium_feed().click()
        print("Premium feed choose")

    def choose_super_premium_feed(self):
        self.get_super_premium_feed().click()
        print("Super premium feed choose")

    def choose_country_filter(self):
        self.get_country_filter().click()
        print("Country filter choose")

    def canada_choose(self):
        self.get_canada_country().click()
        print("Canada choose")

    def russia_choose(self):
        self.get_russia_country().click()
        print("Russia choose")

    def japan_choose(self):
        self.get_japan_country().click()
        print("Japan choose")

    def china_choose(self):
        self.get_china_country().click()
        print("China choose")

    def press_show_button(self):
        self.get_show_button().click()
        print("Press show button")

    def click_sausage_img(self):
        self.get_sausages_img().click()
        print("Click sausage img")

    def filters_work(self):
        self.assert_url(self.url_treats_page)
        self.input_min_price(500)
        self.input_max_price(750)
        self.choose_dogs_size()
        self.choose_breeds_filter()
        self.choose_dogs_age()
        self.choose_filter_ages()
        self.choose_feed_line()
        self.choose_premium_feed()
        self.choose_super_premium_feed()
        self.choose_country_filter()
        self.japan_choose()
        self.russia_choose()
        self.china_choose()
        self.canada_choose()
        assert False is self.get_italy_country().is_selected()
        self.press_show_button()
        self.scroll_browser_to_up_page()
        self.click_sausage_img()
        print("Filter work checked")