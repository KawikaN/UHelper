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



def classData(Username, Password):

    # Initializing driver 

    options = undetected_chromedriver.ChromeOptions()

    # options.headless = True
    driver = undetected_chromedriver.Chrome(headless=True, options=options)
    options.add_experimental_option("detach", True)
    # Uncomment if you want headless mode
    # options.headless = True

    # Try accessing a website with antibot service 
    driver.get("https://laulima.hawaii.edu/portal/xlogin")

    dic = {}
    assignments = {}
    tabs = {}

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

    count = 0
    while(count<5):
        try:
            z=driver.find_element("xpath", '//*[@class="Mrphs-sitesNav__menuitem--myworkspace-label"]')
            break
        except:
            count = count+1
            time.sleep(.5)
    def updateDriver():
        return

    # checks if its on the pushing screen or if we were pushed through
    # while(True):
    #     out_of_stock_text = "your"
    #     if out_of_stock_text in driver.page_source:
    #         break
    #     else:
    #         print("Please push the duo")
    #         time.sleep(.5)
    #         continue

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

    # tries = 0
    # while(True):
    #     # if(tries == 5):
    #     #     print("Duo Push Did Not Load Quick Enough")
    #     #     quit
    #     #     exit
    #     #     break
    #     try:
    #         driver.find_element("xpath", '//*[@id="trust-browser-button"]').click()
    #         break
    #     except:
    #         pass
    #     time.sleep(tries+1)
    #     tries = tries+1

    # Might need sleep timer here to let the page load before retrieving html
    while(True):
        try:
            response = requests.get(driver.current_url)
            break
        except:
            pass
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
    while(True):
        try:
            elem = getData(membership, '//a[@href]')[1]
            break
        except:
            print('having a hard time finding correct html')
            continue
    # getData will go to the page of the url and search for elements containing the tag given
    # it retuend it in a set [0][1]
    # the elems are returned as a list [1]
    # all tags with the element are saved to this list

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
    # if the link is already in do not add it
        #ERROR: Gradebook is always in tabs.values
        #tablink doesnt exist for some
            # doesnt run for gradebook
            #tabLink doesnt exist for gradebook
            if("Gradebook" in tabName):
                tabLink = "https://laulima.hawaii.edu/portal/site/LEE.51761.202510/tool/88e26520-e01b-4222-a2c7-59ce6c50e2e4/studentView.jsf"
            if(tabLink not in tabs.values()):
                tabs[course+" "+tabName] = tabLink
            return True
        return False
    tabz = ["Assignments", "Tests", "Announcements", "Gradebook", "Digital Dropbox"]
    for course in dic:
        elem = getData(dic[course], '//a[@href]')[1]
        for a in elem:
            TabTitles = a.get_attribute("title")

            # breakpoint()

            tabz = ["Assignments", "Tests", "Announcements", "Gradebook", "Digital Dropbox"]
        #These are the tabs that we will look for in each courses dashboard
            for b in tabz:
                getTabs(b, TabTitles, a)

    print(tabs, "\n")

    headerTitle = ""

    def get_dates(course, tab):
        currentCourse = []
        assignmentsExist = False
        assingmentTitle = ''
        global headerTitle
        headerTitle = ""
        # try:
        #     elem = getData(tabs[course+"Assignments"], '//a[@href]')[1]
        #     assignmentsExist = True
        # except KeyError:
        #     continue
        # print(tabs["ICS-212-0 [LEE.51761.FA24] Gradebook"])
        try:
            driver.get(tabs[course+" "+tab])
        #gets from the tabs dictionary that stores the links to each tab for each class. 
        # we will find the tab that has our assignments in it
        except KeyError:
            return 1
        response = requests.get(driver.current_url)
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")
        elem = driver.find_elements("xpath", '//a[@href]')
        # if("Gradebook" in tab):
        #     elem = driver.find_elements("xpath", "//*[@id]")
        #     elem = [el for el in elem if "__hide_division_" in el.get_attribute("id")]
        #     cnt = 0
        #     while(True):
        #         try:
        #             element = driver.find_element("id","_id_"+cnt+"__hide_division_")
        #             cnt = cnt+1
        #         except:
        #             break

            #elem = driver.find_elements("xpath", "//*[@id[contains(., '__hide_division_')]]")

        elem2 = driver.find_elements("xpath", '//td[@headers]')
        if("Gradebook" in tab):
            elem2 = driver.find_elements("xpath", '//td[@class]')
        count = 0
        if(elem):
            for a in range(10000):
                currentCourse = []
                currentCourse2 = []
                try:
                    assingnmentLink = elem[a].get_attribute("name")
                except:
                    break
                # if("asnActionLink" in assingnmentLink):
                #     assingmentTitle = elem[a].get_attribute("title")
                #     headerTitle = assingmentTitle
                #     assingnmentLink = elem[a].get_attribute("href")
                #     currentCourse.append(assingnmentLink)
                # if(elem)
                if("Gradebook" not in tab):
                    if(a < len(elem2)):
                        # elem2[a].text has all the info we need
                        # elem2[1].text coorelates to the first announcment 
                        # elem2[0].text coorelates to the first wokrsheet in assignments and the author of the first announcment
                        # print(elem2[a].text, "  ---   ", elem2[a].get_attribute("headers"))

                    # tabz = ["Assignments", "Tests", "Announcements", "Gradebook, Digital Dropbox"]
                        if(tab == "Assignments"):
                            c = elem2[a].get_attribute("headers")
                        elif("Gradebook" in tab):
                            c = elem2[a].get_attribute("id")
                        else:
                            c=""
                        # if("left" in c):
                        #     print(c.text)
                        # if("left" in c):
                        #     print("HERE", c.text)
            
                        if("title" in c):
                            title = elem2[a].text
                            headerTitle = title
                            # currentCourse2.append(title)
                        if("status" in c):
                            if(elem2[a].text == ""):
                                assingmentStatus = "No Status"
                            else:
                                assingmentStatus = elem2[a].text
                            currentCourse2.append(assingmentStatus)
                        if("openDate" in c):
                            assingmentOpenDate = elem2[a].text
                            currentCourse2.append(assingmentOpenDate)
                        if("dueDate" in c):
                            assingmentDueDate = elem2[a].text
                            currentCourse2.append(assingmentDueDate)
                        elif("Due Date" in c):
                            assingmentDueDate = elem2[a].text
                            currentCourse2.append(assingmentDueDate)

                    result = []
                    result.append(currentCourse2)

                    # add link and assignment info into results
                    # print(currentCourse2)
                    # if currentCourse2:

                    #     try:
                    #         assignments[course+headerTitle] = assignments[course+headerTitle].append(currentCourse2)
                    #     except:
                    #         assignments[course+headerTitle] = currentCourse2
                    if currentCourse2:
                        try:
                            addition = assignments[course+headerTitle] + "|" + elem2[a].text
                            if(addition in assignments[course+headerTitle]):
                                pass
                            assignments[course+headerTitle] = addition
                        except:
                            assignments[course+headerTitle] = elem2[a].text + "|"
                # sets the course and assignment title(key) to the link and information list(value)

                    count = count+1
                else:
                # elem2[a].text has all the info we need
                    # elem2[1].text coorelates to the first announcment 
                    # elem2[0].text coorelates to the first wokrsheet in assignments and the author of the first announcment
                    # print(elem2[a].text, "  ---   ", elem2[a].get_attribute("headers"))

                # tabz = ["Assignments", "Tests", "Announcements", "Gradebook, Digital Dropbox"]
                    if("Gradebook" in tab):
                        try:
                            c = elem2[a].get_attribute("id")
                        except:
                            continue
                    else:
                        c=""
                    # if("left" in c):
                    #     print(c.text)
                    # if("left" in c):
                    #     print("HERE", c.text)
                    if("left" in c):
                        k = c.find_element("xpath", "//td[contains(@class, 'left')]")
                        print(k.text)
                        title = k.text
                        headerTitle = title
                    if("center" in c):
                        try:
                            if(assingmentDueDate):
                                pass
                        except:
                            assingmentDueDate = elem2[a].text
                            currentCourse2.append(assingmentDueDate)
                        
        
                    if("title" in c):
                        title = elem2[a].text
                        headerTitle = title
                        # currentCourse2.append(title)
                    if("status" in c):
                        if(elem2[a].text == ""):
                            assingmentStatus = "No Status"
                        else:
                            assingmentStatus = elem2[a].text
                        currentCourse2.append(assingmentStatus)
                    if("openDate" in c):
                        assingmentOpenDate = elem2[a].text
                        currentCourse2.append(assingmentOpenDate)
                    if("dueDate" in c):
                        assingmentDueDate = elem2[a].text
                        currentCourse2.append(assingmentDueDate)
                    elif("Due Date" in c):
                        assingmentDueDate = elem2[a].text
                        currentCourse2.append(assingmentDueDate)

                result = []
                result.append(currentCourse2)

                # add link and assignment info into results
                # print(currentCourse2)
                # if currentCourse2:

                #     try:
                #         assignments[course+headerTitle] = assignments[course+headerTitle].append(currentCourse2)
                #     except:
                #         assignments[course+headerTitle] = currentCourse2
                if currentCourse2:
                    try:
                        addition = assignments[course+headerTitle] + "|" + elem2[a].text
                        if(addition in assignments[course+headerTitle]):
                            pass
                        assignments[course+headerTitle] = addition
                    except:
                        assignments[course+headerTitle] = elem2[a].text + "|"
            # sets the course and assignment title(key) to the link and information list(value)

                count = count+1
        else:
            currentCourse = []
            currentCourse2 = []
            for a in range(len(elem2)):

                assingnmentLink = elem[a].get_attribute("name")

                if(tab == "Assignments"):
                    c = elem2[a].get_attribute("headers")
                elif(tab == "Gradebook"):
                    c = elem2[a].get_attribute("id")
                    print('here')
                    print(c)
                else:
                    c=""
                # if("left" in c.text):
                #     print("here")
                # if("left" in c):
                #     print("HERE", c.text)

                if("title" in c):
                    title = elem2[a].text
                    headerTitle = title
                    # currentCourse2.append(title)
                if("status" in c):
                    if(elem2[a].text == ""):
                        assingmentStatus = "No Status"
                    else:
                        assingmentStatus = elem2[a].text
                    currentCourse2.append(assingmentStatus)
                if("openDate" in c):
                    assingmentOpenDate = elem2[a].text
                    currentCourse2.append(assingmentOpenDate)
                if("dueDate" in c):
                    assingmentDueDate = elem2[a].text
                    currentCourse2.append(assingmentDueDate)
                elif("Due Date" in c):
                    assingmentDueDate = elem2[a].text
                    currentCourse2.append(assingmentDueDate)
            result = []
            result.append(currentCourse2)

            # add link and assignment info into results
            # print(currentCourse2)
            # if currentCourse2:

            #     try:
            #         assignments[course+headerTitle] = assignments[course+headerTitle].append(currentCourse2)
            #     except:
            #         assignments[course+headerTitle] = currentCourse2
            if currentCourse2:
                try:
                    addition = assignments[course+headerTitle] + "|" + elem2[a].text
                    if(addition in assignments[course+headerTitle]):
                        pass
                    assignments[course+headerTitle] = addition
                except:
                    assignments[course+headerTitle] = elem2[a].text + "|"
        # sets the course and assignment title(key) to the link and information list(value)

            count = count+1

    # for each course
    # foe each assignment, test, quizzes page
    for course in dic:
        for tab in tabz:
            if(get_dates(course, tab) == 1):
                continue
    driver.quit()
    return assignments


print(classData("kawikakn", "Kanani99!"))

