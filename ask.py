import json
import requests
import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch
def new_query():
    return question("Etherium right?")

@ask.intent("YesIntent")
def next_round():
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD')
    data = json.loads(r.text)
    value = "One Etherium is currently valued at " + str(data['USD']) + " US Dollars"
    return statement(value)

if __name__ == '__main__':
    app.run(debug=True)