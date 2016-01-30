# -*- coding: utf-8 -*-

from helpers.sessionHelper import SessionHelper
from helpers.groupsHelper import GroupsHelper
from helpers.contactsHelper import ContactsHelper

from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupsHelper(self)
        self.contacts = ContactsHelper(self)

    def destroy(self):
        self.wd.quit()
