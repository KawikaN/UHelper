# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
import re
from flask import Flask, jsonify, Blueprint, request, redirect, url_for, render_template, session, json
import os
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#import bsObj


path_cwd = os.path.dirname(os.path.realpath(__file__))
path_templates = os.path.join(path_cwd,"templates")
path_static = os.path.join(path_cwd,"static")

app = Flask(__name__)
app.secret_key = 'Eo'

@app.route('/', methods=['GET'])
def home():
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
         # /html/body/div[2]/div/div/div[4]/div[1]/div[1]/div[5]/button
         show_more_button = driver.find_element(By.XPATH, "//button[contains(text(),'Show More')]")
         if show_more_button.is_displayed() and show_more_button.is_enabled():
            # click "show more" button
            driver.execute_script("arguments[0].click();", show_more_button)
            print("button clicked")
            time.sleep(1)
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
      time.sleep(3)

   driver.quit()

   return render_template('wordle.html', professors=professor_list)

if __name__ == "__main__":
   app.run(debug=True)


"""
@app.route('/answer', methods=['GET', 'POST']) 
def process(): 
   # words = word()
   words = session.get('word') #uses sessions to pass data between routes
   definitions = defs(words) 

   
   return render_template('answer.html', definitions = " ".join(definitions), word=words)


@app.route('/further/<finds>', methods=['GET', 'POST']) 
def run(finds): 
   return defs(finds)
   


def defs(find):
   words = find
   page_to_scrape2 = requests.get("https://wehewehe.org/gsdl2.85/cgi-bin/hdict?a=q&r=1&hs=1&m=-1&o=-1&qto=4&e=p-11000-00---off-0hdict--00-1----0-10-0---0---0direct-10-ED--4--textpukuielbert%252ctextmamaka-----0-1l--11-haw-Zz-1---Zz-1-home---00-3-1-00-0--4----0-0-11-00-0utfZz-8-00&q=" + find + "&fqv=textpukuielbert%252ctextmamaka&af=1&fqf=ED#hero-bottom-banner")
   sou2 = BeautifulSoup(page_to_scrape2.content, "html.parser")

   try:
      for a in sou2.find_all('a', href=True):
         if("gsd" in (a["href"]) and "hero-bottom-banner" in (a["href"])):
            answerLink = (a["href"])
            newLink = "https://wehewehe.org/" + answerLink
            break
      page_to_scrape2 = requests.get(newLink)
      sou2 = BeautifulSoup(page_to_scrape2.content, "html.parser")
      msg2 = sou2.find_all('p')
      for text in msg2:
         definitions = [text.text for text in msg2]

   except:
      msg2 = sou2.find_all('p')

      for text in msg2:
         definitions = [text.text for text in msg2]
   finally:
      if not definitions:
         definitions[0] = ("Definition not found")
   return definitions

if __name__ == "__main__":
   app.run(debug=True)
"""
