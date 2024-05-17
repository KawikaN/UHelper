from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import requests
import time
import timeit
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium import webdriver
#options.page_load_strategy = 'eager'
#options.add_argument("--headless") # Headless working yippee!

def scrape_professors():
    options = webdriver.ChromeOptions() # allowing for options
    
    

    driver = webdriver.Chrome(options=options) # launching selenium chrome simulator
    
    options = uc.ChromeOptions()   
    options.add_experimental_option("detach", True)

    url = "https://authn.hawaii.edu/cas/login?service=https%3A%2F%2Fwww.star.hawaii.edu%2Fstudentinterface%2FProcessorCAS.jsp&renew=true"
    driver.implicitly_wait(0) # driver will wait 0 seconds for elements to load
    driver.get(url) # opening url with selenium chrome
   
    username_input = driver.find_element("xpath", "//input[@name='username']")
    password_input = driver.find_element("xpath", "//input[@name='password']")
    # Enter username and password
    username_input.send_keys("kawikakn")
    password_input.send_keys("Kanani99!")
    #submitBtn
    z=driver.find_element("xpath", '//*[@name="submitBtn"]')
    #z=driver.find_element_by_xpath("//input[@name='submitBtn']")
    z.click()

    while(True):
        out_of_stock_text = "your"
        if out_of_stock_text in driver.page_source:
            break
        else:
            print("Please push the duo")
            time.sleep(2)
            continue
    driver.find_element("xpath", "//button[@id='trust-browser-button']").click()


    #class="header item ng-binding"
    html_content = driver.page_source # retrieves HTML of current webpage simulator(selenium) is on
    soup = BeautifulSoup(html_content, 'html.parser') # makes the html readable by BeautifulSoup

    semester = soup.find('div', class_="header item ng-binding")
    print(semester)
    
    # for a in semester:
    #     if(a.text == )

    currentSemester = soup.find('option', class_="ng-binding ng-scope")
    print(currentSemester)
    print("here")
    time.sleep(10)

scrape_professors()