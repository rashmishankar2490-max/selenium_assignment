import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce")
])
def test_login_success(driver, config, username, password):
    driver.get(config["url"])
    login = LoginPage(driver)
    login.login(username, password)

    assert "inventory" in driver.current_url
