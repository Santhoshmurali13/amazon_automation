from selenium.webdriver.common.by import By
import time

locators = {
            "SEARCH_BUTTON": (By.XPATH, "//input[@id='nav-search-submit-button']"),
            "SEARCH": (By.XPATH, "//input[@id='twotabsearchtextbox']"),
            "ADD_TO_CART_BUTTON": (By.XPATH, "(//button[text()='Add to cart'])[1]"),
            "CONFIRM_ADD_TO_CART": (By.XPATH, "(//div[contains(@class, 'puis-atc-variation-element')]//button[text()='Add to cart'])[1]")
        
            }


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def search_for_item(self, searchitem):
        self.driver.find_element(*locators["SEARCH_BUTTON"]).click()
        self.driver.find_element(*locators["SEARCH"]).send_keys(searchitem)
        time.sleep(2)
        self.driver.find_element(*locators["SEARCH_BUTTON"]).click()
        time.sleep(5)

    def add_to_cart(self, ):
        self.driver.find_element(*locators["ADD_TO_CART_BUTTON"]).click()
        time.sleep(3)
        self.driver.find_element(*locators["CONFIRM_ADD_TO_CART"]).click() 
        time.sleep(3)            