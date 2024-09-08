import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from someshop_ui.base.base_class import Base


class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators at cart page
    items_cart = "//a[@data-entity='basket-items-count']"
    coupon_field = "//input[@data-entity='basket-coupon-input']"
    coupon_text = "//span[@class='basket-coupon-text']"
    coupon_button = "basket-coupon-block-coupon-btn"
    coupon_error_text = "//span[@class='basket-coupon-text']"
    checkout_button = "//button[@data-entity='basket-checkout-button']"
    clear_cart_button = "//div[contains(@class, 'top_control')]"
    clear_cart_text = "//div[@class='bx-sbb-empty-cart-text']"

    def get_items_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.items_cart)))

    def get_coupon_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.coupon_field)))

    def get_coupon_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.coupon_text)))

    def get_coupon_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.coupon_button)))

    def get_coupon_error_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.coupon_error_text)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.checkout_button)))

    def get_clear_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.clear_cart_button)))

    def get_clear_cart_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.clear_cart_text)))

    def click_clear_cart_button(self):
        self.get_clear_button().click()

    def press_items_cart(self):
        self.get_items_cart().click()

    def get_count_items_cart(self):
        text_of_count = self.get_items_cart().text
        number_of_count = text_of_count[:text_of_count.rfind(' ')]
        number_of_count = number_of_count[number_of_count.rfind(' ') + 1:]
        print(number_of_count)
        return int(number_of_count)

    def press_coupon_field(self):
        self.get_coupon_field().click()

    def input_coupon_text(self, text="test"):
        self.get_coupon_text().send_keys(text)

    def press_coupon_button(self):
        self.get_coupon_button().click()

    def press_checkout_button(self):
        self.get_checkout_button().click()

    def press_clear_button(self):
        self.get_clear_button().click()

    def checking_cart_page(self):
        print(self.get_count_items_cart())
        self.get_clear_button().is_enabled()
        self.press_coupon_field()
        self.input_coupon_text()
        self.press_coupon_button()
        self.assert_text(self.get_coupon_error_text, "test - купон не найден")
        self.press_checkout_button()
