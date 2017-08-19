#!/usr/bin/env python

import argparse
import json
import requests
import time
import sys

version = 0.50

if __name__ == "__main__":
     r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD')
     data = json.loads(r.text)
     value = "One Etherium is currently valued at " + str(data['USD']) + " US Dollars"
     print(value)
