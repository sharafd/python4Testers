# -*- coding: utf-8 -*-

# Проверки групп контактов - удаление

from model import LoginPage

# Параметры авторизации
login = LoginPage(login = "admin", password = "secret")

# Тест - удаление первой группы контактов
def test_delete_first_group(app):
    # Логин
    app.session.login(login)
    # Удаляем группу контактов
    app.group.delete_first_contacts_group()

# Тест - удаление  группы контактов по имени
def test_delete_group_by_name(app):
    # Логин
    app.session.login(login)
    # Удаляем группу контактов
    app.group.delete_contacts_group_by_name(name = "New_01")
