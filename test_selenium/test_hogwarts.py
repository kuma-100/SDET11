from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts:
    def setup_method(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(5)  # 隐式等待，找不到元素时重复查找直到5秒超时

    def wait(self, timeout, method):
        # 显式等待，封装方法
        WebDriverWait(self.driver, timeout).until(method)

    def test_hogwarts(self):
        self.driver.find_element(By.LINK_TEXT, "社团").click()
        # 尽量使用css的定位方法集，Link有可能会导致解析元素的时候出现异常
        # todo：显式等待
        element = (By.PARTIAL_LINK_TEXT, '测试媛')
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()
        # 使用css比link更好用
        # self.driver.find_element(By.CSS_SELECTOR, "[data-name=测试媛]").click()
        # sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".topic .title > a").click()

    def teardown_method(self):
        pass
        # sleep(20)
        # self.driver.quit()
