*************************************** Project Description ********************************************************

This project is all about testing the salesforce application marketing UI Using Selenium and Python

Required Packages:

pytest                         7.1.3
pytest-html                    3.1.1
selenium                       4.5.0
setuptools                     58.1.0


#######################################################################################################################
************************************************* Instructions ********************************************************
#######################################################################################################################

1. You need to specify your salesforce developer id and password in "data_conftest.json" file also the chrome
driver path in your machine.

2. For all the test cases there is some input data which are specified in "data_testCaseName_testCaseNum,json" file.
you change that default data according to your need for testing or you can go with default data.

3. The csv file have same condition as above.

4. "GenericFunction.py" consist of common function for pulling data from json, which received "jsonFileName" 
and "property_you_want_to_pool" from json file.

5. "conftest.py" consist of setup and teardown approches as fixture.


######################################## Application Running Instructions ##########################################

==>> Select Default Testing Environment As pytest 
==>> change directory(cd) to project directory.
==>> Run cmd => "pytest -s"
==>>For Html Report Generation Run cmd  "pytest --html=report.html"

Or 

==>> You can run test file via Pytest TestRunner in one go