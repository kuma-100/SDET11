from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from test_selenium.page.base_page import BasePage
from test_selenium.page.contact import Contact
from test_selenium.page.message import Message


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def download(self):
        pass

    def import_user(self, path):
        self.find(By.LINK_TEXT, "导入通讯录").click()
        # 文件上传
        self.find(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(path)
        self.find(By.LINK_TEXT, "导入").click()
        self.wait(10, expected_conditions.element_to_be_clickable((By.LINK_TEXT, "完成")))
        self.find(By.LINK_TEXT, "完成").click()
        return self

    def goto_app(self):
        pass

    def goto_company(self):
        pass

    def get_message(self):
        return ["aaa", "bbb"]

    def add_member(self):
        locator = (By.LINK_TEXT, "添加成员")
        self.find(locator).click()
        # driverBug：浏览器缩放时，无法执行点击，可使用JS点击
        # self._driver.execute_script("arguments[0].click();", self.find(locator))
        return Contact(reuse=True)

    def send_message(self):
        locator = (By.LINK_TEXT, "消息群发")
        self.find(locator).click()
        return Message(reuse=True)
