from time import sleep

from selenium.webdriver.common.by import By

from test_selenium.page.base_page import BasePage


class Message(BasePage):
    def send(self, app="", title="", content="", group="", author=""):
        self.find(By.LINK_TEXT, "选择需要发消息的应用").click()
        self.find(By.CSS_SELECTOR, "div [data-name='%s']" % app).click()
        self.find(By.LINK_TEXT, "确定").click()

        self.find(By.LINK_TEXT, "选择发送范围").click()
        element = (By.CSS_SELECTOR, "#memberSearchInput")
        self.wait_until_visibility_located(10, element)
        self.find(element).send_keys(group)
        self.find(By.CSS_SELECTOR, "#searchResult li").click()
        self.find(By.LINK_TEXT, "确认").click()

        self.find(By.CSS_SELECTOR, ".ww_editorTitle").send_keys(title)
        self._driver.switch_to.frame("ueditor_0")
        self.find(By.CSS_SELECTOR, ".mpnews").send_keys(content)
        self._driver.switch_to.parent_frame()
        self.find(By.CSS_SELECTOR, ".js_amrd_sendName").send_keys(author)
        element = (By.CSS_SELECTOR, ".js_save_send")
        self.find(element).click()

    def get_history(self):
        pass
