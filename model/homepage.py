# -*- coding: utf-8 -*-

# Домашняя страница

class HomePage:

    def __init__(self, wd, login, password):
        self.wd = wd
        self.login = login
        self.password = password

    # Открытие тестового приложения
    def open_homepage(HomePage):
        HomePage.wd.get("http://192.168.1.25/addressbook/index.php")

      # Логин
    def login(HomePage):
      #  HomePage.wd.find_element_by_css_selector("body").click()
        HomePage.wd.find_element_by_name("user").click()
        HomePage.wd.find_element_by_name("user").clear()
        HomePage.wd.find_element_by_name("user").send_keys(HomePage.login)
        HomePage.wd.find_element_by_name("pass").click()
        HomePage.wd.find_element_by_name("pass").clear()
        HomePage.wd.find_element_by_name("pass").send_keys(HomePage.password)
        HomePage.wd.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()

    def logout(HomePage):
        HomePage.wd.find_element_by_link_text("Logout").click()