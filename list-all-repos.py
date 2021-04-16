#!/usr/bin/env python
""" Print all of the clone-urls for a GitHub organization.
It requires the PyGithub module, which you can install like this::
    $ sudo yum -y install python-virtualenv
    $ mkdir scratch
    $ cd scratch
    $ virtualenv my-virtualenv
    $ source my-virtualenv/bin/activate
    $ pip3 install PyGithub
    $ export GITHUB_TOKEN=<user_token>
Usage example::
    $ python3 list-all-repos.py
"""

import os
from github import Github

gh = None
user_token = os.environ.get('GITHUB_TOKEN')

if __name__ == '__main__':
    gh = Github(user_token)

    all_repos = gh.get_organization("Jimdo").get_repos(type='all')
    for repo in all_repos:
        print ("        \"%s\" : {\n            \"url\" : \"%s\"\n        },\n" % (repo.name, repo.ssh_url))
