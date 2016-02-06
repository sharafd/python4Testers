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
        fixture = Application()
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
