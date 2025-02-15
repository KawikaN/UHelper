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

def scrape_professors():
   options = webdriver.ChromeOptions() # allowing for options
   options.add_argument("--headless") # Headless working yippee!
   options.page_load_strategy = 'eager'
   driver = webdriver.Chrome(options=options) # launching selenium chrome simulator

   url = "https://www.ratemyprofessors.com/search/professors/1106?q=*"
   driver.implicitly_wait(0) # driver will wait 0 seconds for elements to load
   driver.get(url) # opening url with selenium chrome

   # simulate clicking "close" on cookies popup
   try: # using a try catch just incase close is not present
      close_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Close')]") 
      WebDriverWait(driver, 100, poll_frequency=0.1).until(EC.element_to_be_clickable(close_button)).click() # waits until close is clickable and clicks it
      print("Clicked 'Close' button.")
   except Exception as e:
      print("Close button not found or already closed.", e) # prints error message

   # simulate clicking "show more" button
   delay = 0.6 # seconds
   professor_count = 0
   while professor_count <= 3806:
      try: # checking if we can load more teachers
         show_more_button = WebDriverWait(driver, 10, poll_frequency=0.1).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Show More')]")))
         if(show_more_button): # waits until the element is located in html
            button = WebDriverWait(driver, 100, poll_frequency=delay).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Show More')]"))) # waits until element is clickable 
            driver.execute_script("arguments[0].click()", button) # clicks button
            print(f"button clicked - {professor_count}")
            professor_count += 8
      except TimeoutException:
         print("No more button to click.")
         break
      except Exception as e: 
         print("An exception occured while trying to Find More button: ", e) # prints error message
         break
   
   html_content = driver.page_source # retrieves HTML of current webpage simulator(selenium) is on
   soup = BeautifulSoup(html_content, 'html.parser') # makes the html readable by BeautifulSoup

   # extract data
   professor_list = []
   professors = soup.find_all('a', class_='TeacherCard__StyledTeacherCard-syjs0d-0 dLJIlx') # finds all the cards for teachers in html and stores into array
   for prof in professors: # iterates over professor tags saved in list
      name = prof.find('div', class_="CardName__StyledCardName-sc-1gyrgim-0 cJdVEK").text # saves the text(professor name)
      rating = prof.find('div', class_="CardNumRating__StyledCardNumRating-sc-17t4b9u-0 eWZmyX").text # saves the text(professor rating)
      dept = prof.find('div', class_="CardSchool__Department-sc-19lmz2k-0 haUIRO").text # saves professor's department
      school = prof.find('div', class_="CardSchool__School-sc-19lmz2k-1 iDlVGM").text # saves professor's school
      data_class_name = "CardFeedback__CardFeedbackNumber-lq6nix-2 hroXqf"
      # feedback includes difficulty & take again % (rn: only includes take again %)
      # only scrapes take again % but skips over professor difficulty
      feedback = prof.find('div', class_=data_class_name).text 
      professor_list.append({'name': name, 'rating': rating, 'department': dept,'feedback': feedback, 'school': school}) # saves scrapped data to an array

   driver.quit()

   # convert list to pandas dataframe and save it as csv file
   df = pd.DataFrame(professor_list) 
   df.to_csv("professors.csv")

scrape_professors()