# -*- coding: utf-8 -*-

# Проверки групп контактов - редактирование

from model import LoginPage, Groups

# Параметры авторизации
login = LoginPage(login = "admin", password = "secret")

# Тест - редактирование группы контактов по имени
def test_edit_group_by_name(app):
    # Параметры группы контактов
    group = Groups(name="New_06661", header="664464664", footer= None)
    # Логин
    app.session.ensure_login(login, "admin")
    # редактирование группы контактов по имени
    app.group.edit_contacts_group_by_name(name = "New_01", groups = group)

# Тест - редактирование группы контактов по имени - только наименование
def test_edit_first_contacts_group(app):
    # Параметры группы контактов
    group = Groups(name="New_045456661")

    app.session.ensure_login(login, "admin")
    # редактирование первой в списке группы контактов
    app.group.edit_first_contacts_group(groups = group)
