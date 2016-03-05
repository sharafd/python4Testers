# -*- coding: utf-8 -*-

# Модель группы контактов
from sys import maxsize

class Group:

    def __init__(self, id=None, name=None, header=None, footer= None):
        self.id = id
        self.name = name
        self.header = header
        self.footer = footer

    def __repr__(self):
        return "%s;%s;%s;%s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.name == other.name or self.name is None or other.name is None)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize