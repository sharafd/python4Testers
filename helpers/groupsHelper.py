# -*- coding: utf-8 -*-

# Класс для работы с группами контактов

class GroupsHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        self.app.wd.find_element_by_link_text("groups").click()

    # Создание новой группы контактов
    def add_new_contacts_group(self, groups):

        self.open_groups_page()

        self.app.wd.find_element_by_name("new").click()
        self.app.wd.find_element_by_name("group_name").click()
        self.app.wd.find_element_by_name("group_name").clear()
        self.app.wd.find_element_by_name("group_name").send_keys(groups.name)
        self.app.wd.find_element_by_name("group_header").click()
        self.app.wd.find_element_by_name("group_header").clear()
        self.app.wd.find_element_by_name("group_header").send_keys(groups.header)
        self.app.wd.find_element_by_name("group_footer").click()
        self.app.wd.find_element_by_name("group_footer").clear()
        self.app.wd.find_element_by_name("group_footer").send_keys(groups.footer)
        self.app.wd.find_element_by_name("submit").click()
        
    def delete_first_contacts_group(self):

        self.open_groups_page()

        self.app.wd.find_element_by_name("selected[]").click()
        self.app.wd.find_element_by_name("delete").click()