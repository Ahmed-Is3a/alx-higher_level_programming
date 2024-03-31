#!/usr/bin/python3
""" print last 10 commits """
import requests
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    # params = {'per_page': 10}
    response = requests.get(url)
    json = response.json()
    i = 0
    for item in json:
        if i == 10:
            break
        # id = response.json()[i]['sha']
        id = item.get('sha')
        # name = response.json()[i]['commit']['author']['name']
        name = item.get('commit').get('author').get('name')
        print(f"{id}: {name}")
        i += 1

    # if response.status_code == 200:
    #     commits_data = response.json()
    #     for commit in commits_data:
    #         commit_info = commit['commit']
    #         author_name = commit_info['author']['name']
    #         print(f"{commit_info['tree']['sha']}: {author_name}")
