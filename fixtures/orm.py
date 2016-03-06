# -*- coding: utf-8 -*-

from pony.orm import *
from datetime import datetime

from pymysql.converters import decoders

from model import Group
from model import Contact

class ORMFixture:

    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='id')
        deprecated = Optional(str, column='deprecated')
        firstname = Optional(datetime, column='firstname')
        lastname = Optional(str, column='lastname')


    def __init__(self, host, database, user, password):
        self.db.bind('mysql', host = host, database=database,
                                              user = user, password = password, conv = decoders)
        self.db.generate_mapping()
    #    sql_debug(True)

    def orm2modelGroup(selfself, groups):
        def convert(group):
            return Group(id = str(group.id), name = group.name,
                     header = group.header, footer = group.footer)
        return list(map(convert, groups))

    def orm2modelContact(selfself, contacts):
        def convert(contact):
            return Contact(id = str(contact.id), firstname = contact.firstname,
                   lastname = contact.lastname )
        return list(map(convert, contacts))

    def get_group_list(self):
        with db_session:
            return self.orm2modelGroup(select(g for g in ORMFixture.ORMGroup))

    def get_contact_list(self):
        with db_session:
            return self.orm2modelContact(select(g for g in ORMFixture.ORMContact if c.deprecated is None))
