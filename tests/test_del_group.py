# -*- coding: utf-8 -*-

# Проверки групп контактов - удаление

from model import LoginPage

# Тест - удаление первой группы контактов
def test_delete_first_group(app):
    # Страница авторизации
    login = LoginPage(login="admin", password="secret")
    # Открытие страницы
    app.session.open_login_page()
    # Логин
    app.session.login(login)
    # Удаляем группу контактов
    app.group.delete_first_contacts_group()
    # Выход
    app.session.logout()

# Тест - удаление  группы контактов по имени
def test_delete_group_by_name(app):
    # Страница авторизации
    login = LoginPage(login="admin", password="secret")
    # Открытие страницы
    app.session.open_login_page()
    # Логин
    app.session.login(login)
    # Удаляем группу контактов
    app.group.delete_contacts_group_by_name(name = "New_01")
    # Выход
    app.session.logout()
