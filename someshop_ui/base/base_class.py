class Base:
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url
        return get_url

    def assert_word(self, word, result):
        value_word = word.text
        assert result == value_word

    def assert_url(self, url, result):
        url = self.get_current_url()
        assert url == result, "get invalid url"

    def assert_is_selected(self, locator, result):
        assert locator == result