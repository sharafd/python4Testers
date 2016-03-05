# -*- coding: utf-8 -*-

# Проверки групп контактов - удаление
from random import randrange
import random
from model import Group

# Создаём группу контактов
def create_group(app):
    group = Group(name="New_01")
    app.group.add_new_contacts_group(group)

# Тест - удаление первой группы контактов
def test_delete_first_group(app,db,checkUI):
    if not app.group.is_group_exist:
        # групп нет - надо создать
        create_group(app)
     # Запoминаем список групп
    old_groups = db.database.get_groups_list()
    # Удаляем группу контактов
    app.group.delete_first_contacts_group()
    #  Получаем новый список групп
    new_groups = db.database.get_groups_list()
 #   old_groups[0:1] = []
    # Удаляем  правильную группу
    group = app.group.get_group_by_position(1)
    group.name = group.name[9:-1] # изюавляемся от Select ( в имени группы
    old_groups.remove(group)
    assert old_groups.sort() == new_groups.sort()
    # Отключаемая проверка с интерфейса
    if (checkUI):
      assert app.group.get_groups_list().sort() == new_groups.sort()


# Тест - удаление группы контактов по имени
def test_delete_group_by_name(app,db,checkUI):
   group = Group(name="New_01")
   if not app.group.is_group_exist(group.name):
      app.group.add_new_contacts_group(group)
   old_groups = db.database.get_groups_list()
   # Запоминаем идентификатор удаленной группы
   group.id = app.group.delete_contacts_group_by_name(group.name)
   #  Получаем новый список групп
   new_groups = db.database.get_groups_list()
 #  group.name = "Select ("+ group.name +")"
   old_groups.remove(group) # Удаляем  правильную группу
   # cравниваем
   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
   if (checkUI):
      assert app.group.get_groups_list().sort() == new_groups.sort()

# Тест - удаление случайно выбранной группы контактов
def test_delete_random_group(app,db,checkUI):
    if not app.group.count == 0:
        # групп нет - надо создать
        create_group(app)
     # Запoминаем список групп
  #  old_groups = app.group.get_groups_list()
    old_groups = db.database.get_groups_list()
    # Cлучайным образом выбираем, что будем удалять
   # index = randrange(len(old_groups))
    group = random.choice(old_groups)
    # Удаляем группу контактов
  #  app.group.delete_contacts_group_by_position(index)
    app.group.delete_contacts_group_by_id(group.id)
    # Сравниваем размер списков
    if (checkUI):
        assert len(old_groups) - 1 == app.group.count()
    #  Получаем новый список групп
   # new_groups = app.group.get_groups_list()
    new_groups = db.database.get_groups_list()
   # old_groups[index:index:1] = []
    old_groups.remove(group) # Удаляем  правильную группу
    # Сравниваем списки по содержимому
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if (checkUI):
      assert app.group.get_groups_list().sort() == new_groups.sort()
