#!/usr/bin/python3
"""
Lists 10 commits (from the most recent to oldest)
"""
from sys import argv
import requests


if __name__ == '__main__':
    url = f'https://api.github.com/repos/{argv[1]}/{argv[2]}/commits'
    with requests.get(url) as response:
        if response.ok:
            try:
                commits = response.json()
                for i in range(0, 10):
                    try:
                        print(
                            f'{commits[i]["sha"]} '
                            f'{commits[i]["commit"]["author"]["name"]}'
                        )
                    except IndexError:
                        break
            except Exception:
                print('Not a valid JSON')
        else:
            print(response.status_code)
