# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
import re
from flask import Flask, jsonify, Blueprint, request, redirect, url_for, render_template, session, json
import os
import random
import mechanicalsoup 
import time
#import bsObj


path_cwd = os.path.dirname(os.path.realpath(__file__))
path_templates = os.path.join(path_cwd,"templates")
path_static = os.path.join(path_cwd,"static")

app = Flask(__name__)
app.secret_key = 'Eo'

"""
def word():
   wordList = ["aliʻi", 'akula', 'lākou', 'ʻāina', 'ihola', 'maila', 'ʻoiai', 'aʻela', 'hōʻea', 'laila', 'kākou', 'haole', 'maoli', 'waena', 'loaʻa', 'aloha', 'oʻahu', 'ʻōpio', 'keiki', 'ʻelua', 'makua', 'waiho', 'heiau', 'kākau', 'kahua', 'lāʻau', 'moana', 'kōkua', 'nīnau', 'hānai', 'mākou', 'kāhea', 'keʻei', 'hānau', 'lāhui', 'ukali', 'puaʻa', 'wāwae', 'kiaʻi', 'hahai', 'mākua', 'nunui', 'ʻīkoi', 'ʻākau', 'māhoe', 'niuhi', 'makoa', 'kaula', 'mōhai', 'hāpai', 'penei', 'ʻāhia', 'lālau', 'ʻeleu', 'mālie', 'keawe', 'ʻolua', 'honua', 'kālua', 'mauna', 'māwae', 'pehea', 'lehua', 'kūʻai', 'uhaʻi', 'mauʻu', 'lehia', 'kāula', 'awāwa', 'ʻeono', 'kālai', 'hauna', 'paukū', 'poina', 'ʻauʻa', 'moena', 'mamao', 'ʻuala', 'maliu', 'kaihe', 'hekau', 'meheu', 'launa', 'ʻōuli', 'kaupō', 'kūlou', 'waele', 'kukui', 'ʻoulu', 'ukana', 'pauka', 'naʻau', 'ʻōniu', 'loloa', 'ʻīlio', 'hōʻeu', 'nanea', 'nonoi', 'noiʻi', 'maika', 'koena', 'pālau', 'laulā', 'kaʻao', 'hālau', 'uhaki', 'wauke', 'okōko', 'kāuna', 'maiʻa', 'hahau', 'ʻāhiu', 'kiola', 'ʻōiwi', 'uhuki', 'kiʻei', 'anana', 'ʻehia', 'huina', 'kaena', 'pūniu', 'kuapā', 'ʻeiwa', 'pāhoa', 'hōʻoi', 'ʻaina', 'kīhei', 'hāmau', 'mākia', 'heana', 'unuhi', 'kūhiō', 'niniu', 'nāihe', 'kainō', 'kuemi', 'ʻāhua', 'līloa', 'hākau', 'ʻanae', 'pouli', 'kinai', 'loina', 'olonā', 'huila', 'kaiao', 'akāka', 'mōlia', 'maile', 'kāmoe', 'hoʻāo', 'kunou', 'pōniu', 'wahie', 'luaʻi', 'kēhau', 'ʻūlei', 'ʻiako', 'hiolo', 'hihia', 'akena', 'hāʻao', 'hāiki', 'kūlia', 'ʻonou', 'hāuna', 'makau', 'ʻōpua', 'ʻikuā', 'ʻōnou', 'puaʻi', 'houpo', 'luahi', 'ʻoaka', 'luina', 'naele', 'kūlua', 'nākai', 'iulai', 'aumoe', 'manuā', 'maunu', 'haupa', 'lānai', 'puehu', 'pōʻai', 'ʻāoʻo', 'haele', 'nanao', 'pōhue', 'hoana', 'kāohi', 'holoi', 'pālua', 'heulu', 'kāʻeo', 'hokua', 'kāpae', 'ʻaeʻa', 'kaona', 'kuʻia', 'ʻalae', 'laukī', 'kākia', 'ʻēheu', 'kāmau', 'ōlaʻi', 'hōʻoā', 'kaʻau', 'uwaʻu', 'pauoa', 'kuili', 'paʻao', 'nīʻau', 'uianu', 'pīkai', 'ulele', 'kuene', 'paila', 'kāoʻo', 'uhalu', 'hāloa', 'kīlou', 'ʻiewe', 'kupua', 'kuehu', 'kalae', 'līwai', 'haili', 'puana', 'ulana', 'haoʻa', 'ʻāhui', 'hahae', 'keanu', 'kuala', 'lupea', 'maiau', 'ʻōmea', 'kaʻeo', 'ikīki', 'ʻaila', 'kēwai', 'keoho', 'mālia', 'ʻāpua', 'puakō', 'hāmoa', 'lēhau', 'neʻeu', 'kuana', 'mulea', 'ʻoāwa', 'ʻumia', 'kawai', 'ʻōhua', 'ʻōmau', 'pahua', 'huhui', 'paina', 'mahae', 'huelo', 'lāʻie', 'kēpau', 'kūoʻo', 'kuewa', 'nahae', 'ʻīnea', 'pōlua', 'kualā', 'pīkoi', 'keaka', 'pāʻia', 'kaohi', 'lāuli']
   word = random.choice(wordList).upper()

   dataReply = ["blank"]
   definitions = []
   answer = word
   return word
"""


@app.route('/', methods=['GET'])
def home():
   browser = mechanicalsoup.StatefulBrowser(
      soup_config={'features': 'lxml'},
      raise_on_404=True,
      user_agent='MyBot/0.1: mysite.example.com/bot_info',
   )
   url = "https://www.ratemyprofessors.com/search/professors/1106?q=*"
   response = requests.get(url)
   response.raise_for_status()

   browser.open_relative(url)  # Load a blank page in the browser
   browser.get_current_page().soup = BeautifulSoup(response.text, 'html.parser')
   
   while True:  # Get the HTML content of the page
      page_html = browser.get_current_page().prettify()
      soup = BeautifulSoup(page_html, 'html.parser')
      show_more_button = soup.find('button', class_='Buttons__Button-sc-19xdot-1 PaginationButton__StyledPaginationButton-txi1dr-1 eUNaBX')
      if show_more_button:
         browser.launch_browser()  # Optional: Launch a browser to see the interaction
         browser.submit_selected(button=show_more_button)  # Click the "Show More" button
      else:
         break  # Break the loop when there are no more "Show More" buttons to click
   
   # get current html content of page
   soup = BeautifulSoup(response.content, 'html.parser')

   # extract data
   professor_list = []
   professors = soup.find_all('a', class_='TeacherCard__StyledTeacherCard-syjs0d-0 dLJIlx')
   for prof in professors:
      name = prof.find('div', class_="CardName__StyledCardName-sc-1gyrgim-0 cJdVEK").text
      rating = prof.find('div', class_="CardFeedback__CardFeedbackItem-lq6nix-1 fyKbws").text
      feedback = prof.find('div', class_="CardFeedback__CardFeedbackItem-lq6nix-1 fyKbws").text
      professor_list.append({'name': name, 'rating': rating, 'feedback': feedback})
   
   browser.close()

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
