# -*- coding: utf-8 -*-

# Проверки  контактов - удаление

from model import *

# Тест - удаление первой в списке группы контактов
def test_delete_group(app):
    app.session.to_homepage()
    if not app.contacts.is_contact_exist():
        # Контактов нет - создадим
        app.contacts.addContact(Contacts(address="Qwerty", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                             title="Contact", company="MyCompany", home="Str, 7790", mobile="+700", work="SOHO", fax="545454554",
                             email2="employee@company.org", email3="boss@foo.org", homepage="www.my.org", address2="Samara",
                             phone2="+999", notes="++++++++++", bday="4", aday="14", amonth= "July", bmonth= "May", group=None))
        app.session.to_homepage()
    # Запoминаем список контактов
    old_contacts = app.contacts.get_contacts_list()
    # Удаляем группу контактов
    app.contacts.delete_first_contact()
    #  Получаем новый список контактов
    app.session.to_homepage()
    new_contacts = app.contacts.get_contacts_list()
    # Сравниваем размер списков
    assert len(old_contacts) - 1 == len(new_contacts)
    # Сравниваем списки по содержимому
    old_contacts[0:1] = []
    assert old_contacts == new_contacts