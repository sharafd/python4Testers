# -*- coding: utf-8 -*-

# Проверки  контактов - удаление

from model import LoginPage

# Тест - удаление первой в списке группы контактов
def test_delete_group(app):
    # Страница авторизации
    login = LoginPage(login="admin", password="secret")
    # Логин
    app.session.ensure_login(login, "admin")
    # Удаляем группу контактов
    app.contacts.delete_first_contact()

