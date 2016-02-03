# -*- coding: utf-8 -*-

# Модель группы контактов

class Groups:

    def __init__(self, name, header, footer):

        if name == None:
            name = ""
        if header == None:
           header = ""
        if footer == None:
            footer = ""

        self.name = name
        self.header = header
        self.footer = footer

