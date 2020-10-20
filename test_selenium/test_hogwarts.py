import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts:
    def setup_method(self):
        browser = os.getenv("browser")
        if browser == "headless":
            self.driver = webdriver.PhantomJS()
        elif browser == "chrome":
            self.driver = webdriver.Chrome()
        else:
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
        # 这种情况下显式等待与隐式等待出现冲突，find方法搜索不到会尝试隐式等待再返回结果
        # WebDriverWait(self.driver, 10).until(lambda x: self.driver.find_elements(element) > 1)
        self.driver.find_element(*element).click()
        # 使用css比link更好用
        # self.driver.find_element(By.CSS_SELECTOR, "[data-name=测试媛]").click()
        # sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, ".topic .title > a").click()

    def test_frame(self):
        self.driver.get("https://testerhome.com/topics/21495")
        submit = (By.CSS_SELECTOR, ".published-form__submit")
        # 若内嵌了frame页面，需要切换frame再查询元素
        self.driver.switch_to.frame(0)
        self.wait(10, expected_conditions.element_to_be_clickable(submit))
        self.driver.find_element(By.CSS_SELECTOR, ".published-form__submit").click()

    def test_mtsc2020(self):
        self.driver.get("https://testerhome.com/topics/25593")
        self.driver.find_element(By.CSS_SELECTOR, '[target="_blank"]').click()
        # 点击链接打开新的页面时，需切换窗口才能对新的页面进行页面操作
        print(self.driver.window_handles)
        # 考虑到网络比较卡时，需等待新页面加载完再切换页面
        self.wait(10, lambda x: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.find_element(By.LINK_TEXT, '合作伙伴').click()

    def teardown_method(self):
        sleep(20)
        self.driver.quit()
