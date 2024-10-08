from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from someshop_ui.utilities.conftest import alert_about_test
from someshop_ui.pages.cart_page import CartPage
from someshop_ui.pages.catalog_page import CatalogPage
from someshop_ui.pages.main_page import MainPage
from someshop_ui.pages.treats_page import TreatsPage
from someshop_ui.pages.sausages_page import SausagesPage
from someshop_ui.pages.order_page import OrderPage


def test_login_into_system():
    """
    Данный тест авторизуется в магазине по заранее зарегистрированному пользователю,
    Открывает вкладку лакомств для собак, проверяет работу фильтров, имитация того, что покупатель не нашел по
    соответствующим фильтрам товар и перешел в раздел колбасок, где оформил заказ
    :return:
    """
    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--incognito')
    options.page_load_strategy = 'eager'
    # options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)

    print("Start test")

    main_page_test = MainPage(driver)
    main_page_test.authorization()

    catalog_page_test = CatalogPage(driver)
    catalog_page_test.products_for_dogs()

    treats_page_test = TreatsPage(driver)
    treats_page_test.filters_work()

    sausages_page_test = SausagesPage(driver)
    sausages_page_test.filters_work()
    sausages_page_test.buy_one_product()

    cart_page_test = CartPage(driver)
    cart_page_test.checking_cart_page()

    order_page_test = OrderPage(driver)
    order_page_test.placing_order_modal_form()

    main_page_test.assert_text(cart_page_test.get_clear_cart_text(), "Ваша корзина пуста")

    print("Finish test")
