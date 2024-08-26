import pytest

@pytest.fixture(scope='function')
def alert_about_test():
    print("\nStart test")
    yield
    print("\nFinish test")