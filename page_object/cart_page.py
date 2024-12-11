from selenium.webdriver.common.by import By
import time

locators = {
            "CART": (By.XPATH, "//a[@href='/gp/cart/view.html?ref_=nav_cart']"),
            "CART_PAGE_HEADER": (By.XPATH, "//h2[@class='a-size-extra-large a-text-normal']"),
            "PROCESS_PAYMENT": (By.XPATH, "//input[@name='proceedToRetailCheckout']")
            }


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_cart(self):
        self.driver.find_element(*locators["CART"]).click()
        time.sleep(3)
        cart_page_displayed = self.driver.find_element(*locators["CART_PAGE_HEADER"]).is_displayed()
        if cart_page_displayed:
            print("cart page is displayed")
        else:
            assert False, "cart page is not displayed"

    def click_on_pay(self):
        self.driver.find_element(*locators["PROCESS_PAYMENT"]).click()
        time.sleep(3)
    