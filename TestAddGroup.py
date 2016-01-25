# -*- coding: utf-8 -*-

# Проверки групп контактов

from model import *
from helpers import *

import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class TestAddGroup(unittest.TestCase):

    # Инициализация
    def setUp(self):
       global wd
       # Получаем WebDriver
       wdh = webDriverHelper.WebDriverHelper()
       wd = wdh.wd

   # Финализация
    def tearDown(self):
        HomePage.logout(home)
        wd.quit()

    # Тест - создание группы контактов
    def test_TestAddGroup(self):
        # Страница авторизации
        global home
        home = HomePage(wd = wd, login = "admin", password = "secret")
        # Параметры группы контактов
        group = groups.Groups(wd = wd, name = "New_01", header = "+", footer = "------------")
        # Открытие страницы
        HomePage.open_homepage(home)
        # Логин
        HomePage.login(home)

        time.sleep(3) # Для удобства восприятия

        Groups.add_new_contacts_group(group)
        time.sleep(3)
        wd.find_element_by_link_text("groups").click()
        time.sleep(3)

       # Тест - создание группы контактов, пустые header, footer
    def test_TestAddGroup2(self):
        global home
        home = HomePage(wd = wd, login = "admin", password = "secret")
        group = groups.Groups(wd = wd, name = "New_02", header = "", footer = "")

        HomePage.open_homepage(home)
        HomePage.login(home)

        Groups.add_new_contacts_group(group)

        wd.find_element_by_link_text("groups").click()

if __name__ == '__main__':
    unittest.main()
