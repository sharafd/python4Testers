# -*- coding: utf-8 -*-

# Проверки групп контактов - добавление

from model import LoginPage, Groups

# Параметры авторизации
login = LoginPage(login = "admin", password = "secret")

 # Тест - создание группы контактов
def test_add_group(app):
    # Параметры группы контактов
    group = Groups(name="New_01", header="+", footer="------------")
    # Логин
    app.session.ensure_login(login, "admin")
    # Создаём группу контактов
    app.group.add_new_contacts_group(group)

# Тест - создание группы контактов, пустые name, header, footer
def test_add_group_empty_params(app):
    group = Groups(name=None, header=None, footer=None)

    app.session.ensure_login(login, "admin")
    app.group.add_new_contacts_group(group)
