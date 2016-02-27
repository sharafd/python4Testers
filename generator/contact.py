# -*- coding: utf-8 -*-
# Параметры контактов - генератор

import json, os, sys, getopt

import jsonpickle
from func import commonFunctions
from model import Contacts

n = 2
f = "../data/contacts.json"

common = commonFunctions.Common()
# ключи командной строки
try:
    opts, args = getopt.getopt(sys.argv[1:], "cn:cf", ["number_of_contacts", "file"])
except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        getopt.usage()
        sys.exit(2)

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

# тестовые данные
testdata = [Contacts(address=common.random_string(10), middlename=common.random_ascii_string(10), lastname=common.random_ascii_string(10), firstname = "FOO",
                                     nickname=common.random_ascii_string(10), byear="1988", ayear="2000",email = "mymail@hosting.com",
                             title=common.random_string(10), company=common.random_string(10), home=common.random_digits(5), mobile="+7", work=common.random_digits(5), fax=common.random_digits(11),
                             email2="employee@company.org", email3="boss@foo.org", homepage="www.my.org", address2="Samara",
                             photo= os.path.join(os.path.abspath(os.path.dirname(__file__)), "../resources/avatar.png"), phone2=common.random_digits(5), notes="++++++++++", bday="4", aday="14",
                             amonth= "July", bmonth= "May", group=None)
    for i in range(n)
]

filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), f)
# форматируем JSON
jsonpickle.set_encoder_options('json', sort_keys=True, indent=2)
# сохраняем тестовые данные как JSON
with open(filename, "write") as f:
    f.write(jsonpickle.encode(testdata))