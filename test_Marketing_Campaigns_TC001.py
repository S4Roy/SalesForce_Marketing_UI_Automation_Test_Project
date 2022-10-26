from selenium.webdriver.common.by import By
from time import sleep


def test_TC001_verify_available_views(my_driver, salesforce):
    salesforce
    my_driver.find_element(By.XPATH, "//div[@class='slds-icon-waffle']").click()
    my_driver.find_element(By.XPATH,"//*[@id='07p5g000001AvVhAAK']/div/lightning-formatted-rich-text/span/p").click()
    text=my_driver.find_element(By.XPATH,"//span[@title='Marketing']").text
    assert text=="Marketing"
    print("Marketing page displayed successfully!")
    my_driver.find_element(By.XPATH,"/html/body/div[4]/div[1]/section/div[1]/div[1]/one-appnav/div/one-app-nav-bar/nav/div/one-app-nav-bar-item-root[3]").click()
    my_driver.find_element(By.XPATH,"//button[@title='Select a List View']").click()
    drop_down=my_driver.find_elements(By.XPATH,"//span[@class=' virtualAutocompleteOptionText']")
    for item in drop_down[:-1]:
        assert item.text=="All Active Campaigns" or item.text=="My Active Campaigns"
    print('All Active Campaigns and My Active Campaigns Displaying! Final Expected Result Opted Sucessfully!')
