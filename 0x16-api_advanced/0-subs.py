#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    res = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "MyApp/0.0.1"},
    )
    if res.status_code == 404:
        return 0
    results = res.json().get('data')
    return results.get('subscribers')
