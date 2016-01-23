# -*- coding: utf-8 -*-

from selenium.webdriver.firefox.webdriver import WebDriver

global wd

class WebDriverHelper:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
