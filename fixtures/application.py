# -*- coding: utf-8 -*-

from helpers.sessionHelper import SessionHelper
from helpers.groupsHelper import GroupsHelper
from helpers.contactsHelper import ContactsHelper

from selenium import webdriver

class Application:

    def __init__(self, browser, baseurl):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        elif browser == "opera":
            self.wd = webdriver.Opera()
        elif browser == "safari":
            self.wd = webdriver.Safari()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupsHelper(self)
        self.contacts = ContactsHelper(self)
        self.baseurl= baseurl

    # Разрушение фикстуры
    def destroy(self):
        self.wd.quit()

    # Проверка фикстуры
    def isValid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
