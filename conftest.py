# -*- coding: utf-8 -*-

import json

import os
import pytest
from fixtures import Application
from model import LoginPage

fixture = None
configuration = None
login = LoginPage(login = None, password = None)

@pytest.fixture
def app(request):
    global login
    global fixture
    global configuration
    # Чтение клнфигурационного файла
    if configuration is None:
        with open(request.config.getoption("--cfg")) as config_file:
            configuration  = json.load(config_file)
    # Создание фикстуры
    if fixture is None or not fixture.isValid():
        browser = request.config.getoption("--browser")
        fixture = Application(browser=browser, baseurl = configuration['baseurl'])
        login = LoginPage(login = configuration['username'], password = configuration['password'])

    fixture.session.open_login_page()
    fixture.session.ensure_login(login, configuration['username'])
    return fixture

@pytest.fixture(scope="session", autouse="True")
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "firefox")
    parser.addoption("--cfg", action = "store", default = os.path.join(os.path.abspath(os.path.dirname(__file__)), "cfg.json"))