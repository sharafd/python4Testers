# -*- coding: utf-8 -*-

# Класс для работы с контактами

class ContactsHelper:

    def __init__(self, app):
        self.app = app

    # Добавление контакта в адресную книгу
    def addContact(self, contacts):
        self.app.wd.find_element_by_link_text("add new").click()
        self.app.wd.find_element_by_name("address").click()
        self.app.wd.find_element_by_name("address").clear()
        self.app.wd.find_element_by_name("address").send_keys(contacts.address)
        self.app.wd.find_element_by_xpath("//input[@type='submit' and @name='quickadd' and @value='Next']").click()
        self.app.wd.find_element_by_name("middlename").click()
        self.app.wd.find_element_by_name("middlename").clear()
        self.app.wd.find_element_by_name("middlename").send_keys(contacts.middlename)
        self.app.wd.find_element_by_name("lastname").click()
        self.app.wd.find_element_by_name("lastname").clear()
        self.app.wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        self.app.wd.find_element_by_name("nickname").click()
        self.app.wd.find_element_by_name("nickname").clear()
        self.app.wd.find_element_by_name("nickname").send_keys(contacts.nickname)

        if contacts.bday != "":
         if not self.app.wd.find_element_by_xpath("//select[@name='bday']//option[text()='" + contacts.bday + "']").is_selected():
           self.app.wd.find_element_by_xpath("//select[@name='bday']//option[text()='" + contacts.bday + "']").click()

        if contacts.bmonth != "":
         if not self.app.wd.find_element_by_xpath("//select[@name='bmonth']//option[@value='" + contacts.bmonth + "']").is_selected():
           self.app.wd.find_element_by_xpath("//select[@name='bmonth']//option[@value='" + contacts.bmonth + "']").click()

        self.app.wd.find_element_by_name("byear").click()
        self.app.wd.find_element_by_name("byear").clear()
        self.app.wd.find_element_by_name("byear").send_keys(contacts.byear)

        if contacts.aday != "":
         if not self.app.wd.find_element_by_xpath("//select[@name='aday']//option[text()='" + contacts.aday + "']").is_selected():
           self.app.wd.find_element_by_xpath("//select[@name='aday']//option[text()='" + contacts.aday + "']").click()

        if contacts.amonth != "":
         if not self.app.wd.find_element_by_xpath("//select[@name='amonth']//option[@value='" + contacts.amonth + "']").is_selected():
           self.app.wd.find_element_by_xpath("//select[@name='amonth']//option[@value='" + contacts.amonth + "']").click()

        self.app.wd.find_element_by_name("ayear").click()
        self.app.wd.find_element_by_name("ayear").clear()
        self.app.wd.find_element_by_name("ayear").send_keys(contacts.ayear)

        if contacts.photo != "":
          self.app.wd.find_element_by_xpath("//input[@type='file' and @name='photo']").send_keys(contacts.photo)

        self.app.wd.find_element_by_name("title").click()
        self.app.wd.find_element_by_name("title").clear()
        self.app.wd.find_element_by_name("title").send_keys(contacts.title)
        self.app.wd.find_element_by_name("company").click()
        self.app.wd.find_element_by_name("company").clear()
        self.app.wd.find_element_by_name("company").send_keys(contacts.company)
        self.app.wd.find_element_by_name("address").click()
        self.app.wd.find_element_by_name("address").clear()
        self.app.wd.find_element_by_name("address").send_keys(contacts.address)
        self.app.wd.find_element_by_name("home").click()
        self.app.wd.find_element_by_name("home").clear()
        self.app.wd.find_element_by_name("home").send_keys(contacts.home)
        self.app.wd.find_element_by_name("mobile").click()
        self.app.wd.find_element_by_name("mobile").clear()
        self.app.wd.find_element_by_name("mobile").send_keys(contacts.mobile)
        self.app.wd.find_element_by_name("work").click()
        self.app.wd.find_element_by_name("work").clear()
        self.app.wd.find_element_by_name("work").send_keys(contacts.work)
        self.app.wd.find_element_by_name("fax").click()
        self.app.wd.find_element_by_name("fax").clear()
        self.app.wd.find_element_by_name("fax").send_keys(contacts.fax)
        self.app.wd.find_element_by_name("email2").click()
        self.app.wd.find_element_by_name("email2").clear()
        self.app.wd.find_element_by_name("email2").send_keys(contacts.email2)
        self.app.wd.find_element_by_name("email3").click()
        self.app.wd.find_element_by_name("email3").clear()
        self.app.wd.find_element_by_name("email3").send_keys(contacts.email3)
        self.app.wd.find_element_by_name("homepage").click()
        self.app.wd.find_element_by_name("homepage").clear()
        self.app.wd.find_element_by_name("homepage").send_keys(contacts.homepage)
        self.app.wd.find_element_by_name("address2").click()
        self.app.wd.find_element_by_name("address2").clear()
        self.app.wd.find_element_by_name("address2").send_keys(contacts.address2)
        self.app.wd.find_element_by_name("phone2").click()
        self.app.wd.find_element_by_name("phone2").clear()
        self.app.wd.find_element_by_name("phone2").send_keys(contacts.phone2)
        self.app.wd.find_element_by_name("notes").click()
        self.app.wd.find_element_by_name("notes").clear()
        self.app.wd.find_element_by_name("notes").send_keys(contacts.notes)

        if contacts.group != "":
         if not self.app.wd.find_element_by_xpath("//select[@name='new_group']//option[text() = '" + contacts.group + "']").is_selected():
           self.app.wd.find_element_by_xpath("//select[@name='new_group']//option[text() ='" + contacts.group + "']").click()

        self.app.wd.find_element_by_xpath("//input[@type='submit' and @name='submit' and @value='Enter']").click()

    # Удаление первого сверху группы контакта в списке
    def delete_first_contact(self):
        self.app.wd.find_element_by_link_text("home").click()
        self.app.wd.find_element_by_name("selected[]").click()
        self.app.wd.find_element_by_xpath("//input[@type='button' and @value='Delete']").click()
        self.app.wd.switch_to_alert().accept()

      # Удаление  контактa по имени
    def delete_contact_by_name(self, name):

        self.app.wd.find_element_by_link_text("home").click()
        self.app.wd.find_element_by_xpath("//input[contains(@title, 'Select (" + name + ")')]").click()
        self.app.wd.find_element_by_name("delete").click()
        self.app.wd.find_element_by_xpath("//input[@type='button' and @value='Delete']").click()
        self.app.wd.switch_to_alert().accept()