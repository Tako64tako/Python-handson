# データベース編

# データベースに接続し，データの挿入および取得を行いましょう．
# 今回はMySQLを使用します．

# MySQLのログイン情報:
# ユーザー名: root
# パスワード: (空欄)
# ホスト名: localhost
# ポート番号: 3306
# データベース名: dbtest

# データベースのテーブル名: tabletest
# テーブルのカラム名: id(int,not null,auto_increment), name(varchar(255))
# ただし，idは主キーとして設定してください．

# """注意:データベース及びテーブルは事前に作成しておいてください．"""


# テーブルに以下のデータを挿入し，データを取得してください．

# name: hoge
# name: fuga
# name: piyo

# データを出力する際，id, nameと両方を出力してください．

# MySQLの公式ドキュメントが参考になります. 以下を見ながら組んでみましょう.
# https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html

import mysql.connector


def main():


if __name__ == '__main__':
    main()
