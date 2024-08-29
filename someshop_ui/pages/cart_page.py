from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ..base.base_class import Base

class Cart_page(Base):
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