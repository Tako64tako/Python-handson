# Step8
# 以下のコードは意図した通りに動作しません。動作するように修正してください。
# welcom関数内の変更はできない物とします。

def welcom(u):
    print('ようこそ{}さん'.format(u['name']))
    u['age'] = u['age'] + 1
    print('あなたは来年{}歳になりますね'.format(u['age']))

username = input()
userage = int(input())
user = {'name': username, 'age': userage}

welcom(user)