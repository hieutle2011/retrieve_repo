#!/usr/bin/env python3
import sys
import requests


def githubrepos(username):
    link = 'https://api.github.com/users/{0}/repos'
    res = requests.get(link.format(username))
    repos = res.json()
    try:
        result = [repo['name'] for repo in repos]
        return result
    except TypeError:
        print('There is no such existing username')


def main():
    if len(sys.argv) > 1:
        username = sys.argv[1]
        print('Number of repos is: ' + str(len(githubrepos(username))))
        print(githubrepos(username))
    else:
        print('No username provided')


if __name__ == "__main__":
    main()
