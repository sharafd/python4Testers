# -*- coding: utf-8 -*-

# Проверки групп контактов - телефоны
from random import randrange

import os
from model import Contacts
from func import commonFunctions
common = commonFunctions.Common()

root_dir = os.path.abspath(os.path.dirname(__file__))
contact = Contacts(address='phones_test', middlename=common.random_ascii_string(10), lastname=common.random_ascii_string(10),
                             nickname=common.random_ascii_string(10), byear="1988", ayear="2000", email = "mymail@hosting.com",
                             title="Contact", company="MyCompany", home="779", mobile="+75-1", work="+951-705-96-11", fax="545454554",
                             email2="employee@company.org", email3="boss@foo.org", homepage="www.my.org", address2="Samara",
                             photo= os.path.join(os.path.abspath(os.path.dirname(__file__)), "resources/avatar.png"),
                             phone2="+999(55)6", notes="++++++++++", bday="4", aday="14", amonth= "July", bmonth= "May", group=None)

# Телефоны на главной странице - прямая проверка
def test_phones_on_homepage_split(app):

    app.session.to_homepage()
    #Принудительная очистка кеша во избежание сравнения с несуществующими в кеше полями
    app.contacts.clear_cache()
    # Ищем контакт с правильно заполненными телефонами
    index = app.contacts.get_contact_index_by_address("phones_test")
    if -1 == index:
    # Контакта нет - создадим
        app.contacts.addContact(contact)
        app.session.to_homepage()
        index = 0

    contacts_from_phone_app = app.contacts.get_contacts_list()[index]
    contacts_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)

    assert(contacts_from_phone_app.home == common.clear(contacts_from_edit_page.home,"[() -]"))
    assert(contacts_from_phone_app.mobile == common.clear(contacts_from_edit_page.mobile,"[() -]"))
    assert(contacts_from_phone_app.work == common.clear(contacts_from_edit_page.work,"[() -]"))
    assert(contacts_from_phone_app.phone2 == common.clear(contacts_from_edit_page.phone2,"[() -]"))

# Телефоны на странице просмотра - прямая проверка
def test_phones_on_viewpage_split(app):
    app.session.to_homepage()
    #Принудительная очистка кеша во избежание сравнения с несуществующими в кеше полями
    app.contacts.clear_cache()
    # Ищем контакт с правильно заполненными телефонами
    index = app.contacts.get_contact_index_by_address("phones_test")
    if -1 == index:
    # Контакта нет - создадим
        app.contacts.addContact(contact)
        app.session.to_homepage()
        index = 0

    contacts_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)

    app.session.to_homepage()

    contacts_from_view_page = app.contacts.get_contact_info_from_view_page(index)

    assert(contacts_from_edit_page.home == contacts_from_view_page.home)
    assert(contacts_from_edit_page.mobile == contacts_from_view_page.mobile)
    assert(contacts_from_edit_page.work == contacts_from_view_page.work)
    assert(contacts_from_edit_page.phone2 == contacts_from_view_page.phone2)

# Телефоны на главной странице - обратная проверка
def test_phones_on_homepage_merge(app):

    app.session.to_homepage()
    if not app.contacts.is_contact_exist():
        # Контактов нет - создадим
        app.contacts.addContact(contact)
        app.session.to_homepage()

    #Принудительная очистка кеша во избежание сравнения с несуществующими в кеше полями
    app.contacts.clear_cache()

    # Cлучайным образом выбираем контакт
    index = randrange(app.contacts.count())

    contacts_from_phone_app = app.contacts.get_contacts_list_merged()[index]
    contacts_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)

    assert(contacts_from_phone_app.all_phones_from_home_page == app.contacts.merge_phones_like_on_home_page(contacts_from_edit_page))
