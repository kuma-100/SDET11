from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts:
    def setup_method(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)  # 隐式等待，找不到元素时重复查找直到5秒超时

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        # 尽量使用css的定位方法集，Link有可能会导致解析元素的时候出现异常
        # todo：显式等待
        WebDriverWait(self.driver,10).until()
        self.driver.find_element(By.CSS_SELECTOR, "[data-name=测试媛]").click()
        # sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".topic .title > a").click()

    def teardown_method(self):
        pass
        # sleep(20)
        # self.driver.quit()
