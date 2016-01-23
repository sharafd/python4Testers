# -*- coding: utf-8 -*-

from model import *
from helpers import *

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
       wdh = webDriverHelper.WebDriverHelper();
       self.wd = wdh.wd

   # Финализация
    def tearDown(self):
        self.logout(self.wd)
        self.wd.quit()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    # Логин
    def login(self, wd, login, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    # Тест - создание группы контактов
    def test_TestAddGroup(self):

        home = homepage.HomePage(self.wd, "admin", "secret")
        group = groups.Groups(self.wd, "New_01", "+", "------------")

        HomePage.open_homepage(home)

        self.login(self.wd, "admin", "secret")
       # HomePage.login(home)
        Groups.add_new_contacts_group(group)

if __name__ == '__main__':
    unittest.main()
