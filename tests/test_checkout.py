from faker import Faker
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

def test_checkout_form(driver, config):
    fake = Faker()
    driver.get(config["url"])

    LoginPage(driver).login(config["username"], config["password"])
    driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
    driver.find_element("class name", "shopping_cart_link").click()
    driver.find_element("id", "checkout").click()

    checkout = CheckoutPage(driver)
    checkout.fill_checkout_form(
        fake.first_name(),
        fake.last_name(),
        fake.postcode()
    )

    assert "checkout-step-two" in driver.current_url
