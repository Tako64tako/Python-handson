from flask import Flask, jsonify,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# TODO: GETメソッドで/apiにアクセスしたときの処理を書いてください
# return render_template('get.html')を返すようにしてください
@app.route('/api')
def get_articles():
    return render_template('get.html')

# TODO: POSTメソッドで/api/articlesにアクセスしたときの処理を書いてください
# name = request.form.get("name")でフォームから送られてきたnameを取得してください
# nameがない場合は"名無し"を代入してください
# return render_template('post.html', name=name)を返すようにしてください
@app.route('/api/articles', methods=['POST'])
def get_api_articles():
    name = request.form.get("name")
    if not name:
        name = "名無し"
    return render_template('post.html', name=name)


if __name__ == "__main__":
    # TODO: host='127.0.0.1',port=8888,debug=Trueで起動してください
    app.run(host='127.0.0.1', port=8888, debug=True)