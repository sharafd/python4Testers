# -*- coding: utf-8 -*-

# Проверки групп контактов

from model import LoginPage

 # Тест - удаление первой группы контактов
def test_add_group(app):
    # Страница авторизации
    login = LoginPage(login="admin", password="secret")
    # Открытие страницы
    app.session.open_login_page()
    # Логин
    app.session.login(login)
    # Удаляем группу контактов
    app.group.delete_first_contacts_group()
    # Выход
    app.session.logout()
