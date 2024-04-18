from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send_message():
    message = request.form['message']
    messages.append((datetime.now(), message))
    return 'Message sent!'

if __name__ == '__main__':
    app.run(debug=True)