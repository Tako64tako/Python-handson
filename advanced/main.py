from flask import Flask
from flask import render_template, request, redirect, url_for, session, flash

import os
import db

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

database = db.connector()


@app.route('/')
def index():
    if "flag" in session and session["flag"]:
        return render_template('index.html', username=session["username"])
    else:
        return redirect("/login")


@app.route('/login')
def login():
    if "flag" in session and session["flag"]:
        return render_template('index.html', username=session["username"])
    else:
        return render_template('login.html')


@app.route('/login', methods=['POST'])
# TODO:ログイン処理を行う
def login_post():
    if session["flag"]:
        return render_template('index.html', username=session["username"])
    else:
        return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup_post():
    # TODO:ユーザの登録処理を行う
    return render_template('index.html', username=session["username"])


@app.route('/logout')
def logout():
    session.pop("flag", None)
    session.pop("username", None)
    session["flag"] = False
    session["username"] = None

    return redirect("/login")


if __name__ == '__main__':
    # Webサーバの起動は，host='127.0.0.1', port=8888, debug=Trueを指定してください.
    app.run()
