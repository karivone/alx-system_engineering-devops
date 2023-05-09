#!/usr/bin/python3

""" a script to retrieve the no of subs on a subreddi"""

import requests


def number_of_subscribers(subreddit):
    '''defines the no of subcribers on sub reddit '''

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Set custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyBot/0.0.1'}
    # Make a request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the number of subscribers from the response JSON
        return response.json()['data']['subscribers']
    else:
        # Return 0 if the subreddit is invalid
        return 0
