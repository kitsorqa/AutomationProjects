from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ..base.base_class import Base

class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    #Locators at cart page
    items_cart = "//a[@data-entity='basket-items-count']"
    coupon_field = "//input[@data-entity='basket-coupon-input']"
    coupon_text = "//span[@class='basket-coupon-text']"
    checkout_button = "//button[@data-entity='basket-checkout-button']"
    city_field = "//input[@class='bx-ui-sls-fake']"
    continue_button = "//a[contains(text(), 'Далее')]"
    delivery_cdek = "//div[contains(text(), 'СДЭК')]"
    delivery_cash = "//div[contains(text(), 'Наличные курьеру при получении товара')]"
    field_name = "//input[@id='soa-property-1']"
    mail_field = "//input[@id='soa-property-2']"
    phone_field = "//input[@type='tel']"
    phone_field_error = "//div[@class='tooltip-inner']"
    address_field = "//textarea[@id='soa-property-7']"
    comment_order_field = "//textarea[@id='orderDescription']"
    personal_info_checkbox = "//label[@class='license']"
    personal_info_error = "//label[@class='error']"
    main_page_logo = "//img[@title='Сайт по умолчанию']"
    clear_button = "//div[contains(@class, 'top_control')]"

    def get_items_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.items_cart))

    def get_coupon_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.coupon_field))

    def get_coupon_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.coupon_text))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.checkout_button))

    def get_city_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.city_field))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.continue_button))

    def get_delivery_cdek(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.delivery_cdek))

    def get_delivery_cash(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.delivery_cash))

    def get_field_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.field_name))

    def get_mail_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.mail_field))

    def get_phone_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.phone_field))

    def get_phone_error_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.phone_field_error))

    def get_address_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.address_field))

    def get_comment_order_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.comment_order_field))

    def get_personal_info_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.personal_info_checkbox))

    def get_personal_info_error(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.personal_info_error))

    def get_main_page_logo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.main_page_logo))

    def get_clear_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.clear_button))


    def press_items_cart(self):
        self.get_items_cart().click()

    def press_coupon_field(self):
        self.get_coupon_field().click()

    def input_coupon_text(self, text):
        self.get_coupon_text().send_keys(text)

    def press_checkout_button(self):
        self.get_checkout_button().click()

    def press_city_field(self):
        self.get_city_field().click()

    def press_continue_button(self):
        self.get_continue_button().click()

    def press_delivery_cdek(self):
        self.get_delivery_cdek().click()

    def press_delivery_cash(self):
        self.get_delivery_cash().click()

    def click_field_name(self):
        self.get_field_name().click()

    def input_name_field(self, name):
        self.get_field_name().send_keys(name)

    def click_mail_field(self):
        self.get_mail_field().click()

    def input_mail_field(self, mail):
        self.get_mail_field().send_keys(mail)

    def click_address_field(self):
        self.get_address_field().click()

    def input_address_field(self, address):
        self.get_address_field().send_keys(address)

    def click_comment_field(self):
        self.get_comment_order_field().click()

    def input_comment_field(self, comment):
        self.get_comment_order_field().send_keys(comment)

    def press_checkbox_personal_info(self):
        self.get_personal_info_checkbox().click()

    def press_main_page_logo(self):
        self.get_main_page_logo().click()

    def press_clear_button(self):
        self.get_clear_button().click()