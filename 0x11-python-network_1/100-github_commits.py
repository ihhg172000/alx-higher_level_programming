#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest)
"""
from sys import argv
import requests


if __name__ == '__main__':
    url = f'https://api.github.com/repos/{argv[1]}/{argv[2]}/commits'
    params = {
        'per_page' : 10
    }
    with requests.get(url, params=params) as response:
        if response.ok:
            commits = response.json()
            for commit in commits:
                try:
                    print(
                        f'{commit["sha"]} '
                        f'{commit["commit"]["author"]["name"]}'
                    )
                except IndexError:
                    break
        else:
            print(response.status_code)
