# -*- coding: utf-8 -*-
# Проверки групп контактов - добавление из параметра

import pytest
from data import *
from model import Groups
from func import commonFunctions

common = commonFunctions.Common()

# Параметры групп контактов
testdata = [Groups(name="", header=None, footer=None)]+[
    Groups(name=common.random_string(15), header=common.random_string(),
                   footer=common.random_string(15))
    for i in range(4)
]

 # Тест - создание группы контактов
@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group_parametrize(app, group):
    # Запоминаем список групп
    old_groups = app.group.get_groups_list()
    # Создаём группу контактов
    app.group.add_new_contacts_group(group)
    # Сравниваем размер списков
    assert len(old_groups) + 1 == app.group.count()
    #  Получаем новый список групп
    new_groups = app.group.get_groups_list()
    # Сравниваем списки по содержимому
    group.name  = "Select ("+ group.name +")"
    old_groups.append(group)
    assert sorted(old_groups, key=Groups.id_or_max) == sorted(new_groups, key=Groups.id_or_max)

 # Тест - создание группы контактов из генератора данных
@pytest.mark.parametrize("group", groups_testdata, ids=[repr(x) for x in groups_testdata])
def test_add_group_from_generator(app, group):
    # Запоминаем список групп
    old_groups = app.group.get_groups_list()
    # Создаём группу контактов
    app.group.add_new_contacts_group(group)
    # Сравниваем размер списков
    assert len(old_groups) + 1 == app.group.count()
    #  Получаем новый список групп
    new_groups = app.group.get_groups_list()
    # Сравниваем списки по содержимому
    group.name  = "Select ("+ group.name +")"
    old_groups.append(group)
    assert sorted(old_groups, key=Groups.id_or_max) == sorted(new_groups, key=Groups.id_or_max)

 # Тест - создание группы контактов из генератора данных
@pytest.mark.parametrize("group", constant_group_data, ids=[repr(x) for x in constant_group_data])
def test_add_group_from_constant(app, group):
    # Запоминаем список групп
    old_groups = app.group.get_groups_list()
    # Создаём группу контактов
    app.group.add_new_contacts_group(group)
    # Сравниваем размер списков
    assert len(old_groups) + 1 == app.group.count()
    #  Получаем новый список групп
    new_groups = app.group.get_groups_list()
    # Сравниваем списки по содержимому
    group.name  = "Select ("+ group.name +")"
    old_groups.append(group)
    assert sorted(old_groups, key=Groups.id_or_max) == sorted(new_groups, key=Groups.id_or_max)