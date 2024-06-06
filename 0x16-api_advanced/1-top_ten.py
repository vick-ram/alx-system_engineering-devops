#!/usr/bin/python3
"""query for top ten results from reddit api"""
import requests


def top_ten(subreddit):
    """A function that queries Reddit API and prints
    the titles of the first 10 hot posts
    """
    headers = {'User-Agent': 'MyApp/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(None)
