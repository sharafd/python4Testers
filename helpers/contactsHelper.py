# -*- coding: utf-8 -*-

# Класс для работы с контактами

class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def fill_contact_params(self, contacts):
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
        if contacts.home is not None:
            self.app.wd.find_element_by_name("home").click()
            self.app.wd.find_element_by_name("home").clear()
            self.app.wd.find_element_by_name("home").send_keys(contacts.home)
        if contacts.mobile is not None:
            self.app.wd.find_element_by_name("mobile").click()
            self.app.wd.find_element_by_name("mobile").clear()
            self.app.wd.find_element_by_name("mobile").send_keys(contacts.mobile)
        if contacts.work is not None:
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
        if contacts.phone2 is not None:
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
        if contacts.address is not None:
            self.app.wd.find_element_by_name("address").click()
            self.app.wd.find_element_by_name("address").clear()
            self.app.wd.find_element_by_name("address").send_keys(contacts.address)
        self.app.wd.find_element_by_xpath("//input[@type='submit' and @name='quickadd' and @value='Next']").click()
        self.fill_contact_params(contacts)

        self.app.wd.find_element_by_xpath("//input[@type='submit' and @name='submit' and @value='Enter']").click()

    # Удаление первого сверху контакта в списке
    def delete_first_contact(self):
        self.app.wd.find_element_by_link_text("home").click()
        self.app.wd.find_element_by_name("selected[]").click()
        self.app.wd.find_element_by_xpath("//input[@type='button' and @value='Delete']").click()
        self.app.wd.switch_to_alert().accept()

    # Редактирование первого сверху контакта в списке
    def editFirstContact(self, contacts):
        self.app.wd.find_element_by_link_text("home").click()
        self.app.wd.find_element_by_name("selected[]").click()
        self.app.wd.find_element_by_xpath("//img[@title ='Edit']").click()

        if contacts.address is not None:
            self.app.wd.find_element_by_name("address").click()
            self.app.wd.find_element_by_name("address").clear()
            self.app.wd.find_element_by_name("address").send_keys(contacts.address)
        self.fill_contact_params(contacts)

        self.app.wd.find_element_by_xpath("//input[@type='submit' and @value='Update']").click()

    # Удаление фото у первого сверху контакта в списке
    def deleteFirstContactPhoto(self):
        self.app.wd.find_element_by_link_text("home").click()
        self.app.wd.find_element_by_name("selected[]").click()
        self.app.wd.find_element_by_xpath("//img[@title ='Edit']").click()
        self.app.wd.find_element_by_xpath("//input[@name='delete_photo']").click()
        self.app.wd.find_element_by_xpath("//input[@type='submit' and @value='Update']").click()

    # Редактирование первого сверху контакта в списке со страницы просмотра
    def modifyFirstContact(self, contacts):
        self.app.wd.find_element_by_link_text("home").click()
        self.app.wd.find_element_by_name("selected[]").click()
        self.app.wd.find_element_by_xpath("//img[@title ='Details']").click()
        self.app.wd.find_element_by_xpath("//input[@type='submit' and @value='Modify']").click()

        if contacts.address is not None:
            self.app.wd.find_element_by_name("address").click()
            self.app.wd.find_element_by_name("address").clear()
            self.app.wd.find_element_by_name("address").send_keys(contacts.address)
        self.fill_contact_params(contacts)

        self.app.wd.find_element_by_xpath("//input[@type='submit' and @value='Update']").click()

    # Проверка существования контактоа в принципе
    def is_contact_exist(self):
          self.app.wd.find_element_by_link_text("home").click()
          if self.app.wd.find_element_by_name("selected[]"):
             return True
          else:
             return False