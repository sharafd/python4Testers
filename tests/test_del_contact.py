# -*- coding: utf-8 -*-

# Проверки  контактов - удаление

from model import LoginPage

# Тест - удаление первой в списке группы контактов
def test_delete_group(app):
    # Страница авторизации
    login = LoginPage(login="admin", password="secret")
    # Открытие страницы
    app.session.open_login_page()
    # Логин
    app.session.login(login)
    # Удаляем группу контактов
    app.contacts.delete_first_contact()
    # Выход
    app.session.logout()
