# -*- coding: utf-8 -*-

# Класс для работы с группами контактов

class GroupsHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        self.app.wd.find_element_by_link_text("groups").click()

    # Создание новой группы контактов
    def add_new_contacts_group(self, groups):

        if groups.name == None:
            groups.name = ""

        if groups.header == None:
            groups.header = ""

        if groups.footer == None:
            groups.footer = ""

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

    # Удаление первой сверху группы контакоов в списке
    def delete_first_contacts_group(self):

        self.open_groups_page()

        self.app.wd.find_element_by_name("selected[]").click()
        self.app.wd.find_element_by_name("delete").click()

    # Удаление группы контактов по имени
    def delete_contacts_group_by_name(self, name):

        self.open_groups_page()

        self.app.wd.find_element_by_xpath("//input[contains(@title, 'Select (" + name + ")')]").click()
        self.app.wd.find_element_by_name("delete").click()

    # Редактирование группы контактов
    def edit_contacts_group_by_name(self, name, groups):

        if groups.name == None:
            groups.name = ""

        if groups.header == None:
            groups.header = ""

        if groups.footer == None:
            groups.footer = ""

        self.open_groups_page()

        self.app.wd.find_element_by_xpath("//input[contains(@title, 'Select (" + name + ")')]").click()
        self.app.wd.find_element_by_name("edit").click()
        self.app.wd.find_element_by_name("group_name").click()
        self.app.wd.find_element_by_name("group_name").clear()
        self.app.wd.find_element_by_name("group_name").send_keys(groups.name)
        self.app.wd.find_element_by_name("group_header").click()
        self.app.wd.find_element_by_name("group_header").clear()
        self.app.wd.find_element_by_name("group_header").send_keys(groups.header)
        self.app.wd.find_element_by_name("group_footer").click()
        self.app.wd.find_element_by_name("group_footer").clear()
        self.app.wd.find_element_by_name("group_footer").send_keys(groups.footer)
        self.app.wd.find_element_by_name("update").click()