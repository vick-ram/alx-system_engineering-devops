#!/usr/bin/python3
"""some docs"""
import requests


def number_of_subscribers(subreddit):
    """a function that returns number f subscribers from redit"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyApp/0.0.1'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0
