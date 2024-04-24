from bs4 import BeautifulSoup
import requests
import sys
import re
from flask import Flask, jsonify, Blueprint, request, redirect, url_for, render_template, session, json
import os
import random
import mechanicalsoup
import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver

# page_to_scrape = requests.get("https://www.ratemyprofessors.com/")
# soup = BeautifulSoup(page_to_scrape.content, "html.parser")

# soup.find('input').value = "university of hawaii at manoa"
# soup.find('input')['value'] = "university of hawaii at manoa"
driver = uc.Chrome(headless=True) 
options = uc.ChromeOptions()

