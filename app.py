from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'ვინმე ხომ არ მოკლეს ვინმე ხომ არ მო**ეს'
