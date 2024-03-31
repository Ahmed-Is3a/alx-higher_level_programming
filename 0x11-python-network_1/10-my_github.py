#!/usr/bin/python3
""" """

import requests
import sys


def get_user_id(username, password):
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        print(user_id)
    else:
        print(None)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <password>")
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    get_user_id(username, password)
