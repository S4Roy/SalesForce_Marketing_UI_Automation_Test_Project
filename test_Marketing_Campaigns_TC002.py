from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

from GenericFunction import *


def test_TC002_create_new_campaign(my_driver, salesforce):
    salesforce
    my_driver.find_element(By.XPATH, "//div[@class='slds-icon-waffle']").click()#click dropdown
    my_driver.find_element(
        By.XPATH,
        "//*[@id='07p5g000001AvVhAAK']/div/lightning-formatted-rich-text/span/p",
    ).click()#select marketing
    my_driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div[1]/section/div[1]/div[1]/one-appnav/div/one-app-nav-bar/nav/div/one-app-nav-bar-item-root[3]",
    ).click() #click on campaign
    
    text = my_driver.find_element(
        By.XPATH, "//span[@class='slds-var-p-right_x-small']"
    ).text
    assert text == "Campaigns"
    print("Campaigns page displayed successfully!")
    
    my_driver.find_element(
        By.XPATH, "//*[@id='brandBand_1']/div/div/div/div/div[1]/div[1]/div[2]/ul/li"
    ).click()#click on new campaign
    
    my_driver.switch_to.active_element
    text = my_driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/article/div[3]/div/div[1]/h3/span",
    ).text
    assert text == "Campaign Information"
    print("A new campaigns form displayed Sucessfully!")
    #Fill Data In New Campaign Form
    form = my_driver.find_elements(By.XPATH, "//input[@type='text']")
    form[0].send_keys(
        bring_data_from_json_file(
            "data_Marketing_Campaigns_TC002.json", "campaign_name"
        )
    )
    form[1].send_keys(
        bring_data_from_json_file("data_Marketing_Campaigns_TC002.json", "start_date")
    )
    form[2].send_keys(
        bring_data_from_json_file("data_Marketing_Campaigns_TC002.json", "end_date")
    )
    #click on save and new 
    my_driver.find_element(By.XPATH, "//button[@title='Save & New']").click()
    sleep(5)
    
    #verify
    ele = my_driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/article/div[3]/div/div[1]/h3/span",
    )
    assert ele.text == "Campaign Information"
    print("Campaign Created & A new campaigns form displayed Sucessfully!")
    #click on cancel
    my_driver.find_element(By.XPATH, "//button[@title='Cancel']").click()
