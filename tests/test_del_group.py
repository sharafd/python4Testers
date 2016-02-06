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
    # Удаляем группу контактов
    app.group.delete_first_contacts_group()

# Тест - удаление  группы контактов по имени
def test_delete_group_by_name(app):
    if not app.group.is_group_exist(name = "New_01"):
        # группы нет - надо создать
        create_group(app)
    # Удаляем группу контактов
    app.group.delete_first_contacts_group()