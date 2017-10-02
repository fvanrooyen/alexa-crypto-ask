#!/usr/bin/env python

import argparse
import json
import requests
import time
import sys


version = 0.50

class TokenAuth(requests.auth.AuthBase):
    """Authentication using a Grafana API token."""
    def __init__(self, token):
        self.token = token

    def __call__(self, request):
        request.headers.update({
            "Authorization": "Bearer {0}".format(self.token)
        })
        return request

if __name__ == "__main__":
     r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD')
     data = json.loads(r.text)
     value = "One Etherium is currently valued at " + str(data['USD']) + " US Dollars"
     print(value)
     url = 'http://core1.local:3000/api/alerts'
     g = (requests.get(url, auth=TokenAuth("eyJrIjoieWhjZ1pMSlZvdFBsTXgzZXFqQzVSeDNZRnBTbVRSNVYiLCJuIjoibW9uaXRvciIsImlkIjoxfQ==")).text)
     gdata = json.loads(g)
     for i in gdata:
         print(i['state'])
         

