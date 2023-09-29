#!/usr/bin/python3
"""  Fetches https://alx-intranet.hbtn.io/status using urllib """
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        body = response.read()
        print(
            'Body response:\n'
            f'\t- type: {type(body)}\n'
            f'\t- content: {body}\n'
            f'\t- utf8 content: {body.decode("utf-8")}'
        )
