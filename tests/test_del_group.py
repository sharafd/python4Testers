# -*- coding: utf-8 -*-

# Проверки групп контактов - удаление
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
    #  Получаем новый список групп
    new_groups = app.group.get_groups_list()
    # Сравниваем размер списков
    assert len(old_groups) - 1 == len(new_groups)
    # Сравниваем списки по содержимому
    old_groups[0:1] = []
    assert old_groups == new_groups

# Тест - удаление  группы контактов по имени
def test_delete_group_by_name(app):
    if not app.group.is_group_exist(name = "New_01"):
        create_group(app)
    old_groups = app.group.get_groups_list()
    app.group.delete_contacts_group_by_name("New_01")
    new_groups = app.group.get_groups_list()
    assert len(old_groups) - 1 == len(new_groups)
