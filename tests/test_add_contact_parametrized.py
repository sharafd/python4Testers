# -*- coding: utf-8 -*-

# Проверки контактов - добавление - добавление из параметра

import os

import pytest
from model import *
from func import commonFunctions

common = commonFunctions.Common()
root_dir = os.path.abspath(os.path.dirname(__file__))

# Параметры  контактов
testdata = [Contacts(address=common.random_string(10), middlename=common.random_ascii_string(10), lastname=common.random_ascii_string(10), firstname = "FOO",
                                     nickname=common.random_ascii_string(10), byear="1988", ayear="2000",email = "mymail@hosting.com",
                             title=common.random_string(10), company=common.random_string(10), home=common.random_digits(5), mobile="+7", work=common.random_digits(5), fax=common.random_digits(11),
                             email2="employee@company.org", email3="boss@foo.org", homepage="www.my.org", address2="Samara",
                             photo= root_dir + "/resources/avatar.png", phone2=common.random_digits(5), notes="++++++++++", bday="4", aday="14",
                             amonth= "July", bmonth= "May", group=None)
    for i in range(4)
]

 # Тест - создание группы контактов
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_TestAddContact_parametrized(app, contact):
    root_dir = os.path.abspath(os.path.dirname(__file__))
    app.session.to_homepage()
    # Запoминаем список контактов
    old_contacts = app.contacts.get_contacts_list()

    app.contacts.addContact(contact)
    app.session.to_homepage()
    # Сравниваем размер списков
    assert len(old_contacts) + 1 == app.contacts.count()
    #  Получаем новый список контактов
    new_contacts = app.contacts.get_contacts_list()
    # Сравниваем списки по содержимому
    assert old_contacts.sort() == new_contacts.sort()

