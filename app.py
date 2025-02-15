# -*- coding: utf-8 -*-
import sys
import re
import uuid
from sqlalchemy import String
from flask import Flask, jsonify, Blueprint, request, redirect, url_for, render_template, session, json, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, ValidationError, Length
from flask_bcrypt import Bcrypt
import os
import pandas as pd
import pymysql
import sqlite3
from datetime import date
from flask_migrate import Migrate
from validateUH import ValidateUH

app = Flask(__name__)

path_cwd = os.path.dirname(os.path.realpath(__file__))
path_templates = os.path.join(path_cwd,"templates")
path_static = os.path.join(path_cwd,"static")


# app.secret_key = 'Eo'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/kawikanaweli/Desktop/Code/UHELPER/database.db'
app.config['SQLALCHEMY_BINDS'] = {
   'db2': 'sqlite:////Users/kawikanaweli/Desktop/Code/UHELPER/forums.db',  # Secondary DB
   'db3': 'sqlite:////Users/kawikanaweli/Desktop/Code/UHELPER/marketplace.db',  # Third DB
   #  'db4': 'sqlite:////Users/kawikanaweli/Desktop/Code/UHELPER/database4.db',  # Fourth DB
}
app.config['SECRET_KEY'] = 'Eo'
app.config['WTF_CSRF_ENABLED'] = True
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

# app.init_app(app)
# sqlite:////absolute/path/to/foo.db

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))



professors = pd.read_csv("profs.csv")
# creaitng database to store user info
class User(db.Model, UserMixin):
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   username = db.Column(db.String(20), nullable=False, unique=True)
   # set max input to 80 because password will be hashed
   password = db.Column(db.String(80), nullable=False)
   calendarAccessDate = db.Column(db.String(10))

class RegisterForm(FlaskForm):
   username = StringField(validators=[InputRequired(), Length(
      min=4, max=20)], render_kw={"placeholder": "Username"})
# setting perameters for form requirnments
   password = PasswordField(validators=[InputRequired(), Length(
      min=4, max=20)], render_kw={"placeholder": "Password"})
   submit = SubmitField("Register")

   def validate_username(self, username):
      existing_user_username = User.query.filter_by(
         username=username.data).first()
      if existing_user_username:
         raise ValidationError(
            'That username already exists. Please choose a different one.')

class ForumPost(FlaskForm):
   title = StringField(validators=[InputRequired(), Length(
      min=0, max=2000)], render_kw={"placeholder": "Title"})
# setting perameters for form requirnments
   text = StringField(validators=[InputRequired(), Length(
      min=0, max=5000)], render_kw={"placeholder": "Body"})
   submit = SubmitField("Post")
   
   def validate_title(self, title):
      pass

class MarketplacePost(FlaskForm):
   item = StringField(validators=[InputRequired(), Length(
      min=0, max=2000)], render_kw={"placeholder": "Item"})
# setting perameters for form requirnments
   description = StringField(validators=[InputRequired(), Length(
      min=0, max=5000)], render_kw={"placeholder": "Description"})
   submit = SubmitField("Post")



class LoginForm(FlaskForm):
   username = StringField(validators=[InputRequired(), Length(
      min=4, max=20)], render_kw={"placeholder": "Username"})
# setting perameters for form requirnments
   password = PasswordField(validators=[InputRequired(), Length(
      min=4, max=20)], render_kw={"placeholder": "Password"})
   submit = SubmitField("Login")

class Forum(db.Model, UserMixin):
   __bind_key__ = 'db2'
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   title = db.Column(db.String(1000), nullable=False, unique=False)
   text = db.Column(db.String(5000), nullable=False)

class Search(FlaskForm):
   password = StringField(validators=[InputRequired()], render_kw={"placeholder": "Search"})
   submit = SubmitField("Search")

   def validate_title(self, title):
      pass

class Marketplace(db.Model, UserMixin):
   __bind_key__ = 'db3'
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   item = db.Column(db.String(1000), nullable=False, unique=False)
   description = db.Column(db.String(5000), nullable=False)





@app.route('/')
def home():
   return render_template('wordle.html', professors=professors)

@app.route('/forum_post', methods=['GET', 'POST'])
def forum_post():
   form = ForumPost()
   if form.validate_on_submit():
      print(f"Form Submitted! Title: {form.title.data}, Text: {form.text.data}")
      new_post = Forum(title=form.title.data, text=form.text.data)
      db.session.add(new_post)
      db.session.commit()
      return redirect(url_for("forum"))
   return render_template('forum_post.html', form=form)


@app.route('/marketplace_post', methods=['GET', 'POST'])
def marketplace_post():
   form = MarketplacePost()
   if form.validate_on_submit():
      print(f"Form Submitted! Item: {form.item.data}, Description: {form.description.data}")
      new_post = Marketplace(item=form.item.data, description=form.description.data)
      db.session.add(new_post)
      db.session.commit()
      return redirect(url_for("marketplace"))
   else:
      print(f"Form Errors: {form.errors}")
   return render_template('marketplace_post.html', form=form)

from courseData import classData  # Import at the top of the file

@app.route('/calendar', methods=['GET', 'POST'])
def calendar():
   data = {}  # To store due dates
   today = str(date.today())
   user = current_user
   # user = User.query.filter_by(username=current_user.password).first()
   # dateAccessed = user.password
   dateAccessed = user.calendarAccessDate
   username = user.username
   password = user.password
   print(password)
   print(dateAccessed)
   print(today[8:10])
   if(dateAccessed != None):
      if(today[0:4] > dateAccessed[0:4]):
         result = classData(username, password)  # Run the function once and store the returned dictionary
         for assignment in result:  # Iterate over the keys of the dictionary
            parts = result[assignment].split('|')  # Split the key by '|'
            end = len(parts) -1
            last_part = parts[end]  # Access the last part of the split result
            data[assignment] = last_part
         user.calendarAccessDate = today
         db.session.commit()
         print(user.calendarAccessDate)
      elif(today[5:7] > dateAccessed[5:7]):
         result = classData(username, password)  # Run the function once and store the returned dictionary
         for assignment in result:  # Iterate over the keys of the dictionary
            parts = result[assignment].split('|')  # Split the key by '|'
            end = len(parts) -1
            last_part = parts[end]  # Access the last part of the split result
            data[assignment] = last_part
         user.calendarAccessDate = today
         db.session.commit()
         print(user.calendarAccessDate)
      elif(today[8:10] > dateAccessed[8:19]):
         result = classData(username, password)  # Run the function once and store the returned dictionary
         for assignment in result:  # Iterate over the keys of the dictionary
            parts = result[assignment].split('|')  # Split the key by '|'
            end = len(parts) -1
            last_part = parts[end]  # Access the last part of the split result
            data[assignment] = last_part
         user.calendarAccessDate = today
         db.session.commit()
         print(user.calendarAccessDate)
   else:
      result = classData(username, password)  # Run the function once and store the returned dictionary
      for assignment in result:  # Iterate over the keys of the dictionary
         parts = result[assignment].split('|')  # Split the key by '|'
         end = len(parts) -1
         last_part = parts[end]  # Access the last part of the split result
         data[assignment] = last_part
      user.calendarAccessDate = today
      db.session.commit()
      print(user.calendarAccessDate)

#  print("HERE", dueDates)  # Debugging: Print the list of due dates
   return render_template("calendar.html", dueDates=data)  # Pass dueDates to the template


@app.route('/searching', methods=['GET', 'POST'])
def searching():
   word = request.args.get('word')  # Retrieve the search word from the query parameter
   db_path = '/Users/kawikanaweli/Desktop/Code/UHELPER/forums.db'
   db = sqlite3.connect(db_path)
   cursor = db.cursor()

   # Use parameterized query to prevent SQL injection
   cursor.execute("SELECT * FROM forum WHERE title LIKE ?", ('%' + word + '%',))
   data = cursor.fetchall()

   db.close()

   # Return the results as JSON
   return jsonify(data)

@app.route('/forum', methods=['GET', 'POST'])
def forum():
   data = []
   db_path = '/Users/kawikanaweli/Desktop/Code/UHELPER/forums.db'
   db = sqlite3.connect(db_path)
   cursor = db.cursor()


   cursor.execute("SELECT * FROM forum")
   data = cursor.fetchall()
   db.close()

   form = Search()
   if(form.validate_on_submit()):
      print("searching")
   return render_template('forum.html', data=data, form=form)



@app.route('/professors', methods=['GET', 'POST'])
def process():
   prof = session.get('professor')
   
   return render_template('professors.html', professors=professors)

@app.route('/login', methods=['GET', 'POST'] )
def login():
   form = LoginForm()
   if(form.validate_on_submit()):
      user = User.query.filter_by(username=form.username.data).first()
      if(user):
         # if bcrypt.check_password_hash(user.password, form.password.data):
         #    login_user(user)
         #    return redirect(url_for('dashboard'))
         if (user.password == form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
   return render_template('login.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
   logout_user
   return redirect(url_for('login'))


@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
   form = RegisterForm()

   if form.validate_on_submit():

      validation = ValidateUH(form.username.data, form.password.data)
      if(validation == 0):
         hashed_password = bcrypt.generate_password_hash(form.password.data)
         new_user = User(username=form.username.data, password=form.password.data)
         db.session.add(new_user)
         db.session.commit()
         return redirect(url_for("login"))
      else:
         return render_template('register.html', form=form, wrong = True)

   return render_template('register.html', form=form, wrong = False)

@app.route('/marketplace', methods=['GET', 'POST'])
def marketplace():
   data = []
   db_path = '/Users/kawikanaweli/Desktop/Code/UHELPER/marketplace.db'
   db = sqlite3.connect(db_path)
   cursor = db.cursor()


   cursor.execute("SELECT * FROM marketplace")
   data = cursor.fetchall()
   db.close()

   form = Search()
   if(form.validate_on_submit()):
      print("searching")
   return render_template('marketplace.html', data=data, form=form)

with app.app_context():
   db.create_all()

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
