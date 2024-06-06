#!/usr/bin/python3
"""Recusive requests  module 2-recurse.py"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ A function(recursive) that queries Reddit API and
    returns a list containing thew titles o fall the
    hot articles for a give subreddit
    """
    headers = {'User-Agent': 'MyApp/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
                        url, headers=headers,
                        params=params,
                        allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        return None
