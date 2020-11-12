from test_selenium.page.main import Main


class TestMain:
    def test_add_member(self):
        main = Main()
        main.add_member().add_member("xxx")
        assert "aaa" in main.import_user().get_message()
