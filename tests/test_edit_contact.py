# -*- coding: utf-8 -*-

# Проверки  контактов - редактирование

import os
from model import LoginPage, Contacts

# Параметры авторизации
login = LoginPage(login = "admin", password = "secret")

# Редактирование контакта
def test_TestEditContact(app):
    root_dir = os.path.abspath(os.path.dirname(__file__))

    app.session.ensure_login(login, "admin")

    app.contacts.editFirstContact(Contacts(address="Qwerty00", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                             title="Contact", company="", home="", mobile="", work="", fax="545454554",
                             email2="", email3="", homepage="", address2="Samara",
                             photo= root_dir + "/resources/avatar.png", phone2="+999", notes="++++++++++", bday="4", aday="14",
                             amonth= "July", bmonth= "May", group=""))

# Удаление фото контакта
def test_TestDelContactPhoto(app):
    app.session.ensure_login(login, "admin")
    app.contacts.deleteFirstContactPhoto()

# Редактирование контакта со страницы просмотра
def test_TestModifyContact(app):
    root_dir = os.path.abspath(os.path.dirname(__file__))

    app.session.ensure_login(login, "admin")
    app.contacts.modifyFirstContact(Contacts(address="Qwerty00", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                             title="Contact", fax="545454554", address2="Samara",  photo= root_dir + "/resources/avatar.png", phone2="+999", notes="++++++++++", bday="4", aday="14",
                             amonth= "July", bmonth= "May", group=""))