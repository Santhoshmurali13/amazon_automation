from selenium.webdriver.common.by import By
import time

locators = {
            "SIGNIN": (By.XPATH, "//span[@id='nav-link-accountList-nav-line-1']"),
            "USERNAME": (By.XPATH, "//input[@id='ap_email']"),
            "CONTINUE": (By.XPATH, "//input[@id='continue']"),
            "PASSWORD": (By.XPATH, "//input[@id='ap_password']"),
            "SIGNIN_BUTTON": (By.XPATH, "//input[@id='signInSubmit']"),
            }


class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver
        
    def launch_the_app(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        print("amazon application is launched Successfully")

    def login_application(self, username, password):
        self.driver.find_element(*locators["SIGNIN"]).click()
        time.sleep(5)
        self.driver.find_element(*locators["USERNAME"]).send_keys(username)
        self.driver.find_element(*locators["CONTINUE"]).click()
        self.driver.find_element(*locators["PASSWORD"]).send_keys(password)
        self.driver.find_element(*locators["SIGNIN_BUTTON"]).click()
        time.sleep(3)
        