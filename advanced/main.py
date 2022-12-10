import mysql.connector
from flask import Flask
from flask import render_template, request, redirect, url_for, session, flash

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


def get_user(username, password):
    arr = []
    # TODO: データベースからユーザー情報を取得する
    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        port='3306',
        database='flask'
    )
    return arr


def add_user(username, password):
    # TODO: データベースにユーザー情報を追加する
    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        port='3306',
        database='flask'
    )

####ここまでがデータベースの処理####
####ここからFlaskの処理####


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

    if :  # ログイン成功の時
        session["username"] = request.form['username']
        return redirect("/")
    else:
        flash("ログインに失敗しました")
        return redirect("/login")


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/signup', methods=['POST'])
def signup_post():
    # TODO:ユーザの登録処理を行う
    flash("ユーザー登録が完了しました")
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop("flag", None)
    session.pop("username", None)
    session["flag"] = False
    session["username"] = None
    flash("ログアウトしました")

    return redirect("/login")


if __name__ == '__main__':
    # Webサーバの起動は，host='127.0.0.1', port=8888, debug=Trueを指定してください.
    app.run()
