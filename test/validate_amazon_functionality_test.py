import pytest
from page_object.home_page import HomePage
from page_object.login_page import LoginPage
from page_object.cart_page import CartPage
from page_object.payment_page import PaymentPage


@pytest.mark.usefixtures("browser_cbt")
class Testamazon:

    def test_amazon_application(self, readJson):
        Login = LoginPage(self.driver)
        Login.launch_the_app(readJson['amazon_URL'])
        Login.login_application(readJson["username"], readJson["password"])
        Home = HomePage(self.driver)
        Home.search_for_item(readJson['serach_item'])
        Home.add_to_cart()
        Cart = CartPage(self.driver)
        Cart.click_on_cart()
        Cart.click_on_pay()
        Payment = PaymentPage(self.driver)
        Payment.click_on_payment(readJson['payment_type'])

  

    