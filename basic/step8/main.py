# Step8
# TODO:
# 以下のコードに辞書型でユーザー情報を作成し、welcom関数に渡してください
# welcom関数内の変更はできない物とします。

def welcom(u):
    print('ようこそ{}さん'.format(u['name']))
    u['age'] = u['age'] + 1
    print('あなたは来年{}歳になりますね'.format(u['age']))

def main():
    username = "hoge"
    userage = 20
    # ここに書いてね


if __name__ == '__main__':
    main()