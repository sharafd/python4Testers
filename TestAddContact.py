# -*- coding: utf-8 -*-

# Проверки контактов

import time, unittest

from model import *
from helpers import *


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class TestAddContact(unittest.TestCase):

    # Инициализация
    def setUp(self):
       # Получаем WebDriver
       global wd
       wdh = webDriverHelper.WebDriverHelper()
       wd = wdh.wd

   # Финализация
    def tearDown(self):
        HomePage.logout(home)
        time.sleep(3)
        wd.quit()

     # Логин
    def login(self, wd, login, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()

    # Добавление нового контакта без привязки к группе
    def test_TestAddContact(self):

        # Страница авторизации
        global home
        home = HomePage(wd = wd, login = "admin", password = "secret")
        HomePage.open_homepage(home)

        self.login(wd, "admin", "secret")

        Contacts.addContact(Contacts(wd=wd, address="Qwerty", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                                 title="Contact", company="MyCompany", home="Str, 7790", mobile="+700", work="", fax="", email2="", email3="",
                                 homepage="www.my.org", address2="", phone2="", notes="++++++++++", bday="4", aday="" , amonth= "July",
                                 bmonth= "May", group=""))

        wd.find_element_by_link_text("home page").click()
        time.sleep(3)


      # Добавление нового контакта в группу New_01
    def test_TestAddContactToGroup(self):

        # Страница авторизации
        global home
        home = HomePage(wd = wd, login = "admin", password = "secret")

        HomePage.open_homepage(home)

        self.login(wd, "admin", "secret")

        Contacts.addContact(Contacts(wd=wd, address="Qwerty", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                                 title="Contact", company="MyCompany", home="Str, 7790", mobile="+700", work="", fax="", email2="", email3="fff@bar.ru",
                                 homepage="www.my.org", address2="964646466", phone2="146546546", notes="++++++++++", bday="4", aday="" , amonth= "July",
                                 bmonth= "", group="New_01"))

        wd.find_element_by_link_text("home page").click()
        time.sleep(3)

if __name__ == '__main__':
    unittest.main()
