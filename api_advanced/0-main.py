#!/usr/bin/python3
"""
0-main
"""
import sys
import importlib.util

# Load the module from file
spec = importlib.util.spec_from_file_location("subs", "0-subs.py")
subs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(subs)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(subs.number_of_subscribers(sys.argv[1])))
