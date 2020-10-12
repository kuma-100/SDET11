from selenium import webdriver

class TestHogwarts:
    def setup_method(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://testerhome.com/")
    def test_hogwarts(self):
        pass