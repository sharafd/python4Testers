# -*- coding: utf-8 -*-

# Проверки групп контактов - добавление
from model import Groups

 # Тест - создание группы контактов
def test_add_group(app):
    # Параметры группы контактов
    group = Groups(name="New_01", header="+", footer="------------")
    # Запоминаем список групп
    old_groups = app.group.get_groups_list()
    # Создаём группу контактов
    app.group.add_new_contacts_group(group)
    #  Получаем новый список групп
    new_groups = app.group.get_groups_list()
    # Сравниваем размер списков
    assert len(old_groups) + 1 == len(new_groups)
    # Сравниваем списки по содержимому
    group.name  = "Select ("+ group.name +")"
    old_groups.append(group)
    assert sorted(old_groups, key=Groups.id_or_max) == sorted(new_groups, key=Groups.id_or_max)

# Тест - создание группы контактов, пустые name, header, footer
def test_add_group_empty_params(app):
    group = Groups(name=None, header=None, footer=None)
    old_groups = app.group.get_groups_list()
    app.group.add_new_contacts_group(group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) + 1 == len(new_groups)
    # Сравниваем списки по содержимому
    group.name  = "Select ("")"
    old_groups.append(group)
    assert sorted(old_groups, key=Groups.id_or_max) == sorted(new_groups, key=Groups.id_or_max)