from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

def scrape_professors():
   driver = webdriver.Chrome() 

   url = "https://www.ratemyprofessors.com/search/professors/1106?q=*"
   response = requests.get(url)
   response.raise_for_status()

   driver.get(url)

   # simulate clicking "close" on cookies popup
   try:
      close_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Close')]")
      close_button.click()
      print("Clicked 'Close' button.")
   except Exception as e:
      print("Close button not found or already closed.")

   # simulate clicking "show more" button
   while True:  
      try:
         show_more_button = driver.find_element(By.XPATH, "//button[contains(text(),'Show More')]")
         if show_more_button.is_displayed():
            # click "show more" button
            driver.execute_script("arguments[0].click();", show_more_button)
            print("button clicked")
            time.sleep(3)
         else:
            print("no more button to click")
            break  # Break the loop when there are no more "Show More" buttons to click
      except Exception as e:
         print("exception occurred while trying to click button: ", e)
         break
   
   # get current html content of page
   html_content = response.content
   soup = BeautifulSoup(html_content, 'html.parser')

   # extract data
   professor_list = []
   professors = soup.find_all('a', class_='TeacherCard__StyledTeacherCard-syjs0d-0 dLJIlx')
   for prof in professors:
      name = prof.find('div', class_="CardName__StyledCardName-sc-1gyrgim-0 cJdVEK").text
      rating = prof.find('div', class_="CardFeedback__CardFeedbackItem-lq6nix-1 fyKbws").text
      feedback_class_name = "CardFeedback__CardFeedbackItem-lq6nix-1 fyKbws"
      difficulty = prof.find('div', class_=feedback_class_name).find('div', 
         class_="CardFeedback__CardFeedbackNumber-lq6nix-2 hroXqf").text
      take_again_percent = prof.find('div', class_=feedback_class_name).find('div',
         class_="CardFeedback__CardFeedbackNumber-lq6nix-2 hroXqf").text
      professor_list.append({'name': name, 'rating': rating, 'difficulty': difficulty, 'take_again': take_again_percent})
      print(f"Professor: {name}, Rating: {rating}, Difficulty: {difficulty}, Take Again?: {take_again_percent}")
      time.sleep(1)

   driver.quit()
