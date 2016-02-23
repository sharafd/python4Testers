import pytest
from fixtures import Application
from model import LoginPage

fixture = None
login = LoginPage(login = "admin", password = "secret")

@pytest.fixture
def app(request):
    global fixture
    global login
    if fixture is None:
        browser = request.config.getoption("--browser")
        baseurl = request.config.getoption("--baseurl")
        fixture = Application(browser=browser, baseurl = baseurl)
    else:
        if not fixture.isValid():
            fixture = Application()

    fixture.session.open_login_page()
    fixture.session.ensure_login(login, "admin")
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
    parser.addoption("--baseurl", action = "store", default = "http://192.168.1.25/addressbook/index.php")
