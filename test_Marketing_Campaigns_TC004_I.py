from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver import Keys
from GenericFunction import *

from selenium.webdriver import ActionChains


def test_TC004_Verify_diff_type_imported_campaigns(my_driver, salesforce):
    salesforce
    my_driver.find_element(By.XPATH, "//input[@class='filter-box input']").send_keys(
        bring_data_from_json_file("data_Marketing_Campaigns_TC004.json", "search_key")
    )  # send data import wizard into search keys

    #If below link not found then check your user settings
    my_driver.find_element(
        By.XPATH, "//div[@title='Data Import Wizard']"
    ).click()  # click data import wizard
    sleep(2)
    iframe = my_driver.find_element(By.XPATH, "//iframe")
    my_driver.switch_to.frame(iframe)
    sleep(2)
    #Launch Wizard
    my_driver.find_element(By.LINK_TEXT,"Launch Wizard!").click()
    sleep(5)
    print(
        "According To Test Case In Data Import Wizard Bulk Import For Campaigns Option Not Found! Please Review Test Case! "
    )
    my_driver.switch_to.default_content()
    sleep(5)
    assert False
