# -*- coding: utf-8 -*-

# Класс для работы с контактами
import re

from model import Contact
from func import commonFunctions

common = commonFunctions.Common()

class ContactsHelper:

    def __init__(self, app):
        self.app = app

    contacts_cache = None

    # Выбор контакта по индексу сверхy вниз
    def select_contact_by_index(self, index):
        self.app.wd.find_elements_by_name("selected[]")[index].click()

    # Выбор контакта по индексу сверхy вниз для редактирования
    def select_contact_for_edit_by_index(self, index):
        row = self.app.wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    # Выбор контакта по индексу сверхy вниз для просмотра
    def select_contact_for_view_by_index(self, index):
        row = self.app.wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    # Заполнение формы редактирования
    def fill_contact_params(self, contacts):
        if contacts.firstname is not None:
            self.app.wd.find_element_by_name("firstname").click()
            self.app.wd.find_element_by_name("firstname").clear()
            self.app.wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        if contacts.middlename is not None:
            self.app.wd.find_element_by_name("middlename").click()
            self.app.wd.find_element_by_name("middlename").clear()
            self.app.wd.find_element_by_name("middlename").send_keys(contacts.middlename)
        if contacts.lastname is not None:
            self.app.wd.find_element_by_name("lastname").click()
            self.app.wd.find_element_by_name("lastname").clear()
            self.app.wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        if contacts.nickname is not None:
            self.app.wd.find_element_by_name("nickname").click()
            self.app.wd.find_element_by_name("nickname").clear()
            self.app.wd.find_element_by_name("nickname").send_keys(contacts.nickname)
        if contacts.bday != "" and contacts.bday is not None:
            if not self.app.wd.find_element_by_xpath(
                                    "//select[@name='bday']//option[text()='" + contacts.bday + "']").is_selected():
                self.app.wd.find_element_by_xpath(
                    "//select[@name='bday']//option[text()='" + contacts.bday + "']").click()
        if contacts.bmonth != "" and contacts.bmonth is not None:
            if not self.app.wd.find_element_by_xpath(
                                    "//select[@name='bmonth']//option[@value='" + contacts.bmonth + "']").is_selected():
                self.app.wd.find_element_by_xpath(
                    "//select[@name='bmonth']//option[@value='" + contacts.bmonth + "']").click()
        if contacts.byear is not None:
            self.app.wd.find_element_by_name("byear").click()
            self.app.wd.find_element_by_name("byear").clear()
            self.app.wd.find_element_by_name("byear").send_keys(contacts.byear)
        if contacts.aday != "" and contacts.aday is not None:
            if not self.app.wd.find_element_by_xpath(
                                    "//select[@name='aday']//option[text()='" + contacts.aday + "']").is_selected():
                self.app.wd.find_element_by_xpath(
                    "//select[@name='aday']//option[text()='" + contacts.aday + "']").click()
        if contacts.amonth != "" and contacts.amonth is not None:
            if not self.app.wd.find_element_by_xpath(
                                    "//select[@name='amonth']//option[@value='" + contacts.amonth + "']").is_selected():
                self.app.wd.find_element_by_xpath(
                    "//select[@name='amonth']//option[@value='" + contacts.amonth + "']").click()
        if contacts.ayear is not None:
            self.app.wd.find_element_by_name("ayear").click()
            self.app.wd.find_element_by_name("ayear").clear()
            self.app.wd.find_element_by_name("ayear").send_keys(contacts.ayear)
        if contacts.photo != "" and contacts.photo is not None:
            self.app.wd.find_element_by_xpath("//input[@type='file' and @name='photo']").send_keys(contacts.photo)
        if contacts.title is not None:
            self.app.wd.find_element_by_name("title").click()
            self.app.wd.find_element_by_name("title").clear()
            self.app.wd.find_element_by_name("title").send_keys(contacts.title)
        if contacts.company is not None:
            self.app.wd.find_element_by_name("company").click()
            self.app.wd.find_element_by_name("company").clear()
            self.app.wd.find_element_by_name("company").send_keys(contacts.company)
        if contacts.address is not None:
            self.app.wd.find_element_by_name("address").click()
            self.app.wd.find_element_by_name("address").clear()
            self.app.wd.find_element_by_name("address").send_keys(contacts.address)
        if contacts.home != "" and  contacts.home is not None:
            self.app.wd.find_element_by_name("home").click()
            self.app.wd.find_element_by_name("home").clear()
            self.app.wd.find_element_by_name("home").send_keys(contacts.home)
        if contacts.email != "" and  contacts.email is not None:
            self.app.wd.find_element_by_name("email").click()
            self.app.wd.find_element_by_name("email").clear()
            self.app.wd.find_element_by_name("email").send_keys(contacts.email)
        if contacts.mobile != "" and contacts.mobile is not None:
            self.app.wd.find_element_by_name("mobile").click()
            self.app.wd.find_element_by_name("mobile").clear()
            self.app.wd.find_element_by_name("mobile").send_keys(contacts.mobile)
        if contacts.work != "" and contacts.work is not None:
            self.app.wd.find_element_by_name("work").click()
            self.app.wd.find_element_by_name("work").clear()
            self.app.wd.find_element_by_name("work").send_keys(contacts.work)
        if contacts.fax is not None:
            self.app.wd.find_element_by_name("fax").click()
            self.app.wd.find_element_by_name("fax").clear()
            self.app.wd.find_element_by_name("fax").send_keys(contacts.fax)
        if contacts.email2 is not None:
            self.app.wd.find_element_by_name("email2").click()
            self.app.wd.find_element_by_name("email2").clear()
            self.app.wd.find_element_by_name("email2").send_keys(contacts.email2)
        if contacts.email3 is not None:
            self.app.wd.find_element_by_name("email3").click()
            self.app.wd.find_element_by_name("email3").clear()
            self.app.wd.find_element_by_name("email3").send_keys(contacts.email3)
        if contacts.homepage is not None:
            self.app.wd.find_element_by_name("homepage").click()
            self.app.wd.find_element_by_name("homepage").clear()
            self.app.wd.find_element_by_name("homepage").send_keys(contacts.homepage)
        if contacts.address2 is not None:
            self.app.wd.find_element_by_name("address2").click()
            self.app.wd.find_element_by_name("address2").clear()
            self.app.wd.find_element_by_name("address2").send_keys(contacts.address2)
        if contacts.phone2 != "" and contacts.phone2 is not None:
            self.app.wd.find_element_by_name("phone2").click()
            self.app.wd.find_element_by_name("phone2").clear()
            self.app.wd.find_element_by_name("phone2").send_keys(contacts.phone2)
        if contacts.notes is not None:
            self.app.wd.find_element_by_name("notes").click()
            self.app.wd.find_element_by_name("notes").clear()
            self.app.wd.find_element_by_name("notes").send_keys(contacts.notes)
        if contacts.group != "" and contacts.group is not None:
            if not self.app.wd.find_element_by_xpath(
                                    "//select[@name='new_group']//option[text() = '" + contacts.group + "']").is_selected():
                self.app.wd.find_element_by_xpath(
                    "//select[@name='new_group']//option[text() ='" + contacts.group + "']").click()

    # Добавление контакта в адресную книгу
    def addContact(self, contacts):
        self.app.wd.find_element_by_link_text("add new").click()
     #   if contacts.address is not None:
     #       self.app.wd.find_element_by_name("address").click()
     #       self.app.wd.find_element_by_name("address").clear()
     #       self.app.wd.find_element_by_name("address").send_keys(contacts.address)
     #   self.app.wd.find_element_by_xpath("//input[@type='submit' and @name='quickadd' and @value='Next']").click()
        self.fill_contact_params(contacts)
        self.app.wd.find_element_by_xpath("//input[@type='submit' and @name='submit' and @value='Enter']").click()
        self.contacts_cache = None

    # Удаление контактa по номеру в списке сверху вниз
    def delete_contact_by_index(self, index):
        self.select_contact_by_index(index)
        self.app.wd.find_element_by_xpath("//input[@type='button' and @value='Delete']").click()
        self.app.wd.switch_to_alert().accept()
        self.contacts_cache = None

    # Удаление первого сверху контакта в списке
    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    # Редактирование контактa по номеру в списке сверху вниз
    def edit_contact_by_index(self, index, contacts):
      #  self.select_contact_by_index(index)
      #  self.app.wd.find_element_by_xpath("//img[@title ='Edit']").click()
        self.select_contact_for_edit_by_index(index)
        if contacts.address is not None:
            self.app.wd.find_element_by_name("address").click()
            self.app.wd.find_element_by_name("address").clear()
            self.app.wd.find_element_by_name("address").send_keys(contacts.address)
        self.fill_contact_params(contacts)
        self.app.wd.find_element_by_xpath("//input[@type='submit' and @value='Update']").click()
        self.contacts_cache = None

    # Редактирование первого сверху контакта в списке
    def edit_first_contact(self, contacts):
        self.edit_contact_by_index(0, contacts)

    # Удаление фото у первого сверху контакта в списке
    def delete_first_contact_photo(self):
        self.app.wd.find_element_by_name("selected[]").click()
        self.app.wd.find_element_by_xpath("//img[@title ='Edit']").click()
        self.app.wd.find_element_by_xpath("//input[@name='delete_photo']").click()
        self.app.wd.find_element_by_xpath("//input[@type='submit' and @value='Update']").click()

    # Редактирование первого сверху контакта в списке со страницы просмотра
    def modify_first_contact(self, contacts):
        self.app.wd.find_element_by_name("selected[]").click()
        self.app.wd.find_element_by_xpath("//img[@title ='Details']").click()
        self.app.wd.find_element_by_xpath("//input[@type='submit' and @value='Modify']").click()
        if contacts.address is not None:
            self.app.wd.find_element_by_name("address").click()
            self.app.wd.find_element_by_name("address").clear()
            self.app.wd.find_element_by_name("address").send_keys(contacts.address)
        self.fill_contact_params(contacts)
        self.app.wd.find_element_by_xpath("//input[@type='submit' and @value='Update']").click()
        self.contacts_cache = None

    # Проверка существования контактов в принципе
    def is_contact_exist(self):
          if self.app.wd.find_elements_by_name("selected[]"):
             return True
          else:
             return False

    #Список контактов
    def get_contacts_list(self):
        if self.contacts_cache is None:
            self.contacts_cache  = []
            for element in self.app.wd.find_elements_by_xpath("//tr[@name='entry']"):
             #   value = element.find_element_by_xpath("//input[@type='checkbox']").get_attribute("value")
             #   address  =  element.find_element_by_xpath("//td[4]").text
                cells = element.find_elements_by_tag_name("td")
                value = cells[0].find_element_by_tag_name("input").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                allmails = cells[4].text.splitlines()
                allphones = cells[5].text.splitlines()
                try:
                  home = allphones[0]
                except IndexError:
                    home = ""
                try:
                  mobile = allphones[1]
                except IndexError:
                    mobile = ""
                try:
                  work = allphones[2]
                except IndexError:
                    work = ""
                try:
                  phone2 = allphones[3]
                except IndexError:
                    phone2  = ""
                try:
                  email = allmails[0]
                except IndexError:
                    email = ""
                try:
                  email2 = allmails[1]
                except IndexError:
                    email2 = ""
                try:
                  email3 = allmails[2]
                except IndexError:
                    email3 = ""
                self.contacts_cache.append(Contact(id = value, firstname = firstname, lastname = lastname, address = address,
                                                   home = home, mobile = mobile, work = work, phone2 = phone2,
                                                   email = email, email2 = email2, email3 = email3))
        return list(self.contacts_cache)

    #Список контактов (склейка)
    def get_contacts_list_merged(self):
        if self.contacts_cache is None:
            self.contacts_cache  = []
            for element in self.app.wd.find_elements_by_xpath("//tr[@name='entry']"):
                cells = element.find_elements_by_tag_name("td")
                value = cells[0].find_element_by_tag_name("input").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                allmails = cells[4].text
                allphones = cells[5].text
                self.contacts_cache.append(Contact(id = value, address = address, firstname = firstname, lastname = lastname,
                                                   all_phones_from_home_page = allphones, all_emails_from_home_page = allmails))
        return list(self.contacts_cache)

    # Подсчёт кoличества контактов
    def count(self):
       return len(self.app.wd.find_elements_by_xpath("//tr[@name='entry']"))

    # Получение данных контакта из диалога редактирования (нарезка)
    def get_contact_info_from_edit_page(self, index):
       self.select_contact_for_edit_by_index(index)

       id = self.app.wd.find_element_by_xpath("//input[@name='id']").get_attribute("value")
       firstname = self.app.wd.find_element_by_xpath("//input[@name='firstname']").get_attribute("value")
       lastname = self.app.wd.find_element_by_xpath("//input[@name='lastname']").get_attribute("value")
       middlename = self.app.wd.find_element_by_xpath("//input[@name='middlename']").get_attribute("value")
     # address = self.app.wd.find_element_by_xpath("//input[@name='address']").get_attribute("value")
       address = self.app.wd.find_element_by_xpath("//textarea[@name='address']").get_attribute("value")
       home = self.app.wd.find_element_by_xpath("//input[@name='home']").get_attribute("value")
       work = self.app.wd.find_element_by_xpath("//input[@name='work']").get_attribute("value")
       phone2 = self.app.wd.find_element_by_xpath("//input[@name='phone2']").get_attribute("value")
       mobile = self.app.wd.find_element_by_xpath("//input[@name='mobile']").get_attribute("value")
       email = self.app.wd.find_element_by_xpath("//input[@name='email']").get_attribute("value")
       email2 = self.app.wd.find_element_by_xpath("//input[@name='email2']").get_attribute("value")
       email3 = self.app.wd.find_element_by_xpath("//input[@name='email3']").get_attribute("value")

       return Contact(id = id, firstname = firstname, lastname = lastname, middlename = middlename, home = home, address = address,
                      mobile = mobile, work = work, phone2 = phone2, email = email, email2 = email2, email3 = email3)

    # Получение данных контакта из диалога редактирования (нарезка)
    def get_contact_info_from_view_page(self, index):
       self.select_contact_for_view_by_index(index)

       text = self.app.wd.find_element_by_xpath("//div[@id='content']").text
       home = re.search("H: (.*)", text).group(1)
       work = re.search("W: (.*)", text).group(1)
       mobile = re.search("M: (.*)", text).group(1)
       phone2 = re.search("P: (.*)", text).group(1)

       return Contact(home = home, mobile = mobile, work = work, phone2 = phone2)

    # Поиск контакта по адресу
    def get_contact_index_by_address(self, address):
       index = -1
       i = -1

       for element in self.app.wd.find_elements_by_xpath("//tr[@name='entry']"):
           i = i + 1
           cells = element.find_elements_by_tag_name("td")
           if address == cells[3].text:
               index = i
               break
       return int(index)

    # Вспомогательный метод для обратной проверки телефонов
    def merge_phones_like_on_home_page(self, contact):

       res = "\n".join(
               map(
                   lambda x: common.clear(x, "[() -]"),[contact.home, contact.mobile, contact.work, contact.phone2]))
       return filter(
               lambda x: x !="", filter(
                       lambda x: x is not None, res))

    # Вспомогательный метод для обратной проверки email
    def merge_emails_like_on_home_page(self, contact):

        res = "\n".join([contact.email, contact.email2, contact.email3])
        return filter(
                lambda x: x !="", filter(
                        lambda x: x is not None, res))

    # Принудительная очистка кеша
    def clear_cache(self):
        self.contacts_cache = None

    # Редактирование контактa по номеру в списке сверху вниз
    def remove_contact_from_group(self, group, contact):
        self.app.wd.find_element_by_xpath(
                                    "//select[@name='group']//option[text()='" + group.name + "']").click()
        index = self.get_contact_index_by_address(contact.address)
        self.select_contact_by_index(index)
        self.app.wd.find_element_by_xpath("//input[@type='submit' and @name= 'remove']").click()

    # показать все контакты
    def show_all_contacts(self):
        self.app.wd.find_element_by_xpath(
                                    "//select[@name='group']//option[text()='[all]']").click()