# -*- coding: utf-8 -*-

# Класс для работы с контактами

class Contacts:
    
    def __init__(self, wd, address, middlename, lastname, nickname, byear, ayear, title, company, home, mobile,
                 work, fax, email2, email3, homepage, address2, phone2, notes, bday, bmonth, aday, amonth, group):
        self.wd = wd
        self.address = address
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.bday = bday
        self.bmonth = bmonth
        self.byear= byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.title = title
        self.company = company
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.group= group

    # Добавление контакта в адресную книгу
    def addContact(Contacts):
        Contacts.wd.find_element_by_link_text("add new").click()
        Contacts.wd.find_element_by_name("address").click()
        Contacts.wd.find_element_by_name("address").clear()
        Contacts.wd.find_element_by_name("address").send_keys(Contacts.address)
        Contacts.wd.find_element_by_xpath("//input[@type='submit' and @name='quickadd' and @value='Next']").click()
        Contacts.wd.find_element_by_name("middlename").click()
        Contacts.wd.find_element_by_name("middlename").clear()
        Contacts.wd.find_element_by_name("middlename").send_keys(Contacts.middlename)
        Contacts.wd.find_element_by_name("lastname").click()
        Contacts.wd.find_element_by_name("lastname").clear()
        Contacts.wd.find_element_by_name("lastname").send_keys(Contacts.lastname)
        Contacts.wd.find_element_by_name("nickname").click()
        Contacts.wd.find_element_by_name("nickname").clear()
        Contacts.wd.find_element_by_name("nickname").send_keys(Contacts.nickname)

        if Contacts.bday <> "":
         if not Contacts.wd.find_element_by_xpath("//select[@name='bday']//option[text()='" + Contacts.bday + "']").is_selected():
           Contacts.wd.find_element_by_xpath("//select[@name='bday']//option[text()='" + Contacts.bday + "']").click()

        if Contacts.bmonth <> "":
         if not Contacts.wd.find_element_by_xpath("//select[@name='bmonth']//option[@value='" + Contacts.bmonth + "']").is_selected():
           Contacts.wd.find_element_by_xpath("//select[@name='bmonth']//option[@value='" + Contacts.bmonth + "']").click()

        Contacts.wd.find_element_by_name("byear").click()
        Contacts.wd.find_element_by_name("byear").clear()
        Contacts.wd.find_element_by_name("byear").send_keys(Contacts.byear)

        if Contacts.aday <> "":
         if not Contacts.wd.find_element_by_xpath("//select[@name='baay']//option[text()='" + Contacts.aday + "']").is_selected():
           Contacts.wd.find_element_by_xpath("//select[@name='aday']//option[text()='" + Contacts.aday + "']").click()

        if Contacts.amonth <> "":
         if not Contacts.wd.find_element_by_xpath("//select[@name='amonth']//option[@value='" + Contacts.amonth + "']").is_selected():
           Contacts.wd.find_element_by_xpath("//select[@name='amonth']//option[@value='" + Contacts.amonth + "']").click()

        Contacts.wd.find_element_by_name("ayear").click()
        Contacts.wd.find_element_by_name("ayear").clear()
        Contacts.wd.find_element_by_name("ayear").send_keys(Contacts.ayear)
        Contacts.wd.find_element_by_name("theform").click()
        Contacts.wd.find_element_by_name("lastname").click()
        Contacts.wd.find_element_by_name("lastname").clear()
        Contacts.wd.find_element_by_name("lastname").send_keys(Contacts.lastname)
        Contacts.wd.find_element_by_name("nickname").click()
        Contacts.wd.find_element_by_name("nickname").clear()
        Contacts.wd.find_element_by_name("nickname").send_keys(Contacts.nickname)
        Contacts.wd.find_element_by_name("title").click()
        Contacts.wd.find_element_by_name("title").clear()
        Contacts.wd.find_element_by_name("title").send_keys(Contacts.title)
        Contacts.wd.find_element_by_name("company").click()
        Contacts.wd.find_element_by_name("company").clear()
        Contacts.wd.find_element_by_name("company").send_keys(Contacts.company)
        Contacts.wd.find_element_by_name("address").click()
        Contacts.wd.find_element_by_name("address").clear()
        Contacts.wd.find_element_by_name("address").send_keys(Contacts.address)
        Contacts.wd.find_element_by_name("home").click()
        Contacts.wd.find_element_by_name("home").clear()
        Contacts.wd.find_element_by_name("home").send_keys(Contacts.home)
        Contacts.wd.find_element_by_name("mobile").click()
        Contacts.wd.find_element_by_name("mobile").clear()
        Contacts.wd.find_element_by_name("mobile").send_keys(Contacts.mobile)
        Contacts.wd.find_element_by_name("work").click()
        Contacts.wd.find_element_by_name("work").clear()
        Contacts.wd.find_element_by_name("work").send_keys(Contacts.work)
        Contacts.wd.find_element_by_name("fax").click()
        Contacts.wd.find_element_by_name("fax").clear()
        Contacts.wd.find_element_by_name("fax").send_keys(Contacts.fax)
        Contacts.wd.find_element_by_name("email2").click()
        Contacts.wd.find_element_by_name("email2").clear()
        Contacts.wd.find_element_by_name("email2").send_keys(Contacts.email2)
        Contacts.wd.find_element_by_name("email3").click()
        Contacts.wd.find_element_by_name("email3").clear()
        Contacts.wd.find_element_by_name("email3").send_keys(Contacts.email3)
        Contacts.wd.find_element_by_name("homepage").click()
        Contacts.wd.find_element_by_name("homepage").clear()
        Contacts.wd.find_element_by_name("homepage").send_keys(Contacts.homepage)
        Contacts.wd.find_element_by_name("address2").click()
        Contacts.wd.find_element_by_name("address2").clear()
        Contacts.wd.find_element_by_name("address2").send_keys(Contacts.address2)
        Contacts.wd.find_element_by_name("phone2").click()
        Contacts.wd.find_element_by_name("phone2").clear()
        Contacts.wd.find_element_by_name("phone2").send_keys(Contacts.phone2)
        Contacts.wd.find_element_by_name("notes").click()
        Contacts.wd.find_element_by_name("notes").clear()
        Contacts.wd.find_element_by_name("notes").send_keys(Contacts.notes)

        if Contacts.group <> "":
         if not Contacts.wd.find_element_by_xpath("//select[@name='new_group']//option[text() = '" + Contacts.group + "']").is_selected():
           Contacts.wd.find_element_by_xpath("//select[@name='new_group']//option[text() ='" + Contacts.group + "']").click()

        Contacts.wd.find_element_by_xpath("//input[@type='submit' and @name='submit' and @value='Enter']").click()