# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import sys
import re
from flask import Flask, jsonify, Blueprint, request, redirect, url_for, render_template, session, json
import os
import random
import mechanicalsoup 
#import bsObj


path_cwd = os.path.dirname(os.path.realpath(__file__))
path_templates = os.path.join(path_cwd,"templates")
path_static = os.path.join(path_cwd,"static")

app = Flask(__name__)
app.secret_key = 'Eo'

def word():
   wordList = ["aliʻi", 'akula', 'lākou', 'ʻāina', 'ihola', 'maila', 'ʻoiai', 'aʻela', 'hōʻea', 'laila', 'kākou', 'haole', 'maoli', 'waena', 'loaʻa', 'aloha', 'oʻahu', 'ʻōpio', 'keiki', 'ʻelua', 'makua', 'waiho', 'heiau', 'kākau', 'kahua', 'lāʻau', 'moana', 'kōkua', 'nīnau', 'hānai', 'mākou', 'kāhea', 'keʻei', 'hānau', 'lāhui', 'ukali', 'puaʻa', 'wāwae', 'kiaʻi', 'hahai', 'mākua', 'nunui', 'ʻīkoi', 'ʻākau', 'māhoe', 'niuhi', 'makoa', 'kaula', 'mōhai', 'hāpai', 'penei', 'ʻāhia', 'lālau', 'ʻeleu', 'mālie', 'keawe', 'ʻolua', 'honua', 'kālua', 'mauna', 'māwae', 'pehea', 'lehua', 'kūʻai', 'uhaʻi', 'mauʻu', 'lehia', 'kāula', 'awāwa', 'ʻeono', 'kālai', 'hauna', 'paukū', 'poina', 'ʻauʻa', 'moena', 'mamao', 'ʻuala', 'maliu', 'kaihe', 'hekau', 'meheu', 'launa', 'ʻōuli', 'kaupō', 'kūlou', 'waele', 'kukui', 'ʻoulu', 'ukana', 'pauka', 'naʻau', 'ʻōniu', 'loloa', 'ʻīlio', 'hōʻeu', 'nanea', 'nonoi', 'noiʻi', 'maika', 'koena', 'pālau', 'laulā', 'kaʻao', 'hālau', 'uhaki', 'wauke', 'okōko', 'kāuna', 'maiʻa', 'hahau', 'ʻāhiu', 'kiola', 'ʻōiwi', 'uhuki', 'kiʻei', 'anana', 'ʻehia', 'huina', 'kaena', 'pūniu', 'kuapā', 'ʻeiwa', 'pāhoa', 'hōʻoi', 'ʻaina', 'kīhei', 'hāmau', 'mākia', 'heana', 'unuhi', 'kūhiō', 'niniu', 'nāihe', 'kainō', 'kuemi', 'ʻāhua', 'līloa', 'hākau', 'ʻanae', 'pouli', 'kinai', 'loina', 'olonā', 'huila', 'kaiao', 'akāka', 'mōlia', 'maile', 'kāmoe', 'hoʻāo', 'kunou', 'pōniu', 'wahie', 'luaʻi', 'kēhau', 'ʻūlei', 'ʻiako', 'hiolo', 'hihia', 'akena', 'hāʻao', 'hāiki', 'kūlia', 'ʻonou', 'hāuna', 'makau', 'ʻōpua', 'ʻikuā', 'ʻōnou', 'puaʻi', 'houpo', 'luahi', 'ʻoaka', 'luina', 'naele', 'kūlua', 'nākai', 'iulai', 'aumoe', 'manuā', 'maunu', 'haupa', 'lānai', 'puehu', 'pōʻai', 'ʻāoʻo', 'haele', 'nanao', 'pōhue', 'hoana', 'kāohi', 'holoi', 'pālua', 'heulu', 'kāʻeo', 'hokua', 'kāpae', 'ʻaeʻa', 'kaona', 'kuʻia', 'ʻalae', 'laukī', 'kākia', 'ʻēheu', 'kāmau', 'ōlaʻi', 'hōʻoā', 'kaʻau', 'uwaʻu', 'pauoa', 'kuili', 'paʻao', 'nīʻau', 'uianu', 'pīkai', 'ulele', 'kuene', 'paila', 'kāoʻo', 'uhalu', 'hāloa', 'kīlou', 'ʻiewe', 'kupua', 'kuehu', 'kalae', 'līwai', 'haili', 'puana', 'ulana', 'haoʻa', 'ʻāhui', 'hahae', 'keanu', 'kuala', 'lupea', 'maiau', 'ʻōmea', 'kaʻeo', 'ikīki', 'ʻaila', 'kēwai', 'keoho', 'mālia', 'ʻāpua', 'puakō', 'hāmoa', 'lēhau', 'neʻeu', 'kuana', 'mulea', 'ʻoāwa', 'ʻumia', 'kawai', 'ʻōhua', 'ʻōmau', 'pahua', 'huhui', 'paina', 'mahae', 'huelo', 'lāʻie', 'kēpau', 'kūoʻo', 'kuewa', 'nahae', 'ʻīnea', 'pōlua', 'kualā', 'pīkoi', 'keaka', 'pāʻia', 'kaohi', 'lāuli']
   word = random.choice(wordList).upper()

   dataReply = ["blank"]
   definitions = []
   answer = word
   return word


@app.route('/')

def home():
   browser = mechanicalsoup.StatefulBrowser(
      soup_config={'features': 'lxml'},
      raise_on_404=True,
      user_agent='MyBot/0.1: mysite.example.com/bot_info',
   )
   find = ""
   browser.select(class_name="HomepageHero__HeroToggle-rvkinu-3 eOMiLm").text = find

   school = "University of Hawaii at Manoa"
   browser.open("https://www.ratemyprofessors.com/")
   browser.follow_link(school)
   browser.select_form("Search__DebouncedSearchInput-sc-10lefvq-1 fwqnjW")
   browser["University of Hawaii at Manoa"] = school
   resp = browser.submit_selected()

   browser.launch_browser()
   
   return render_template('wordle.html', word=words)



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