# -*- coding: utf-8 -*-

# Класс для работы с контактами

class Contacts:
    
    def __init__(self, address, middlename, lastname, nickname, byear, ayear, photo, title, company, home, mobile,
                 work, fax, email2, email3, homepage, address2, phone2, notes, bday, bmonth, aday, amonth, group):
        self.address = address
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
