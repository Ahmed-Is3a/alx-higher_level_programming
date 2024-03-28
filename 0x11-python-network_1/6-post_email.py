#!/usr/bin/python3

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    res = requests.post(url, {'email': email})
    print(res.text)
