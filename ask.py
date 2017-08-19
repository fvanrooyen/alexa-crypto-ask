#Alexa Tests

import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session
import json
import requests


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent("CurrencyValue")

def new_crypto_query():

    ethvalue = 288.79

    return statement(ethvalue)

if __name__ == '__main__':

    app.run(debug=True)