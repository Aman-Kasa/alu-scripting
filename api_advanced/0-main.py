#!/usr/bin/python3
"""
0-main
"""
import sys
import importlib

if __name__ == '__main__':
    # Dynamically import the module
    subs_module = importlib.import_module('0-subs')
    number_of_subscribers = subs_module.number_of_subscribers

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
