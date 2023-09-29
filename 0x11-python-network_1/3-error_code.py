#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8)
"""
from sys import argv
from urllib import request
from urllib.error import HTTPError


if __name__ == '__main__':
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as error:
        print(f'Error code: {error.code}')
