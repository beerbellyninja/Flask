from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
import os

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SECRET_KEY'] = str(os.urandom(24))
bookmarks = []

def store_bookmark(url):
    bookmarks.append(dict(
        url = url,
        user = "banj294",
        date = datetime.today()
    ))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        url = request.form['url']
        store_bookmark(url)
        flash(f"Stored book mark {url}")
        return redirect(url_for('add'))
    return render_template('add.html')

@app.route('/')
@app.route('/index')
def index():
    #return render_template('index.html', added_by = [u["user"] for u in bookmarks], bookmark_list = [i["url"] for i in bookmarks])
    return render_template('index.html', bookmark_list = bookmarks)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
    

if __name__ == '__main__':
    print(app.url_map)
    app.run()
    