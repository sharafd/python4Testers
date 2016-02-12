# -*- coding: utf-8 -*-

# Проверки групп контактов - редактирование

from model import LoginPage, Groups

# Тест - редактирование группы контактов по имени
def test_edit_group_by_name(app):
    # Параметры группы контактов
    group = Groups(name="New_06661", header="664464664", footer= None)
    if not app.group.is_group_exist(name = "New_01"):
        # группы нет - надо создать
        app.group.add_new_contacts_group(Groups(name="New_01"))
    # Запoминаем список групп
    old_groups = app.group.get_groups_list()
    # редактирование группы контактов по имени
    app.group.edit_contacts_group_by_name(name = "New_01", groups = group)
    #  Получаем норвый список групп
    new_groups = app.group.get_groups_list()
    # Сравниваем размер списков
    assert len(old_groups) == len(new_groups)

# Тест - редактирование группы контактов  - только наименование
def test_edit_first_contacts_group(app):
    # Параметры группы контактов
    group = Groups(name="New_045456661")
    if app.group.is_group_exist():
        # групп нет - надо создать
        app.group.add_new_contacts_group(Groups(name="New_01"))
     # Запoминаем список групп
    old_groups = app.group.get_groups_list()
    # редактирование группы контактов
    app.group.edit_first_contacts_group(groups = group)
    #  Получаем норвый список групп
    new_groups = app.group.get_groups_list()
    # Сравниваем размер списков
    assert len(old_groups) == len(new_groups)