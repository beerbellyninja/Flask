from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
import os, csv
import pandas as pd

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SECRET_KEY'] = str(os.urandom(24))

db = []
with open('C:/Users/blanj/OneDrive/Git/Flask/Globalmantics/static/db.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        db.append({"name":row[0], 'phone': row[1], 'id': row[2], 'bal': row[3]})

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', cust_db = db)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    print(app.url_map)
    app.run()
    