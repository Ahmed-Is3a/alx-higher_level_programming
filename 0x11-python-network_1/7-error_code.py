#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to
    the URL and displays the body of the response.
"""

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]

    response = requests.get(url)
    status = response.status_code
    if (status >= 400):
        print('Error code: {}'.format(status))
    else:
        print(response.text)
