import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwarts:
    def setup_method(self):
        # 多浏览器
        '''
        Windows：
        set browser=edge
        pytest test_selenium/test_hogwarts.py
        Mac:
        browser=chrome pytest test_selenium/test_hogwarts.py
        '''
        browser = os.getenv("browser", "").lower()
        if browser == "headless":
            self.driver = webdriver.PhantomJS()
        elif browser == "edge":
            self.driver = webdriver.Edge()
        else:
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1280,1696")
            # 在后台启动一个chrome进程
            # /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --romote-debugging-port=9222
            # 使用已经存在的chrome进程
            # options.debugger_address="127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
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
        self.driver.minimize_window()  # 最小化界面
        self.driver.find_element(By.CSS_SELECTOR, '[target="_blank"]').click()
        # 点击链接打开新的页面时，需切换窗口才能对新的页面进行页面操作
        print(self.driver.window_handles)
        # 考虑到网络比较卡时，需等待新页面加载完再切换页面
        self.wait(10, lambda x: len(self.driver.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        element = (By.LINK_TEXT, '关于社区')
        self.wait(10, expected_conditions.element_to_be_clickable(element))
        self.driver.find_element(*element).click()

    def test_js(self):
        # 执行js语句
        for code in ["return document.title",
                     'return document.querySelector(".active").className',
                     'return JSON.stringify(performance.timing)'
                     ]:
            result = self.driver.execute_script(code)
            print(result)

    def teardown_method(self):
        sleep(20)
        self.driver.quit()
