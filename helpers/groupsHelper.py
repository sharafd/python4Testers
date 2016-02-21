# -*- coding: utf-8 -*-

# Класс для работы с группами контактов
from model import Groups

class GroupsHelper:

    def __init__(self, app):
        self.app = app

    group_cache = None

    def type_value(self, field_name, text):
        if text is not None:
            self.app.wd.find_element_by_name(field_name).click()
            self.app.wd.find_element_by_name(field_name).clear()
            self.app.wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_params(self, groups):
        self.type_value("group_name", groups.name)
        self.type_value("group_header", groups.header)
        self.type_value("group_footer", groups.footer)

    def open_groups_page(self):
        if not (self.app.wd.current_url.endswith("/group.php") and len(self.app.wd.find_elements_by_name("new")) > 0):
            self.app.wd.find_element_by_link_text("groups").click()

    def select_group_by_index(self, index):
        self.app.wd.find_elements_by_name("selected[]")[index].click()

    # Создание новой группы контактов
    def add_new_contacts_group(self, groups):
        self.open_groups_page()
        self.app.wd.find_element_by_name("new").click()
        self.fill_group_params(groups)
        self.app.wd.find_element_by_name("submit").click()
        self.group_cache = None

    # Удаление группы контактов в списке по номеру в списке сверху вниз
    def delete_contacts_group_by_position(self, index):
        self.open_groups_page()
        self.select_group_by_index(index)
        self.app.wd.find_element_by_name("delete").click()
        self.group_cache = None

    # Удаление первой сверху группы контактов в списке
    def delete_first_contacts_group(self):
        self.delete_contacts_group_by_position(0)

    # Удаление группы контактов по имени
    def delete_contacts_group_by_name(self, name):
        self.open_groups_page()
        gid = self.app.wd.find_element_by_xpath("//input[contains(@title, 'Select " +  "(%s)" % name + "')]").get_attribute("value")
        self.app.wd.find_element_by_xpath("//input[contains(@title, 'Select " +  "(%s)" % name + "')]").click()
        self.app.wd.find_element_by_name("delete").click()
        self.group_cache = None
        return gid

    # Редактирование группы контактов по имеии
    def edit_contacts_group_by_name(self, name, groups):
        self.open_groups_page()
        gid = self.app.wd.find_element_by_xpath("//input[contains(@title, 'Select " +  "(%s)" % name + "')]").get_attribute("value")
        self.app.wd.find_element_by_xpath("//input[contains(@title, 'Select " +  "(%s)" % name + "')]").click()
        self.app.wd.find_element_by_name("edit").click()
        self.fill_group_params(groups)
        self.app.wd.find_element_by_name("update").click()
        self.group_cache = None
        return gid

    # Редактирование  группы контактов в списке по номеру в списке сверху вниз
    def edit_contacts_group_by_position(self, index, groups):
        self.open_groups_page()
        gid = self.select_group_by_index(index)
        self.app.wd.find_element_by_name("edit").click()
        self.fill_group_params(groups)
        self.app.wd.find_element_by_name("update").click()
        self.group_cache = None
        return gid

    # Редактирование первой сверху группы контактов
    def edit_first_contacts_group(self, groups):
        self.edit_contacts_group_by_position(0, groups)

    # Проверка существования группы
    def is_group_exist(self, name=None):
        self.open_groups_page()
        if name is None:
            #  Есть ли группы вообще
            if self.app.wd.find_elements_by_name("selected[]"):
                return True
            else:
                return False
        # Ищем группу по имени
        else:
            if  self.app.wd.find_elements_by_xpath("//input[contains(@title, 'Select " +  "(%s)" % name + "')]"):
                return True
            else:
                return False

    # Cписок групп
    def get_groups_list(self):
        if self.group_cache is None:
          self.group_cache = []
          self.open_groups_page()
          for element in self.app.wd.find_elements_by_name("selected[]"):
              text = element.get_attribute("title")
              id = element.get_attribute("value")
              self.group_cache.append(Groups(id = id, name = text))
        return list(self.group_cache)

    # Подсчёт кoличества групп
    def count(self):
        self.open_groups_page()
        return len(self.app.wd.find_elements_by_name("selected[]"))
