from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker
from someshop_ui.base.base_class import Base
from someshop_ui.pages.cart_page import CartPage

faker = Faker()


class OrderPage(CartPage, Base):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators at order page
    city_field = "(//a[contains(text(), 'Владивосток')])[2]"
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
    phone_field_modal = "//input[@id='one_click_buy_id_PHONE']"
    comment_field_modal = "//textarea[@id='one_click_buy_id_COMMENT']"
    personal_info_modal = "//label[@class='license']"
    complete_order_button = "//button[@id='one_click_buy_form_button']"
    fio_field_modal = "//input[@id='one_click_buy_id_FIO']"
    email_field_modal = "//input[@id='one_click_buy_id_EMAIL']"
    complete_alert = "//div[contains(@class, 'one_click_buy_basket_frame')]"
    frame_modal = "//div[contains(@class, 'one_click_buy_basket_frame')]"
    close_modal = "//a[contains(@class, 'jqmClose ')]"

    def get_city_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.city_field)))

    def get_close_modal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.close_modal)))

    def get_frame_modal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.frame_modal)))

    def get_complete_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.complete_order_button)))

    def get_fio_field_modal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.fio_field_modal)))

    def get_email_field_modal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.email_field_modal)))

    def get_personal_info_modal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.personal_info_modal)))

    def get_comment_field_modal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.comment_field_modal)))

    def get_phone_field_modal(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.phone_field_modal)))

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

    def get_complete_order_alert(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(("xpath", self.complete_alert)))

    def press_city_field(self):
        self.get_city_field().click()
        print("Choose city")

    def press_continue_button(self):
        self.get_continue_button().click()
        print("Press continue button")

    def press_delivery_cdek(self):
        self.get_delivery_cdek().click()
        print("Choose cdek")

    def press_delivery_cash(self):
        self.get_delivery_cash().click()
        print("Choose cash")

    def click_field_name(self):
        self.get_field_name().click()

    def input_name_field(self, name):
        self.get_field_name().send_keys(name)
        print("Press name")

    def click_mail_field(self):
        self.get_mail_field().click()

    def input_mail_field(self, mail):
        self.get_mail_field().send_keys(mail)
        print("input mail")

    def click_address_field(self):
        self.get_address_field().click()

    def click_fio_field_modal(self):
        self.get_fio_field_modal().click()
        print("Click fio field")

    def click_email_field_modal(self):
        self.get_email_field_modal().click()
        print("Click email field")

    def clear_fio_field_modal(self):
        self.get_fio_field_modal().clear()
        print("Clear fio field")

    def input_fio_field_modal(self):
        self.get_fio_field_modal().send_keys(faker.name())
        print("Input fio")

    def clear_email_field_modal(self):
        self.get_email_field_modal().clear()
        print("Clear email field")

    def input_email_field_modal(self, email="Faker.faker@mail.ru"):
        self.get_email_field_modal().send_keys(email)
        print("Input email")

    def input_address_field(self, address):
        self.get_address_field().send_keys(address)
        print("Input address")

    def click_comment_field(self):
        self.get_comment_order_field().click()
        print("Click comment field")

    def input_comment_field(self, comment):
        self.get_comment_order_field().send_keys(comment)
        print("Input comment")

    def press_checkbox_personal_info(self):
        self.get_personal_info_checkbox().click()
        print("Press checkbox personal info")

    def press_main_page_logo(self):
        self.get_main_page_logo().click()
        print("Press main page logo")

    def press_order_button_modal(self):
        self.get_complete_order_button().click()
        print("Press order button")

    def press_phone_modal(self):
        self.get_phone_field_modal().click()
        print("Press phone field")

    def input_phone_modal(self, number="8126607008"):
        self.get_phone_field_modal().send_keys(number)
        print("Input phone")

    def input_comment_modal(self, text="Проверочные работы"):
        self.get_comment_field_modal().send_keys(text)
        print("Input comment")

    def press_checkbox_info_modal(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_personal_info_modal()).move_by_offset(-100, 0).click().perform()
        print("Press checkbox")

    def alert_order_is_displayer(self):
        if self.get_complete_order_alert().is_displayed():
            self.click_get_close_modal()
            self.press_fast_order_button()
            self.click_fio_field_modal()
            self.clear_fio_field_modal()
            self.input_fio_field_modal()
            self.press_phone_modal()
            self.input_phone_modal()
            self.click_email_field_modal()
            self.clear_email_field_modal()
            self.input_email_field_modal()
            self.get_comment_field_modal()
            self.input_comment_modal()
            self.press_checkbox_info_modal()
            self.press_order_button_modal()


    def click_get_close_modal(self):
        self.get_close_modal().click()

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
        print("placing order is over")

    def placing_order_modal_form(self):
        #self.switch_to_frame(self.get_frame_modal())
        self.click_fio_field_modal()
        self.clear_fio_field_modal()
        self.input_fio_field_modal()
        self.press_phone_modal()
        self.input_phone_modal()
        self.click_email_field_modal()
        self.clear_email_field_modal()
        self.input_email_field_modal()
        self.get_comment_field_modal()
        self.input_comment_modal()
        self.press_checkbox_info_modal()
        self.press_order_button_modal()
        self.alert_order_is_displayer()
        self.get_complete_order_alert().is_displayed()
        print("placing order is over")