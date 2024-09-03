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

    def assert_word(self, word, result):
        value_word = word.text
        assert result == value_word

    def assert_url(self, url, result):
        url = self.get_current_url()
        assert url == result, "get invalid url"

    def assert_title(self, page_title, needs_title):
        page_title = self.get_current_title()
        assert page_title == needs_title

    def assert_is_selected(self, locator, result):
        assert locator == result

    def scroll_browser(self, x=0, y=0):
        self.x = x
        self.y = y