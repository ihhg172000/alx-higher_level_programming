#!/usr/bin/python3
"""
Takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from sys import argv
import requests


if __name__ == '__main__':
    with requests.post(argv[1], data={'email': argv[2]}) as response:
        print(response.text)
