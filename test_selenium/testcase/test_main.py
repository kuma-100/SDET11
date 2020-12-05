from test_selenium.page.main import Main


class TestMain:
    def setup(self):
        self.main = Main(reuse=True)

    def test_add_member(self):
        self.main.add_member().add_member("xxx")
        assert "aaa" in self.main.import_user().get_message()

    def test_import_user(self):
        self.main.import_user(
            "E:\\TestDevelopment\\PycharmProjects\\pythonProject\\test_selenium\\testcase\\通讯录批量导入模板.xlsx")
        # assert "success" in self.main.get_message()

    def test_send_message(self):
        message = self.main.send_message()
        message.send(app="公告", content="contect", group="羽汐动漫社")
        # assert "contect" in message.get_history()
