# -*- coding: utf-8 -*-

# Проверки групп контактов - редактирование

from model import LoginPage, Groups

# Тест - редактирование группы контактов по имени
def test_edit_group_by_name(app):
      # Параметры группы контактов
    group = Groups(name="New_06661", header="664464664", footer= None)
    # Страница авторизации
    login = LoginPage(login="admin", password="secret")
    # Открытие страницы
    app.session.open_login_page()
    # Логин
    app.session.login(login)

    app.group.edit_contacts_group_by_name(name = "New_01", groups = group)
    # Выход
    app.session.logout()

# Тест - редактирование группы контактов по имени - только наименование
def test_edit_first_contacts_group(app):
      # Параметры группы контактов
    group = Groups(name="New_045456661")
    # Страница авторизации
    login = LoginPage(login="admin", password="secret")
    # Открытие страницы
    app.session.open_login_page()
    # Логин
    app.session.login(login)

    app.group.edit_first_contacts_group(groups = group)
    # Выход
    app.session.logout()
