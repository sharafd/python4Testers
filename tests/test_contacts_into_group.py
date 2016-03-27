# -*- coding: utf-8 -*-
# Проверки нахождения котакта в группе - сравнение с БД
import allure
from model import Contact, Group

group = Group(name="Group_for_ORM")
contact = Contact(middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000", email ="mymail@hosting.com",
                  title="Contact", company="MyCompany", home="S779", mobile="+76-6", work="56641646", fax="", email2="", email3="fff@bar.ru",
                  homepage="www.my.org", address2="964646466", phone2="146546546", notes="++++++++++", bday="4", aday="6", amonth= "July",
                  bmonth= "", photo= "", group=group.name, address = group.name)

@allure.feature('Проверки нахождения контакта в группе - сравнение с БД')
@allure.story('Добавление контакта в группу')
def test_TestAddContactIntoGroup(app, orm, checkUI):
    if not app.group.is_group_exist(group.name):
        # группы нет - надо создать
        app.group.add_new_contacts_group(group)
    app.session.to_homepage()
    app.contacts.addContact(contact)
    app.session.to_homepage()

    # Ищем контакт в списке контактов группы
    group.id = app.group.get_contacts_group_id_by_name(group)
    contacts_in_group = orm.get_contacts_in_groups(group)

    assert (contact in list(contacts_in_group))

    # Сравниваем списки по содержимому
    if (checkUI):
        assert app.contacts.get_contacts_list().sort() == orm.database.get_contacts_list().sort()

@allure.feature('Проверки нахождения контакта в группе - сравнение с БД')
@allure.story('Исключение контакта из группы')
def test_TestRemoveContactFromGroup(app, orm, checkUI):
    if not app.group.is_group_exist(group.name):
        # группы нет - надо создать
        app.group.add_new_contacts_group(group)
    app.session.to_homepage()

      # Bыбираем контакт
    index = app.contacts.get_contact_index_by_address(contact.address)
    if  -1 == index:
        # Контакта нет - создадим
        app.contacts.addContact(contact)
        app.session.to_homepage()

    # Ищем контакт
    group.id = app.group.get_contacts_group_id_by_name(group)

    # Исключаем контакт из группы
    app.session.to_homepage()
    contact.group = None
    app.contacts.remove_contact_from_group(group, contact)
    contacts = orm.get_contacts_not_in_groups(group)

    assert (contact in list(contacts))

    # Сравниваем списки по содержимому
    if checkUI:
        app.session.to_homepage()
        app.contacts.show_all_contacts()
        assert app.contacts.get_contacts_list().sort() == orm.get_contacts_list().sort()