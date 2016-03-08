# -*- coding: utf-8 -*-
# Проверки групп и контактов - смравнение с БД

import os
from fixtures import ORMFixture
from func import commonFunctions
from model import Group, Contact

common = commonFunctions.Common()

root_dir = os.path.abspath(os.path.dirname(__file__))
contact = Contact(address='phones_test', middlename=common.random_ascii_string(10), lastname=common.random_ascii_string(10),
                  nickname=common.random_ascii_string(10), byear="1988", ayear="2000", email = "mymail@hosting.com",
                  title="Contact", company="MyCompany", home="779", mobile="+75-1", work="+951-705-96-11", fax="545454554",
                  email2="employee@company.org", email3="boss@foo.org", homepage="www.my.org", address2="Samara",
                  photo= os.path.join(os.path.abspath(os.path.dirname(__file__)), "../resources/avatar.png"),
                  phone2="+999(55)6", notes="++++++++++", bday="4", aday="14", amonth= "July", bmonth= "May", group=None)

# Создаём группу контактов
def create_group(app):
    group = Group(name="New_01")
    app.group.add_new_contacts_group(group)

# dbfixture
def test_groups_list(app, db):
    if not app.group.is_group_exist:
        # групп нет - надо создать
        create_group(app)
    # Запоминаем список групп
    ui_list = app.group.get_groups_list()
    #  Получаем список групп из БД
    db_list = map(app.group.format_groups_as_from_ui, db.database.get_groups_list())

    assert ui_list.sort() == db_list.sort()

# dbfixture
def test_contacts_list(app, db):

    app.session.to_homepage()
    #Принудительная очистка кеша во избежание сравнения с несуществующими в кеше полями
    app.contacts.clear_cache()
    # Ищем контакт с правильно заполненными телефонами
    index = app.contacts.get_contact_index_by_address("phones_test")
    if -1 == index:
    # Контакта нет - создадим
        app.contacts.addContact(contact)
        app.session.to_homepage()
        index = 1

    # Запоминаем список
    ui_list = app.contacts.get_contacts_list()
    #  Получаем список  из БД
    db_list = db.database.get_contacts_list()

    assert ui_list.sort() == db_list.sort()

# ORMFixture
def test_groups_list_as_orm(app, orm):

    if not app.group.is_group_exist:
        # групп нет - надо создать
        create_group(app)
    # Запоминаем список групп
    ui_list = app.group.get_groups_list()
    #  Получаем список групп из БД
    db_list = orm.get_groups_list()

    assert(ui_list.sort() == db_list.sort())

# ORMFixture
def test_contacts_list_as_orm(app, orm):

    app.session.to_homepage()
    #Принудительная очистка кеша во избежание сравнения с несуществующими в кеше полями
    app.contacts.clear_cache()
    # Ищем контакт с правильно заполненными телефонами
    index = app.contacts.get_contact_index_by_address("phones_test")
    if -1 == index:
    # Контакта нет - создадим
        app.contacts.addContact(contact)
        app.session.to_homepage()
        index = 1

    # Запоминаем список
    ui_list = app.contacts.get_contacts_list()
    #  Получаем список  из БД
    db_list = orm.get_contacts_list()

    assert ui_list.sort() == db_list.sort()
