# -*- coding: utf-8 -*-

# Проверки контактов

import time, os, pytest

from fixtures import Application
from model import *

@pytest.fixture()
def app(request):
    fixture = Application()
   # request.addfinalizer(fixture.destroy())
    return fixture

# Добавление нового контакта без привязки к группе
def test_TestAddContact(app):

    # Страница авторизации
    login = LoginPage(login = "admin", password = "secret")
    root_dir = os.path.abspath(os.path.dirname(__file__))

    app.session.open_login_page()
    app.session.login(login)


    Contacts.addContact(Contacts(wd=app.wd, address="Qwerty", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                             title="Contact", company="MyCompany", home="Str, 7790", mobile="+700", work="SOHO", fax="545454554",
                             email2="employee@company.org", email3="boss@foo.org", homepage="www.my.org", address2="Samara",
                             photo= root_dir + "/resources/avatar.png", phone2="+999", notes="++++++++++", bday="4", aday="14",
                             amonth= "July", bmonth= "May", group=""))
    time.sleep(3)
    app.wd.find_element_by_link_text("home").click()
    time.sleep(3)
    app.session.logout()
    app.destroy()

# Добавление нового контакта в группу New_01
def test_TestAddContactToGroup(app):

    # Страница авторизации
    login = LoginPage(login = "admin", password = "secret")

    app.session.open_login_page()
    app.session.login(login)

    Contacts.addContact(Contacts(wd=app.wd, address="Qwerty", middlename="foo", lastname="Bar", nickname="boo", byear="1988", ayear="2000",
                             title="Contact", company="MyCompany", home="Str, 7790", mobile="+700", work="", fax="", email2="", email3="fff@bar.ru",
                             homepage="www.my.org", address2="964646466", phone2="146546546", notes="++++++++++", bday="4", aday="6" , amonth= "July",
                             bmonth= "", photo= "", group="New_01"))

    app.wd.find_element_by_link_text("home").click()
    app.session.logout()
    app.destroy()



