# -*- coding: utf-8 -*-

# Проверки групп контактов - добавление

from model import LoginPage, Groups

 # Тест - создание группы контактов
def test_add_group(app):
    # Страница авторизации
    login = LoginPage(login="admin", password="secret")
    # Параметры группы контактов
    group = Groups(name="New_01", header="+", footer="------------")
    # Открытие страницы
    app.session.open_login_page()
    # Логин
    app.session.login(login)
    # Создаём группу контактов
    app.group.add_new_contacts_group(group)
    # Выход
    app.session.logout()

# Тест - создание группы контактов, пустые name, header, footer
def test_add_group_empty_params(app):
    login = LoginPage(login="admin", password="secret")
    group = Groups(name=None, header=None, footer=None)

    app.session.open_login_page()
    app.session.login(login)

    app.group.add_new_contacts_group(group)

    app.session.logout()
