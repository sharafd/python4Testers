# -*- coding: utf-8 -*-

#from helpers import webDriverHelper
from selenium.webdriver.firefox.webdriver import WebDriver

class Application:

    def __init__(self):
      # self.wdh = webDriverHelper.WebDriverHelper()
      # self.wd = self.wdh.wd
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def destroy(self):
       self.wd.quit()