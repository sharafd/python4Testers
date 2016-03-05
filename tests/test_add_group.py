# -*- coding: utf-8 -*-

# Проверки групп контактов - добавление
from model import Group
from func import commonFunctions
common = commonFunctions.Common()

 # Тест - создание группы контактов
def test_add_group(app, db, checkUI):
    # Параметры группы контактов
    group = Group(name=common.random_string(15), header=common.random_digits(5), footer=common.random_ascii_string())
    # Запоминаем список групп
  #  old_groups = app.group.get_groups_list()
    old_groups = db.database.get_groups_list()
    # Создаём группу контактов
    app.group.add_new_contacts_group(group)
    # Сравниваем размер списков
    if (checkUI):
      assert len(old_groups) + 1 == app.group.count()
    #  Получаем новый список групп
   # new_groups = app.group.get_groups_list()
    new_groups = db.database.get_groups_list()
    # Сравниваем списки по содержимому
  #  group.name  = "Select ("+ group.name +")"
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if (checkUI):
      assert app.group.get_groups_list().sort() == new_groups.sort()

# Тест - создание группы контактов, пустые name, header, footer
def test_add_group_empty_params(app, db, checkUI):
    group = Group(name=None, header=None, footer=None)
    old_groups = db.database.get_groups_list()
    app.group.add_new_contacts_group(group)
    #  Получаем новый список групп
    new_groups = db.database.get_groups_list()
    # Сравниваем списки по содержимому
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if (checkUI):
      assert app.group.get_groups_list().sort() == new_groups.sort()