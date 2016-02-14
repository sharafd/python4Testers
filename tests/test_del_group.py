# -*- coding: utf-8 -*-

# Проверки групп контактов - удаление
from random import randrange
from model import Groups

# Создаём группу контактов
def create_group(app):
    group = Groups(name="New_01")
    app.group.add_new_contacts_group(group)

# Тест - удаление первой группы контактов
def test_delete_first_group(app):
    if not app.group.is_group_exist:
        # групп нет - надо создать
        create_group(app)
     # Запoминаем список групп
    old_groups = app.group.get_groups_list()
    # Удаляем группу контактов
    app.group.delete_first_contacts_group()
    # Сравниваем размер списков
    assert len(old_groups) - 1 == app.group.count()
    #  Получаем новый список групп
    new_groups = app.group.get_groups_list()
    # Сравниваем списки по содержимому
    old_groups[0:1] = []
    assert old_groups == new_groups

# Тест - удаление группы контактов по имени
def test_delete_group_by_name(app):
   group = Groups(name="New_01")
   if not app.group.is_group_exist(group.name):
      app.group.add_new_contacts_group(group)
   old_groups = app.group.get_groups_list()
   # Запоминаем идентификатор удаленной группы
   group.id = app.group.delete_contacts_group_by_name(group.name)
   # Сравниваем размер списков
   assert len(old_groups) - 1 == app.group.count()
   # Сравниваем списки по содержимому
      #  Получаем новый список групп
   new_groups = app.group.get_groups_list()
   group.name = "Select ("+ group.name +")"
   old_groups.remove(group) # Удаляем  правильную группу
   # cравниваем
   assert old_groups.sort() == new_groups.sort()

# Тест - удаление случайно выбранной группы контактов
def test_delete_random_group(app):
    if not app.group.count == 0:
        # групп нет - надо создать
        create_group(app)
     # Запoминаем список групп
    old_groups = app.group.get_groups_list()
    # Cлучайным образом выбираем, что будем удалять
    index = randrange(len(old_groups))
    # Удаляем группу контактов
    app.group.delete_contacts_group_by_position(index)
    # Сравниваем размер списков
    assert len(old_groups) - 1 == app.group.count()
    #  Получаем новый список групп
    new_groups = app.group.get_groups_list()
    # Сравниваем списки по содержимому
    old_groups[index:index:1] = []
    assert old_groups.sort() == new_groups.sort()