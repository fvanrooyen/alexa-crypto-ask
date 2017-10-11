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
     url = 'http://core1.local:3000/api/alerts'
     g = (requests.get(url, auth=TokenAuth("eyJrIjoieWhjZ1pMSlZvdFBsTXgzZXFqQzVSeDNZRnBTbVRSNVYiLCJuIjoibW9uaXRvciIsImlkIjoxfQ==")).text)
     gdata = json.loads(g)
     issuecount = 0 
     for i in gdata:
         if i['state'] != "ok":
             issuecount += 1 
     print(issuecount)
         

