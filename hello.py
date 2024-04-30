#!/usr/bin/env python

import requests

def run():
    print('Hello world')
    demo()

def demo():
    x = requests.get('https://w3schools.com/python/demopage.htm')
    print(x.text)

run()
