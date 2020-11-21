from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage
from test_selenium.page.contact import Contact


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def download(self):
        pass

    def import_user(self):
        return self

    def goto_app(self):
        pass

    def goto_company(self):
        pass

    def get_message(self):
        return ["aaa", "bbb"]

    def add_member(self):
        locator = (By.LINK_TEXT, "添加成员")
        self.find(*locator).click()
        # driverBug：浏览器缩放时，无法执行点击，可使用JS点击
        # self._driver.execute_script("arguments[0].click();", self.find(*locator))
        return Contact(reuse=True)
