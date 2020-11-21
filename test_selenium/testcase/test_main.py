from test_selenium.page.main import Main


class TestMain:
    def setup(self):
        self.main = Main(reuse=True)

    def test_add_member(self):
        self.main.add_member().add_member("xxx")
        assert "aaa" in self.main.import_user().get_message()

    def test_import_user(self):
        self.main.import_user("xxx.file")
        assert "success" in self.main.get_message()

    def test_send_message(self):
        self.main.send_message()
        assert "" in self.main.get_message()
