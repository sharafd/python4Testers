# -*- coding: utf-8 -*-

# Проверки  контактов - удаление
from random import randrange

import allure
from model import *

contact = Contact(address="Qwerty", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                  title="Contact", company="MyCompany", home="7795", mobile="+7", work="SOHO", fax="545454554",
                  email2="employee@company.org", email3="boss@foo.org", homepage="www.my.org", address2="Samara",
                  phone2="+999", notes="++++++++++", bday="4", aday="14", amonth= "July", bmonth= "May", group=None,
                  email = "mymail@hosting.com")

@allure.feature('Проверки  контактов - удаление')
@allure.story('Тест - удаление первой в списке группы контактов')
def test_delete_contact(app, db, checkUI):
    app.session.to_homepage()
    if not app.contacts.count == 0:
        # Контактов нет - создадим
        app.contacts.addContact(contact)
        app.session.to_homepage()
    # Запoминаем список контактов
    old_contacts = db.database.get_contacts_list()
    # Удаляем группу контактов
    app.contacts.delete_first_contact()
    app.session.to_homepage()
    # Сравниваем размер списков
    if checkUI:
        assert len(old_contacts) - 1 == app.contacts.count()
    #  Получаем новый список контактов
    new_contacts = db.database.get_contacts_list()
    # Сравниваем списки по содержимому
    old_contacts[0:1] = []
    assert old_contacts.sort() == new_contacts.sort()
    if checkUI:
        assert app.contacts.get_contacts_list().sort() == new_contacts.sort()

@allure.feature('Проверки  контактов - удаление')
@allure.story('Тест - удаление случайно выбранного контактa')
def test_delete_random_contact(app, db, checkUI):
    app.session.to_homepage()
    if not app.contacts.count == 0:
        # Контактов нет - создадим
        app.contacts.addContact(contact)
        app.session.to_homepage()
    # Запoминаем список контактов
    old_contacts = db.database.get_contacts_list()
    # Cлучайным образом выбираем, что будем удалять
    index = randrange(len(old_contacts))
    # Удаляем группу контактов
    app.contacts.delete_contact_by_index(index)
    app.session.to_homepage()
    # Сравниваем размер списков
    if checkUI:
        assert len(old_contacts) - 1 == app.contacts.count()
    #  Получаем новый список контактов
    new_contacts = db.database.get_contacts_list()
    # Сравниваем списки по содержимому
    old_contacts[index:index:1] = []
    assert old_contacts.sort() == new_contacts.sort()
    if checkUI:
        assert app.contacts.get_contacts_list().sort() == new_contacts.sort()