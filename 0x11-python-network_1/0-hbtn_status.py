#!/usr/bin/python3
"""  Fetches https://alx-intranet.hbtn.io/status using urllib """
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print(
            'Body response:\n'
            f'\t- type: {type(html)}\n'
            f'\t- content: {html}\n'
            f'\t- utf8 content: {html.decode("utf-8")}'
        )
