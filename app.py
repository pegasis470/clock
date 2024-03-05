from flask import Flask, render_template
from datetime import datetime
import pytz
app = Flask(__name__)

## Template renders 
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/NYC')
def NYC():
    return render_template('NCY.html')
@app.route('/canada-central')
def Canada_central():
    return render_template('Canada_cenral.html')
@app.route('/canada-eastern')
def Canada_eastern():
    return render_template('Canada_eastern.html')
@app.route('/LONDON')
def Canada_eastern():
    return render_template('london.html')


## Time API's

@app.route('/current_time')
def current_time():
    current_time = datetime.now().strftime('%d-%m-%Y %I:%M:%S %p')
    return current_time
@app.route('/NYC-TIME')
def NYCTIME():
    current_time=datetime.now(pytz.timezone("America/New_York")).strftime('%d-%m-%Y %I:%M:%S %p')  
    return current_time
@app.route('/canada-central-time')
def CCT():
    current_time=datetime.now(pytz.timezone("Canada/Central")).strftime('%d-%m-%Y %I:%M:%S %p')  
    return current_time
@app.route('/canada-eastern-time')
def CET():
    current_time=datetime.now(pytz.timezone("Canada/Eastern")).strftime('%d-%m-%Y %I:%M:%S %p')
    return current_time
@app.route('/London-time')
def BST():
    current_time=datetime.now(pytz.timezone("Europe/London")).strftime('%d-%m-%Y %I:%M:%S %p')
    return current_time
# INIT

if __name__ == '__main__':
    app.run(debug=True)
    app.config['TEMPLATiES_AUTO_RELOAD']=True

