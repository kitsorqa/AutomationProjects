class Base:
    def __init__(self, driver):
        self.driver = driver
        self.mail = "Faker.faker@mail.ru"
        self.password = "fakerfaker"

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

    def scroll_browser(self, x=0, y=0):
        self.x = x
        self.y = y