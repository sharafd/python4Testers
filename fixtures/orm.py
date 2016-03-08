# -*- coding: utf-8 -*-

#  ORM модель

from pony.orm import *
from datetime import datetime

from pymysql.converters import decoders

from model import Group
from model import Contact

class ORMFixture:

    db = Database()

    def __init__(self, host, database, user, password):
        self.db.bind('mysql', host = host, database=database,
                                              user = user, password = password, conv = decoders)
        self.db.generate_mapping()
        sql_debug(True)

    # Объект Группы
    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact,table='address_in_groups',
                       column='id', reverse='groups', lazy=True)

    # Объект Kонтакты
    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        deprecated = Optional(str, column='deprecated')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        middlename = Optional(str, column='middlename')
        nickname = Optional(str, column='nickname')
        bday = Optional(str, column='bday')
        bmonth = Optional(str, column='bmonth')
        byear = Optional(str, column='byear')
        aday = Optional(str, column='aday')
        amonth = Optional(str, column='amonth')
        ayear = Optional(str, column='ayear')
        photo = Optional(str, column='photo')
        title = Optional(str, column='title')
        company = Optional(str, column='company')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        fax = Optional(str, column='fax')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        homepage = Optional(str, column='homepage')
        address2 = Optional(str, column='address2')
        phone2 = Optional(str, column='phone2')
        notes = Optional(str, column='notes')
        email  = Optional(str, column='email')
        groups = Set(lambda: ORMFixture.ORMGroup,table='address_in_groups',
                     column='group_id', reverse='contacts', lazy=True)



    # Преобразование к модели группы
    def orm2modelGroup(self, group):
        def convert(group):
            return Group(id = str(group.id), name = group.name,
                     header = group.header, footer = group.footer)
        return list(map(convert, group))

    # Преобразование к модели контакта
    def orm2modelContact(self, contact):
        def convert(contact):
         return Contact(id = str(contact.id),
              firstname = contact.firstname,
              lastname = contact.lastname,
              nickname = contact.nickname,
              bday = contact.bday,
              bmonth = contact.bmonth,
              byear= contact.byear,
              aday = contact.aday,
              amonth = contact.amonth,
              ayear = contact.ayear,
              photo = contact.photo,
              title = contact.title,
              company = contact.company,
              home = contact.home,
              mobile = contact.mobile,
              work = contact.work,
              fax = contact.fax,
              email2 = contact.email2,
              email3 = contact.email3,
              homepage = contact.homepage,
              address2 = contact.address2,
              phone2 = contact.phone2,
              notes = contact.notes,
              group= contact.groups,
              email = contact.email)
        return list(map(convert, contact))

    # Список групп
    @db_session
    def get_groups_list(self):
        return self.orm2modelGroup(select(g for g in ORMFixture.ORMGroup))

    # Список контактов
    @db_session
    def get_contacts_list(self):
        return self.orm2modelContact(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    # Принадлежит ли контакт группе
    @db_session
    def get_contacts_in_groups(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return  self.orm2modelContact(orm_group.contacts)

    @db_session
    def get_contacts_not_in_groups(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id  == group.id))[0]
        return self.orm2modelContact(select(c for c in ORMFixture.ORMContact if c.deprecated is None
                                            and orm_group not in c.groups))

