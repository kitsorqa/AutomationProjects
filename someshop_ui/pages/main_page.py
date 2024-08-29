from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from ..base.base_class import Base

class Main_page(Base):
    def __init__(self, driver):
        super().__init__(driver)


    #Locators at main page
    enter_button = "//span[contains(text(), 'Войти')]"
    login_field = "//input[@id='USER_LOGIN_POPUP']"
    password_field = "//input[@id='USER_PASSWORD_POPUP']"
    enter_modal_form = "//input[@name='Login']"
    remember_user = "//label[@for='USER_REMEMBER_frm']"
    login_alert = "//div[@class='notice__inner']"
    catalog_button = "//a[@class='dropdown-toggle' and @href='/catalog/']"
    cart_button = "//a[@data-entity='basket-items-count']"

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.enter_button))

    def get_login_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.login_field))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.password_field))

    def get_enter_modal_form(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.enter_modal_form))

    def get_remember_user(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.remember_user))

    def get_alert_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.login_alert))

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.catalog_button))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable("xpath", self.cart_button))


    def click_login_button(self):
        self.get_enter_button().click()

    def input_login(self):
        self.get_login_field().click()

    def input_password(self):
        self.get_password_field().click()

    def press_login_button(self):
        self.get_enter_modal_form().click()

    def press_remember_user(self):
        self.get_remember_user().click()

    def check_login_alert(self):
        return self.get_alert_login().is_enabled()

    def press_catalog_button(self):
        self.get_catalog_button().click()