from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


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

    def find(self, *locator):
        return self._driver.find_element(*locator)

    def close(self):
        sleep(20)
        self._driver.quit()
