from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
from ..base.base_class import Base


faker = Faker()

class OrderPage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators at order page
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


    def get_city_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.city_field)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.continue_button)))

    def get_delivery_cdek(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.delivery_cdek)))

    def get_delivery_cash(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.delivery_cash)))

    def get_field_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.field_name)))

    def get_mail_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.mail_field)))

    def get_phone_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.phone_field)))

    def get_phone_error_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.phone_field_error)))

    def get_address_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.address_field)))

    def get_comment_order_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.comment_order_field)))

    def get_personal_info_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.personal_info_checkbox)))

    def get_personal_info_error(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.personal_info_error)))

    def get_main_page_logo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.main_page_logo)))


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


    def placing_order(self):
        self.press_city_field()
        self.press_continue_button()
        self.press_delivery_cdek()
        self.press_continue_button()
        self.press_delivery_cash()
        self.press_continue_button()
        self.click_mail_field()
        self.get_field_name().send_keys(faker.full_name())
        self.click_mail_field()
        self.input_mail_field(faker.email())
        self.click_address_field()
        self.input_address_field(faker.address())
        self.click_comment_field()
        self.input_comment_field("Проверочный комментарий")
        self.press_continue_button()
        self.get_phone_error_field().is_displayed()
        self.assert_text(self.get_phone_error_field().text, 'Поле "Телефон" обязательно для заполнения')
        self.press_checkbox_personal_info()
        self.press_main_page_logo()