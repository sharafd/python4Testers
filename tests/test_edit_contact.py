# -*- coding: utf-8 -*-

# Проверки  контактов - редактирование
from random import randrange

import os
from func import commonFunctions
from model import Contacts

common = commonFunctions.Common()
contact = Contacts(Contacts(address=common.random_string(15), middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                             title="Contact", company="", home="11", mobile="444", work="5656", fax="545454554",
                             email2="", email3="", homepage="", address2="Samara",
                             photo= os.path.join(os.path.abspath(os.path.dirname(__file__)), "../resources/avatar.png"),
                             phone2="+999", notes="++++++++++", bday="4", aday="14", amonth= "July", bmonth= "May", group=""))
new_contact = Contacts(Contacts(address="Qwerty00", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                             title="Contact", company="", home="56565", mobile="566(8)", work="4564", fax="545454554",
                             email2="", email3="", homepage="", address2="Samara",email = "mymail@hosting.com",
                             photo= os.path.join(os.path.abspath(os.path.dirname(__file__)), "../resources/avatar.png"),
                             phone2="+9(5)-78-99", notes="++++++++++", bday="4", aday="14",
                             amonth= "July", bmonth= "May", group=""))

# Редактирование контакта
def test_TestEditContact(app):
    app.session.to_homepage()
    if not app.contacts.is_contact_exist():
        # Контактов нет - создадим
        app.contacts.addContact(contact)
        app.session.to_homepage()

    # Запoминаем список контактов
    old_contacts= app.contacts.get_contacts_list()
    new_contact.id = old_contacts[0].id

    app.contacts.edit_first_contact(new_contact)
    app.session.to_homepage()
    # Сравниваем размер списков
    assert len(old_contacts) == app.contacts.count()
    #  Получаем новый список контактов
    new_contacts = app.contacts.get_contacts_list()
    old_contacts[0] = new_contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

# Удаление фото контакта
def test_TestDelContactPhoto(app):
    if not app.contacts.is_contact_exist():
        # Контактов нет - создадим
        app.contacts.addContact(contact)
        app.session.to_homepage()
    # Запoминаем список контактов
    old_contacts= app.contacts.get_contacts_list()
    new_contact.id = old_contacts[0].id

    app.contacts.delete_first_contact_photo()
    app.session.to_homepage()
    # Сравниваем размер списков
    assert len(old_contacts) == app.contacts.count()
    #  Получаем новый список контактов
    new_contacts = app.contacts.get_contacts_list()
    old_contacts[0] = new_contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

# Редактирование первого контакта со страницы просмотра
def test_TestModifyContact(app):
    app.session.to_homepage()
    if not app.contacts.is_contact_exist():
        # Контактов нет - создадим
        app.contacts.addContact(contact)
        app.session.to_homepage()
    # Запoминаем список контактов
    old_contacts= app.contacts.get_contacts_list()
    new_contact.id = old_contacts[0].id
    app.contacts.modify_first_contact(new_contact)
    app.session.to_homepage()
    # Сравниваем размер списков
    assert len(old_contacts)  == app.contacts.count()
    #  Получаем новый список контактов
    new_contacts = app.contacts.get_contacts_list()
    # Сравниваем списки по содержимому
    old_contacts[0] = new_contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)

# Редактирование случайно выброанного контакта
def test_TestEditRandomContact(app):
    app.session.to_homepage()
    if not app.contacts.is_contact_exist():
        # Контактов нет - создадим
        app.contacts.addContact(contact)
        app.session.to_homepage()
    # Запoминаем список контактов
    old_contacts= app.contacts.get_contacts_list()
    # Cлучайным образом выбираем контакт
    index = randrange(len(old_contacts))
    #  Получаем новый список контактов
    new_contact.id = old_contacts[index].id
    app.contacts.edit_contact_by_index(index,new_contact)
    app.session.to_homepage()
    # Сравниваем размер списков
    assert len(old_contacts) == app.contacts.count()
    #  Получаем новый список контактов
    new_contacts = app.contacts.get_contacts_list()
    old_contacts[index] = new_contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)