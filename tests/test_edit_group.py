# -*- coding: utf-8 -*-

# Проверки групп контактов - редактирование

from model import LoginPage, Groups

# Тест - редактирование группы контактов по имени
def test_edit_group_by_name(app):
    # Параметры группы контактов
    group = Groups(name="New_06661", header="664464664", footer= None)
    # редактирование группы контактов по имени
    if not app.group.is_group_exist(name = "New_01"):
        # группы нет - надо создать
        app.group.add_new_contacts_group(Groups(name="New_01"))
    app.group.edit_contacts_group_by_name(name = "New_01", groups = group)

# Тест - редактирование группы контактов по имени - только наименование
def test_edit_first_contacts_group(app):
    # Параметры группы контактов
    group = Groups(name="New_045456661")
    # редактирование первой в списке группы контактов
    if app.group.is_group_exist():
        # групп нет - надо создать
        app.group.add_new_contacts_group(Groups(name="New_01"))
    app.group.edit_first_contacts_group(groups = group)