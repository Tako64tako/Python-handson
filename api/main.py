from flask import Flask, jsonify,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# TODO: GETメソッドで/apiにアクセスしたときの処理を書いてください
# return render_template('get.html')を返すようにしてください

# TODO: POSTメソッドで/api/articlesにアクセスしたときの処理を書いてください
# name = request.form.get("name")でフォームから送られてきたnameを取得してください
# nameがない場合は"名無し"を代入してください
# return render_template('post.html', name=name)を返すようにしてください

if __name__ == "__main__":
    # TODO: host='127.0.0.1',port=8888,debug=Trueで起動してください
    app.run()