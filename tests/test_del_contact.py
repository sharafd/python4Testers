# -*- coding: utf-8 -*-

# Проверки  контактов - удаление

from model import *

# Тест - удаление первой в списке группы контактов
def test_delete_group(app):
    # Удаляем группу контактов
    app.contacts.delete_first_contact()

