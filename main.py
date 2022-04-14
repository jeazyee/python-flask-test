from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hi, from Python Flask!</h1>'


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = {'message': 'hi, the webhook in python flask is working fine!'}
        return data, 200


app.run(host='0.0.0.0', port=5500)
