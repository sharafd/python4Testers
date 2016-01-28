# -*- coding: utf-8 -*-

# Проверки групп контактов

from application import Application


import time, pytest

from model import HomePage, Groups


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy())
    return fixture

# Тест - создание группы контактов
def test_TestAddGroup(app):
    # Страница авторизации
    home = HomePage(wd=app.wd, login="admin", password="secret")
    # Параметры группы контактов
    group = Groups(wd=app.wd, name="New_01", header="+", footer="------------")
    # Открытие страницы
    HomePage.open_homepage(home)
    # Логин
    HomePage.login(home)
    time.sleep(3)  # Для удобства восприятия
    Groups.add_new_contacts_group(group)
    time.sleep(3)
    HomePage.logout(home)
    time.sleep(3)

# Тест - создание группы контактов, пустые header, footer
def test_TestAddGroup2(app):
    home = HomePage(wd=app.wd, login="admin", password="secret")
    group = Groups(wd=app.wd, name="New_02", header="", footer="")

    HomePage.open_homepage(home)
    HomePage.login(home)

    Groups.add_new_contacts_group(group)

    HomePage.logout(home)
