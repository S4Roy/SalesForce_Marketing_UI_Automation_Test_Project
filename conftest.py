from time import sleep
import pytest
from GenericFunction import *

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

# by default scope='function' you can test it in module level also
@pytest.fixture(scope="module")
def my_driver():

    # Setting Driver
    opt = Options()
    opt.add_argument("--disable-notifications")
    driver_path = bring_data_from_json_file("data_conftest.json", "driver_path")
    ser = Service(driver_path)
    driver = webdriver.Chrome(service=ser, options=opt)
    # Wait In Every Case Until Page Reload
    driver.implicitly_wait(120)

    yield driver

    # Close Driver
    driver.close()


@pytest.fixture(scope="module")
def salesforce(my_driver):

    # Bring_Data
    url = bring_data_from_json_file("data_conftest.json", "salesforce_login_url")
    username = bring_data_from_json_file(
        "data_conftest.json", "salesforce_login_username"
    )
    password = bring_data_from_json_file(
        "data_conftest.json", "salesforce_login_password"
    )
    my_driver.get(url)
    # Login
    sleep(5)
    my_driver.find_element(By.CSS_SELECTOR, "input#username").send_keys(username)
    my_driver.find_element(By.CSS_SELECTOR, "input.password").send_keys(password)
    my_driver.find_element(By.CSS_SELECTOR, "input[type=submit]").click()
    text = my_driver.find_element(By.XPATH, "//span[@class='title slds-truncate']").text
    assert text == "Home"
    print("\nPre Condition met and Successfully login to Sales force application!")
    sleep(5)
    yield my_driver
    sleep(5)
    # LogOut
    my_driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div[1]/section/header/div[2]/span/div[2]/ul/li[9]/span/button",
    ).click()
    my_driver.find_element(By.LINK_TEXT, "Log Out").click()
    sleep(3)
    text = my_driver.find_element(By.XPATH, "//label[@for='username']").text
    assert text == "Username"
    print("Successfully logout from Sales force application!")
    sleep(5)
