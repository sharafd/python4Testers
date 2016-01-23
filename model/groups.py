# -*- coding: utf-8 -*-
# Класс для работы с группами контактов

class Groups:

    def __init__(self, wd, name, header, footer):
        self.wd = wd
        self.name = name
        self.header = header
        self.footer = footer

    # Создание новой группы контактов
    def add_new_contacts_group(Groups):
        Groups.wd.find_element_by_link_text("groups").click()
        Groups.wd.find_element_by_name("new").click()
        Groups.wd.find_element_by_name("group_name").click()
        Groups.wd.find_element_by_name("group_name").clear()
        Groups.wd.find_element_by_name("group_name").send_keys(Groups.name)
        Groups.wd.find_element_by_name("group_header").click()
        Groups.wd.find_element_by_name("group_header").clear()
        Groups.wd.find_element_by_name("group_header").send_keys(Groups.header)
        Groups.wd.find_element_by_name("group_footer").click()
        Groups.wd.find_element_by_name("group_footer").clear()
        Groups.wd.find_element_by_name("group_footer").send_keys(Groups.footer)
        Groups.wd.find_element_by_name("submit").click()