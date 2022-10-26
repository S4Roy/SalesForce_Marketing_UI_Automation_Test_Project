from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver import Keys
from GenericFunction import *

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


def test_TC008_Create_and_validate_Assignment_Manager_rules_for_Leads(my_driver, salesforce):
    salesforce
    my_driver.maximize_window()

    my_driver.find_element(By.XPATH, "//input[@class='filter-box input']").send_keys(
        bring_data_from_json_file("data_Marketing_Leads_TC008.json", "search_key")
    )  # send assignment rule into search keys

    #If below link not found then check your user settings
    my_driver.find_element(
        By.XPATH, "//div[@title='Lead Assignment Rules']"
    ).click()  # select lead assignment rule

    
    iframe = my_driver.find_element(By.XPATH, "//iframe")
    my_driver.switch_to.frame(iframe)
    my_driver.find_element(
        By.XPATH, "//input[@name='new']"
    ).click()  # click on new for creating new rule
    sleep(3)

    # switching to iframe of new rule form
    iframe = my_driver.find_element(By.XPATH, "//iframe")
    my_driver.switch_to.frame(iframe)
    sleep(3)

    my_driver.find_element(By.XPATH, "//input[@name='name']").send_keys(
        bring_data_from_json_file("data_Marketing_Leads_TC008.json", "rule_name")
    )  # send new rule name

    my_driver.find_element(By.XPATH, "//input[@name='use']").click()  # mark as active
    ele = my_driver.find_elements(By.XPATH, "//input[@name='save' and @title='Save']")
    ele[1].click()  # save new rule
    sleep(3)

    # switching iframe of rule list
    iframe = my_driver.find_element(By.XPATH, "//iframe")
    my_driver.switch_to.frame(iframe)

    my_driver.find_element(
        By.LINK_TEXT,
        bring_data_from_json_file("data_Marketing_Leads_TC008.json", "rule_name"),
    ).click()  # click on newly created rule for define rule
    sleep(3)

    # switch to add new rule frame
    iframe = my_driver.find_element(By.XPATH, "//iframe")
    my_driver.switch_to.frame(iframe)
    # click new rule
    my_driver.find_element(By.XPATH, "//input[@name='new']").click()
    sleep(4)
    # switching to frame of new rule form
    iframe = my_driver.find_element(
        By.XPATH,
        "//iframe",
    )
    my_driver.switch_to.frame(iframe)
    # fill form
    my_driver.find_element(By.XPATH, "//input[@id='SortOrder']").send_keys("1")
    sleep(2)
    # select lhs
    ele = Select(my_driver.find_element(By.XPATH, "//select[@title='Field 1']"))
    ele.select_by_value("Lead.Company")
    ele = Select(my_driver.find_element(By.XPATH, "//select[@title='Operator 1']"))
    ele.select_by_value("e")
    sleep(2)
    # send RHS as wipro
    my_driver.find_element(By.XPATH, "//input[@title='Value 1']").send_keys(
        bring_data_from_json_file("data_Marketing_Leads_TC008.json", "rhs")
    )
    sleep(2)
    # send assign to
    my_driver.find_element(By.XPATH, "//input[@ name='Assignee']").send_keys(
        bring_data_from_json_file("data_Marketing_Leads_TC008.json", "assign_to")
    )
    sleep(3)
    # click save
    my_driver.find_element(By.XPATH, "//input[@ name='save' and @tabindex='5']").click()
    sleep(3)

    # verify
    iframe = my_driver.find_element(
        By.XPATH,
        "//iframe",
    )
    my_driver.switch_to.frame(iframe)
    sleep(2)
    newly_created_rule_name = my_driver.find_element(
        By.XPATH, "//h2[@class='pageDescription']"
    ).text
    sleep(2)
    assert newly_created_rule_name == bring_data_from_json_file(
        "data_Marketing_Leads_TC008.json", "rule_name"
    )
    print(
        "From Searchbox, Lead Assignment Rule created and New Rule definded Sucessfully!"
    )

    my_driver.switch_to.default_content()
    # creation_of_new_lead_according_to_new_rule_and_verifying_owner
    my_driver.find_element(
        By.XPATH, "//div[@class='slds-icon-waffle']"
    ).click()  # left dropdown
    my_driver.find_element(
        By.XPATH,
        "//*[@id='07p5g000001AvVhAAK']/div/lightning-formatted-rich-text/span/p",
    ).click()  # select marketing
    my_driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div[1]/section/div[1]/div[1]/one-appnav/div/one-app-nav-bar/nav/div/one-app-nav-bar-item-root[4]",
    ).click()  # click on lead
    my_driver.find_element(
        By.XPATH, "//*[@id='brandBand_1']/div/div/div/div/div[1]/div[1]/div[2]/ul/li"
    ).click()  # click on new lead
    my_driver.switch_to.active_element
    sleep(3)
    # Fill Data In New Lead Form
    form = my_driver.find_elements(By.XPATH, "//input[@type='text']")

    form[1].send_keys(
        bring_data_from_json_file("data_Marketing_Leads_TC008.json", "First_Name")
    )
    form[2].send_keys(
        bring_data_from_json_file("data_Marketing_Leads_TC008.json", "Last_Name")
    )
    form[3].send_keys(
        bring_data_from_json_file("data_Marketing_Leads_TC008.json", "Mobile")
    )

    form[4].send_keys(
        bring_data_from_json_file("data_Marketing_Leads_TC008.json", "Company")
    )

    form[7].send_keys(
        bring_data_from_json_file("data_Marketing_Leads_TC008.json", "Email")
    )

    sleep(3)
    # mark new assignment rule to be applied
    my_driver.find_element(By.XPATH, "//*[@class='slds-checkbox_faux']").click()
    sleep(3)
    # click on save
    my_driver.find_element(By.XPATH, "//button[@name='SaveEdit']").click()
    sleep(5)
    # verify
    my_driver.find_element(By.XPATH, "//a[@data-label='Details']").click()
    sleep(3)

    ele = my_driver.find_element(
        By.XPATH, "//a[@class='flex-wrap-ie11']/slot/slot/span"
    )

    sleep(3)
    assert ele.text == bring_data_from_json_file(
        "data_Marketing_Leads_TC008.json", "assign_to"
    )

    print(
        "Newly created Rule Ran and Apply Sucessfully,The primary sales team member verify as earlier given in the time of rule creation!"
    )
    sleep(3)
