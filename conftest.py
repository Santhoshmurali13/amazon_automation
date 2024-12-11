import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json


@pytest.fixture(scope="function") 
def browser_fun(request): 
    print("initiating chrome driver") 
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome() 
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.instance.driver = driver
    driver.maximize_window()

    yield driver 
    driver.close()


@pytest.fixture(scope="class")  
def browser_cls(request):
    print("initiating chrome driver")
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome()  
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver
    driver.maximize_window()

    yield driver  

    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="input browser")
    parser.addoption("--headless", action="store", help="input browser to execute in headless mode")


@pytest.fixture()
def params(request):
    params = {}
    params['browser'] = request.config.getoption('--browser')
    params['headless'] = request.config.getoption('--headless')
    return params


@pytest.fixture(scope="function")  
def browser_cbt(request, params): 
    if params['browser'] == 'chrome':
        driver = ""
        print("initiating chrome driver") 
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome() 
        driver.maximize_window()
        driver.implicitly_wait(20)
        request.instance.driver = driver
        driver.maximize_window()
    elif params['browser'] == 'edge':
        print("initiating chrome driver") 
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Edge() 
        driver.maximize_window()
        driver.implicitly_wait(20)
        request.instance.driver = driver
        driver.maximize_window()
    else:
        pass
  
    yield driver  
    driver.close()


@pytest.fixture()
def readJson():
    with open('test_data/prereq.json') as json_file:
        data = json.load(json_file)
    return data