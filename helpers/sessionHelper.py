# -*- coding: utf-8 -*-

# Cтраница авторизации

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def is_logged_in(self):
        if len(self.app.wd.find_elements_by_link_text("Logout")) > 0:
            return True
        else:
            return False

    def is_logged_as(self, username):
        if self.app.wd.find_element_by_xpath("//div/div[1]/form/b").text == "(" + username + ")":
            return True
        else:
            return False

    # Открытие тестового приложения
    def open_login_page(self):
        self.app.wd.get("http://192.168.1.25/addressbook/index.php")

    # Логин
    def login(self, loginpage):
        if loginpage.login is not None:
            self.app.wd.find_element_by_name("user").click()
            self.app.wd.find_element_by_name("user").clear()
            self.app.wd.find_element_by_name("user").send_keys(loginpage.login)
        if loginpage.password is not None:
            self.app.wd.find_element_by_name("pass").click()
            self.app.wd.find_element_by_name("pass").clear()
            self.app.wd.find_element_by_name("pass").send_keys(loginpage.password)
        self.app.wd.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()

    def to_homepage(self):
        if not (self.app.wd.current_url.endswith("/addressbook/") and len(self.app.wd.find_elements_by_xpath("//input[@type='button' and @value='Send e-Mail']")) > 0):
           self.app.wd.find_element_by_link_text("home").click()

    def logout(self):
        self.app.wd.find_element_by_link_text("Logout").click()

    # Проверка выхода из приложения
    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    #Проверка корректности логина
    def ensure_login(self, loginpage, username):
        if self.is_logged_in():
            if self.is_logged_as(username):
               return
            else:
                self.logout()
        self.login(loginpage)

