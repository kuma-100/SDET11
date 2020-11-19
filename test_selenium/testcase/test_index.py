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
        register_page=self.index.goto_login().goto_registry().register("霍格沃兹学院")
        print(register_page.get_error_message())
        assert "请选择" in "|".join(register_page.get_error_message())

    def teardown(self):
        self.index.close()
