# -*- coding: utf-8 -*-
# Проверки групп контактов - добавление из параметра
import os
import pytest

from data import *
from model import Groups
from func import commonFunctions
from generator.groups import generate_json

common = commonFunctions.Common()

# Параметры групп контактов
data = [Groups(name="", header=None, footer=None)]+[
    Groups(name=common.random_string(15), header=common.random_string(),
                   footer=common.random_string(15))
    for i in range(4)
]

 # Тест - создание группы контактов
@pytest.mark.parametrize("group", data, ids=[repr(x) for x in data])
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

 # Тест - создание группы контактов из фикстуры
def test_add_group_from_fixture(app, data_groups):
    # Запоминаем список групп
    old_groups = app.group.get_groups_list()
    # Создаём группу контактов
    app.group.add_new_contacts_group(data_groups)
    # Сравниваем размер списков
    assert len(old_groups) + 1 == app.group.count()
    #  Получаем новый список групп
    new_groups = app.group.get_groups_list()
    # Сравниваем списки по содержимому
    data_groups.name  = "Select (" + data_groups.name + ")"
    old_groups.append(data_groups)
    assert sorted(old_groups, key=Groups.id_or_max) == sorted(new_groups, key=Groups.id_or_max)

 # Тест - создание группы контактов из JSON
def test_add_group_from_json(app, json_groups):
    # Формируем тестовые данные
    jsonfile = "../data/groups.json"
    if not os.path.isfile(os.path.join(os.path.abspath(os.path.dirname(__file__)), jsonfile)):
        generate_json(1, jsonfile)
    # Запоминаем список групп
    old_groups = app.group.get_groups_list()
    # Создаём группу контактов
    app.group.add_new_contacts_group(json_groups)
    # Сравниваем размер списков
    assert len(old_groups) + 1 == app.group.count()
    #  Получаем новый список групп
    new_groups = app.group.get_groups_list()
    # Сравниваем списки по содержимому
    json_groups.name  = "Select (" + json_groups.name + ")"
    old_groups.append(json_groups)
    assert sorted(old_groups, key=Groups.id_or_max) == sorted(new_groups, key=Groups.id_or_max)