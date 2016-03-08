# -*- coding: utf-8 -*-

# Добавление нового контакта в группу New_01
from model import Contact, Group


def test_TestAddContactToGroup(app, db, checkUI):
    if not app.group.is_group_exist(name = "Group_for_ORM"):
        # группы нет - надо создать
        app.group.add_new_contacts_group(Group(name="Group_for_ORM"))
    app.session.to_homepage()
    old_contacts = db.database.get_contacts_list()
    app.contacts.addContact(Contact(address="Qwerty", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000", email ="mymail@hosting.com",
                                    title="Contact", company="MyCompany", home="S779", mobile="+76-6", work="56641646", fax="", email2="", email3="fff@bar.ru",
                                    homepage="www.my.org", address2="964646466", phone2="146546546", notes="++++++++++", bday="4", aday="6", amonth= "July",
                                    bmonth= "", photo= "", group="Group_for_ORM"))
    app.session.to_homepage()
    gid = app.group.get_contacts_group_id_by_name(Group(name="Group_for_ORM"))
    # Сравниваем размер списков
    if (checkUI):
        assert len(old_contacts) + 1 == app.contacts.count()
    #  Получаем новый список контактов
    new_contacts = db.database.get_contacts_list()
    # Сравниваем списки по содержимому
    assert old_contacts.sort() == new_contacts.sort()
    if (checkUI):
        assert app.group.get_groups_list().sort() == new_contacts.sort()

    