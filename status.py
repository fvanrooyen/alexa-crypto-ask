import json
import requests
import logging
from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

class TokenAuth(requests.auth.AuthBase):
    """Authentication using a Grafana API token."""
    def __init__(self, token):
        self.token = token

    def __call__(self, request):
        request.headers.update({
            "Authorization": "Bearer {0}".format(self.token)
        })
        return request

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.launch

def new_query():
    return question("Which miner would you like to know about?")

@ask.intent("MinerIntent", convert={'mtype': str})

def miner_status(mtype):
    if mtype == 'all':
        url = 'http://core1.local:3000/api/alerts'
        g = (requests.get(url, auth=TokenAuth("eyJrIjoieWhjZ1pMSlZvdFBsTXgzZXFqQzVSeDNZRnBTbVRSNVYiLCJuIjoibW9uaXRvciIsImlkIjoxfQ==")).text)
        gdata = json.loads(g)
        issuecount = 0 
        for i in gdata:
            if i['state'] != "ok":
                issuecount += 1
        if issuecount == 0:
            status = "Everything is good"
        elif issuecount < 2:
            status = "There are some problems"
        else: 
            status = "All hell is breaking loose"
        
        return statement(status)

if __name__ == '__main__':
    app.run(debug=True)