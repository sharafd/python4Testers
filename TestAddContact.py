# -*- coding: utf-8 -*-

# Проверки контактов

import time, os, unittest

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
       # Получаем корневой каталог тестов с волным путем
       global root_dir
       root_dir = os.path.abspath(os.path.dirname(__file__))

   # Финализация
    def tearDown(self):
        HomePage.logout(home)
        wd.quit()

    # Добавление нового контакта без привязки к группе
    def test_TestAddContact(self):

        # Страница авторизации
        global home
        home = HomePage(wd = wd, login = "admin", password = "secret")

        HomePage.open_homepage(home)
        HomePage.login(home)

        Contacts.addContact(Contacts(wd=wd, address="Qwerty", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                                 title="Contact", company="MyCompany", home="Str, 7790", mobile="+700", work="SOHO", fax="545454554",
                                 email2="employee@company.org", email3="boss@foo.org", homepage="www.my.org", address2="Samara",
                                 photo= root_dir + "/resources/avatar.png", phone2="+999", notes="++++++++++", bday="4", aday="14",
                                 amonth= "July", bmonth= "May", group=""))
        time.sleep(3)
        wd.find_element_by_link_text("home").click()
        time.sleep(3)

    # Добавление нового контакта в группу New_01
    def test_TestAddContactToGroup(self):

        # Страница авторизации
        global home
        home = HomePage(wd = wd, login = "admin", password = "secret")

        HomePage.open_homepage(home)
        HomePage.login(home)

        Contacts.addContact(Contacts(wd=wd, address="Qwerty", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                                 title="Contact", company="MyCompany", home="Str, 7790", mobile="+700", work="", fax="", email2="", email3="fff@bar.ru",
                                 homepage="www.my.org", address2="964646466", phone2="146546546", notes="++++++++++", bday="4", aday="6" , amonth= "July",
                                 bmonth= "", photo= "", group="New_01"))

        wd.find_element_by_link_text("home").click()

if __name__ == '__main__':
    unittest.main()
