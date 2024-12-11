from selenium.webdriver.common.by import By
import time

locators = {
            "CONFIRM_ADDRESS": (By.XPATH, "//input[@data-testid='bottom-continue-button']"),
            "DELIVERY_ADDRESS": (By.XPATH, "//span[contains(text(), 'Delivery addresses')]"),
            "CHECK_PAYMENT": (By.XPATH, "(//input[@checked=''])[2]"),
            "PAYMENT_TYPE": (By.XPATH, "//span[text()='Cash on Delivery/Pay on Delivery']"),
            }


class PaymentPage:

    def __init__(self, driver):
        self.driver = driver

    def click_on_payment(self, payment_type):
        self.driver.find_element(*locators["DELIVERY_ADDRESS"]).is_displayed()
        time.sleep(2)
        self.driver.find_element(*locators["CONFIRM_ADDRESS"]).click()
        time.sleep(3)
        self.driver.find_element(*locators["CHECK_PAYMENT"]).click()
        actual_text = self.driver.find_element(*locators["PAYMENT_TYPE"]).text
        if payment_type in actual_text:
            print("verify the payment method")
        else:
            assert False, "payment method is not displayed"    
        time.sleep(3)