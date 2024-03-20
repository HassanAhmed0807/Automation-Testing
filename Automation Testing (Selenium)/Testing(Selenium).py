from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.chrome.service import Service

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)



login_url = "https://lcdwebapp1.azurewebsites.net/accounts/login/"
registration_url = "https://lcdwebapp1.azurewebsites.net/accounts/register/"



# Registration Page Test
def test_registration():
    driver.get(registration_url)
    username_input = driver.find_element("id","register")
    password_input = driver.find_element("id","regpassword")
    register_button = driver.find_element("id","registerbtn")

    username_input.send_keys("testuser12345")
    password_input.send_keys("pass12345")
    register_button.click()


    assert "Login" in driver.page_source

# Login Page Test
def test_login():
    driver.get(login_url)
    username_input = driver.find_element("id", "username")
    password_input = driver.find_element("id","userpassword")
    login_button = driver.find_element("id","login")

    username_input.send_keys("testuser12345")
    password_input.send_keys(("pass12345"))
    login_button.click()


    assert "Patient Information Form" in driver.title



#Run the tests
try:
    # test_registration()
    # print("Hurrah...!!!! All tests passed successfully For Register Page!\nwith usename = testuser12345 and password = pass12345")
    test_login()
    print("Hurrah...!!!! All tests passed successfully For Login Page!\nwith usename = testuser12345 and password = pass12345")
    
except AssertionError as e:
    print(f"Test failed: {e}")
finally:
    driver.quit()
