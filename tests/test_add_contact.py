# -*- coding: utf-8 -*-

# Проверки контактов - добавление

import time, os

from model import *

# Добавление нового контакта без привязки к группе
def test_TestAddContact(app):
    root_dir = os.path.abspath(os.path.dirname(__file__))
    app.session.to_homepage()
    # Запoминаем список контактов
    old_contacts= app.contacts.get_contacts_list()

    app.contacts.addContact(Contacts(address="Qwerty", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                             title="Contact", company="MyCompany", home="Str, 7790", mobile="+700", work="SOHO", fax="545454554",
                             email2="employee@company.org", email3="boss@foo.org", homepage="www.my.org", address2="Samara",
                             photo= root_dir + "/resources/avatar.png", phone2="+999", notes="++++++++++", bday="4", aday="14",
                             amonth= "July", bmonth= "May", group=None))
    #  Получаем новый список контактов
    app.session.to_homepage()
    new_contacts = app.contacts.get_contacts_list()
    # Сравниваем размер списков
    assert len(old_contacts) + 1 == len(new_contacts)
    # Сравниваем списки по содержимому
    assert old_contacts.sort() == new_contacts.sort()

# Добавление нового контакта в группу New_01
def test_TestAddContactToGroup(app):
    if not app.group.is_group_exist(name = "New_01"):
        # группы нет - надо создать
        app.group.add_new_contacts_group(Groups(name="New_01"))
    app.session.to_homepage()
    old_contacts= app.contacts.get_contacts_list()
    app.contacts.addContact(Contacts(address="Qwerty", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                             title="Contact", company="MyCompany", home="Str, 7790", mobile="+700", work="", fax="", email2="", email3="fff@bar.ru",
                             homepage="www.my.org", address2="964646466", phone2="146546546", notes="++++++++++", bday="4", aday="6" , amonth= "July",
                             bmonth= "", photo= "", group="New_01"))
    # Получаем новый список контактов
    app.session.to_homepage()
    new_contacts = app.contacts.get_contacts_list()
    # Сравниваем размер списков
    assert len(old_contacts) + 1 == len(new_contacts)
    # Сравниваем списки по содержимому
    assert old_contacts.sort() == new_contacts.sort()
