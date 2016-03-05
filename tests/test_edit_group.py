# -*- coding: utf-8 -*-

# Проверки групп контактов - редактирование
from random import randrange

from model import Group

# Тест - редактирование группы контактов по имени
def test_edit_group_by_name(app):
    # Параметры групп контактов
    group = Group(name="New_06661", header="664464664", footer= None)
    editgroup = Group(name="New_01")
    if not app.group.is_group_exist(editgroup.name):
        # группы нет - надо создать
        app.group.add_new_contacts_group(editgroup)
    # Запoминаем список групп
    old_groups = app.group.get_groups_list()
    # редактирование группы контактов по имени
    editgroup.id = app.group.edit_contacts_group_by_name(name = "New_01", groups = group)
    # Сравниваем размер списков
    assert len(old_groups) == app.group.count()
    #  Получаем норвый список групп
    new_groups = app.group.get_groups_list()
    # Сравниваем списки по содержимому
    editgroup.name = "Select " + "(%s)" % editgroup.name
    old_groups.remove(editgroup) # Удаляем отредактирорванную группу
    # записываем в списoк исправленную группу
    group.id = editgroup.id
    old_groups.append(group)
    # cравниваем
    assert old_groups.sort() == new_groups.sort()

# Тест - редактирование группы контактов  - только наименование
def test_edit_first_contacts_group(app):
    # Параметры группы контактов
    group = Group(name="New_045456661")
    if app.group.is_group_exist():
        # групп нет - надо создать
        app.group.add_new_contacts_group(Group(name="New_01"))
    # Запoминаем список групп
    old_groups = app.group.get_groups_list()
    group.id = old_groups[0].id
    # редактирование группы контактов
    app.group.edit_first_contacts_group(groups = group)
    # Сравниваем размер списков
    assert len(old_groups) == app.group.count()
    #  Получаем норвый список групп
    new_groups = app.group.get_groups_list()
    # Сравниваем списки по содержимому
    old_groups[0]= group
    old_groups[0].name = "Select " + "(%s)" % group.name
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# Тест - редактирование группы контактов
def test_edit_random_contacts_group(app):
    # Параметры группы контактов
    group = Group(name="New_045456661")
    if app.group.count == 0:
        # групп нет - надо создать
        app.group.add_new_contacts_group(Group(name="New_01"))
    # Запoминаем список групп
    old_groups = app.group.get_groups_list()
    # случайно выбираем группу
    index = randrange(len(old_groups))
    group.id = old_groups[index].id
    # редактирование группы контактов
    app.group.edit_contacts_group_by_position(index=index,groups = group)
    # Сравниваем размер списков
    assert len(old_groups) == app.group.count()
    #  Получаем норвый список групп
    new_groups = app.group.get_groups_list()
    # Сравниваем списки по содержимому
    old_groups[index]= group
    old_groups[index].name = "Select " + "(%s)" % group.name
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
