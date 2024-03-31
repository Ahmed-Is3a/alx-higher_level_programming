#!/usr/bin/python3
""" git github user id """


if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    user = response.json()
    print(user.get('id'))
