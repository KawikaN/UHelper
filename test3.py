import undetected_chromedriver as uc 
import selenium
from bs4 import BeautifulSoup
import mechanicalsoup
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver


dic = {}
assignments = {}
tabs = {}


# Initializing driver 
driver = uc.Chrome(headless=True) 
options = uc.ChromeOptions()
#headless=True


# Try accessing a website with antibot service 
driver.get("https://authn.hawaii.edu/cas/login?service=https%3A%2F%2Flaulima.hawaii.edu%2Fsakai-login-tool%2Fcontainer&renew=true")

# Find the username and password input fields and submit button using XPath
username_input = driver.find_element("xpath", "//input[@name='username']")
password_input = driver.find_element("xpath", "//input[@name='password']")

#submitBtn
# Enter username and password
username_input.send_keys("kawikakn")
password_input.send_keys("Kanani99!")
z=driver.find_element("xpath", '//*[@name="submitBtn"]')
#z=driver.find_element_by_xpath("//input[@name='submitBtn']")
z.click()

time.sleep(1)

def updateDriver():
    return



# checks if its on the pushing screen or if we were pushed through
while(True):
    out_of_stock_text = "your"
    if out_of_stock_text in driver.page_source:
        break
    else:
        print("Please push the duo")
        time.sleep(2)
        continue


def getData(url, tag):
    try:
        driver.get(url)
    except KeyError:
        pass
    response = requests.get(driver.current_url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    elem = driver.find_elements("xpath", tag)
    return soup, elem



driver.find_element("xpath", '//*[@id="trust-browser-button"]').click()

time.sleep(2)
response = requests.get(driver.current_url)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
elem = driver.find_elements("xpath", '//a[@href]')
membership = ''
for a in elem:
    # print(a.get_attribute("href")+"\n")
    # print(a.get_attribute("title"))
    if("Membership" in a.get_attribute("title")):
        # print(a.get_attribute("title"))
        membership = a.get_attribute("href")
        break


elem = getData(membership, '//a[@href]')[1]
for a in elem:
    className = a.get_attribute("title")
    if("Go" in className):
        link = a.get_attribute("href")
        if("[SP24]" in className):
            className = className[:23]
        dic[className[11:]] = link

def getTabs(tabName, tabTitles, a):
    if(tabName in tabTitles):
        tabLink = a.get_attribute("href")
        tabs[course+tabName] = tabLink
        return True
    return False

for course in dic:
    elem = getData(dic[course], '//a[@href]')[1]
    for a in elem:
        TabTitles = a.get_attribute("title")
        tabz = ["Assignments", "Tests", "Announcements", "Gradebook"]
        for b in tabz:
            getTabs(b, TabTitles, a)

for course in dic:
    currentCourse = []
    assignmentsExist = False
    assingmentTitle = ''
    # try:
    #     elem = getData(tabs[course+"Assignments"], '//a[@href]')[1]
    #     assignmentsExist = True
    # except KeyError:
    #     continue

    try:
        driver.get(tabs[course+"Assignments"])
    except KeyError:
        continue
    response = requests.get(driver.current_url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    elem = driver.find_elements("xpath", '//a[@href]')
    elem2 = driver.find_elements("xpath", '//td[@headers]')
    
    count = 0
    for a in range(len(elem)):
        currentCourse = []
        currentCourse2 = []
        
        assingnmentLink = elem[a].get_attribute("name")
        if("asnActionLink" in assingnmentLink):
            assingmentTitle = elem[a].get_attribute("title")
            assingnmentLink = elem[a].get_attribute("href")
            currentCourse.append(assingnmentLink)
        if(a < len(elem2)):
            c = elem2[a].get_attribute("headers")
            if("status" in c):
                assingmentStatus = elem2[a].text
                currentCourse2.append(assingmentStatus)
            if("openDate" in c):
                assingmentOpenDate = elem2[a].text
                currentCourse2.append(assingmentOpenDate)
            if("dueDate" in c):
                assingmentDueDate = elem2[a].text
                currentCourse2.append(assingmentDueDate)
        result = currentCourse + currentCourse2
        print(currentCourse2 + count)
        assignments[course+assingmentTitle] = result

        count = count+1




# print(assignments)



driver.quit()

