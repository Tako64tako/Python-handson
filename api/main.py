from flask import Flask, jsonify,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    user = request.args.get('user')
    data = request.args.get('data')
    return jsonify({'user': user, 'data': data})

@app.route('/post', methods=['POST'])
def post():
    user = request.form['user']
    data = request.form['data']
    return jsonify({'user': user, 'data': data})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)