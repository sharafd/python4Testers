# -*- coding: utf-8 -*-

# Проверки групп контактов - добавление

from model import Groups

 # Тест - создание группы контактов
def test_add_group(app):
    # Параметры группы контактов
    group = Groups(name="New_01", header="+", footer="------------")
    # Создаём группу контактов
    app.group.add_new_contacts_group(group)

# Тест - создание группы контактов, пустые name, header, footer
def test_add_group_empty_params(app):
    group = Groups(name=None, header=None, footer=None)

    app.group.add_new_contacts_group(group)
