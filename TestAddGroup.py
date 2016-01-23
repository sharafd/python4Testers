# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver

import  unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class TestAddGroup(unittest.TestCase):

    # Инициализация
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    # Финализация
    def tearDown(self):
        self.wd.quit()

    # Открытие тестового приложения
    def open_homepage(self, wd):
        wd.get("http://192.168.1.25/addressbook/index.php")

    # Логин
    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    # Создание новой группы контактов
    def add_new_contacts_group(self, wd):
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("New_01")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("+")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("------------")
        wd.find_element_by_name("submit").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    # Тест - создание группы контактов
    def test_TestAddGroup(self):

        wd = self.wd

        self.open_homepage(wd)
        self.login(wd)
        self.add_new_contacts_group(wd)

        wd.find_element_by_link_text("group page").click()

        self.logout(wd)

if __name__ == '__main__':
    unittest.main()
