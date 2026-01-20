import pytest, json
from utils.driver_factory import get_driver

@pytest.fixture
def config():
    with open("config/config.json") as f:
        return json.load(f)

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            driver.save_screenshot(f"reports/{item.name}.png")
