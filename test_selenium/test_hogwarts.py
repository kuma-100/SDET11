from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts:
    def setup_method(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://testerhome.com/")

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT,"社团").click()
        self.driver.find_element(By.LINK_TEXT,"测试媛").click()
        # sleep(2)
        self.driver.find_element(By.CSS_SELECTOR,".topic-22425 .title > a").click()

    def teardown_method(self):
        # sleep(20)
        self.driver.quit()
