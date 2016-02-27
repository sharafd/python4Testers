# -*- coding: utf-8 -*-

# Проверки контактов - добавление

import os

from model import *
from func import commonFunctions
common = commonFunctions.Common()

# Добавление нового контакта без привязки к группе
def test_TestAddContact(app):
    app.session.to_homepage()
    # Запoминаем список контактов
    old_contacts = app.contacts.get_contacts_list()

    app.contacts.addContact(Contacts(address=common.random_ascii_string(10), middlename=common.random_ascii_string(10), lastname=common.random_ascii_string(10),
                                     nickname=common.random_ascii_string(10), byear="1988", ayear="2000",email = "mymail@hosting.com",
                             title="Contact", company="MyCompany", home="S79", mobile="+7", work="SOHO", fax="545454554",
                             email2="employee@company.org", email3="boss@foo.org", homepage="www.my.org", address2="Samara",
                             photo= os.path.join(os.path.abspath(os.path.dirname(__file__)), "../resources/avatar.png"), phone2="+999",
                             notes="++++++++++", bday="4", aday="14", amonth= "July", bmonth= "May", group=None))
    app.session.to_homepage()
    # Сравниваем размер списков
    assert len(old_contacts) + 1 == app.contacts.count()
    #  Получаем новый список контактов
    new_contacts = app.contacts.get_contacts_list()
    # Сравниваем списки по содержимому
    assert old_contacts.sort() == new_contacts.sort()

# Добавление нового контакта в группу New_01
def test_TestAddContactToGroup(app):
    if not app.group.is_group_exist(name = "New_01"):
        # группы нет - надо создать
        app.group.add_new_contacts_group(Groups(name="New_01"))
    app.session.to_homepage()
    old_contacts = app.contacts.get_contacts_list()
    app.contacts.addContact(Contacts(address="Qwerty", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",email = "mymail@hosting.com",
                             title="Contact", company="MyCompany", home="S779", mobile="+76-6", work="56641646", fax="", email2="", email3="fff@bar.ru",
                             homepage="www.my.org", address2="964646466", phone2="146546546", notes="++++++++++", bday="4", aday="6" , amonth= "July",
                             bmonth= "", photo= "", group="New_01"))
    app.session.to_homepage()
    # Сравниваем размер списков
    assert len(old_contacts) + 1 == app.contacts.count()
    #  Получаем новый список контактов
    new_contacts = app.contacts.get_contacts_list()
    # Сравниваем списки по содержимому
    assert old_contacts.sort() == new_contacts.sort()
