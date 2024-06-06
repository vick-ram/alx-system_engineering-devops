#!/usr/bin/python3
"""0-subs.py module to return number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """a function that returns number f subscribers from redit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'MyApp/0.0.1'}

    try:
        response = requests.get(
                        url,
                        headers=headers,
                        allow_redirects=False
        )
        if response.status_code == 200:
            return response.json().get("data").get("subscribers")
        else:
            return 0
    except Exception as e:
        return 0
