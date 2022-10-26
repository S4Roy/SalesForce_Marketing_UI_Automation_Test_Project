from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver import Keys
from GenericFunction import *

from selenium.webdriver import ActionChains


def test_TC005_Create_different_types_leads(my_driver, salesforce):
    salesforce
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
    ).click()#click on lead
    
    my_driver.find_element(
        By.XPATH, "//*[@id='brandBand_1']/div/div/div/div/div[1]/div[1]/div[2]/ul/li"
    ).click()#click on new lead
    my_driver.switch_to.active_element
    sleep(3)
    #Fill Data In New Lead Form
    form = my_driver.find_elements(By.XPATH, "//input[@type='text']")
    
    form[1].send_keys(
        bring_data_from_json_file(
            "data_Marketing_Leads_TC005.json", "First_Name"
        )
    )
    
    form[2].send_keys(
        bring_data_from_json_file("data_Marketing_Leads_TC005.json", "Last_Name")
    )
    
    form[3].send_keys(
        bring_data_from_json_file("data_Marketing_Leads_TC005.json", "Mobile")
    )
    
    form[4].send_keys(
        bring_data_from_json_file("data_Marketing_Leads_TC005.json", "Company")
    )
    
    form[7].send_keys(
        bring_data_from_json_file("data_Marketing_Leads_TC005.json", "Email")
    )
   
    #click on save and new
    my_driver.find_element(By.XPATH, "//button[@name='SaveAndNew']").click()
    
    sleep(5)
    #verify
    ele = my_driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker/slot/records-lwc-detail-panel/div/h2",
    )
    assert ele.text == "New Lead"
    print("Lead created successfully and a new lead creation page displayed Sucessfully!")
    #click on cancel
    my_driver.find_element(By.XPATH, "//button[@name='CancelEdit']").click()

    