import pytest
from fixtures import Application

fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.isValid():
           fixture = Application()
    fixture.session.open_login_page()
    request.addfinalizer(fixture.session.ensure_logout)
    return fixture

@pytest.fixture(scope="session", autouse="True")
def stop(request):
    def fin():
      #  fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

