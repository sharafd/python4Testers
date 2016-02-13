# -*- coding: utf-8 -*-

# Проверки  контактов - редактирование

import os
from model import Contacts

root_dir = os.path.abspath(os.path.dirname(__file__))

contact = Contacts(Contacts(address="Qwerty00", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                             title="Contact", company="", home="", mobile="", work="", fax="545454554",
                             email2="", email3="", homepage="", address2="Samara",
                             photo= root_dir + "/resources/avatar.png", phone2="+999", notes="++++++++++", bday="4", aday="14",
                             amonth= "July", bmonth= "May", group=""))
new_contact = Contacts(Contacts(address="Qwerty00", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                             title="Contact", company="", home="", mobile="", work="", fax="545454554",
                             email2="", email3="", homepage="", address2="Samara",
                             photo= root_dir + "/resources/avatar.png", phone2="+999", notes="++++++++++", bday="4", aday="14",
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

    app.contacts.editFirstContact(new_contact)
    #  Получаем новый список контактов
    app.session.to_homepage()
    new_contacts = app.contacts.get_contacts_list()
    # Сравниваем размер списков
    assert len(old_contacts) == len(new_contacts)
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

    app.contacts.deleteFirstContactPhoto()
    #  Получаем новый список контактов
    app.session.to_homepage()
    new_contacts = app.contacts.get_contacts_list()
    # Сравниваем размер списков
    assert len(old_contacts) == len(new_contacts)
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
    app.contacts.modifyFirstContact(new_contact)
    #  Получаем новый список контактов
    app.session.to_homepage()
    new_contacts = app.contacts.get_contacts_list()
    # Сравниваем размер списков
    assert len(old_contacts) == len(new_contacts)
    # Сравниваем списки по содержимому
    old_contacts[0] = new_contact
    assert sorted(old_contacts, key=Contacts.id_or_max) == sorted(new_contacts, key=Contacts.id_or_max)