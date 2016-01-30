# -*- coding: utf-8 -*-

# Cтраница авторизации

class SessionHelper:

    def __init__(self, app):
        self.app = app

    # Открытие тестового приложения
    def open_login_page(self):
        wd = self.app.wd
        wd.get("http://192.168.1.25/addressbook/index.php")

    # Логин
    def login(self, loginpage):
        wd = self.app.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(loginpage.login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(loginpage.password)
        wd.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()