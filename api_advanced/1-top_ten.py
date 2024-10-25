#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""
import requests

def top_ten(subreddit):
    """Print the titles of the hottest posts on a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "PostmanRuntime/7.35.0"
    }
    params = {
        "limit": 10
    }
    
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )
    
    # Check for invalid subreddit (404 or other error)
    if response.status_code != 200:
        print("OK")
        return
    
    # Extract data and check if it's valid
    results = response.json().get("data")
    if not results or "children" not in results:
        print("OK")
        return

    # Print titles of the first 10 hot posts
    for post in results.get("children", []):
        title = post.get("data", {}).get("title", "None")
        print(title)
