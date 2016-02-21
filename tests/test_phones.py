# -*- coding: utf-8 -*-

import os
from model import Contacts

root_dir = os.path.abspath(os.path.dirname(__file__))

def test_phones_on_homepage(app):

    app.session.to_homepage()
    if not app.contacts.is_contact_exist():
    # Контактов нет - создадим
        app.contacts.addContact(Contacts(address="Qwerty", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                             title="Contact", company="MyCompany", home="7790", mobile="+75-1", work="+951-705-96-11", fax="545454554",
                             email2="employee@company.org", email3="boss@foo.org", homepage="www.my.org", address2="Samara",
                             photo= root_dir + "/resources/avatar.png", phone2="+999(55)6<br/)>", notes="++++++++++", bday="4", aday="14",
                             amonth= "July", bmonth= "May", group=None))
        app.session.to_homepage()

    contacts_from_phone_app = app.contacts.get_contacts_list()[0]
    contacts_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)

    assert(contacts_from_phone_app.home == contacts_from_edit_page.home)
    assert(contacts_from_phone_app.mobile == contacts_from_edit_page.mobile)
    assert(contacts_from_phone_app.work == contacts_from_edit_page.work)


def test_phones_on_viewpage(app):

    app.session.to_homepage()
    if not app.contacts.is_contact_exist():
    # Контактов нет - создадим
        app.contacts.addContact(Contacts(address="Qwerty", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                             title="Contact", company="MyCompany", home="7790", mobile="+75-1", work="+951-705-96-11", fax="545454554",
                             email2="employee@company.org", email3="boss@foo.org", homepage="www.my.org", address2="Samara",
                             photo= root_dir + "/resources/avatar.png", phone2="+999(55)6<br/)>", notes="++++++++++", bday="4", aday="14",
                             amonth= "July", bmonth= "May", group=None))
        app.session.to_homepage()

    contacts_from_phone_app = app.contacts.get_contacts_list()[0]
    contacts_from_view_page = app.contacts.get_contact_info_from_view_page(0)

    assert(contacts_from_phone_app.home == contacts_from_view_page.home)
    assert(contacts_from_phone_app.mobile == contacts_from_view_page.mobile)
    assert(contacts_from_phone_app.work == contacts_from_view_page.work)
