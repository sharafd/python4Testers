# -*- coding: utf-8 -*-
# Параметры групп контактов - генератор

import json, os, sys, getopt

from func import commonFunctions
from model import Groups

n = 5
f = "../data/groups.json"

common = commonFunctions.Common()

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number_of_groups", "file"])
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

testdata = [Groups(name=common.random_ascii_string(), header=common.random_digits(),
                       footer=common.random_string())
        for i in range(n)]

filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), f)

with open(filename, "write") as f:
    f.write(json.dumps(testdata,default=lambda x: x.__dict__, indent = 2))