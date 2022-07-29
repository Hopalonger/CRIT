from flask import Flask
import sys
sys.path.insert(1, '../Core/')
from Core.core import *



app = Flask(__name__,static_folder='/static',)


@app.route("/")
def index():
    return RenderFile("index.html")

@app.route('/Create/')
def Create():
    # show the user profile for that user
    return "True"

@app.route('/Switch/<switchID>')
def show_user_profile(switchID):
    # show the user profile for that user
    return f'User {escape(switchID)}'

@app.route('/Download/<switchID>')
def Download(switchID):
    # show the user profile for that user
    return f'User {escape(switchID)}'

#@app.route('/style.css')
#def css():
#    return RenderFile("style.css")

app.run()
