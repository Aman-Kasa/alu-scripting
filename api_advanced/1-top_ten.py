#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""
import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the top 10 hot posts of the subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "python:top_ten:v1.0 (by /u/yourusername)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check for non-200 responses or invalid subreddit
        if response.status_code == 404:
            print("None")
            return
        elif response.status_code >= 300:
            print("None")
            return
        
        # Get post data
        data = response.json().get("data")
        if not data:
            print("None")
            return
        
        # Retrieve and print the titles of the first 10 hot posts
        posts = data.get("children", [])
        for post in posts[:10]:  # Only get up to 10 posts
            print(post.get("data", {}).get("title", "No Title"))
    
    except requests.exceptions.RequestException as e:
        print("None")
