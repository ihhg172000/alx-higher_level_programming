#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status using requests """
import requests


if __name__ == '__main__':
    with requests.get('https://alx-intranet.hbtn.io/status') as response:
        print(
            'Body response:\n'
            f'\t- type: {type(response.text)}\n'
            f'\t- content: {response.text}'
        )
