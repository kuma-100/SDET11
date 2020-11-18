from test_selenium.page.index import Index


class TestIndex:
    def setup(self):
        self.index = Index()

    def test_register(self):
        # self.driver.find_element(By.LINK_TEXT, "立即注册").click()

        self.index.goto_register().register("霍格沃兹学院")
        # self.driver.find_element(By.ID, "corp_name").send_keys("霍格沃兹学院")
        # self.driver.find_element(By.ID, "submit_btn").click()

    def test_login(self):
        self.index.goto_login().goto_registry().register("霍格沃兹学院")

    def teardown(self):
        self.index.close()
