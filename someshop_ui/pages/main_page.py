from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from someshop_ui.base.base_class import Base


class MainPage(Base):
    """
    Класс основной страницы, используется для авторизации и перехода в каталог
    """
    def __init__(self, driver, url="https://dogokot.ru/"):
        super().__init__(driver)
        self.url = url

    # Locators at main page
    enter_button = "//span[contains(text(), 'Войти')]"
    login_field = "//input[@id='USER_LOGIN_POPUP']"
    password_field = "//input[@id='USER_PASSWORD_POPUP']"
    enter_modal_form = "//input[@name='Login']"
    remember_user = "//label[@for='USER_REMEMBER_frm']"
    login_alert = "//div[@class='notice__inner']"
    catalog_button = "//a[@class='dropdown-toggle' and @href='/catalog/']"
    cart_button = "//a[@data-entity='basket-items-count']"

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.enter_button)))

    def get_login_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.login_field)))

    def get_password_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.password_field)))

    def get_enter_modal_form(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.enter_modal_form)))

    def get_remember_user(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.remember_user)))

    def get_alert_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.login_alert)))

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.catalog_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.cart_button)))

    def press_cart_button(self):
        self.get_cart_button().click()
        print("Press cart button")

    def click_login_button(self):
        self.get_enter_button().click()
        print("Press login button")

    def input_login(self):
        self.get_login_field().send_keys(self.mail)
        print("Input login")

    def input_password(self):
        self.get_password_field().send_keys(self.password)
        print("Input password")

    def press_login_button(self):
        self.get_enter_modal_form().click()
        print("Press login button")

    def press_remember_user(self):
        self.get_remember_user().click()
        print("Press remember user")

    def check_login_alert(self):
        print("Check login alert")
        return self.get_alert_login().is_enabled()

    def press_catalog_button(self):
        self.get_catalog_button().click()
        print("Press catalog button")

    def authorization(self):
        self.driver.get(self.url)
        self.click_login_button()
        self.input_login()
        self.input_password()
        self.press_remember_user()
        self.press_login_button()
        self.check_login_alert()
        self.assert_title(self.get_current_title(), 'Личный кабинет')
        self.press_catalog_button()
