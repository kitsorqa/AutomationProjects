import datetime

from ui_project.config.load_data import load_data_from_config


class Base:
    data_from_json = load_data_from_config()

    def __init__(self, driver, url=data_from_json['url']):
        self.driver = driver
        self.url = url


class ExtensionMethods(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def get_url_of_current_page(self):
        return self.driver.current_url

    def get_title_of_current_page(self):
        return self.driver.title

    def scroll_browser_to_points(self, point_x=0, point_y=0):
        self.driver.execute_script(f"window.scrollTo({point_x}, {point_x});")
        
    def scroll_browser_to_top_of_page(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    def switch_to_iframe(self, iframe_locator):
        self.driver.switch_to.frame(iframe_locator)

    def delete_cookies(self):
        self.driver.delete_all_cookies()

    def get_screenshot(self, path=f'../data/screen{datetime.datetime.now()}'):
        path = path
        self.driver.save_screenshot(path)

class AssertMethods(ExtensionMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def assert_text(self, example_word, compare_word):
        assert example_word == compare_word

    def assert_url(self, url):
        expected_url = self.get_url_of_current_page()
        assert expected_url == url

