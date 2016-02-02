# -*- coding: utf-8 -*-

# Cтраница авторизации

class SessionHelper:

    def __init__(self, app):
        self.app = app

    # Открытие тестового приложения
    def open_login_page(self):
        self.app.wd.get("http://192.168.1.25/addressbook/index.php")

    # Логин
    def login(self, loginpage):
        self.app.wd.find_element_by_name("user").click()
        self.app.wd.find_element_by_name("user").clear()
        self.app.wd.find_element_by_name("user").send_keys(loginpage.login)
        self.app.wd.find_element_by_name("pass").click()
        self.app.wd.find_element_by_name("pass").clear()
        self.app.wd.find_element_by_name("pass").send_keys(loginpage.password)
        self.app.wd.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()

    def to_homepage(self):
        self.app.wd.find_element_by_link_text("home").click()

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()