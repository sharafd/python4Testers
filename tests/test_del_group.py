# -*- coding: utf-8 -*-

# Проверки групп контактов - удаление

# Тест - удаление первой группы контактов
def test_delete_first_group(app):
    # Удаляем группу контактов
    app.group.delete_first_contacts_group()

# Тест - удаление  группы контактов по имени
def test_delete_group_by_name(app):
    # Удаляем группу контактов
    app.group.delete_contacts_group_by_name(name = "New_01")
