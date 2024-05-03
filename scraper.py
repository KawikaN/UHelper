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
   options = Options() # allowing for options
   # options.add_argument("--headless=new") # Headless not currently working
   options.page_load_strategy = 'eager'
   driver = webdriver.Chrome(options=options) # launching selenium chrome simulator

   url = "https://www.ratemyprofessors.com/search/professors/1106?q=*"
   # response = requests.get(url) 
   # response.raise_for_status()
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
   x = 0
   delay = 3 # seconds
   professors = 0
   while True:  

      try: # checking if we can load more teachers
         show_more_button = driver.find_element(By.XPATH, "//button[contains(text(),'Show More')]")

         if(WebDriverWait(driver, 10, poll_frequency=0.1).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Show More')]")))): # waits until the element is located in html
            WebDriverWait(driver, 100, poll_frequency=0.1).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Show More')]"))).click() # waits until element is clickable and clicks it
            # click "show more" button 
            # driver.execute_script("arguments[0].click();", show_more_button)
            
            # show_more_button.click()
            print("button clicked - " + professors)
            professors = professors + 8
            # x = x+1 # counts the amount of show more tags clicked
            # if(x==5): # limiter for testing 

            #    break
         

            # time.sleep(3)


            # try:
            #    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Show More')]")))
            #    # click "show more" button
            #    print("Page ready")
            # except TimeoutException:
            #    print ("Loading took too much time!")


         else:
            print("no more button to click")
            break  # Break the loop when there are no more "Show More" buttons to click
      except Exception as e: 
         print("An exception occured while trying to Find More button: ", e) # prints error message
         continue
         break
   
   html_content = driver.page_source # retrieves HTML of current webpage simulator(selenium) is on
   soup = BeautifulSoup(html_content, 'html.parser') # makes the html readable by BeautifulSoup

   # extract data
   professor_list = []
   professors = soup.find_all('a', class_='TeacherCard__StyledTeacherCard-syjs0d-0 dLJIlx') # finds all the cards for teachers in html and stores into array
   for prof in professors: # itterates over professor tags saved in list
      name = prof.find('div', class_="CardName__StyledCardName-sc-1gyrgim-0 cJdVEK").text # saves the text(professor name)
      rating = prof.find('div', class_="CardFeedback__CardFeedbackItem-lq6nix-1 fyKbws").text # saves the text(professor rating)
      feedback_class_name = "CardFeedback__CardFeedbackItem-lq6nix-1 fyKbws"
      difficulty = prof.find('div', class_=feedback_class_name).find('div', 
         class_="CardFeedback__CardFeedbackNumber-lq6nix-2 hroXqf").text
      take_again_percent = prof.find('div', class_=feedback_class_name).find('div',
         class_="CardFeedback__CardFeedbackNumber-lq6nix-2 hroXqf").text
      professor_list.append({'name': name, 'rating': rating, 'difficulty': difficulty, 'take_again': take_again_percent}) # saves scrapped data to an array
      print(f"Professor: {name}, Rating: {rating}, Difficulty: {difficulty}, Take Again?: {take_again_percent}") 
   
      #time.sleep(1)
      

   driver.quit()

   # convert list to pandas dataframe and save it as csv file
   df = pd.DataFrame(professor_list) 
   df.to_csv("professors.csv")
   print(df, flush=True)
   print("", flush = True) # required to be able to print to terminal while using Flask