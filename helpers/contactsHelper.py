# -*- coding: utf-8 -*-

# Класс для работы с контактами

class ContactsHelper:

    def __init__(self, app):
        self.app = app

    # Добавление контакта в адресную книгу
    def addContact(self, contacts):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contacts.address)
        wd.find_element_by_xpath("//input[@type='submit' and @name='quickadd' and @value='Next']").click()
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contacts.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contacts.nickname)

        if contacts.bday != "":
         if not wd.find_element_by_xpath("//select[@name='bday']//option[text()='" + contacts.bday + "']").is_selected():
           wd.find_element_by_xpath("//select[@name='bday']//option[text()='" + contacts.bday + "']").click()

        if contacts.bmonth != "":
         if not wd.find_element_by_xpath("//select[@name='bmonth']//option[@value='" + contacts.bmonth + "']").is_selected():
           wd.find_element_by_xpath("//select[@name='bmonth']//option[@value='" + contacts.bmonth + "']").click()

        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contacts.byear)

        if contacts.aday != "":
         if not wd.find_element_by_xpath("//select[@name='aday']//option[text()='" + contacts.aday + "']").is_selected():
           wd.find_element_by_xpath("//select[@name='aday']//option[text()='" + contacts.aday + "']").click()

        if contacts.amonth != "":
         if not wd.find_element_by_xpath("//select[@name='amonth']//option[@value='" + contacts.amonth + "']").is_selected():
           wd.find_element_by_xpath("//select[@name='amonth']//option[@value='" + contacts.amonth + "']").click()

        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contacts.ayear)

        if contacts.photo != "":
          wd.find_element_by_xpath("//input[@type='file' and @name='photo']").send_keys(contacts.photo)

        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contacts.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contacts.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contacts.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contacts.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contacts.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contacts.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contacts.fax)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contacts.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contacts.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contacts.homepage)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contacts.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contacts.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contacts.notes)

        if contacts.group != "":
         if not wd.find_element_by_xpath("//select[@name='new_group']//option[text() = '" + contacts.group + "']").is_selected():
           wd.find_element_by_xpath("//select[@name='new_group']//option[text() ='" + contacts.group + "']").click()

        wd.find_element_by_xpath("//input[@type='submit' and @name='submit' and @value='Enter']").click()