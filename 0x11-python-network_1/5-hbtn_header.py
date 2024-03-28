#!/usr/bin/python3

""" print X-Request-ID value """

import requests
import sys

url = sys.argv[1]

with requests.get(url) as response:
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
