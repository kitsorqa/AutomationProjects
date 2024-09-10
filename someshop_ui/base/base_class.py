from someshop_ui.utilities.config_loader import load_config


class Base:
    data_config = load_config()

    def __init__(self, driver, mail=data_config['mail'], password=data_config['password']):
        self.driver = driver
        self.mail = mail
        self.password = password

    def get_current_url(self):
        get_url = self.driver.current_url
        return get_url

    def get_current_title(self):
        get_title = self.driver.title
        return get_title

    def assert_text(self, word, result):
        value_word = word.text
        assert result == value_word, 'The words are different'

    def assert_url(self, result):
        url_of_page = self.get_current_url()
        assert url_of_page == result, "get invalid url"

    def assert_title(self, page_title, needs_title):
        page_title = self.get_current_title()
        assert page_title == needs_title

    def assert_count_of_locator(self, value, real_count):
        assert value == real_count

    def assert_length_of_field(self, value, real_value):
        assert value == real_value

    def scroll_browser_to_points(self, x=0, y=0):
        self.x = x
        self.y = y
        self.driver.execute_script(f"window.scrollTo({self.x}, {self.y});")

    def scroll_browser_to_up_page(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def switch_to_frame(self, iframe_locator):
        self.driver.switch_to.frame(iframe_locator)
