# -*- coding: utf-8 -*-

from func import commonFunctions
from model import Groups

common = commonFunctions.Common()

# Параметры групп контактов

constant_group_data = [ Groups(name="New_06661", header="664464664", footer= None) ]

groups_testdata = [Groups(name="", header=None, footer=None)]+[
        Groups(name=common.random_ascii_string(), header=common.random_digits(),
                       footer=common.random_string())
        for i in range(5)
    ]

