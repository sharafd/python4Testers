# -*- coding: utf-8 -*-

# Контакты
from sys import maxsize

class Contacts:
    
    def __init__(self, id = None, address=None, firstname = None, middlename=None, lastname=None, nickname=None, byear=None, ayear=None, photo=None, title=None, company=None,
                 home=None, mobile=None, work=None, fax=None, email2=None, email3=None, homepage=None, address2=None, phone2=None, notes=None, bday=None, bmonth=None,
                 aday=None, amonth=None, group=None, all_phones_from_home_page = None, email = None):
        self.id = id
        self.address = address
        self.firstname= firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.bday = bday
        self.bmonth = bmonth
        self.byear= byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.photo = photo
        self.title = title
        self.company = company
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.group= group
        self.email = email
        self.all_phones_from_home_page =  all_phones_from_home_page

    def __repr__(self):
        return "%s" % (self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.address == other.address or self.address is None or other.address is None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize