# -*- coding: utf-8 -*-

from random import randrange

import time

import os
from func import commonFunctions
from model import Contacts

common = commonFunctions.Common()

root_dir = os.path.abspath(os.path.dirname(__file__))
contact = Contacts(address='phones_test', middlename=common.random_ascii_string(10), lastname=common.random_ascii_string(10),
                                     nickname=common.random_ascii_string(10), byear="1988", ayear="2000", email = "mymail@hosting.com",
                             title="Contact", company="MyCompany", home="779", mobile="+75-1", work="+951-705-96-11", fax="545454554",
                             email2="employee@company.org", email3="boss@foo.org", homepage="www.my.org", address2="Samara",
                             photo= root_dir + "/resources/avatar.png", phone2="+999(55)6", notes="++++++++++", bday="4", aday="14",
                             amonth= "July", bmonth= "May", group=None)

# Инфо о контакте на главной странице - прямая проверка
def test_compare_contact_info_split(app):

    app.session.to_homepage()
    #Принудительная очистка кеша
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
  #  assert(contacts_from_phone_app.phone2 == common.clear(contacts_from_edit_page.phone2,"[() -]"))
    assert(contacts_from_phone_app.email == contacts_from_edit_page.email)
    assert(contacts_from_phone_app.email2 == contacts_from_edit_page.email2)
  #  assert(contacts_from_phone_app.email3 == contacts_from_edit_page.email3)

# Инфо о контакте на главной странице - обратная проверка
def test_compare_contact_info_merge(app):

    app.session.to_homepage()
    if not app.contacts.is_contact_exist():
        # Контактов нет - создадим
        app.contacts.addContact(contact)
        app.session.to_homepage()

    #Принудительная очистка кеша
    app.contacts.clear_cache()

    # Cлучайным образом выбираем контакт
    index = randrange(app.contacts.count())

    contacts_from_phone_app = app.contacts.get_contacts_list_merged()[index]
    contacts_from_edit_page = app.contacts.get_contact_info_from_edit_page(index)

    assert(contacts_from_phone_app.all_emails_from_home_page == app.contacts.merge_emails_like_on_home_page(contacts_from_edit_page))
    assert(contacts_from_phone_app.all_phones_from_home_page == app.contacts.merge_phones_like_on_home_page(contacts_from_edit_page))
