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
    return question("Which crypto currency would you like to know about?")

@ask.intent("CryptoTypeIntent", convert={'ctype': str})

def crypto_price(ctype):

    if ctype == "etherium":
        csymbol = "ETH"
    if ctype == "bitcoin":
        csymbol = "BTC"
    if ctype == "litecoin":
        csymbol = "LTC" 

    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=' + csymbol + '&tsyms=USD')
    data = json.loads(r.text)
    value = "One " + ctype + " is currently valued at " + str(data['USD']) + " US Dollars"
  
    return statement(value)

if __name__ == '__main__':
    app.run(debug=True)