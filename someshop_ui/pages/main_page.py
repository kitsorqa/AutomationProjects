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