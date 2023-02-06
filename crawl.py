#!/usr/bin/env python3
import argparse
import sys
import requests
from bs4 import BeautifulSoup

# setting up the command line argument parser
parser = argparse.ArgumentParser(description='Crawl a website and print all links')
parser.add_argument('-u', '--url', help='URL of the website to crawl')
parser.add_argument('-v', '--verbose', action='store_true', help='Print verbose output')
args = parser.parse_args()

url = args.url
verbose = args.verbose

if not url:
    url = input().strip()

# adding "http://" or "https://" to the URL if it is not included
if not url.startswith("http"):
    url = "http://" + url

try:
    # sending a GET request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # finding all links on the website
    links = [link.get('href') for link in soup.find_all('a')]
    for link in links:
        if verbose:
            print("Link:", link)
        else:
            print(link)

    # finding all src on the website
    srcs = [src.get('src') for src in soup.find_all('img')]
    for src in srcs:
        if verbose:
            print("source:", src)
        else:
            print(src)
    # finding all src on the website
    svgs = [src.get('src') for src in soup.find_all('svg')]
    for src in svgs:
        if verbose:
            print("source:", src)
        else:
            print(src)

    # finding all script tags on the website
    scripts = [script.get('src') for script in soup.find_all('script')]
    for script in scripts:
        if verbose:
            print("Script:", script)
        else:
            print(script)

except Exception as e:
    print("An error occurred:", e)
