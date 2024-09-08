from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from someshop_ui.utilities.conftest import alert_about_test
from someshop_ui.pages.cart_page import CartPage
from someshop_ui.pages.catalog_page import CalatogPage
from someshop_ui.pages.main_page import MainPage
from someshop_ui.pages.treats_page import TreatsPage
from someshop_ui.pages.sausages_page import SausagesPage


def test_login_into_system():
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--incognito')
    options.page_load_strategy = 'eager'
    #options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)

    print("Start test")

    main_page_test = MainPage(driver)
    main_page_test.authorization()

    catalog_page_test = CalatogPage(driver)
    catalog_page_test.products_for_dogs()



    print("Finish test")