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

import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def classData(Username, Password):
    def _create_driver(headless=True):
        options = undetected_chromedriver.ChromeOptions()
        # if headless:
        #     options.add_argument('--headless')
        return undetected_chromedriver.Chrome(options=options)

    driver = _create_driver(headless="True")
    while(True):
        try:
            # Try accessing a website with antibot service
            driver.get("https://lamaku.hawaii.edu/d2l/home")
            break
        except selenium.common.exceptions.NoSuchWindowException:
            # Sometimes the initial window dies immediately; recreate once.
            driver = _create_driver(headless="False")
            driver.get("https://lamaku.hawaii.edu/d2l/home")
    dic = {}
    assignments = {}
    tabs = {}
    wait = WebDriverWait(driver, 15)
    while(True):
        try:
            z=driver.find_element("xpath", '//*[@class="d2l-button d2l-button-sso-1"]')
            break
        except:
            pass
    z.click()
    # Find the username and password input fields and submit button using XPath
    username_input = wait.until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys(Username)
    password_input.send_keys(Password)
    z = driver.find_element(By.NAME, "submitBtn")
    z.click()
    while(True):
        out_of_stock_text = "your"
        if out_of_stock_text in driver.page_source:
            break
        else:
            print("Please push the duo")
            time.sleep(.5)
            continue
    # time.sleep(2)
    while(True):
        try:
            z=driver.find_element("xpath", '//*[@class="c--primary primary button align-flex-items-center align-flex-justify-content-start input__width-full size-margin-top-medium  button--xlarge"]')
            break
        except selenium.common.exceptions.NoSuchElementException:
            print('no button found')
            pass
    z.click()
    # while(True):
    #     try:
    #         response = requests.get(driver.current_url)
    #         break
    #     except:
    #         pass

    # html_content = driver.page_source
    # soup = BeautifulSoup(html_content, "html.parser")

    # while(True):
    #     pass

    time.sleep(7)

    shadow_host1 = driver.find_element(By.CSS_SELECTOR, "d2l-my-courses-v2")
    shadow_host2 = shadow_host1.shadow_root
    shadow_host3 = shadow_host2.find_element(By.CSS_SELECTOR, "d2l-my-courses-container-v2")
    shadow_host4 = shadow_host3.shadow_root
    print(shadow_host4, 'here')
    shadow_host5 = shadow_host4.find_element(By.CSS_SELECTOR, "d2l-tabs")
    shadow_host7 = shadow_host5.find_element(By.CSS_SELECTOR, "d2l-tab-panel")
    shadow_host9 = shadow_host7.find_element(By.CSS_SELECTOR, "d2l-my-courses-content-v2")
    shadow_host10 = shadow_host9.shadow_root
    shadow_host11 = shadow_host10.find_element(By.CSS_SELECTOR, "d2l-my-courses-card-grid-v2")
    shadow_host12 = shadow_host10.shadow_root
    shadow_host13 = shadow_host11.find_element(By.CSS_SELECTOR, "div")
    shadow_host14 = shadow_host13.find_elements(By.CSS_SELECTOR, "d2l-my-courses-enrollment-card")
    print(shadow_host14, 'here')
    print('got here')

    # 2. Access the shadow root itself
    # shadow_root = shadow_host.shadow_root
    # second = shadow_root.find_element(By.TAG_NAME, "d2l-my-courses-card-grid-v2")
    # second2 = second.shadow_root
    # second3 = second2.find_element(By.CSS_SELECTOR, "course-card-grid columns-2")
    # second4 = second3.find_elements(By.TAG_NAME, "d2l-my-courses-enrollment-card")
    # print(second4)

    # # 3. Search INSIDE the shadow root for your cards
    # elem = shadow_root.find_elements(By.TAG_NAME, "d2l-my-courses-enrollment-card")

    # print(f"Found {len(elem)} cards inside the Shadow DOM!")
    # cards = soup.find_all("d2l-my-courses-enrollment-card")
    # print(f"Found {len(cards)} course cards.")
    # while(True):
    #     try:
    #         WebDriverWait(driver, 5).until(
    #             EC.presence_of_element_located((By.TAG_NAME, "d2l-my-courses-enrollment-card"))
    #         )
    #         print("Page loaded successfully!")
    #         break
    #     except selenium.common.exceptions.TimeoutException:
    #         html_content = driver.page_source
    #         soup = BeautifulSoup(html_content, "html.parser")
    #         print(soup)
    #         pass

    # html_content = driver.page_source
    # soup = BeautifulSoup(html_content, "html.parser")
    # elem = driver.find_elements(By.TAG_NAME, "d2l-my-courses-enrollment-card")
    # print(soup)
    while(True):
        pass
    # find d2l-mpy-courses-enrollment-card element
    # id has "enrollment-card-" in it
    # classes that have not started will have disabled at the end of the elemtn name
    # this is all within a div with class course-card-grid columns-2
    # under this we find d2l-card with text (this will be our course names)
    # we take the href which will be the link to the course home page

    # while(True):
    #     try:
    #         response = requests.get(driver.current_url)
    #         break
    #     except:
    #         pass
    # html_content = response.text
    # soup = BeautifulSoup(html_content, "html.parser")
    # elem = driver.find_elements(By.TAG_NAME, "d2l-my-courses-enrollment-card")
    # print(elem)
    # quit
    # membership = ''
    # for a in elem:
    #     # print(a.get_attribute("href")+"\n")
    #     # print(a.get_attribute("title"))
    #     if("Membership" in a.get_attribute("title")):
    #         # print(a.get_attribute("title"))
    #         membership = a.get_attribute("href")
    #         break
    # while(True):
    #     try:
    #         elem = getData(membership, '//a[@href]')[1]
    #         break
    #     except:
    #         print('having a hard time finding correct html')
    #         continue
    # # getData will go to the page of the url and search for elements containing the tag given
    # # it retuend it in a set [0][1]
    # # the elems are returned as a list [1]
    # # all tags with the element are saved to this list

    # for a in elem:
    #     className = a.get_attribute("title")
    #     if("Go" in className):
    #         link = a.get_attribute("href")
    #         if("[SP24]" in className):
    #             className = className[:23]
    #         dic[className[11:]] = link

    # def getTabs(tabName, tabTitles, a):
    #     if(tabName in tabTitles):
    #         tabLink = a.get_attribute("href")
    # # if the link is already in do not add it
    #     #ERROR: Gradebook is always in tabs.values
    #     #tablink doesnt exist for some
    #         # doesnt run for gradebook
    #         #tabLink doesnt exist for gradebook
    #         if("Gradebook" in tabName):
    #             tabLink = "https://laulima.hawaii.edu/portal/site/LEE.51761.202510/tool/88e26520-e01b-4222-a2c7-59ce6c50e2e4/studentView.jsf"
    #         if(tabLink not in tabs.values()):
    #             tabs[course+" "+tabName] = tabLink
    #         return True
    #     return False
    # tabz = ["Assignments", "Tests", "Announcements", "Gradebook", "Digital Dropbox"]
    # for course in dic:
    #     elem = getData(dic[course], '//a[@href]')[1]
    #     for a in elem:
    #         TabTitles = a.get_attribute("title")

    #         # breakpoint()

    #         tabz = ["Assignments", "Tests", "Announcements", "Gradebook", "Digital Dropbox"]
    #     #These are the tabs that we will look for in each courses dashboard
    #         for b in tabz:
    #             getTabs(b, TabTitles, a)

    # print(tabs, "\n")

    # headerTitle = ""

    # def get_dates(course, tab):
    #     currentCourse = []
    #     assignmentsExist = False
    #     assingmentTitle = ''
    #     global headerTitle
    #     headerTitle = ""
    #     # try:
    #     #     elem = getData(tabs[course+"Assignments"], '//a[@href]')[1]
    #     #     assignmentsExist = True
    #     # except KeyError:
    #     #     continue
    #     # print(tabs["ICS-212-0 [LEE.51761.FA24] Gradebook"])
    #     try:
    #         driver.get(tabs[course+" "+tab])
    #     #gets from the tabs dictionary that stores the links to each tab for each class. 
    #     # we will find the tab that has our assignments in it
    #     except KeyError:
    #         return 1
    #     response = requests.get(driver.current_url)
    #     html_content = response.text
    #     soup = BeautifulSoup(html_content, "html.parser")
    #     elem = driver.find_elements("xpath", '//a[@href]')
    #     # if("Gradebook" in tab):
    #     #     elem = driver.find_elements("xpath", "//*[@id]")
    #     #     elem = [el for el in elem if "__hide_division_" in el.get_attribute("id")]
    #     #     cnt = 0
    #     #     while(True):
    #     #         try:
    #     #             element = driver.find_element("id","_id_"+cnt+"__hide_division_")
    #     #             cnt = cnt+1
    #     #         except:
    #     #             break

    #         #elem = driver.find_elements("xpath", "//*[@id[contains(., '__hide_division_')]]")

    #     elem2 = driver.find_elements("xpath", '//td[@headers]')
    #     if("Gradebook" in tab):
    #         elem2 = driver.find_elements("xpath", '//td[@class]')
    #     count = 0
    #     if(elem):
    #         for a in range(10000):
    #             currentCourse = []
    #             currentCourse2 = []
    #             try:
    #                 assingnmentLink = elem[a].get_attribute("name")
    #             except:
    #                 break
    #             # if("asnActionLink" in assingnmentLink):
    #             #     assingmentTitle = elem[a].get_attribute("title")
    #             #     headerTitle = assingmentTitle
    #             #     assingnmentLink = elem[a].get_attribute("href")
    #             #     currentCourse.append(assingnmentLink)
    #             # if(elem)
    #             if("Gradebook" not in tab):
    #                 if(a < len(elem2)):
    #                     # elem2[a].text has all the info we need
    #                     # elem2[1].text coorelates to the first announcment 
    #                     # elem2[0].text coorelates to the first wokrsheet in assignments and the author of the first announcment
    #                     # print(elem2[a].text, "  ---   ", elem2[a].get_attribute("headers"))

    #                 # tabz = ["Assignments", "Tests", "Announcements", "Gradebook, Digital Dropbox"]
    #                     if(tab == "Assignments"):
    #                         c = elem2[a].get_attribute("headers")
    #                     elif("Gradebook" in tab):
    #                         c = elem2[a].get_attribute("id")
    #                     else:
    #                         c=""
    #                     # if("left" in c):
    #                     #     print(c.text)
    #                     # if("left" in c):
    #                     #     print("HERE", c.text)
            
    #                     if("title" in c):
    #                         title = elem2[a].text
    #                         headerTitle = title
    #                         # currentCourse2.append(title)
    #                     if("status" in c):
    #                         if(elem2[a].text == ""):
    #                             assingmentStatus = "No Status"
    #                         else:
    #                             assingmentStatus = elem2[a].text
    #                         currentCourse2.append(assingmentStatus)
    #                     if("openDate" in c):
    #                         assingmentOpenDate = elem2[a].text
    #                         currentCourse2.append(assingmentOpenDate)
    #                     if("dueDate" in c):
    #                         assingmentDueDate = elem2[a].text
    #                         currentCourse2.append(assingmentDueDate)
    #                     elif("Due Date" in c):
    #                         assingmentDueDate = elem2[a].text
    #                         currentCourse2.append(assingmentDueDate)

    #                 result = []
    #                 result.append(currentCourse2)

    #                 # add link and assignment info into results
    #                 # print(currentCourse2)
    #                 # if currentCourse2:

    #                 #     try:
    #                 #         assignments[course+headerTitle] = assignments[course+headerTitle].append(currentCourse2)
    #                 #     except:
    #                 #         assignments[course+headerTitle] = currentCourse2
    #                 if currentCourse2:
    #                     try:
    #                         addition = assignments[course+headerTitle] + "|" + elem2[a].text
    #                         if(addition in assignments[course+headerTitle]):
    #                             pass
    #                         assignments[course+headerTitle] = addition
    #                     except:
    #                         assignments[course+headerTitle] = elem2[a].text + "|"
    #             # sets the course and assignment title(key) to the link and information list(value)

    #                 count = count+1
    #             else:
    #             # elem2[a].text has all the info we need
    #                 # elem2[1].text coorelates to the first announcment 
    #                 # elem2[0].text coorelates to the first wokrsheet in assignments and the author of the first announcment
    #                 # print(elem2[a].text, "  ---   ", elem2[a].get_attribute("headers"))

    #             # tabz = ["Assignments", "Tests", "Announcements", "Gradebook, Digital Dropbox"]
    #                 if("Gradebook" in tab):
    #                     try:
    #                         c = elem2[a].get_attribute("id")
    #                     except:
    #                         continue
    #                 else:
    #                     c=""
    #                 # if("left" in c):
    #                 #     print(c.text)
    #                 # if("left" in c):
    #                 #     print("HERE", c.text)
    #                 if("left" in c):
    #                     k = c.find_element("xpath", "//td[contains(@class, 'left')]")
    #                     print(k.text)
    #                     title = k.text
    #                     headerTitle = title
    #                 if("center" in c):
    #                     try:
    #                         if(assingmentDueDate):
    #                             pass
    #                     except:
    #                         assingmentDueDate = elem2[a].text
    #                         currentCourse2.append(assingmentDueDate)
                        
        
    #                 if("title" in c):
    #                     title = elem2[a].text
    #                     headerTitle = title
    #                     # currentCourse2.append(title)
    #                 if("status" in c):
    #                     if(elem2[a].text == ""):
    #                         assingmentStatus = "No Status"
    #                     else:
    #                         assingmentStatus = elem2[a].text
    #                     currentCourse2.append(assingmentStatus)
    #                 if("openDate" in c):
    #                     assingmentOpenDate = elem2[a].text
    #                     currentCourse2.append(assingmentOpenDate)
    #                 if("dueDate" in c):
    #                     assingmentDueDate = elem2[a].text
    #                     currentCourse2.append(assingmentDueDate)
    #                 elif("Due Date" in c):
    #                     assingmentDueDate = elem2[a].text
    #                     currentCourse2.append(assingmentDueDate)

    #             result = []
    #             result.append(currentCourse2)

    #             # add link and assignment info into results
    #             # print(currentCourse2)
    #             # if currentCourse2:

    #             #     try:
    #             #         assignments[course+headerTitle] = assignments[course+headerTitle].append(currentCourse2)
    #             #     except:
    #             #         assignments[course+headerTitle] = currentCourse2
    #             if currentCourse2:
    #                 try:
    #                     addition = assignments[course+headerTitle] + "|" + elem2[a].text
    #                     if(addition in assignments[course+headerTitle]):
    #                         pass
    #                     assignments[course+headerTitle] = addition
    #                 except:
    #                     assignments[course+headerTitle] = elem2[a].text + "|"
    #         # sets the course and assignment title(key) to the link and information list(value)

    #             count = count+1
    #     else:
    #         currentCourse = []
    #         currentCourse2 = []
    #         for a in range(len(elem2)):

    #             assingnmentLink = elem[a].get_attribute("name")

    #             if(tab == "Assignments"):
    #                 c = elem2[a].get_attribute("headers")
    #             elif(tab == "Gradebook"):
    #                 c = elem2[a].get_attribute("id")
    #                 print('here')
    #                 print(c)
    #             else:
    #                 c=""
    #             # if("left" in c.text):
    #             #     print("here")
    #             # if("left" in c):
    #             #     print("HERE", c.text)

    #             if("title" in c):
    #                 title = elem2[a].text
    #                 headerTitle = title
    #                 # currentCourse2.append(title)
    #             if("status" in c):
    #                 if(elem2[a].text == ""):
    #                     assingmentStatus = "No Status"
    #                 else:
    #                     assingmentStatus = elem2[a].text
    #                 currentCourse2.append(assingmentStatus)
    #             if("openDate" in c):
    #                 assingmentOpenDate = elem2[a].text
    #                 currentCourse2.append(assingmentOpenDate)
    #             if("dueDate" in c):
    #                 assingmentDueDate = elem2[a].text
    #                 currentCourse2.append(assingmentDueDate)
    #             elif("Due Date" in c):
    #                 assingmentDueDate = elem2[a].text
    #                 currentCourse2.append(assingmentDueDate)
    #         result = []
    #         result.append(currentCourse2)

    #         # add link and assignment info into results
    #         # print(currentCourse2)
    #         # if currentCourse2:

    #         #     try:
    #         #         assignments[course+headerTitle] = assignments[course+headerTitle].append(currentCourse2)
    #         #     except:
    #         #         assignments[course+headerTitle] = currentCourse2
    #         if currentCourse2:
    #             try:
    #                 addition = assignments[course+headerTitle] + "|" + elem2[a].text
    #                 if(addition in assignments[course+headerTitle]):
    #                     pass
    #                 assignments[course+headerTitle] = addition
    #             except:
    #                 assignments[course+headerTitle] = elem2[a].text + "|"
    #     # sets the course and assignment title(key) to the link and information list(value)

    #         count = count+1

    # # for each course
    # # foe each assignment, test, quizzes page
    # for course in dic:
    #     for tab in tabz:
    #         if(get_dates(course, tab) == 1):
    #             continue
    # try:
    #     driver.quit()
    # except Exception:
    #     # If the session already died, don't fail the request during cleanup.
    #     pass
    # return assignments


print(classData("kawikakn", "Kanani99!"))

