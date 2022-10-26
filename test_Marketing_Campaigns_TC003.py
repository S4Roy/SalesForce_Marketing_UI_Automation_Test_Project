from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver import Keys
from GenericFunction import *

from selenium.webdriver import ActionChains


def test_TC003_Modify_existing_campaign(my_driver, salesforce):
    salesforce
    actions = ActionChains(my_driver)
    my_driver.find_element(
        By.XPATH, "//div[@class='slds-icon-waffle']"
    ).click()  # left dropdown
    my_driver.find_element(
        By.XPATH,
        "//*[@id='07p5g000001AvVhAAK']/div/lightning-formatted-rich-text/span/p",
    ).click()  # select marketing
    search = my_driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div[1]/section/header/div[2]/div[2]/div[1]/button/lightning-primitive-icon",
    )
    sleep(3)
    search.click()  # click search
    my_driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div[2]/div[1]/div/div[1]/div/div[1]/lightning-input/div/input",
    ).send_keys(
        bring_data_from_json_file(
            "data_Marketing_Campaigns_TC003.json", "campaign_name"
        ),
        Keys.ENTER,
    )
    my_driver.find_element(
        By.XPATH,
        "//table[@role='grid']/tbody/tr/td[9]/span/div",
    ).click()#click right dropdown of edit
    
    #verify
    camp_text = my_driver.find_element(
        By.XPATH, "//table[@role='grid']/tbody/tr/th/span/a"
    ).text
    assert camp_text == "Fake_Post_Awarness"
    
    print("Campaign found successfully")
    my_driver.find_element(By.XPATH, "//a[@title='Edit']").click()#click on edit
    
    my_driver.switch_to.active_element
    sleep(3)
    
    text = my_driver.find_element(
        By.XPATH,
        "//div[@class='actionBody']/div/article/h2",
    ).text
    sleep(3)
    assert text == "Edit Fake_Post_Awarness"
    print("Campaign in edit mode Sucessful !")

    form = my_driver.find_elements(By.XPATH, "//input[@type='text']")
    form[1].clear()
    form[1].send_keys(
        bring_data_from_json_file(
            "data_Marketing_Campaigns_TC003.json", "new_campaign_name"
        )
    )
    form[2].clear()
    form[2].send_keys(
        bring_data_from_json_file("data_Marketing_Campaigns_TC003.json", "start_date")
    )
    form[3].clear()
    form[3].send_keys(
        bring_data_from_json_file("data_Marketing_Campaigns_TC003.json", "end_date")
    )
    my_driver.find_element(By.XPATH, "//button[@title='Save & New']").click()
    sleep(5)

    ele = my_driver.find_element(
        By.XPATH,
        "//div[@class='actionBody']/div/article/h2",
    )
    assert ele.text == "New Campaign"
    print("Campaign Modified & A new campaigns form displayed Sucessfully!")
    my_driver.find_element(By.XPATH, "//button[@title='Cancel']").click()



