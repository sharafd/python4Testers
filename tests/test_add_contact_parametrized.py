# -*- coding: utf-8 -*-

# Проверки контактов - добавление - добавление из параметра
import allure
import os

import pytest
from generator.contacts import generate_json
from model import *
from func import commonFunctions

common = commonFunctions.Common()

# Параметры  контактов
testdata = [Contact(address=common.random_string(10), middlename=common.random_ascii_string(10), lastname=common.random_ascii_string(10), firstname ="FOO",
                    nickname=common.random_ascii_string(10), byear="1988", ayear="2000", email = "mymail@hosting.com",
                    title=common.random_string(10), company=common.random_string(10), home=common.random_digits(5), mobile="+7",
                    work=common.random_digits(5), fax=common.random_digits(11),
                    email2="employee@company.org", email3="boss@foo.org", homepage="www.my.org", address2="Samara",
                    photo= os.path.join(os.path.abspath(os.path.dirname(__file__)), "../resources/avatar.png"),
                    phone2=common.random_digits(5), notes="++++++++++", bday="4", aday="14", amonth= "July", bmonth= "May", group=None)
            for i in range(4)
            ]

 # Тест - создание группы контактов
@allure.feature('Проверки контактов - добавление - добавление из параметра')
@allure.story('Cоздание группы контактов')
@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_TestAddContact_parametrized(app, contact, db, checkUI):
    app.session.to_homepage()
    # Запoминаем список контактов
    old_contacts = db.database.get_contacts_list()

    app.contacts.addContact(contact)
    app.session.to_homepage()
    # Сравниваем размер списков
    if checkUI:
        assert len(old_contacts) + 1 == app.contacts.count()
    #  Получаем новый список контактов
    new_contacts = db.database.get_contacts_list()
    # Сравниваем списки по содержимому
    assert old_contacts.sort() == new_contacts.sort()
    if checkUI:
        assert app.contacts.get_contacts_list().sort() == new_contacts.sort()

 # Тест - создание группы контактов из JSON
@allure.feature('Проверки контактов - добавление - добавление из параметра')
@allure.story('Тест - создание группы контактов из JSON')
def test_TestAddContact_parametrized_from_json(app, json_contacts, db, checkUI):
    # Формируем тестовые данные
    jsonfile = "../data/groups.json"
    if not os.path.isfile(os.path.join(os.path.abspath(os.path.dirname(__file__)), jsonfile)):
        generate_json(1, jsonfile)

    app.session.to_homepage()
    # Запoминаем список контактов
    old_contacts = db.database.get_contacts_list()
    app.contacts.addContact(json_contacts)
    app.session.to_homepage()
    # Сравниваем размер списков
    if checkUI:
        assert len(old_contacts) + 1 == app.contacts.count()
    #  Получаем новый список контактов
    new_contacts = app.contacts.get_contacts_list()
    # Сравниваем списки по содержимому
    assert old_contacts.sort() == new_contacts.sort()
    if checkUI:
        assert app.contacts.get_contacts_list().sort() == new_contacts.sort()