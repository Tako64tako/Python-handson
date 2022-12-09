import mysql.connector


def connector():
    return mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        port='3306',
        database='flask'
    )


def get_user(conn):
    #TODO: データベースからユーザー情報を取得する
    cursor = conn.cursor()


def add_user(conn, username, password):
    #TODO: データベースにユーザー情報を追加する
    cursor = conn.cursor()
