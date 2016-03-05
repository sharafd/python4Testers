# -*- coding: utf-8 -*-

from func import commonFunctions
from model import Group

common = commonFunctions.Common()

# Параметры групп контактов

constant_group_data = [Group(name="New_06661", header="664464664", footer= None)]

groups_testdata = [Group(name="", header=None, footer=None)] + [
    Group(name=common.random_ascii_string(), header=common.random_digits(),
          footer=common.random_string())
    for i in range(5)
    ]

testdata   = [
    Group(name="New_06661", header="664464664", footer= None),
    Group(name="New_", header=None, footer= None)
    ]