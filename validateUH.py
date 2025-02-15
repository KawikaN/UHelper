from selenium import *
from selenium import webdriver
from bs4 import BeautifulSoup
import mechanicalsoup
import time
from bs4 import BeautifulSoup
import requests
import selenium

import undetected_chromedriver
import selenium
from bs4 import BeautifulSoup
import mechanicalsoup
import time
from bs4 import BeautifulSoup
import requests



def ValidateUH(Username, Password):
     #https://laulima.hawaii.edu/portal/xlogin
     # try:
    options = undetected_chromedriver.ChromeOptions()

    # options.headless = True
    driver = undetected_chromedriver.Chrome(headless=True, options=options)
    options.add_experimental_option("detach", True)
    # Uncomment if you want headless mode
    # options.headless = True

    # Try accessing a website with antibot service 
    driver.get("https://laulima.hawaii.edu/portal/xlogin")

    # Find the username and password input fields and submit button using XPath
    username_input = driver.find_element("xpath", "//input[@name='eid']")
    password_input = driver.find_element("xpath", "//input[@name='pw']")

    #submitBtn
    # Enter username and password
    username_input.send_keys(Username)
    password_input.send_keys(Password)
    z=driver.find_element("xpath", '//*[@name="submit"]')
    #z=driver.find_element_by_xpath("//input[@name='submitBtn']")
    z.click()

    try:
        z=driver.find_element("xpath", '//*[@class="Mrphs-sitesNav__menuitem--myworkspace-label"]')
        if(z):
            print("Creds good")
            driver.close()
            return 0
        else:
            print("Credentials Invalid")
            driver.close()
            return 1
    except:
        print("Failed")
        driver.close()
        return 1
ValidateUH("kawikakn", "Kanani99!")





# WAY WITH TWO FACTOR AUTH
# def validateUH(Username, Password):
#     # try:
#         options = undetected_chromedriver.ChromeOptions()

#         # options.headless = True
#         driver = undetected_chromedriver.Chrome(headless=True, options=options)
#         options.add_experimental_option("detach", True)
#         # Uncomment if you want headless mode
#         # options.headless = True

#         # Try accessing a website with antibot service 
#         driver.get("https://authn.hawaii.edu/cas/login?service=https%3A%2F%2Flaulima.hawaii.edu%2Fsakai-login-tool%2Fcontainer&renew=true")

#         # Find the username and password input fields and submit button using XPath
#         username_input = driver.find_element("xpath", "//input[@name='username']")
#         password_input = driver.find_element("xpath", "//input[@name='password']")

#         #submitBtn
#         # Enter username and password
#         username_input.send_keys(Username)
#         password_input.send_keys(Password)
#         z=driver.find_element("xpath", '//*[@name="submitBtn"]')
#         #z=driver.find_element_by_xpath("//input[@name='submitBtn']")
#         z.click()

#         try:
#             z=driver.find_element("xpath", '//*[@id="loginErrorsPanel"]')
#             if(z):
#                 print("Credentials Invalid")
#                 driver.close()
#                 return 0
#             else:
#                 print("worked")
#                 driver.close()
#                 return 1
#         except:
#             print("worked")
#             driver.close()
#             return 1
#         return 0
#     # except:
#     #     print("Credentials Invalid")
#     #     driver.close()
#     #     return 2