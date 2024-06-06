#!/usr/bin/python3
"""module 100-count.py achieves sorting of paginated
data(titles) from Reddit API
"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """A recursive function that queries the Reddit API. parses the
    titles of all hot articles and prints a sorted count of given
    keywords"""
    headers = {'User-Agent': 'MyApp/0.0.1'}
    word_list = [word.lower() for word in word_list]
    if not word_count:
        word_count = {word: 0 for word in word_list}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
                        url,
                        headers=headers,
                        params=params,
                        allow_redirects=False
        )
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title'].lower().split()
                for word in word_list:
                    word_count[word] += title.count(word)
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, word_count, after)
            else:
                sorted_word_count = sorted(
                                        word_count.items(),
                                        key=lambda item: (-item[1], item[0])
                )
                for word, count in sorted_word_count:
                    if count > 0:
                        print(f'{word}: {count}')
        else:
            return None
    except Exception as e:
        return None
