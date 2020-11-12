from selenium.webdriver.common.by import By


class Contact:
    _add_menber_button=(By.CSS_SELECTOR,"xxxx")
    def add_member(self, data):
        # self.driver.find_element("添加成员").click
        # sendkeys
        # click save
        return self

    def add_member_error(self,data):
        return AddMemberPage()

    def search(self, name):
        pass

    def import_users(self, data):
        pass

    def export_users(self):
        pass

    def set_department(self, data):
        pass

    def delete(self):
        pass

    def invite(self):
        pass

    def add_department(self):
        pass
