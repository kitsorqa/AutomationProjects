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
    phone_filed = "//input[@type='tel']"
    phone_filed_error = "//div[@class='tooltip-inner']"
    address_field = "//textarea[@id='soa-property-7']"
    comment_order_field = "//textarea[@id='orderDescription']"
    personal_info_checkbox = "//label[@class='license']"
    personal_info_error = "//label[@class='error']"
    main_page_logo = "//img[@title='Сайт по умолчанию']"
    clear_button = "//div[contains(@class, 'top_control')]"
