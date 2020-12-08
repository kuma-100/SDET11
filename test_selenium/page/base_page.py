from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""
    _driver = None

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                options = webdriver.ChromeOptions()
                # 在后台启动一个chrome进程
                # windows chrome绝对路径 --remote-debugging-port=9222
                # C:\Users\yh\AppData\Local\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222
                # mac
                # /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --romote-debugging-port=9222
                # 使用已经存在的chrome进程
                options.debugger_address = "127.0.0.1:9222"
                self._driver = webdriver.Chrome(options=options)
            else:
                # index页面会使用这个
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
            if self._base_url != "":
                self._driver.get(self._base_url)
        else:
            # Login与Register等页面需要用这个方法
            self._driver = driver

    def find(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)

    def wait_until_clickable(self, timeout, element):
        # 显式等待，封装方法
        method = expected_conditions.element_to_be_clickable(element)
        WebDriverWait(self._driver, timeout).until(method)

    def wait_until_visibility_located(self, timeout, element):
        method = expected_conditions.visibility_of_element_located(element)
        WebDriverWait(self._driver, timeout).until(method)

    def close(self):
        sleep(20)
        self._driver.quit()
